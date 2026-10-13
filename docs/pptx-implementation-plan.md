# REMUS中期PPT制作计划：从设计图到可编辑PPTX

本文面向后续制作PPT的作者与agent，记录材料入口、前五页的元素拆分和OfficeCLI实施步骤。
当前已完成**第1–3页新主题PPTX及OfficeCLI PNG检查**；第4–5页仍待制作。
第1页文件：[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_1.pptx)、
[PNG预览](../figure/presentation-preview/midterm-background-01.png)。
第2页文件：[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_2.pptx)、
[PNG预览](../figure/presentation-preview/midterm-background-02.png)。
第3页文件：[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_3.pptx)、
[PNG预览](../figure/presentation-preview/midterm-background-03.png)。
已通过OpenXML校验、OfficeCLI问题检查、字体/对象边界检查和独立PNG视觉复核；
尚未在PowerPoint桌面端复核。

2026-10-13核对环境：REMUS工作树为`fix-shell`，`thesis/`为独立的`main`工作树。
下文的目录均相对`thesis/`，命令也在该目录执行。

## 1. 材料分工与阅读顺序

| 材料 | 用途 | 使用边界 |
| --- | --- | --- |
| [论文写作指导](thesis-writing-guidelines.md) | 研究定位、REMUS命名、方法与系统贡献的区分 | 决定新PPT的论述口径 |
| [逐页大纲](midterm-presentation-outline.md) | 15页正文的主题、叙事和内容依赖 | 决定每页讲什么；不作为实验完成的证据 |
| [视觉规范](presentation-style-guide.md) | 配色、Arial字体、16:9画幅、可编辑性 | 决定新PPT的统一样式 |
| [五张设计参考图](../figure/presentation-reference/README.md) | 前五页的构图、比例、图文关系 | 用于重建布局；图中文字和完成状态仍需核对 |
| [十张组件插图](../figure/ppt-assets/README.md) | 芯片、波形、快照等可复用PNG | 只承担图示，不代替可编辑标签与技术连线 |
| [当前中期PPTX](../pptx/midterm/) | 已完成的REMUS新主题页面 | 以第1–3页及对应预览为后续制作基准；SMART旧稿已清理 |
| [开题PPT](../pptx/proposal/proposal-slides.pptx) | 19页历史材料、技术图和叙事背景 | 不直接继承旧主题或将开题目标改称成果 |
| [中期报告大纲](../src/midterm/outline.md) | 技术背景、研究进展和计划 | 与当前代码、实验记录一起核对技术内容 |

现有目录已将内容、设计参考、组件插图和PPTX分开，继续沿用即可。
整页参考图保留在`figure/presentation-reference/`；独立图标保留在`figure/ppt-assets/`；
`figure/`根目录的旧插图与论文图继续保留，按需复用。

## 2. 第一批制作范围与顺序

第一批制作第1–5页，形成一个连续的背景与研究目标小节。第6–15页待补齐技术图和实验依据后继续制作。
封面身份信息、答辩日期及正式题目不从模板示例中推定。

页面顺序沿用逐页大纲：

1. From RTL Simulation to Multi-FPGA Prototyping
2. Multi-FPGA Prototyping Is Fast, but Hard to Debug
3. Key Challenges of Replayable Multi-FPGA Emulation
4. Research Gap and Goal
5. REMUS: Overall Workflow and Mid-Term Scope

制作顺序为：**第1页定版式参数 → 第2页验证流程与对比布局 → 第3、4页复用组件 → 第5页整合架构与状态**。
先完成第1页的渲染检查，再扩展其他页，减少字体、边距和图标比例问题的重复修正。

## 3. 逐页元素拆分

