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
| 7 | Distributed State Capture, Restore and Replay | 复用REMU Scan Dump，将分区状态组织为全局检查点，支持FPGA恢复和软件RTL重放。 | `figure/ckpt-and-replay.png` |
| 8 | Automated Multi-FPGA Circuit Partitioning | 自适应粒度划分、资源感知超图、KaHyPar求解及Path-Cut Number分析；展示阶段性数据。 | `experiments/partitioning.md`、`experiments/synthesis-utilization.md` |
| 9 | Scalable Multi-FPGA Runtime and Fabric | 说明PCIe直连架构的扩展限制、Fabric统一资源访问方案及真实验证进度。 | 论文中的PCIe Direct与Fabric架构对比图 |

### Slide 6. Cycle-Accurate Multi-FPGA Execution and Pause

**1. LI-TDM-Based Cycle-Accurate Execution**

- Based on LI-TDM proposed by DUOHUAFEN
- Optimized the first and last propagation stages
- Reduced one redundant cross-FPGA exchange per DUT cycle

**2. Cycle-Consistent Global Pause**

- Receive barrier for stable progress sampling
- Common target cycle with per-FPGA stepping
- All partitions pause at the same DUT cycle

**说明**：突出LI-TDM来源、首尾阶段的冗余收发优化，以及接收屏障→共同目标周期→差异化步进的一致暂停机制。第三条是**协议层面每逻辑周期减少冗余收发**，并非已测得的百分比性能增益；不要将屏障确认等同于最终一致暂停完成。不必放传播阶段公式和完整算法。正文依据：`src/midterm/progress/cycle_control.tex`。

### Slide 7. Distributed State Capture, Restore and Replay

**1. Distributed State Capture**

- Reuse REMU's Scan Dump mechanism
- Per-FPGA state extraction and mapping
- Cycle-consistent Global Snapshot

**2. State Restoration & Deterministic Replay**

- FPGA state restoration and replay
- Software RTL replay with waveform reconstruction

**3. Preliminary Validation**

- Consistent state values at selected checkpoints
- Successful restoration and replay in tested scenarios

**说明**：本页重点是REMU已有单FPGA机制向分布式环境的扩展，不重复讲解扫描链或VPI的细节。恢复与重放是**已开展并获得阶段性结果**的功能；现有状态比对有指定周期、指定信号/状态范围，不能概括为所有周期、全部状态逐位一致。正文依据：`src/midterm/progress/state_replay.tex`；图：`figure/ckpt-and-replay.png`。

### Slide 8. Automated Multi-FPGA Circuit Partitioning

**1. Partitioning Method**

- Adaptive-granularity RTL partitioning
- Resource-aware hypergraph modeling
- KaHyPar-based partitioning

**2. Communication-Aware Analysis**

- Cut Size and Path-Cut Number
- Propagation-stage configuration for LI-TDM

**3. Experimental Results**

- 5 DUTs, 2–4 partitions, 15 successful partitioning runs
- Maximum Path-Cut Number: 2–5

**说明**：开题已经介绍算法，此页只重述研究关键词并展示当前的划分数据。15组“成功”指所记录的**KaHyPar求解结果成功**，并非全部15组均完成上板或端到端功能验证。2–5是这些记录的最大路径切割数范围；不能据此声称自适应粒度已优于基线算法或各类物理资源已均衡。数据源：`experiments/partitioning.md`、`experiments/synthesis-utilization.md`；正文：`src/midterm/progress/partitioning.tex`。

### Slide 9. Scalable Multi-FPGA Runtime and Fabric

**1. Motivation**

- PCIe direct connection limits system scalability

**2. Fabric-Based Runtime**

- Unified register and memory access
- Reference node for Host connectivity
- Fabric Initiator, Router and Access Agent

**3. Current Progress**

- Fabric components and Driver backend implemented
- Dual-node co-simulation environment established
- Full system validation remains in progress

**说明**：现有双FPGA板级原型采用**Host分别PCIe直连各FPGA**的基础方案；Fabric统一访问为后续扩展设计。组件与Driver后端已有实现及局部测试，但完整双节点联合验收和实际Fabric板级验证尚未完成，不能标为已通过。正文依据：`src/midterm/progress/runtime.tex`；图：`figure/fabric-architecture-comparison-reference.png`。

## 第三部分：Prototype & Evaluation（第10页）

### Slide 10. Dual-FPGA REMUS Prototype and Evaluation

**1. Experimental Platform**

- Two NM37 FPGA boards (Xilinx VU37P)
- Host communication via PCIe
- FPGA-to-FPGA communication via QSFP/Aurora

**2. DUT Deployment**

- PicoRV32 and Rocket: Bare-metal workloads
- Nanhu and KMH: OpenSBI / Linux workloads

**3. Functional Validation**

- Cycle-consistent global pause
- Global Snapshot capture and restoration
- FPGA and software RTL replay

**4. Preliminary Performance**

- PicoRV32: ~0.327 MHz
- KMH: ~0.322 MHz
- Global pause latency: ~0.8–1.1 ms in recorded tests

**说明**：

- 此页集中展示已完成的基础双FPGA直连原型。拟加入用户后续提供的“双FPGA插在同一Host中的真实照片”，搭配代表性DUT输出和简洁的实验表格；不把Fabric原型描述为已上板验证。
- 频率分别来自PicoRV32和KMH当前归档的**较长run片段**，后者为保存检查点前的窗口；不是全部DUT或整个Linux启动的频率。Rocket与Nanhu当前没有同口径定量频率，不预填。
- 暂停延迟为已记录的**Host可见全局同步暂停完成耗时**：PicoRV32 23条约0.804–0.925 ms、KMH 1条约1.047 ms，范围只描述当前记录，不代表独立重复实验或纯硬件屏障延迟。
- 根据真实PPT篇幅决定是否纳入检查点保存/恢复耗时；如使用，应注明总耗时与Host/DDR/文件处理口径，不将其解释为纯扫描时间。
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
- 第6–11页：英文标题及文字初稿已确认，PPTX尚未制作；按对应论文图与实验材料制作，不得将已规划文字视为已制作页面。
- 建议维护状态：`Planned`、`Designed`、`PPTX Created`、`Reviewed`。完成状态需随提交更新，避免以规划代替实际进度。
- 制作入口：[OfficeCLI实施计划](pptx-implementation-plan.md)、[设计参考索引](../figure/presentation-reference/README.md)、[组件资产索引](../figure/ppt-assets/README.md)。
