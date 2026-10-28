# REMUS中期答辩PPT大纲

## 定位与范围

- **用途**：硕士学位论文中期答辩，正文全英文，围绕“从多FPGA原型验证到可暂停、可观测、可重放的多FPGA硬件仿真系统”展开。
- **规模**：11页正文（背景与目标5页、技术进展4页、双FPGA原型及实验1页、问题与计划1页）；封面与结束页分别单列时合计约13页。根据实际答辩时长和实验材料可小幅调整。
- **叙事主线**：Why multi-FPGA? → Research gap & goal → REMUS workflow → Cycle-accurate execution & pause → Distributed state & replay → Automated partitioning → Runtime & Fabric → Dual-FPGA prototype & evaluation → Challenges & future work。
- **术语**：新报告中的系统称REMUS（Replay EMUlation System）；开题阶段的SMART保留为历史名称，不在新页中混用。系统能力和实验完成状态须与最新研究材料一致。
- **风格入口**：[演示文稿视觉规范](presentation-style-guide.md)；学术定位见[论文写作指导](thesis-writing-guidelines.md)；详细技术背景见[中期论文大纲](../src/midterm/outline.md)。

## 第一部分：Background & Research Goal（第1–5页）

| 页码 | Slide Title | 核心信息 | 主要视觉表现 |
| --- | --- | --- | --- |
| 1 | From RTL Simulation to Multi-FPGA Prototyping | RTL软件仿真具有可观测性但速度受限；FPGA提升运行速度；多FPGA突破单片容量限制。 | 从RTL Simulation→FPGA Prototyping→Multi-FPGA Prototyping的三层演进图；波形显示器、FPGA、互连芯片图标。 |
| 2 | Multi-FPGA Prototyping Is Fast, but Hard to Debug | 原型验证强调运行速度和容量；硬件仿真还需要Pause、Dump、Restore、Replay及波形观测。 | 左右对比：传统Prototype的有限可见性 vs. Run→Pause→Dump→Restore→Replay能力链。 |
| 3 | Key Challenges of Replayable Multi-FPGA Emulation | 四个挑战：周期一致的全局暂停、跨FPGA周期精确执行、分布式状态管理、高质量自动化划分。 | 四象限技术问题卡片；每象限1个简图、1句结论。 |
| 4 | Research Gap and Goal | 多FPGA原型验证具备扩展能力；单FPGA Scan Dump有状态重放基础；研究目标是同时具备多FPGA扩展和全局状态调试。 | 3列能力对比矩阵，明确区别“已知技术能力”和“本课题拟实现能力”。 |
| 5 | REMUS: Overall Workflow and Mid-Term Scope | 概括RTL输入、自动划分、多FPGA部署、周期精确执行与暂停、状态提取及重放；界定中期工作范围。 | 五阶段总体工作流与简短的Mid-Term Scope；不重复第4页研究目标。 |

`pptx/midterm/`保留当前REMUS新主题页面，已被替代的SMART旧配色草稿已清理；后续页面继续遵循统一视觉规范。

## 第二部分：Mid-Term Research Progress（第6–9页）

前5页已介绍背景、相关研究、REMUS架构与中期范围，因此**不再单设“Mid-Term Progress Overview”页面**。第6～9页分别介绍一个技术方向。采用“解决的问题→采用的方法→阶段性结果”的讲述顺序，页面以关键词和论文现有图示为主，不展开完整算法、RTL实现或复杂公式。

| 页码 | Slide Title | 这一页需要说明什么 | 论文配图或证据 |
| --- | --- | --- | --- |
| 6 | Cycle-Accurate Multi-FPGA Execution and Pause | 基于DUOHUAFEN的LI-TDM实现周期精确执行，优化首尾传播阶段并提出多FPGA一致暂停协调方法。 | `figure/dual-fpga-consistent-pause-timing.png` |
| 7 | Distributed State Capture, Restore and Replay | 复用REMU Scan Dump，将分区状态组织为全局检查点；FPGA按分区写回，软件通过状态映射恢复RTL。 | `experiments/figure/picorv32-cosim-vs-replay-state-tick42080.png` |
| 8 | Automated Multi-FPGA Circuit Partitioning | 自适应粒度划分、资源感知超图、KaHyPar求解及Path-Cut Number分析；展示阶段性数据。 | `experiments/partitioning.md`、`experiments/synthesis-utilization.md` |
| 9 | Scalable Multi-FPGA Runtime and Fabric | 说明PCIe直连架构的扩展限制、Fabric统一资源访问方案及真实验证进度。 | 论文中的PCIe Direct与Fabric架构对比图 |