| 页码 | 可编辑PowerPoint元素 | 复用插图 | 制作重点 |
| --- | --- | --- | --- |
| 1 | 标题、分隔线、三层圆角面板、文字、项目符号、层间箭头、双芯片间连线、页码 | `waveform-monitor.png`、重复使用`fpga-chip.png` | 保留三层纵向递进；两片FPGA用两个独立图片对象组成，连接关系可编辑 |
| 2 | 左右面板、能力条目、状态符号、Run→Pause→Dump→Restore→Replay节点、方向箭头与标签 | `fpga-chip.png`、`global-snapshot.png`、`waveform-monitor.png` | 右栏表达可重放仿真的目标能力；不能让勾号暗示REMUS全部功能已经验证 |
| 3 | 四象限面板、标题、短句、局部框图、同步连线、状态汇聚箭头 | `fpga-chip.png`、`cycle-control.png`、`global-pause.png`、`global-snapshot.png`、`circuit-partitioning.png` | 周期执行、全局暂停、状态管理、自动划分分别讲清一个问题；控制时序用独立形状表达 |
| 4 | 三列面板、能力行、说明标签、目标栏、连接线 | `fpga-chip.png`、`global-snapshot.png`、`restore-replay.png` | 保留三列比较结构，逐项核对能力表述；REMUS列明确标注Research Goal |
| 5 | 六阶段卡片、编号、阶段标题、方向箭头、Runtime/Fabric/Host支撑栏、中期范围栏 | `rtl-design.png`、`circuit-partitioning.png`、多个`fpga-chip.png`、`cycle-control.png`、`state-capture.png`、`restore-replay.png`、`waveform-monitor.png`、`fabric-topology.png` | Restore/Replay标明计划或实际状态；六阶段图中的四芯片组合只作部署示意，不作为四FPGA实验完成证据 |

第3页的`global-pause.png`只画出了暂停与循环符号，需要与多个FPGA、共同周期标签和同步连线组合，
才能表达全局一致暂停。`state-capture.png`是状态采集的概念插图，不能代替扫描链或DMA结构图。

## 4. 设计图需要调整的内容

- **第2、4页的能力比较**：用“典型侧重点/常见局限”描述原型验证。没有文献依据时，不用一组叉号断言所有原型系统均不支持暂停或重放。第4页可使用`Primary focus`、`Limited by one FPGA`、`Research goal`等明确文字。
- **第3页的术语**：PPD首次出现时解释为Partition Propagation Depth；若空间不足，改写短句或放入紧随其后的说明，不将关键解释只藏在讲稿中。
- **第5页的完成标记**：参考图中的勾号不是实验记录。`Completed`、`In Progress`、`Planned`必须逐项对应实现和验证依据；未核对项先在制作清单中标记`Needs evidence`，正式展示前解决。
- **状态流向**：Dump/Scan Dump导出局部状态，聚合后形成Global Snapshot；Restore与Replay的执行端和方向在技术页明确，不把FPGA状态恢复与软件RTL重放画成无条件等价的步骤。
- **缺少的图标**：`runtime-control`和`host-interface`尚无独立PNG。Runtime可用原生齿轮/控制框，Host可用矩形显示器及标签制作；无须因此阻塞第一批页面。
- **色彩与文字**：参考图中额外的紫色、红色流程框和渐变不必逐像素复制。按照视觉规范统一颜色、文字、留白与层次。

## 5. OfficeCLI实现方式

### 页面与组件

以OfficeCLI的`create`、`set`、`add`和`batch`为主实现，不直接批量拼接底层XML。
所有OfficeCLI命令必须在沙箱外运行，包括读取、编辑、校验和截图；由脚本调用时，脚本也应在沙箱外执行。
PPTX预览统一使用OfficeCLI直接导出PNG。
创建空白宽屏幻灯片，显式设置主题字体和每个文本对象的Arial字体、字号及颜色。
标题先采用视觉规范建议的28–32pt，正文17–20pt；这些项目约定优先于通用skill中的字号与字体建议。

统一封装标题、分隔线、页码、圆角面板、说明文字、图标、状态标签和连接线。
对象采用有意义的名称，例如`S03.GlobalPause.Title`，后续用`@name=`定位，避免插入对象后序号变化。
节点和连线分别创建；技术流程优先使用绑定节点的`connector`，显式指定端点与箭头。

每页按“背景面板 → 图标与连线 → 标签与正文 → 页码”的层次构建。
公共组件确定后，按页产生JSON批量命令；每页执行后回读结构与文本，尽早发现属性不支持或对象丢失。
讲稿写入notes，记录论述补充和证据来源；正文仍需保留必要的能力范围和状态说明。

### 图像放置

十张新插图均为1254×1254的RGBA PNG，但可见图形边界不同，不能用相同的图片框尺寸保证视觉大小一致。
例如波形显示器上下透明留白较多，RTL文档与状态采集图的视觉中心也不同。

