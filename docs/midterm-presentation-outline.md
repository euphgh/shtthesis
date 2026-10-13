# REMUS中期答辩PPT大纲

## 定位与范围

- **用途**：硕士学位论文中期答辩，正文全英文，围绕“从多FPGA原型验证到可暂停、可观测、可重放的多FPGA硬件仿真系统”展开。
- **规模**：15页正文；封面与结束页分别单列时合计约17页。可根据答辩时长和可用实验材料适度调整。
- **叙事主线**：Why multi-FPGA? → Why is prototyping insufficient? → Challenges → Research gap & goal → Cycle-accurate execution → Global pause → Distributed dump → Restore/replay → Automated partitioning → Runtime → Prototype & evaluation → Next steps。
- **术语**：新报告中的系统称REMUS（Replay EMUlation System）；开题阶段的SMART保留为历史名称，不在新页中混用。系统能力和实验完成状态须与最新研究材料一致。
- **风格入口**：[演示文稿视觉规范](presentation-style-guide.md)；学术定位见[论文写作指导](thesis-writing-guidelines.md)；详细技术背景见[中期论文大纲](../src/midterm/outline.md)。

## 第一部分：Background & Research Goal（第1–5页）

| 页码 | Slide Title | 核心信息 | 主要视觉表现 |
| --- | --- | --- | --- |
| 1 | From RTL Simulation to Multi-FPGA Prototyping | RTL软件仿真具有可观测性但速度受限；FPGA提升运行速度；多FPGA突破单片容量限制。 | 从RTL Simulation→FPGA Prototyping→Multi-FPGA Prototyping的三层演进图；波形显示器、FPGA、互连芯片图标。 |
| 2 | Multi-FPGA Prototyping Is Fast, but Hard to Debug | 原型验证强调运行速度和容量；硬件仿真还需要Pause、Dump、Restore、Replay及波形观测。 | 左右对比：传统Prototype的有限可见性 vs. Run→Pause→Dump→Restore→Replay能力链。 |
| 3 | Key Challenges of Replayable Multi-FPGA Emulation | 四个挑战：周期一致的全局暂停、跨FPGA周期精确执行、分布式状态管理、高质量自动化划分。 | 四象限技术问题卡片；每象限1个简图、1句结论。 |
| 4 | Research Gap and Goal | 多FPGA原型验证具备扩展能力；单FPGA Scan Dump有状态重放基础；研究目标是同时具备多FPGA扩展和全局状态调试。 | 3列能力对比矩阵，明确区别“已知技术能力”和“本课题拟实现能力”。 |
| 5 | REMUS: Overall Workflow and Mid-Term Scope | 统一呈现RTL输入、自动划分、LI-TDM/Cycle Control/Scan Dump、Runtime、Global Snapshot与Replay路径；界定中期工作范围。 | 一张主流程/系统架构图，配简短的中期里程碑栏。 |

`pptx/midterm/`保留当前REMUS新主题页面，已被替代的SMART旧配色草稿已清理；后续页面继续遵循统一视觉规范。

## 第二部分：Mid-term Research Progress（第6–12页）

| 页码 | Slide Title | 核心信息 | 主要视觉表现 |
| --- | --- | --- | --- |
| 6 | Mid-Term Progress Overview | 以REMUS架构为索引展示Partition、Cosim、Cycle Control、Scan Dump、Fabric Topology、双FPGA系统的实际完成情况。 | 系统框图上的Completed / In Progress / Planned标识；只使用真实进度。 |
| 7 | Cycle-Accurate Multi-FPGA Execution | DUT逻辑时钟与FPGA物理时钟解耦；LI-TDM跨分区信号交换；一周期内多轮传播与PPD影响。 | DUT Cycle与物理时钟、跨片交换对应的时序图。 |
| 8 | Cycle-Consistent Global Pause | 为什么各节点必须在同一DUT逻辑周期停止；运行、步进、暂停的统一控制语义。 | 两FPGA的时钟/暂停时序和Global Pause握手流程图。 |
| 9 | Distributed State Capture & Global Snapshot | Scan Dump集成；分区局部状态导出；按原始状态映射聚合Global Snapshot。 | 多个FPGA→Local Dump→Global Snapshot的状态流向图。 |
| 10 | State Restoration & Deterministic Replay | Snapshot写回与重执行的设计路径、重放正确性条件、目前完成与待验证范围。 | Dump→Snapshot→Restore→Replay→Waveform的闭环流程；未完成步骤明确标注。 |
| 11 | Automated Multi-FPGA Circuit Partitioning | 层次分析、资源估计、自适应粒度、超图划分、RTL输出；资源均衡、Cut Size和PPD。 | 保留模块层次与按需展开的算法示意 + 有数据时展示评价指标。 |
| 12 | Scalable Runtime Control & State Transfer | Fabric Topology、Host控制入口、数据/控制平面、命令分发和状态汇聚/恢复路径。 | Host→Fabric→FPGA节点结构图；控制和状态传输采用不同线型。 |