### Slide 6. Cycle-Accurate Execution and Global Pause

**1. Cycle-Accurate Execution**

- LI-TDM-based execution
- Optimized communication flow

来源标注：Based on DUOHUAFEN。

**2. Cycle-Consistent Global Pause**

- Stabilize progress
- Set a common target
- Advance and verify

**说明**：按答辩时间限制压缩LI-TDM说明，首尾阶段优化细节及减少冗余收发的效果留在讲稿，不宣称已测得百分比性能增益。右侧直接裁取`figure/presentation-reference/midterm-progress-06-v1.png`中的暂停插图，保留接收屏障、共同目标、差异化步进与最终检查四阶段；41、42、43为示意周期，不是实验记录。删除设计图左侧“One fewer”框、“Different progress”句子和底部“A common DUT”结论行。屏障确认不等同于最终一致暂停完成。正文依据：`src/midterm/progress/cycle_control.tex`。

### Slide 7. Distributed State Capture, Restore and Replay

**1. Global Snapshot**

- Capture partition states at the same DUT cycle.
- Reuse REMU's Scan Dump mechanism.

**2. FPGA Restore**

- Write back scan data by partition.
- Restore local registers, SRAM and memory.

**3. Software RTL Replay**

- Decode partition data through state mapping.
- Load RTL states and replay recorded inputs.

**版式**：采用已确认的`figure/presentation-reference/midterm-state-replay-07-v2.png`。
左侧集中说明方法，突出按分区写回和通过状态映射恢复RTL；右侧用真实波形对照替换设计图占位框，
不添加上方流程图，不展开实验周期、配置或信号数量。
图下仅保留一句结论：`Waveform replay reproduces the same signal values as FPGA execution.`

**说明**：图源为`experiments/figure/picorv32-cosim-vs-replay-state-tick42080.png`，
截图直接展示双Part Cosim检查点与软件RTL重放的对照，须保留简短图源标签，不把它标成物理FPGA运行截图。
上述系统结论沿用作者确认的表述；板级与Cosim检查点对照、FPGA恢复结果及本图的软件重放案例是不同证据，
其来源和范围记入讲稿备注。已有结果限于实际测试条件与比较状态，不概括为全状态、全周期等价。
正文依据：`src/midterm/progress/state_replay.tex`；实验依据：`experiments/picorv32-cosim-replay.md`。

### Slide 8. Automated Multi-FPGA Circuit Partitioning

**1. Automated Partitioning**

- Adaptive-granularity RTL partitioning
- KaHyPar-based hypergraph partitioning
- Path-cut analysis for LI-TDM

**2. Preliminary Observation**

- Smaller graphs and faster solving on well-structured RTL.

**3. Post-Synthesis Resource Utilization**

- KMH · Two partitions · Utilization (%)
- Part 0: LUT 73.18%, FF 17.66%, BRAM 14.31%.
- Part 1: LUT 75.77%, FF 8.17%, BRAM 0.00%.
- Similar LUT usage, uneven FF and BRAM distribution.

**说明**：左侧简述已实现的划分方法及一句初步效率观察；作者目前观察到部分层次结构良好的设计图规模约为网表级基线的1/10、超图求解时间约为1/7，但基线实验尚未结束，因此页面不显示这两个待定比例，也不宣称划分质量更优。右侧用原生可编辑分组柱状图展示KMH各Part的综合资源分布，为第11页多维资源约束做铺垫。图表保留两位小数的原始值，预览数值标签按一位小数显示。

统计范围为EMU_SYSTEM层次综合结果，利用率分母为器件总容量，并非纯DUT、整个Role/Shell或实现后占用。图中现象不能单独归因于标量权重或自适应粒度；划分summary与综合产物仍需精确匹配。数据源：`experiments/synthesis-utilization.md`第3.2节；正文：`src/midterm/progress/partitioning.tex`。其他设计及粒度基线对比保留作后续或备用材料。

### Slide 9. Scalable Multi-FPGA Runtime

**1. Direct PCIe Access**

- Separate Host connection per FPGA
- Limited by Host PCIe connectivity

**2. Fabric-Based Access**

- One Host entry via Ref
- Unified register and memory access
- Extend through inter-FPGA links

**讲稿中的进度说明（不在页面展示）**

- Fabric components and Driver backend implemented
- Dual-node co-simulation environment established
- Full system validation remains in progress