保留原始PNG，使用PPT图片对象的裁剪属性和等比缩放调整。按可见主体确定位置，并在目标浅色背景上检查半透明边缘。
多FPGA拓扑用重复的芯片图标与可编辑连线组合，不截取整页设计图中的局部文字。
正式标签全部用文本框；图标内部已有的“FPGA”是栅格文字，不能宣称可编辑或保证其字体文件为Arial。

### 生成源与输出约定

生成脚本负责计算坐标、生成JSON命令和调用OfficeCLI，不引入第二套PPTX生成库。
使用参数数组调用子进程，避免英文内容中的引号、美元符号或换行被shell解释。

| 拟用路径 | 用途 |
| --- | --- |
| `scripts/build_midterm_pptx.py` | 已实现第1–3页的形状、文字、PNG裁剪、箭头、讲稿及OfficeCLI调用；通过`--slide`选择页面 |
| `build/pptx/` | 批量命令、临时PPTX和检查日志；沿用现有忽略规则 |
| `pptx/midterm/REMUS_Background_Slide_1.pptx` | 已生成的独立第1页；33个可编辑形状（含文字）和4个图片对象 |
| `pptx/midterm/REMUS_Background_Slide_2.pptx` | 已生成的独立第2页；65个可编辑形状（含文字）、9条连接线和5个图片对象 |
| `pptx/midterm/REMUS_Background_Slide_3.pptx` | 已生成的独立第3页；四象限面板、文字、周期脉冲、同步与状态汇聚连线可编辑，12个图片对象复用组件资产 |
| `pptx/midterm/REMUS_Midterm_Background.pptx` | 第一批五页PPTX；尚未创建 |
| `figure/presentation-preview/midterm-background-01.png`至`05.png` | 第1–3页预览已生成；第4–5页待制作，与原始设计参考分开 |

生成过程先输出到`build/pptx/`，通过检查后再交付到`pptx/midterm/`。
已被替代的SMART中期草稿和未引用的旧组件已清理；开题PPT、论文插图、五张设计参考图与新组件保留。
手工调整若需长期保留，应同步回生成源，避免下次生成时丢失。

在沙箱外、`thesis/`目录执行以下命令可分别重建第1–3页到`build/pptx/`，并完成结构检查与PNG导出：

```bash
/usr/bin/python3 scripts/build_midterm_pptx.py
/usr/bin/python3 scripts/build_midterm_pptx.py --slide 2
/usr/bin/python3 scripts/build_midterm_pptx.py --slide 3
```

脚本只使用Python标准库和OfficeCLI；PNG保留原始像素，通过PPT内部裁剪去除透明留白。
当前第1页使用32pt主标题、22pt分区标题、18pt正文与10pt页码，文字和主题字体均为Arial。
第2页使用30pt主标题、22pt分区标题、18pt正文、16pt流程节点、15pt范围说明、
14pt图标标签与10pt页码；全页均为Arial。左栏使用琥珀色减号表示常见局限，
右栏明确标注`Target capabilities`；勾号与闭环流程表示研究目标，不代表REMUS功能全部验证。
PNG复核已修正Restore节点换行与底部标签位置；`validate`通过，`view issues`为0。
源PNG和历史PPTX的内容哈希与Git版本一致，第1页交付文件未改动。

第3页使用30pt主标题、20pt两行分区标题、17pt正文、13–14pt图标标签、18pt总结与10pt页码，
全部可编辑文字为Arial。正文展开Partition Propagation Depth（PPD），用跨FPGA通信延迟描述
周期执行约束，避免在背景页额外引入LI-TDM缩写。全局暂停图标与三片FPGA、同步连线及
共同DUT周期标签组合；局部状态经可编辑连线汇聚为Global Snapshot。三片FPGA为概念示意，
不代表已完成三FPGA实验。已修正文本溢出提示和状态汇聚连线，`validate`通过、
`view issues`为0，独立PNG视觉复核通过；第1–2页交付文件及全部原始PNG/PPTX哈希未变。

### 命令骨架

以下是后续制作的基本调用形式；逐页JSON命令需要由生成脚本提供，并非当前已有文件。
以下命令均在沙箱外执行。当前沙箱外的PATH未包含`/home/hgh/.local/bin`，
可先执行`export PATH="/home/hgh/.local/bin:$PATH"`，或使用OfficeCLI的绝对路径。

