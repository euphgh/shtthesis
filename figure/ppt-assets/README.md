# REMUS PPT illustration assets

This folder contains 10 ImageGen-generated **PNG raster illustrations** for the REMUS mid-term presentation. They are **not SVG/vector files**; SVG may be redrawn separately later. Each image is 1254×1254 pixels with an alpha channel.

The assets are intended to be reused as standalone illustrations, with arrows, module captions, labels, and flow diagrams constructed as editable PowerPoint elements.

| Filename | Meaning |
| --- | --- |
| `waveform-monitor.png` | RTL simulation and waveform view |
| `fpga-chip.png` | Reusable FPGA chip |
| `global-snapshot.png` | Distributed state snapshot storage |
| `rtl-design.png` | Hierarchical RTL input document |
| `global-pause.png` | Globally synchronized pause |
| `cycle-control.png` | Logical cycle progression |
| `restore-replay.png` | Restore/replay control |
| `state-capture.png` | Capture a state snapshot |
| `fabric-topology.png` | FPGA fabric interconnection |
| `circuit-partitioning.png` | Automated partitioning |

The **source PNG pixels still use the original** Deep Navy, Academic Teal, and Amber Orange palette. The [style guide](../../docs/presentation-style-guide.md) now defaults to Academic Red, but changing the PPT theme cannot recolor raster assets. Keep these originals; any red-theme replacements should be saved separately.
See the [OfficeCLI implementation plan](../../docs/pptx-implementation-plan.md) for slide-by-slide placement and the [design reference index](../presentation-reference/README.md) for intended layouts.

## Placement and reuse

- All ten files were checked as 1254×1254 RGBA PNGs. Their visible bounds and transparent margins differ; use proportional scaling and non-destructive PowerPoint picture cropping to align the visible artwork.
- Keep captions, arrows, status labels, and technical connections editable. Any lettering already inside a PNG, such as `FPGA`, remains raster content.
- `global-pause.png` contains a pause/cycle symbol. Combine it with multiple FPGA nodes and synchronization links to express a global pause.
- `state-capture.png` is a conceptual snapshot illustration, not a scan-chain or DMA architecture diagram.
- Build multi-FPGA arrangements by repeating `fpga-chip.png` and adding editable links. A four-chip illustration does not establish a completed four-FPGA experiment.
- The originally proposed `runtime-control` and `host-interface` assets are not included. They can be drawn with editable PowerPoint shapes and labels.
- Preserve these source PNGs. Put future rendered slide previews in `figure/presentation-preview/`, separate from the component assets and design references.
