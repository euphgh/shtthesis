# 实验结果归档

本目录集中保存REMUS中期报告及后续论文的实测材料和实验图片，与报告正文、大纲及[实验需求清单](../src/midterm/experiment_data_checklist.md)分开维护。只有已采集结果写入结果文件，计划与待补项明确标记，不以占位值充当实测。

## 当前内容

| 文件/目录 | 内容 |
| --- | --- |
| [partitioning.md](partitioning.md) | 15组KaHyPar划分结果（含KMH）、标量负载、统计口径及报告使用边界 |
| [board-performance.md](board-performance.md) | PicoRV32/KMH运行频率、检查点分阶段计时、Host—DDR/文件阶段吞吐及一致暂停统计 |
| [raw/board-performance-2026-10-27.md](raw/board-performance-2026-10-27.md) | 原始perf.txt的Markdown归档及SHA-256，保留grep源行号和全部摘录 |
| [raw/perf.txt](raw/perf.txt) | 作者提供的原始性能摘录，保留原文件及链接 |
| [synthesis-utilization.md](synthesis-utilization.md) | 五个DUT双分区、10个Part的EMU_SYSTEM综合资源及利用率，保留层次和BRAM计量口径 |
| [raw/synthesis-utilization-2026-10-27.md](raw/synthesis-utilization-2026-10-27.md) | 10份Vivado综合资源报告全文及SHA-256 |
| [scan-state.md](scan-state.md) | 15组配置、45个Part的寄存器/存储器扫描位数及合计，核对FF_COUNT/MEM_COUNT单位 |
| [raw/scan-state-2026-10-27.md](raw/scan-state-2026-10-27.md) | EMU_SYSTEM参数原始摘录、路径、行号和完整RTL的远端SHA-256 |
| [raw/partitioning-2026-10-27.md](raw/partitioning-2026-10-27.md) | serve41上的12份原始summary文本及SHA-256校验值 |
| [raw/partitioning-kmh-2026-10-27.md](raw/partitioning-kmh-2026-10-27.md) | 后续完成的KMH 2、3、4分区原始summary及校验值，单独保留采集批次 |
| [board-execution.md](board-execution.md) | 手写裸机负载与预期输出、PicoRV32运行图、KMH OpenSBI/暂停保存/Linux启动记录 |
| [figure/](figure/) | 已提供的运行截图及后续实验图片；参见[图片说明](figure/README.md) |

当前划分数据于2026-10-27分两批采集，包含`picorv32`、`rocket`、`xs-minimal`、`nanhu-g`、`kmh`各2、3、4分区，共15组。首批12组原始快照保留不变，KMH三组单独归档；两次采集的checkout HEAD不同，具体标识及比较边界见结果汇总。

2026-10-27补充的板级材料包含PicoRV32的素数/Echo输出，以及KMH运行OpenSBI v1.6后暂停保存、继续启动Linux 6.12.0+的记录。后续加入的`kmh-linux-cli.png`已记录Linux命令行及`cat /proc/cpuinfo`、`uname -a`交互；各图片的完整会话对应与启动墙钟时间仍待核对。

## 目录约定

- 每类实验使用独立Markdown记录，写清来源、采集时间、配置、单位、原始值与派生值，以及实际支持的结论。
- 原始文本按日期归档到`raw/`，后续结果不要无说明地覆盖历史批次。
- 实验图片放在`figure/`，在相应结果Markdown中引用，说明对应数据和配置。
- 本目录图片是实验归档资产；当前中期报告`src/midterm/progress/prototype.tex`直接引用`experiments/figure/`中的四张原图，不另建重复副本。其他正式图仍沿用`thesis/figure/`约定；后续若统一发布位置，应同步引用并保持原始材料可追溯。
- 不将求解成功、组件测试或历史记录扩写为完整系统验收；报告正文另行选取并核对数据。
