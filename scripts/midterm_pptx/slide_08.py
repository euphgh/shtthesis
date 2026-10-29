"""Page 8: automated partitioning and measured per-Part resource distribution."""

from .common import apply_layout_edits, SlideAPI, NAVY, TEAL, inches

TITLE = 'Progress3: Automated Multi-FPGA Circuit Partitioning'
OUTPUT_STEM = "REMUS_Progress_Slide_8"
PREVIEW_STEM = "midterm-progress-08"
slide = SlideAPI(8)

# Vivado 2024.2, KMH two-part EMU_SYSTEM hierarchy. Values are percentages
# of the device capacity reported by Vivado, not percentages of both Parts.
# Source: experiments/synthesis-utilization.md, section 3.2.
RESOURCES = ("LUT", "FF", "BRAM")
PART0 = (73.18, 17.66, 14.31)
PART1 = (75.77, 8.17, 0.00)


# Final reviewed layout for this page. These properties override the base
# component layout below; edit revised text, geometry and rich text here.
LAYOUT_EDITS = {'remove': ['S08.Efficiency.Text'],
 'objects': {'S08.Title': {'props': {'font': 'Arial',
                                     'size': '30pt',
                                     'color': '#183B56',
                                     'bold': 'true',
                                     'align': 'left',
                                     'name': 'S08.Title',
                                     'x': '25.2pt',
                                     'y': '10.08pt',
                                     'width': '910.08pt',
                                     'height': '38.88pt',
                                     'fill': 'none',
                                     'line': 'none',
                                     'margin': '0cm',
                                     'autoFit': 'none'},
                           'paragraphs': [{'command': 'add',
                                           'parent': '{object}/paragraph[1]',
                                           'type': 'run',
                                           'props': {'size': '30pt',
                                                     'bold': 'true',
                                                     'color': '#183B56',
                                                     'text': 'Progress3: Automated '}},
                                          {'command': 'add',
                                           'parent': '{object}/paragraph[1]',
                                           'type': 'run',
                                           'props': {'font.latin': 'Arial',
                                                     'size': '30pt',
                                                     'bold': 'true',
                                                     'color': '#183B56',
                                                     'text': 'Multi-FPGA Circuit Partitioning'}}]},
             'S08.Method.Text3': {'props': {'font': 'Arial',
                                            'size': '19pt',
                                            'color': '#20354A',
                                            'bold': 'false',
                                            'align': 'left',
                                            'name': 'S08.Method.Text3',
                                            'x': '66.24pt',
                                            'y': '290.88pt',
                                            'width': '241.2pt',
                                            'height': '56.16pt',
                                            'fill': 'none',
                                            'font.latin': 'Arial',
                                            'line': 'none',
                                            'margin': '0cm',
                                            'autoFit': 'none'},
                                  'paragraphs': [{'command': 'set',
                                                  'path': '{object}/paragraph[1]',
                                                  'props': {'font.latin': 'Arial',
                                                            'size': '19pt',
                                                            'color': '#20354A',
                                                            'text': 'Path-cut number analysis'}},
                                                 {'command': 'add',
                                                  'parent': '{object}',
                                                  'type': 'paragraph',
                                                  'props': {'font.latin': 'Arial',
                                                            'size': '19pt',
                                                            'color': '#20354A',
                                                            'text': 'for LI-TDM'}}]},
             'S08.Efficiency.Status': {'props': {'font': 'Arial',
                                                 'size': '18pt',
                                                 'color': '#183B56',
                                                 'bold': 'false',
                                                 'align': 'left',
                                                 'name': 'S08.Efficiency.Status',
                                                 'x': '28.8pt',
                                                 'y': '372.6pt',
                                                 'width': '311.04pt',
                                                 'height': '2386232emu',
                                                 'fill': 'none',
                                                 'font.latin': 'Arial',
                                                 'line': 'none',
                                                 'margin': '0cm',
                                                 'autoFit': 'none'},
                                       'paragraphs': [{'command': 'set',
                                                       'path': '{object}/paragraph[1]',
                                                       'props': {'font.latin': 'Arial',
                                                                 'size': '22pt',
                                                                 'bold': 'true',
                                                                 'color': '#183B56',
                                                                 'text': 'Experimental Results:'}},
                                                      {'command': 'add',
                                                       'parent': '{object}',
                                                       'type': 'paragraph',
                                                       'props': {}},
                                                      {'command': 'add',
                                                       'parent': '{object}',
                                                       'type': 'paragraph',
                                                       'props': {'indent': '-22.5pt',
                                                                 'marginLeft': '22.5pt',
                                                                 'bulletRaw': '<a:buFont '
                                                                              'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                              'charset="0" '
                                                                              'panose="020B0604020202020204" '
                                                                              'pitchFamily="34" '
                                                                              'typeface="Arial" '
                                                                              '/><a:buChar '
                                                                              'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                              'char="•" />'}},
                                                      {'command': 'add',
                                                       'parent': '{object}/paragraph[3]',
                                                       'type': 'run',
                                                       'props': {'color': '#183B56',
                                                                 'text': 'The hypergraph size was '
                                                                         'reduced to '}},
                                                      {'command': 'add',
                                                       'parent': '{object}/paragraph[3]',
                                                       'type': 'run',
                                                       'props': {'color': '#183B56',
                                                                 'text': '1/10'}},
                                                      {'command': 'add',
                                                       'parent': '{object}',
                                                       'type': 'paragraph',
                                                       'props': {'indent': '-22.5pt',
                                                                 'marginLeft': '22.5pt',
                                                                 'bulletRaw': '<a:buFont '
                                                                              'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                              'charset="0" '
                                                                              'panose="020B0604020202020204" '
                                                                              'pitchFamily="34" '
                                                                              'typeface="Arial" '
                                                                              '/><a:buChar '
                                                                              'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                              'char="•" />'}},
                                                      {'command': 'add',
                                                       'parent': '{object}/paragraph[4]',
                                                       'type': 'run',
                                                       'props': {'color': '#183B56',
                                                                 'text': 'No significant change in '
                                                                         'the'}},
                                                      {'command': 'add',
                                                       'parent': '{object}/paragraph[4]',
                                                       'type': 'run',
                                                       'props': {'color': '#183B56', 'text': ' '}},
                                                      {'command': 'add',
                                                       'parent': '{object}/paragraph[4]',
                                                       'type': 'run',
                                                       'props': {'color': '#183B56', 'text': 'c'}},
                                                      {'command': 'add',
                                                       'parent': '{object}/paragraph[4]',
                                                       'type': 'run',
                                                       'props': {'color': '#183B56', 'text': 'ut'}},
                                                      {'command': 'add',
                                                       'parent': '{object}/paragraph[4]',
                                                       'type': 'run',
                                                       'props': {'color': '#183B56', 'text': '-'}},
                                                      {'command': 'add',
                                                       'parent': '{object}/paragraph[4]',
                                                       'type': 'run',
                                                       'props': {'color': '#183B56',
                                                                 'text': 'size and path'}},
                                                      {'command': 'add',
                                                       'parent': '{object}/paragraph[4]',
                                                       'type': 'run',
                                                       'props': {'color': '#183B56', 'text': '-'}},
                                                      {'command': 'add',
                                                       'parent': '{object}/paragraph[4]',
                                                       'type': 'run',
                                                       'props': {'color': '#183B56',
                                                                 'text': 'cut'}},
                                                      {'command': 'add',
                                                       'parent': '{object}/paragraph[4]',
                                                       'type': 'run',
                                                       'props': {'color': '#183B56', 'text': ' '}},
                                                      {'command': 'add',
                                                       'parent': '{object}/paragraph[4]',
                                                       'type': 'run',
                                                       'props': {'color': '#183B56',
                                                                 'text': 'number'}},
                                                      {'command': 'add',
                                                       'parent': '{object}',
                                                       'type': 'paragraph',
                                                       'props': {}}]},
             'S08.Results.Context': {'props': {'font': 'Arial',
                                               'size': '18pt',
                                               'color': '#183B56',
                                               'bold': 'false',
                                               'align': 'left',
                                               'name': 'S08.Results.Context',
                                               'x': '344.16pt',
                                               'y': '126.72pt',
                                               'width': '588.96pt',
                                               'height': '25.2pt',
                                               'fill': 'none',
                                               'font.latin': 'Arial',
                                               'line': 'none',
                                               'margin': '0cm',
                                               'autoFit': 'none'},
                                     'paragraphs': [{'command': 'set',
                                                     'path': '{object}/paragraph[1]',
                                                     'props': {'font.latin': 'Arial',
                                                               'color': '#183B56',
                                                               'text': 'KMH · Two partitions · '
                                                                       'Utilization (%)'}}]},
             'S08.Resources.Chart': {'props': {'chartStyle': '2',
                                               'autoTitleDeleted': 'true',
                                               'style': '2',
                                               'roundedCorners': 'true',
                                               'gridline.spPr': '<c:spPr '
                                                                'xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart"><a:ln '
                                                                'w="6350" '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:solidFill><a:srgbClr '
                                                                'val="DDE5EA" '
                                                                '/></a:solidFill></a:ln></c:spPr>',
                                               'catAx.txPr': '<c:txPr '
                                                             'xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart"><a:bodyPr '
                                                             'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                             '/><a:lstStyle '
                                                             'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                             '/><a:p '
                                                             'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:pPr><a:defRPr '
                                                             'sz="1600"><a:solidFill><a:srgbClr '
                                                             'val="20354A" '
                                                             '/></a:solidFill><a:latin '
                                                             'typeface="Arial" /><a:ea '
                                                             'typeface="Arial" '
                                                             '/></a:defRPr></a:pPr><a:endParaRPr '
                                                             'lang="en-CN" /></a:p></c:txPr>',
                                               'valAx.txPr': '<c:txPr '
                                                             'xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart"><a:bodyPr '
                                                             'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                             '/><a:lstStyle '
                                                             'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                             '/><a:p '
                                                             'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:pPr><a:defRPr '
                                                             'sz="1600"><a:solidFill><a:srgbClr '
                                                             'val="20354A" '
                                                             '/></a:solidFill><a:latin '
                                                             'typeface="Arial" /><a:ea '
                                                             'typeface="Arial" '
                                                             '/></a:defRPr></a:pPr><a:endParaRPr '
                                                             'lang="en-CN" /></a:p></c:txPr>',
                                               'series1.dlbls': '<c:dLbls '
                                                                'xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart"><c:spPr><a:noFill '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                '/><a:ln '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:noFill '
                                                                '/></a:ln><a:effectLst '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                '/></c:spPr><c:txPr><a:bodyPr '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                '/><a:lstStyle '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                '/><a:p '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:pPr><a:defRPr '
                                                                'sz="1800"><a:solidFill><a:srgbClr '
                                                                'val="20354A" '
                                                                '/></a:solidFill><a:latin '
                                                                'typeface="Arial" /><a:ea '
                                                                'typeface="Arial" '
                                                                '/></a:defRPr></a:pPr><a:endParaRPr '
                                                                'lang="en-CN" '
                                                                '/></a:p></c:txPr><c:dLblPos '
                                                                'val="outEnd" /><c:showLegendKey '
                                                                'val="0" /><c:showVal val="1" '
                                                                '/><c:showCatName val="0" '
                                                                '/><c:showSerName val="0" '
                                                                '/><c:showPercent val="0" '
                                                                '/><c:showBubbleSize val="1" '
                                                                '/><c:showLeaderLines val="0" '
                                                                '/><c:extLst><c:ext '
                                                                'xmlns:c15="http://schemas.microsoft.com/office/drawing/2012/chart" '
                                                                'uri="{CE6537A1-D6FC-4f65-9D91-7224C49458BB}"><c15:showLeaderLines '
                                                                'val="0" '
                                                                '/></c:ext></c:extLst></c:dLbls>',
                                               'series2.dlbls': '<c:dLbls '
                                                                'xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart"><c:spPr><a:noFill '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                '/><a:ln '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:noFill '
                                                                '/></a:ln><a:effectLst '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                '/></c:spPr><c:txPr><a:bodyPr '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                '/><a:lstStyle '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                '/><a:p '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:pPr><a:defRPr '
                                                                'sz="1800"><a:solidFill><a:srgbClr '
                                                                'val="20354A" '
                                                                '/></a:solidFill><a:latin '
                                                                'typeface="Arial" /><a:ea '
                                                                'typeface="Arial" '
                                                                '/></a:defRPr></a:pPr><a:endParaRPr '
                                                                'lang="en-CN" '
                                                                '/></a:p></c:txPr><c:dLblPos '
                                                                'val="outEnd" /><c:showLegendKey '
                                                                'val="0" /><c:showVal val="1" '
                                                                '/><c:showCatName val="0" '
                                                                '/><c:showSerName val="0" '
                                                                '/><c:showPercent val="0" '
                                                                '/><c:showBubbleSize val="1" '
                                                                '/><c:showLeaderLines val="0" '
                                                                '/><c:extLst><c:ext '
                                                                'xmlns:c15="http://schemas.microsoft.com/office/drawing/2012/chart" '
                                                                'uri="{CE6537A1-D6FC-4f65-9D91-7224C49458BB}"><c15:showLeaderLines '
                                                                'val="0" '
                                                                '/></c:ext></c:extLst></c:dLbls>',
                                               'dataLabels': 'none'}},
             'S08.Results.Observation': {'props': {'x': '416.16pt', 'y': '453.6pt'}},
             'S08.Results.Scope': {'props': {'font': 'Arial',
                                             'size': '12pt',
                                             'color': '#607184',
                                             'bold': 'false',
                                             'align': 'left',
                                             'name': 'S08.Results.Scope',
                                             'x': '344.16pt',
                                             'y': '498.24pt',
                                             'width': '588.96pt',
                                             'height': '20.16pt',
                                             'fill': 'none',
                                             'font.latin': 'Arial',
                                             'line': 'none',
                                             'margin': '0cm',
                                             'autoFit': 'none'},
                                   'paragraphs': [{'command': 'set',
                                                   'path': '{object}/paragraph[1]',
                                                   'props': {'size': '12pt'}}]}}}


def build_commands():
    """Use an editable chart for resource evidence and qualify early efficiency observations.

    The native chart embeds the measured data. Unfinished netlist-baseline
    comparisons and provisional ratios are deliberately not charted as results.
    """
    commands = [slide.title(size=30)]
    commands.append(slide.shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    commands.append(slide.shape("Method.Heading", 0.40, 1.20, 3.95, 0.5,
                                text="Automated Partitioning", size=22,
                                bold="true", color=NAVY))
    for index, text in enumerate([
        "Adaptive-granularity\nRTL partitioning",
        "KaHyPar-based\nhypergraph partitioning",
        "Path-cut analysis\nfor LI-TDM",
    ], 1):
        y = 2.00 + (index - 1) * 1.02
        commands.append(slide.shape(f"Method.Number{index}", 0.42, y + 0.04,
                                    0.33, 0.33, text=str(index), size=14, bold="true",
                                    color="FFFFFF", fill=TEAL, preset="ellipse",
                                    align="center", valign="middle"))
        commands.append(slide.shape(f"Method.Text{index}", 0.92, y, 3.35, 0.78,
                                    text=text, size=19))
    commands.append(slide.shape("Efficiency.Status", 0.40, 5.43, 3.95, 0.35,
                                text="Preliminary observation", size=14, color="607184"))
    commands.append(slide.shape("Efficiency.Text", 0.40, 5.87, 3.95, 1.05,
                                text="Smaller graphs and faster solving\non well-structured RTL.",
                                size=18, color=NAVY))

    commands.append(slide.shape("Results.Heading", 4.78, 1.20, 8.18, 0.5,
                                text="Post-Synthesis Resource Utilization", size=22,
                                bold="true", color=NAVY))
    commands.append(slide.shape("Results.Context", 4.78, 1.76, 8.18, 0.35,
                                text="KMH · Two partitions · Utilization (%)", size=16,
                                color="607184"))
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "chart",
        "props": {
            "name": "S08.Resources.Chart", "chartType": "column",
            "x": inches(4.72), "y": inches(2.18),
            "width": inches(8.25), "height": inches(3.80),
            "categories": ",".join(RESOURCES),
            "series1.name": "Part 0", "series1.values": ",".join(f"{v:.2f}" for v in PART0),
            "series1.color": NAVY,
            "series2.name": "Part 1", "series2.values": ",".join(f"{v:.2f}" for v in PART1),
            "series2.color": TEAL,
            "title": "none", "legend": "top", "legendFont": "15:20354A:Arial",
            "axisfont": "16:20354A:Arial", "axismin": "0", "axismax": "90",
            "majorunit": "20", "axisnumfmt": "0",
            "dataLabels": "value", "labelPos": "outsideEnd",
            "labelfont": "18:20354A:Arial", "gapwidth": "90", "overlap": "-15",
            "gridlines": "DDE5EA:0.5", "chartareafill": "FFFFFF",
            "plotFill": "FFFFFF", "plotborder": "none", "chartborder": "none",
            "seriesoutline": "none",
        },
    })
    commands.append(slide.shape("Results.Observation", 4.78, 6.22, 8.18, 0.65,
                                text="Similar LUT usage, uneven FF and BRAM distribution.",
                                size=20, color=NAVY))
    commands.append(slide.shape("Results.Scope", 4.78, 6.92, 8.18, 0.28,
                                text="EMU_SYSTEM synthesis; percentages of device capacity.",
                                size=12, color="607184"))
    commands.append(slide.shape("PageNumber", 12.72, 7.25, 0.25, 0.20,
                                text="8", size=10, color="607184", align="right"))
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "notes",
        "props": {"text": (
            "REMUS implements adaptive RTL granularity selection, weighted hypergraph "
            "partitioning using KaHyPar, and path-cut analysis for LI-TDM configuration. "
            "The author's revised slide reports graph size around one tenth of the "
            "netlist-level baseline, with no significant change in cut-size and "
            "path-cut number. These are author-reported comparisons; this slide "
            "synchronization does not independently validate the baseline runs. "
            "Confirm matched DUTs, configurations and graph-size definitions when "
            "finalizing the experimental record. "
            "The main chart uses archived KMH two-Part Vivado 2024.2 synthesis results: "
            "Part 0 LUT/FF/BRAM utilization 73.18/17.66/14.31 percent; Part 1 "
            "75.77/8.17/0.00 percent. BRAM counts are 288.5 and 0 tiles. URAM "
            "is 13 versus 0, omitted from the plot for focus. The scope is "
            "role_i/ClockResetCore_0/emu_system, including inserted infrastructure; "
            "not pure DUT, full board consumption, or post-route utilization. "
            "The denominator is whole-device capacity, not the remaining Part budget. "
            "The observed resource asymmetry does not isolate adaptive granularity or "
            "scalar weights as its sole cause. Constraints, module grouping and synthesis "
            "mapping may also matter. Exact build matching between partition summaries "
            "and synthesis reports remains to be completed, so no estimation-error or "
            "baseline-gain inference is made from their combination. "
            "Sources: experiments/synthesis-utilization.md (3.2); "
            "src/midterm/progress/partitioning.tex; src/midterm/problems.tex."
        )},
    })
    commands = apply_layout_edits(commands, LAYOUT_EDITS)
    # Explicit title spacing and page-specific finishing objects.
    commands.extend([{'command': 'set', 'path': '/slide[1]/shape[@name=S08.Title]', 'props': {'lineSpacing': '0.9x'}},
     {'command': 'raw-set',
      'part': '/ppt/slides/charts/chart1.xml',
      'xpath': '//c:barChart/c:gapWidth',
      'action': 'insertbefore',
      'xml': '<c:dLbls><c:dLblPos val="outEnd"/><c:showLegendKey val="0"/><c:showVal '
             'val="1"/><c:showCatName val="0"/><c:showSerName val="0"/><c:showPercent '
             'val="0"/><c:showBubbleSize val="1"/></c:dLbls>'}])
    return commands