```bash
mkdir -p build/pptx
officecli create build/pptx/background.pptx
officecli set build/pptx/background.pptx / --prop slideSize=widescreen
officecli set build/pptx/background.pptx /theme \
  --prop headingFont=Arial --prop bodyFont=Arial \
  --prop accent1=183B56 --prop accent2=008C95 --prop accent3=DF973E
officecli add build/pptx/background.pptx / --type slide \
  --prop layout=blank --prop background=FFFFFF
officecli batch build/pptx/background.pptx --input build/pptx/slide-01.json
officecli get build/pptx/background.pptx '/slide[1]' --depth 1
officecli save build/pptx/background.pptx
officecli validate build/pptx/background.pptx
officecli view build/pptx/background.pptx issues
officecli view build/pptx/background.pptx text
```

属性不确定时先用`officecli help pptx shape|picture|connector|theme`分别查询。
OfficeCLI可能在resident进程中保留修改，导出PNG和交付PPTX前必须`save`或`close`。

### 导出PNG预览

使用`view screenshot`逐页导出，输出仍放在`figure/`下。以第一批五页文件为例：

```bash
# 在沙箱外、thesis/目录执行；输入为已生成的五页PPTX。
mkdir -p figure/presentation-preview
officecli save pptx/midterm/REMUS_Midterm_Background.pptx
for page in 1 2 3 4 5; do
  officecli view pptx/midterm/REMUS_Midterm_Background.pptx screenshot \
    --page "$page" \
    -o "figure/presentation-preview/midterm-background-0${page}.png" || break
done
```

导出后检查每张PNG是否存在、可解码且对应正确页码，再逐页检查布局。
不得用先前留下的同名PNG代替本次成功导出的证据。

## 6. 当前工具验证与制作前待办

2026-10-12实际检查结果：

| 检查 | 结果与边界 |
| --- | --- |
| OfficeCLI | 初次组件检查为1.0.155；本次沙箱外PNG导出实测版本为1.0.156 |
| Arial | `fc-match Arial`命中Arial字体 |
| 现有PPT读取 | 已读取19页开题PPT的结构及旧中期第1页对象；旧中期页面包含可编辑文字和内嵌图片 |
| 组件写入 | 在`/tmp`创建一页组件探针，包含主题设置、两个文本形状、一张PNG、绑定连接线和notes；不是设计样张或正式交付 |
| 结构检查 | 组件探针的`validate`通过，`view issues`为0；这不能证明实际版面无问题 |
| HTML导出 | 旧中期第1页和组件探针已成功导出HTML；未完成浏览器视觉验收 |
| 沙箱外PNG导出 | 已通过：使用`/home/hgh/.local/bin/officecli view … screenshot --page 1 -o …`导出旧中期第1页，得到可解码的1280×720 PNG，并已查看图像 |

PPTX预览采用沙箱外运行OfficeCLI的截图路径。此前沙箱内曾出现浏览器用户目录创建失败及
`setsockopt: Operation not permitted`；沙箱外调用已成功，无须继续排查沙箱内截图。
本次验证复用旧中期草稿，仅证明导出路径可用，不代表新主题页面完成或旧稿已通过内容与版式验收。
HTML文本检查可以辅助排查，但不能代替对重叠、箭头方向、透明边缘和视觉对齐的检查。
当前不需要重新安装OfficeCLI，也没有修改系统字体或全局工具配置。

## 7. 验收与下一步

第一批按以下顺序完成：

1. 确认第2、4、5页的目标/成果表述，建立各状态项的证据对应关系。
2. 实现公共样式与第1页，验证图标裁剪、标题长度、文本可编辑性和渲染路径。
3. 按展示顺序完成第2–5页，复用公共样式；保留必要的逐页布局差异。
4. 执行`validate`、`view issues`、文本与主题检查；逐页渲染并对照设计图检查，修正后重新检查受影响页面。
5. 在PowerPoint或实际使用的演示软件中确认字体、图片与连接线；通过后交付五页PPTX与独立预览图。

交付标准是内容准确、元素可编辑、布局接近设计意图、所有页面可读。
仅有参考图、通过XML验证或完成HTML导出，都不能标为`Reviewed`。

第二批第6–15页需要进一步收集周期/暂停时序、局部状态到全局Snapshot的映射、
Restore/Replay实际完成范围、划分指标、Runtime拓扑、真实板卡照片及实验条件。
这些材料的缺失不妨碍先完成背景页面，但不能用示意图或开题预期数据填充实验结果页。