每页强调“问题→机制→可证明的结果”；避免拆成过多工程模块清单。未实测或尚未实现的部分只以设计/计划形式表达。

## 第三部分：Prototype & Evaluation（第13–14页）

| 页码 | Slide Title | 核心信息 | 主要视觉表现 |
| --- | --- | --- | --- |
| 13 | Dual-FPGA REMUS Prototype | 实际板卡及链路、Host连接、两片FPGA上的DUT部署、已完成的系统级控制/调试能力。 | 真实设备照片 + 简化拓扑，标注DUT及控制/数据路径。 |
| 14 | Mid-Term Experimental Results | 以真实数据呈现DUT功能正确性、周期控制、暂停/状态提取、划分质量与资源/性能开销。 | 2–3组可追溯的表格、波形或曲线；标注测试条件、单位和基线。 |

## 第四部分：Problems & Next Plan（第15页）

| 页码 | Slide Title | 核心信息 | 主要视觉表现 |
| --- | --- | --- | --- |
| 15 | Challenges & Future Work | 问题与行动配对：状态恢复/重放完善、通信与PPD优化、多FPGA扩展、大规模SoC部署、完整评估和论文计划。 | 两列Problem→Next Action，底部给出阶段性时间轴（仅写有依据的时间）。 |

## 封面、目录与结束页

- **封面**：在上述15页正文之外单独制作；采用院校/研究机构标识、中文正式学位论文题目及英文译名、身份与日期信息，具体字段以学校要求为准。
- **目录**：可与封面后的部分过渡页合并，优先不占用技术正文页数；若单独增加目录页，应相应调整总页数。
- **结束页**：简洁的“Thank You / Q&A”，与封面保持视觉呼应。

## 制作状态与内容依赖

- 第1页：新主题状态为`PPTX Created`；[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_1.pptx)和[PNG预览](../figure/presentation-preview/midterm-background-01.png)已生成，OfficeCLI结构检查与独立PNG视觉检查通过，PowerPoint桌面端复核待完成。
- 第2页：新主题状态为`PPTX Created`；[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_2.pptx)和[PNG预览](../figure/presentation-preview/midterm-background-02.png)已生成，OfficeCLI结构检查与独立PNG视觉检查通过，PowerPoint桌面端复核待完成。右栏以`Target capabilities`标明研究目标。
- 第3页：新主题状态为`PPTX Created`；[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_3.pptx)和[PNG预览](../figure/presentation-preview/midterm-background-03.png)已生成，OfficeCLI结构检查与独立PNG视觉检查通过，PowerPoint桌面端复核待完成。四象限表达研究挑战，正文已展开PPD全称并说明全局暂停的共同逻辑周期与链路排空要求。
- 第4页：新主题状态为`PPTX Created`；[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_4.pptx)和[PNG预览](../figure/presentation-preview/midterm-background-04.png)已生成，OfficeCLI结构检查与独立PNG视觉检查通过，PowerPoint桌面端复核待完成。三栏区分原型验证侧重点、单FPGA容量限制与REMUS研究目标。
- 第5页：已有新主题设计参考图，状态为`Designed`，尚未制作可编辑PPTX。
- 第6–15页：大纲已确定，图示细节应与真实实现和实验材料对应。
- 建议维护状态：`Planned`、`Designed`、`PPTX Created`、`Reviewed`。完成状态需随提交更新，避免以规划代替实际进度。
- 制作入口：[OfficeCLI实施计划](pptx-implementation-plan.md)、[设计参考索引](../figure/presentation-reference/README.md)、[组件资产索引](../figure/ppt-assets/README.md)。