**说明**：现有双FPGA板级原型采用**Host分别PCIe直连各FPGA**的基础方案；Fabric统一访问为后续扩展设计。组件与Driver后端已有实现及局部测试，但完整双节点联合验收和实际Fabric板级验证尚未完成，不能标为已通过。正文依据：`src/midterm/progress/runtime.tex`；图：`figure/fabric-architecture-comparison-reference.png`。

页面采用左右架构对比，按用户要求不显示Implemented、In progress及Illustrative topology，
下方正文放大至22pt。三节点连接为架构示意，验证边界保留在讲稿中；不以图中的节点数声称已验证规模。

## 第三部分：Prototype & Evaluation（第10页）

### Slide 10. Dual-FPGA Prototype and Evaluation

**1. Experimental Platform**

- Two NM37 boards with VU37P FPGAs
- PCIe access from a shared Host
- QSFP/Aurora links between FPGAs

**2. DUTs and Workloads**

- PicoRV32 · Rocket: Bare-metal programs
- Nanhu · KMH: OpenSBI and Linux

**3. Board-Level Execution**

- KMH boots Linux and supports interactive shell commands.

**4. Preliminary Performance**

- PicoRV32: ~0.327 MHz
- KMH: ~0.322 MHz
- Global pause latency: ~0.8–1.1 ms in recorded tests

**说明**：

- 此页采用已确认的“左侧实物平台、右侧运行结果、底部性能数据”版式。实物图使用`figure/remus-2fpga-hw.jpg`，裁去上方大部分示波器，突出Host内两块板卡；右侧用两行表格列出DUT与负载，并裁取`experiments/figure/kmh-2fpga-linux-cli.png`中的Shell交互区域。图片保持原始比例与源像素，文字及表格可编辑。本页为PCIe直连原型，不把Fabric架构描述为已上板验证。
- 频率分别来自PicoRV32和KMH当前归档的**较长run片段**，后者为保存检查点前的窗口；不是全部DUT或整个Linux启动的频率。Rocket与Nanhu当前没有同口径定量频率，不预填。
- 暂停延迟为已记录的**Host可见全局同步暂停完成耗时**：PicoRV32 23条约0.804–0.925 ms、KMH 1条约1.047 ms，范围只描述当前记录，不代表独立重复实验或纯硬件屏障延迟。
- 本页不增加检查点耗时、综合资源表或暂停重放机制说明。底部仅保留三个指标及测量口径：`Measured run windows; KMH measured before checkpoint save. Pause latency includes Host control.`
- 正文：`src/midterm/progress/summary.tex`；实验：`experiments/board-execution.md`、`experiments/board-performance.md`及`experiments/figure/`。

## 第四部分：Problems & Next Plan（第11页）

### Slide 11. Current Challenges and Future Work

此页以文字为主，用对应关系压缩当前问题和后续方案，不再新增技术图示。

| Current Challenges | Future Work |
| --- | --- |
| Imbalanced FPGA Resource Utilization | Multi-Dimensional Resource-Aware Partitioning |
| Limited Multi-FPGA Execution Performance | Communication & Cycle Execution Optimization |
| Fabric Polling Overhead | Interrupt-Driven Runtime Control |
| Limited Scale of Current Prototype | Four-FPGA Extension & Large-Scale SoC Validation |

**Thesis & Evaluation Plan**

- Complete Functional & Performance Evaluation
- Extend Multi-FPGA Experiments
- Thesis Writing and Final Defense

**说明**：对应`src/midterm/problems.tex`和`src/midterm/next_plan.tex`。多维资源约束、中断驱动及四FPGA扩展是下一阶段计划，不写成既有成果。预计答辩时间以学校/导师正式安排为准，尚未确认时不填入精确日期。

## 封面、目录与结束页

- **封面**：在上述11页正文之外单独制作；采用院校/研究机构标识、中文正式学位论文题目及英文译名、身份与日期信息，具体字段以学校要求为准。
- **目录**：可与封面后的部分过渡页合并，优先不占用技术正文页数；若单独增加目录页，应相应调整总页数。
- **结束页**：简洁的“Thank You / Q&A”，与封面保持视觉呼应。

## 制作状态与内容依赖

