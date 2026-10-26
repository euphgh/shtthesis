# Standalone thesis figures

`REMUS_FPGA_RTL_Workflow.pptx` is a one-page editable figure source, independent
of the midterm presentation. It reconstructs `figure/FPGA与RTL全流程图.png` on
a custom 15.2 × 6.08 inch canvas, without a slide title, footer or page number.

- RTL Design and Automated Partitioning reuse the existing PNG illustrations
  in `figure/ppt-assets/`, preserving their aspect ratios and source pixels.
- All six FPGA chips are native PowerPoint groups: solid body, pins and an
  editable centered label. Colors are consistent across deployment, snapshot
  capture and restoration.
- Other labels, waveforms, snapshot cylinder, monitor and connectors are native
  editable elements. Restore and software RTL replay are parallel branches.
- This conceptual workflow does not assert implementation or validation status.

From `thesis/`, run **outside the sandbox**, as required by `AGENTS.md`:

```bash
/usr/bin/python3 scripts/build_fpga_rtl_workflow.py
```

The script writes the PPTX, PNG preview, OfficeCLI batch and check reports to
`build/pptx/fpga-rtl-workflow/`. Inspect the preview before using `--publish`,
which rebuilds and copies the checked PPTX here and the PNG to
`figure/presentation-preview/fpga-rtl-workflow.png`.

The two reused illustrations remain raster assets; this is not an all-vector
figure. For paper placement, check the labels at the actual printed width.
