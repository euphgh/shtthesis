# 实验结果归档

本目录集中保存REMUS中期报告及后续论文的实测材料和实验图片，与报告正文、大纲及[实验需求清单](../src/midterm/experiment_data_checklist.md)分开维护。只有已采集结果写入结果文件，计划与待补项明确标记，不以占位值充当实测。

当前划分数据分**两个算法批次**维护，目录名相同但算法与数值均不同，不可混用：

- **自适应划分批次**（2026-10-27）：下表中未加“网表”前缀的文件，共15组。
- **网表划分批次**（2026-11-04）：2026-10-28起serve41改用基于网表的划分后重新生成的RTL、综合与划分结果，见下文“网表划分批次”一节。

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
| [board-execution.md](board-execution.md) | 裸机与Linux板级记录，以及作者确认的单板、双板检查点与Cosim一致性结果 |
| [picorv32-cosim-replay.md](picorv32-cosim-replay.md) | 双Part Cosim的2048周期检查点，经Icarus Verilog恢复重放，在绝对周期42080比较六个选定信号 |
| [picorv32-cosim-cycle-state.md](picorv32-cosim-cycle-state.md) | 单Part与双Part Cosim的串口输出、42080周期四项寄存器及不同层次名称的对应关系 |
| [figure/](figure/) | 已提供的运行截图及后续实验图片；参见[图片说明](figure/README.md) |

当前划分数据于2026-10-27分两批采集，包含`picorv32`、`rocket`、`xs-minimal`、`nanhu-g`、`kmh`各2、3、4分区，共15组。首批12组原始快照保留不变，KMH三组单独归档；两次采集的checkout HEAD不同，具体标识及比较边界见结果汇总。

2026-10-27补充的板级材料包含PicoRV32的素数/Echo输出，以及KMH运行OpenSBI v1.6后暂停保存、继续启动Linux 6.12.0+的记录。后续加入的`kmh-2fpga-linux-cli.png`已记录Linux命令行及`cat /proc/cpuinfo`、`uname -a`交互；各图片的完整会话对应与启动墙钟时间仍待核对。

2026-10-28补充首个有具体周期与信号值对照的非零检查点软件重放案例：PicoRV32在双Part Cosim中保存2048和42080周期检查点，Icarus Verilog从2048恢复重放100000周期，在相对周期40032处比较六项信号，图示数值一致。作者已明确该参考环境为Cosim，不作为物理双FPGA上板恢复证据；详细比较范围及输入轨迹警告见独立记录。

同日另补单Part参考：在相同42080逻辑周期保存检查点，与双Part全局暂停检查点比较，图中四个对应寄存器值一致，串口可见输出前缀也相同。该案例单独记录层次展开、重新打包后的名称对应，与软件恢复重放案例互补，不混同为全状态或全周期等价证明。

随后作者进一步确认已完成单板、双板上板检查点与相应Cosim检查点的比较，结果一致，具体板级周期、比较范围和原始记录继续归档。当前中期正文已将Cosim同周期对照写入1.2、非零检查点软件重放写入1.3、板级检查点对照写入1.6，并同步阶段总结；不将Cosim图像用作物理板级证据。

## 网表划分批次

2026-10-28起`serve41`上的RTL与部分综合改为**基于网表的划分**（`transform/src/partition/decomposer.cc`中自适应展开阈值分支被关闭），并重新生成了划分、RTL与综合结果。该批次与上面的自适应批次是两组独立数据，目录名相同、数值不同，引用时须先确认批次。

| 文件/目录 | 内容 |
| --- | --- |
| [netlist-partitioning.md](netlist-partitioning.md) | 网表划分下15组结果：图规模、求解时间、Cut Size、km1、N_cut、阶段数、标量负载，以及与自适应批次的对照 |
| [raw/netlist-partitioning-2026-11-04.md](raw/netlist-partitioning-2026-11-04.md) | 15份summary原文、mtime与SHA-256 |
| [netlist-scan-state.md](netlist-scan-state.md) | 网表划分RTL的45个Part扫描寄存器/存储器位数及合计 |
| [raw/netlist-scan-state-2026-11-04.md](raw/netlist-scan-state-2026-11-04.md) | 45份`EmuScanCtrl`参数摘录、行号、十六进制原值与完整RTL SHA-256 |
| [netlist-synthesis-utilization.md](netlist-synthesis-utilization.md) | 网表划分EMU_SYSTEM综合资源：40份报告覆盖2/3/4分区，缺5个Part |
| [raw/netlist-synthesis-utilization-2026-11-04.md](raw/netlist-synthesis-utilization-2026-11-04.md) | 40份Vivado综合报告全文及SHA-256 |

采集时间统一为`2026-11-04T04:18:18Z`，采集时远端checkout为`vivado2024.2` / `828600a0`。该批次各配置的生成时间分散在2026-10-28至2026-11-04之间，不是同一次批量运行；`picorv32_part2`的综合报告早于其当前RTL，引用时须注意时间差。

## 目录约定

- 每类实验使用独立Markdown记录，写清来源、采集时间、配置、单位、原始值与派生值，以及实际支持的结论。
- 原始文本按日期归档到`raw/`，后续结果不要无说明地覆盖历史批次。
- 实验图片放在`figure/`，在相应结果Markdown中引用，说明对应数据和配置。
- 本目录图片是实验归档资产；当前中期报告`src/midterm/progress/prototype.tex`直接引用`experiments/figure/`中的四张原图，不另建重复副本。其他正式图仍沿用`thesis/figure/`约定；后续若统一发布位置，应同步引用并保持原始材料可追溯。
- 不将求解成功、组件测试或历史记录扩写为完整系统验收；报告正文另行选取并核对数据。