- 第1页：新主题状态为`PPTX Created`；[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_1.pptx)和[PNG预览](../figure/presentation-preview/midterm-background-01.png)已生成，OfficeCLI结构检查与独立PNG视觉检查通过，PowerPoint桌面端复核待完成。
- 第2页：新主题状态为`PPTX Created`；[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_2.pptx)和[PNG预览](../figure/presentation-preview/midterm-background-02.png)已生成，OfficeCLI结构检查与独立PNG视觉检查通过，PowerPoint桌面端复核待完成。右栏以`Target capabilities`标明研究目标。
- 第3页：新主题状态为`PPTX Created`；[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_3.pptx)和[PNG预览](../figure/presentation-preview/midterm-background-03.png)已生成，OfficeCLI结构检查与独立PNG视觉检查通过，PowerPoint桌面端复核待完成。四象限表达研究挑战，既有PPTX展开了旧术语PPD；生成脚本现改用Path-Cut Number，需重新生成并复核PPTX与PNG后，才能认为交付文件已完成术语统一。其他全局暂停说明保持原有设计。
- 第4页：新主题状态为`PPTX Created`；[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_4.pptx)和[PNG预览](../figure/presentation-preview/midterm-background-04.png)已生成，OfficeCLI结构检查与独立PNG视觉检查通过，PowerPoint桌面端复核待完成。三栏区分原型验证侧重点、单FPGA容量限制与REMUS研究目标。
- 第5页：新主题状态为`PPTX Created`；[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_5.pptx)和[PNG预览](../figure/presentation-preview/midterm-background-05.png)已生成，OfficeCLI结构检查与独立PNG视觉检查通过，PowerPoint桌面端复核待完成。采用更新后的五阶段设计；State Capture与前四阶段使用相同蓝色系，旧PPTX中的Restore/Replay被标为计划，但截至最新中期正文已具有阶段性实现与测试结果；正式使用前需同步更新该标签。底部圆点表示工作范围。
- 第6页：状态为`PPTX Created`；[PPTX](../pptx/midterm/REMUS_Progress_Slide_6.pptx)和[PNG预览](../figure/presentation-preview/midterm-progress-06.png)已生成。标题、左侧文字与页码可编辑，右侧按用户要求复用设计图的裁剪图片；OfficeCLI校验、问题检查及PNG视觉复核通过，PowerPoint桌面端复核待完成。
- 第7页：状态为`PPTX Created`；[PPTX](../pptx/midterm/REMUS_Progress_Slide_7.pptx)和[PNG预览](../figure/presentation-preview/midterm-progress-07.png)已生成。采用已确认的v2设计，左侧方法说明、右侧真实波形对照与一句结论。17个原生形状可编辑，1张实验截图原样嵌入；OpenXML校验、OfficeCLI问题检查、字体/边界检查及PNG视觉复核通过。PowerPoint桌面端复核待完成。
- 第9页：状态为`PPTX Created`；[PPTX](../pptx/midterm/REMUS_Progress_Slide_9.pptx)和[PNG预览](../figure/presentation-preview/midterm-progress-09.png)已生成。架构图、箭头与文字均为原生可编辑元素，下方正文22pt；OfficeCLI校验、问题检查及PNG视觉复核通过。PowerPoint桌面端复核待完成。
- 第10页：状态为`PPTX Created`；[PPTX](../pptx/midterm/REMUS_Prototype_Slide_10.pptx)和[PNG预览](../figure/presentation-preview/midterm-prototype-10.png)已生成。左侧实物照片、右侧DUT表格与Linux截图、底部三项性能指标；29个原生形状可编辑，2张原始图片通过PPT裁剪。OpenXML、OfficeCLI问题检查、字体/边界/图片比例检查及独立PNG视觉复核通过，PowerPoint桌面端复核待完成。
- 第8页：状态为`PPTX Created`；[PPTX](../pptx/midterm/REMUS_Progress_Slide_8.pptx)和[PNG预览](../figure/presentation-preview/midterm-progress-08.png)已生成。方法说明、初步效率观察及KMH分组柱状图均可编辑；OfficeCLI校验、问题检查、图表数据核对与PNG视觉复核通过。PowerPoint桌面端复核待完成。
- 第11页：英文标题及文字初稿已确认，PPTX尚未制作；按对应论文图与实验材料制作，不得将已规划文字视为已制作页面。
- 建议维护状态：`Planned`、`Designed`、`PPTX Created`、`Reviewed`。完成状态需随提交更新，避免以规划代替实际进度。
- 制作入口：[OfficeCLI实施计划](pptx-implementation-plan.md)、[设计参考索引](../figure/presentation-reference/README.md)、[组件资产索引](../figure/ppt-assets/README.md)。
