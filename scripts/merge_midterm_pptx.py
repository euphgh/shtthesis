#!/usr/bin/env python3
"""Merge the approved REMUS slides, retaining editable objects and source themes.

Uses only Python's standard library for OPC package assembly, and OfficeCLI for
validation/previews. Run outside the agent sandbox per thesis/AGENTS.md.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import shutil
import subprocess
import tempfile
from urllib.parse import unquote
from xml.dom import minidom
import xml.etree.ElementTree as ET
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL = "http://schemas.openxmlformats.org/package/2006/relationships"
CT = "http://schemas.openxmlformats.org/package/2006/content-types"
ET.register_namespace("p", P)
ET.register_namespace("a", A)
ET.register_namespace("r", R)


def xml_bytes(element):
    if element.tag.startswith((f"{{{REL}}}", f"{{{CT}}}")):
        ET.register_namespace("", element.tag[1:].split("}", 1)[0])
    return ET.tostring(element, encoding="utf-8", xml_declaration=True)


def relationship_path(part):
    path = PurePosixPath(part)
    return str(path.parent / "_rels" / (path.name + ".rels"))


def resolve_target(part, target):
    target = unquote(target)
    result = posixpath.normpath(posixpath.join(posixpath.dirname(part), target))
    result = result.lstrip("/")
    if result.startswith("../"):
        raise ValueError(f"Invalid relationship target: {part}: {target}")
    return result


class Source:
    """A read-only source package; slide order comes from presentation relations."""

    def __init__(self, path, number):
        self.path = path
        self.number = number
        self.sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
        with ZipFile(path) as archive:
            self.parts = {name: archive.read(name) for name in archive.namelist()}
        root_rels = self.relationships("")
        self.presentation = next(
            resolve_target("", e.get("Target"))
            for e in root_rels
            if e.get("Type") == R + "/officeDocument"
        )
        self.tree = ET.fromstring(self.parts[self.presentation])
        links = {e.get("Id"): e for e in self.relationships(self.presentation)}
        self.slides = [
            resolve_target(self.presentation, links[e.get(f"{{{R}}}id")].get("Target"))
            for e in self.tree.findall(f"{{{P}}}sldIdLst/{{{P}}}sldId")
        ]
        size = self.tree.find(f"{{{P}}}sldSz")
        self.size = (int(size.get("cx")), int(size.get("cy")))
        types = ET.fromstring(self.parts["[Content_Types].xml"])
        defaults = {
            e.get("Extension"): e.get("ContentType")
            for e in types
            if e.tag == f"{{{CT}}}Default"
        }
        self.types = {
            name: defaults.get(name.rsplit(".", 1)[-1]) for name in self.parts
        }
        self.types.update(
            {
                e.get("PartName").lstrip("/"): e.get("ContentType")
                for e in types
                if e.tag == f"{{{CT}}}Override"
            }
        )

    def relationships(self, part):
        name = relationship_path(part) if part else "_rels/.rels"
        return list(ET.fromstring(self.parts[name])) if name in self.parts else []

    def destination(self, part):
        path = PurePosixPath(part)
        return str(path.parent / f"merged{self.number:02}_{path.name}")


def merge(sources, pages, output):
    """Copy each selected slide's dependency graph, remapping only package links.

    Layout/master cycles are visited once per source. XML for slides, charts,
    notes and themes is copied byte for byte; embedded assets are not reencoded.
    Each source has a filename prefix, preventing media and theme collisions.
    """
    parts, types, copied = {}, {}, set()
    masters, notes_masters = [], []
    layout_id = 2147483649

    def copy_part(source, part):
        nonlocal layout_id
        key = (source.number, part)
        dest = source.destination(part)
        if key in copied:
            return dest
        copied.add(key)
        data = source.parts[part]
        kind = source.types[part]
        if not kind:
            raise ValueError(f"Missing content type: {source.path.name}: {part}")
        if kind.endswith("presentationml.slideMaster+xml"):
            masters.append(dest)
            # Layout IDs must remain unique across the combined presentation.
            doc = minidom.parseString(data)
            for node in doc.getElementsByTagNameNS(P, "sldLayoutId"):
                node.setAttribute("id", str(layout_id))
                layout_id += 1
            data = doc.toxml(encoding="utf-8")
        elif kind.endswith("presentationml.notesMaster+xml"):
            notes_masters.append(dest)
        parts[dest], types[dest] = data, kind
        links = source.relationships(part)
        if links:
            relroot = ET.Element(f"{{{REL}}}Relationships")
            for link in links:
                attrs = dict(link.attrib)
                if attrs.get("TargetMode") != "External":
                    target = copy_part(source, resolve_target(part, attrs["Target"]))
                    attrs["Target"] = posixpath.relpath(target, posixpath.dirname(dest))
                ET.SubElement(relroot, f"{{{REL}}}Relationship", attrs)
            parts[relationship_path(dest)] = xml_bytes(relroot)
        return dest

    selected = [copy_part(source, source.slides[index - 1]) for source, index in pages]
    presentation = ET.Element(f"{{{P}}}presentation")
    relations = ET.Element(f"{{{REL}}}Relationships")

    def add_relation(target, kind):
        rid = f"rId{len(relations) + 1}"
        ET.SubElement(
            relations,
            f"{{{REL}}}Relationship",
            Id=rid,
            Type=R + "/" + kind,
            Target=posixpath.relpath(target, "ppt"),
        )
        return rid

    master_list = ET.SubElement(presentation, f"{{{P}}}sldMasterIdLst")
    for index, master in enumerate(masters):
        ET.SubElement(
            master_list,
            f"{{{P}}}sldMasterId",
            id=str(2147483648 + index),
            attrib={f"{{{R}}}id": add_relation(master, "slideMaster")},
        )
    if notes_masters:
        notes_list = ET.SubElement(presentation, f"{{{P}}}notesMasterIdLst")
        # PresentationPart permits one default notes master. Each imported
        # notes slide retains its own relationship to its original master.
        for master in notes_masters[:1]:
            ET.SubElement(
                notes_list,
                f"{{{P}}}notesMasterId",
                {f"{{{R}}}id": add_relation(master, "notesMaster")},
            )
    slide_list = ET.SubElement(presentation, f"{{{P}}}sldIdLst")
    for index, slide in enumerate(selected):
        ET.SubElement(
            slide_list,
            f"{{{P}}}sldId",
            id=str(256 + index),
            attrib={f"{{{R}}}id": add_relation(slide, "slide")},
        )
    ET.SubElement(
        presentation,
        f"{{{P}}}sldSz",
        cx=str(sources[0].size[0]),
        cy=str(sources[0].size[1]),
        type="screen16x9",
    )
    ET.SubElement(presentation, f"{{{P}}}notesSz", cx="6858000", cy="9144000")
    parts["ppt/presentation.xml"] = xml_bytes(presentation)
    parts["ppt/_rels/presentation.xml.rels"] = xml_bytes(relations)
    types["ppt/presentation.xml"] = (
        "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"
    )
    root_rels = ET.Element(f"{{{REL}}}Relationships")
    ET.SubElement(
        root_rels,
        f"{{{REL}}}Relationship",
        Id="rId1",
        Type=R + "/officeDocument",
        Target="ppt/presentation.xml",
    )
    parts["_rels/.rels"] = xml_bytes(root_rels)
    content_types = ET.Element(f"{{{CT}}}Types")
    ET.SubElement(
        content_types,
        f"{{{CT}}}Default",
        Extension="rels",
        ContentType="application/vnd.openxmlformats-package.relationships+xml",
    )
    for name, kind in sorted(types.items()):
        ET.SubElement(
            content_types, f"{{{CT}}}Override", PartName="/" + name, ContentType=kind
        )
    parts["[Content_Types].xml"] = xml_bytes(content_types)
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for name, data in sorted(parts.items()):
            archive.writestr(name, data)
    # Byte-level checks cover content, pictures, charts, speaker notes and themes.
    with ZipFile(output) as archive:
        for source in sources:
            for number, original in copied:
                if number != source.number:
                    continue
                if not source.types[original].endswith(
                    "presentationml.slideMaster+xml"
                ):
                    assert (
                        archive.read(source.destination(original))
                        == source.parts[original]
                    )
    return [
        {
            "page": n,
            "source": str(source.path),
            "source_page": index,
            "source_sha256": source.sha256,
            "part": selected[n - 1],
        }
        for n, (source, index) in enumerate(pages, 1)
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=ROOT / "pptx/midterm")
    parser.add_argument(
        "--output", type=Path, default=ROOT / "pptx/midterm/REMUS_Midterm_Final.pptx"
    )
    parser.add_argument(
        "--preview-dir", type=Path, help="Optionally render all 14 pages as PNG"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing output, never source files",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Check sources and print page order without writing",
    )
    parser.add_argument(
        "--officecli",
        default=shutil.which("officecli") or "/home/hgh/.local/bin/officecli",
    )
    args = parser.parse_args()
    names = (
        ["REMUS-midterm.pptx", "REMUS_Midterm_Contents.pptx"]
        + [f"REMUS_Background_Slide_{i}.pptx" for i in range(1, 6)]
        + [f"REMUS_Progress_Slide_{i}.pptx" for i in range(6, 10)]
        + ["REMUS_Prototype_Slide_10.pptx", "REMUS_Future_Work_Slide_11.pptx"]
    )
    sources = [
        Source((args.input_dir / name).resolve(), i) for i, name in enumerate(names, 1)
    ]
    if len(sources[0].slides) != 3 or any(len(s.slides) != 1 for s in sources[1:]):
        parser.error(
            "Expected three frontmatter slides and one slide in each remaining source."
        )
    if any(s.size != sources[0].size for s in sources):
        parser.error("Source slide sizes differ; refusing to stretch slides.")
    pages = [(sources[0], 1)] + [(s, 1) for s in sources[1:]] + [(sources[0], 3)]
    output = args.output.resolve()
    if output in [s.path for s in sources] or (
        output.exists() and any(os.path.samefile(output, s.path) for s in sources)
    ):
        parser.error("Output must not overwrite a source presentation.")
    for n, (source, page) in enumerate(pages, 1):
        print(f"{n:02}. {source.path.name} / slide {page}", flush=True)
    if args.dry_run:
        return
    if output.exists() and not args.force:
        parser.error("Output already exists; use --force to replace it.")
    output.parent.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, OFFICECLI_NO_AUTO_RESIDENT="1")

    def cli(*arguments):
        result = subprocess.run(
            [args.officecli, *map(str, arguments)],
            env=env,
            text=True,
            capture_output=True,
        )
        if result.returncode:
            raise RuntimeError(
                f"OfficeCLI {arguments[0]} failed:\n{result.stdout}{result.stderr}"
            )
        return result.stdout

    # Validate a temporary package before atomically replacing the delivery file.
    with tempfile.TemporaryDirectory(
        prefix="merge-midterm-", dir=output.parent
    ) as work:
        candidate = Path(work) / output.name
        manifest = merge(sources, pages, candidate)
        validation = cli("validate", candidate)
        if "Validation passed" not in validation:
            raise RuntimeError(validation)
        issues = cli("view", candidate, "issues")
        print(validation.strip(), flush=True)
        print(issues.strip(), flush=True)
        cli("close", candidate)
        if args.preview_dir:
            args.preview_dir.mkdir(parents=True, exist_ok=True)
            for page in range(1, len(pages) + 1):
                cli(
                    "view",
                    candidate,
                    "screenshot",
                    "--page",
                    page,
                    "-o",
                    args.preview_dir / f"slide-{page:02}.png",
                )
                print(f"Rendered {page}/{len(pages)}", flush=True)
        for source in sources:
            if hashlib.sha256(source.path.read_bytes()).hexdigest() != source.sha256:
                raise RuntimeError(f"Source changed during merge: {source.path}")
        os.replace(candidate, output)
    output.with_suffix(".manifest.json").write_text(
        json.dumps(
            {"slides": manifest, "validation": validation, "issues": issues},
            ensure_ascii=False,
            indent=2,
        )
        + "\n"
    )
    print(f"Saved: {output}")


if __name__ == "__main__":
    main()
