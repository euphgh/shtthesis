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

## Checkpoint and replay

`REMUS_Checkpoint_and_Replay.pptx` is a standalone, fully editable 16 × 8 inch
figure reconstructed from `figure/ckpt-and-replay.png`. All objects are native
PowerPoint shapes, groups, text or connectors; no raster illustration is embedded.

- Dashed scan boundaries enclose registers and SRAM, excluding combinational logic.
- The host collects all partition data at the same DUT cycle. Only cycle 0 is
  expanded; overlapping cards labeled DUT Cycle 20 and DUT Cycle 100 represent
  additional checkpoints. These cycle numbers are illustrative.
- Input Traces remain a supporting record without extra arrows. State Mapping
  Metadata has one dashed dependency into the software RTL replay path.
- FPGA Restore uses three equally spaced, staggered chip groups. The stack
  represents multiple targets and does not imply a three-FPGA experiment.

Run outside the sandbox from `thesis/`:

```bash
/usr/bin/python3 scripts/build_checkpoint_replay.py
```

Review `build/pptx/checkpoint-replay/checkpoint-and-replay.png` and its check
reports before using `--publish`. The published preview is
`figure/presentation-preview/checkpoint-and-replay.png`. The original PNG and
the report's existing figure reference are not replaced by this command.
Native drawing helpers are imported from `scripts/build_fpga_rtl_workflow.py`;
checkpoint-specific layout and components belong to the new script.
