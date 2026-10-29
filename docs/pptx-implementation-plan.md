# REMUS中期PPT制作计划：从设计图到可编辑PPTX

第6、7、10页已按后续确认的方案制作，见文末逐页制作记录；前五页的历史制作记录保留如下。

本文面向后续制作PPT的作者与agent，记录材料入口、前五页的元素拆分和OfficeCLI实施步骤。
当前已完成**第1–5页独立新主题PPTX及OfficeCLI PNG检查**；五页合并文件尚未创建。
第1页文件：[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_1.pptx)、
[PNG预览](../figure/presentation-preview/midterm-background-01.png)。
第2页文件：[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_2.pptx)、
[PNG预览](../figure/presentation-preview/midterm-background-02.png)。
第3页文件：[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_3.pptx)、
[PNG预览](../figure/presentation-preview/midterm-background-03.png)。
第4页文件：[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_4.pptx)、
[PNG预览](../figure/presentation-preview/midterm-background-04.png)。
第5页文件：[可编辑PPTX](../pptx/midterm/REMUS_Background_Slide_5.pptx)、
[PNG预览](../figure/presentation-preview/midterm-background-05.png)。
已通过OpenXML校验、OfficeCLI问题检查、字体/对象边界检查和独立PNG视觉复核；
尚未在PowerPoint桌面端复核。

2026-10-13核对环境：REMUS工作树为`vivado2024.2`，`thesis/`为独立的`main`工作树。
下文的目录均相对`thesis/`，命令也在该目录执行。

## 1. 材料分工与阅读顺序

| 材料 | 用途 | 使用边界 |
| --- | --- | --- |
| [论文写作指导](thesis-writing-guidelines.md) | 研究定位、REMUS命名、方法与系统贡献的区分 | 决定新PPT的论述口径 |
| [逐页大纲](midterm-presentation-outline.md) | 15页正文的主题、叙事和内容依赖 | 决定每页讲什么；不作为实验完成的证据 |
| [视觉规范](presentation-style-guide.md) | 配色、Arial字体、16:9画幅、可编辑性 | 决定新PPT的统一样式 |
| [五张设计参考图](../figure/presentation-reference/README.md) | 前五页的构图、比例、图文关系 | 用于重建布局；图中文字和完成状态仍需核对 |
| [十张组件插图](../figure/ppt-assets/README.md) | 芯片、波形、快照等可复用PNG | 只承担图示，不代替可编辑标签与技术连线 |
| [当前中期PPTX](../pptx/midterm/) | 已完成的REMUS新主题页面 | 以第1–5页及对应预览为后续制作基准；SMART旧稿已清理 |
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
| 5 | 五阶段卡片、编号、阶段标题、方向箭头、原生时钟/暂停图标、同步连线、中期范围栏 | `rtl-design.png`、`circuit-partitioning.png`、多个`fpga-chip.png`、`global-snapshot.png`、`waveform-monitor.png` | 按更新后的五阶段图制作；Fabric/Runtime并入部署，执行与暂停合为一个阶段，状态捕获/恢复/重放合为一个阶段；第5阶段沿用蓝色系，Restore/Replay标为计划，四芯片组合仅作部署示意 |

第3页的`global-pause.png`只画出了暂停与循环符号，需要与多个FPGA、共同周期标签和同步连线组合，
才能表达全局一致暂停。`state-capture.png`是状态采集的概念插图，不能代替扫描链或DMA结构图。

## 4. 设计图需要调整的内容

- **第2、4页的能力比较**：用“典型侧重点/常见局限”描述原型验证。没有文献依据时，不用一组叉号断言所有原型系统均不支持暂停或重放。第4页可使用`Primary focus`、`Limited by one FPGA`、`Research goal`等明确文字。
- **第3页的术语**：改用Maximum Path-Cut Number，不再将PPD作为论文指标；如涉及LI-TDM传播阶段，应区分$N_{\mathrm{cut}}$与$S=N_{\mathrm{cut}}+1$。保持Slide文字精简，具体公式放在技术章节。
- **第5页的完成标记**：参考图中的勾号不是实验记录。制作时改用中性圆点表示工作范围，并根据中期大纲将Restore/Replay标为`Planned`。后续若使用`Completed`或`In Progress`，必须逐项对应实现和验证依据。
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
| `scripts/build_midterm_pptx.py` | 命令行入口与页面注册；通过`--slide`选择页面，统一调用OfficeCLI、检查并导出 |
| `scripts/midterm_pptx/common.py` | 公共路径、颜色及`SlideAPI`，生成标题、形状、图片裁剪和连接线命令 |
| `scripts/midterm_pptx/slide_01.py`至`slide_05.py` | 每页独立定义`TITLE`和`build_commands()`，保存该页的布局、内容及讲稿 |
| `build/pptx/` | 批量命令、临时PPTX和检查日志；沿用现有忽略规则 |
| `pptx/midterm/REMUS_Background_Slide_1.pptx` | 已生成的独立第1页；33个可编辑形状（含文字）和4个图片对象 |
| `pptx/midterm/REMUS_Background_Slide_2.pptx` | 已生成的独立第2页；65个可编辑形状（含文字）、9条连接线和5个图片对象 |
| `pptx/midterm/REMUS_Background_Slide_3.pptx` | 已生成的独立第3页；四象限面板、文字、周期脉冲、同步与状态汇聚连线可编辑，12个图片对象复用组件资产 |
| `pptx/midterm/REMUS_Background_Slide_4.pptx` | 已生成的独立第4页；99个可编辑形状（含文字）、1条连接线和8个图片对象 |
| `pptx/midterm/REMUS_Background_Slide_5.pptx` | 已生成的独立第5页；57个可编辑形状（含文字）、14条连接线和8个图片对象 |
| `pptx/midterm/REMUS_Midterm_Background.pptx` | 第一批五页PPTX；尚未创建 |
| `figure/presentation-preview/midterm-background-01.png`至`05.png` | 第1–5页预览均已生成，与原始设计参考分开 |

生成过程先输出到`build/pptx/`，通过检查后再交付到`pptx/midterm/`。
修改单页时只需编辑对应的`slide_XX.py`；调整共用样式与绘图接口时编辑`common.py`。
新增页面时提供`TITLE`和`build_commands()`，再加入主文件的`SLIDES`注册表。
页面模块只构造命令，不调用OfficeCLI；各页不依赖其他页面。命令行参数与输出路径保持不变。
已被替代的SMART中期草稿和未引用的旧组件已清理；开题PPT、论文插图、五张设计参考图与新组件保留。
手工调整若需长期保留，应同步回生成源，避免下次生成时丢失。

在沙箱外、`thesis/`目录执行以下命令可分别重建第1–5页到`build/pptx/`，并完成结构检查与PNG导出：

```bash
/usr/bin/python3 scripts/build_midterm_pptx.py
/usr/bin/python3 scripts/build_midterm_pptx.py --slide 2
/usr/bin/python3 scripts/build_midterm_pptx.py --slide 3
/usr/bin/python3 scripts/build_midterm_pptx.py --slide 4
/usr/bin/python3 scripts/build_midterm_pptx.py --slide 5
```

脚本只使用Python标准库和OfficeCLI；PNG保留原始像素，通过PPT内部裁剪去除透明留白。
当前第1页使用32pt主标题、22pt分区标题、18pt正文与10pt页码，文字和主题字体均为Arial。
第2页使用30pt主标题、22pt分区标题、18pt正文、16pt流程节点、15pt范围说明、
14pt图标标签与10pt页码；全页均为Arial。左栏使用琥珀色减号表示常见局限，
右栏明确标注`Target capabilities`；勾号与闭环流程表示研究目标，不代表REMUS功能全部验证。
PNG复核已修正Restore节点换行与底部标签位置；`validate`通过，`view issues`为0。
源PNG和历史PPTX的内容哈希与Git版本一致，第1页交付文件未改动。

第3页使用30pt主标题、20pt两行分区标题、17pt正文、13–14pt图标标签、18pt总结与10pt页码，
全部可编辑文字为Arial。此前导出的PPTX仍展开Partition Propagation Depth（PPD），本次已修改生成脚本使用Maximum Path-Cut Number；重新生成PPTX和预览图之前，旧产物仍包含历史术语。正文用跨FPGA通信延迟描述
周期执行约束，避免在背景页额外引入LI-TDM缩写。全局暂停图标与三片FPGA、同步连线及
共同DUT周期标签组合；局部状态经可编辑连线汇聚为Global Snapshot。三片FPGA为概念示意，
不代表已完成三FPGA实验。已修正文本溢出提示和状态汇聚连线，`validate`通过、
`view issues`为0，独立PNG视觉复核通过；第1–2页交付文件及全部原始PNG/PPTX哈希未变。

第4页使用32pt主标题、21pt栏标题、17pt能力行、14pt范围说明、12pt栏下注释、
18pt目标说明和10pt页码，全部可编辑文字为Arial。左栏用问号和
`Debug support varies by system`表示调试能力因系统而异，中栏以`Limited by one FPGA`
说明容量限制，右栏明确标注`Research Goal`与`Target capabilities; validation follows`。
底部目标是结合多FPGA可扩展性与可重放仿真，不将该比较作为穷尽相关工作或证明创新性的证据。
已调整状态符号和主机连线对齐，`validate`通过、`view issues`为0，独立PNG视觉复核通过；
第1–3页交付文件及现有图片资产哈希未变。

第5页以用户更新的五阶段参考图为准，使用30pt主标题、22pt分节标题、17pt阶段标题、
14pt阶段说明、15pt范围标题及13pt范围说明；所有可编辑文字为Arial。
State Capture阶段的背景为`EAF4F3`，编号与状态箭头为`008C95`，与前四阶段保持一致，
不使用黄色强调。时钟、暂停符号和同步总线均为原生可编辑元素；四FPGA示意标注
`Illustrative topology`。Restore/Replay依据中期大纲标为`Planned`，底部范围栏用圆点代替完成勾号。
已修正长标题、底部说明换行和流程箭头遮挡，`validate`通过、`view issues`为0，
独立PNG视觉复核通过；前四页交付文件和用户更新的参考图哈希未变。

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

## 第6页制作记录（2026-10-28）

第6页采用简短左侧文字与右侧暂停示意图。按用户要求，删除设计图中的“One fewer”框、
“Different progress”说明和底部“A common DUT”结论行，不展开LI-TDM首尾阶段细节。
标题、左侧说明与页码为原生可编辑元素；右图在PPT中裁取设计参考的右侧面板，
保留原始PNG像素与比例，不重新绘制。图中标签和箭头为栅格内容。

- 页面源：`scripts/midterm_pptx/slide_06.py`。
- 设计参考：`figure/presentation-reference/midterm-progress-06-v1.png`。
- PPTX：`pptx/midterm/REMUS_Progress_Slide_6.pptx`。
- 预览：`figure/presentation-preview/midterm-progress-06.png`。
- 在沙箱外执行`/usr/bin/python3 scripts/build_midterm_pptx.py --slide 6`，默认产物位于`build/pptx/`。

OfficeCLI的OpenXML校验通过，`view issues`为0；原生文字为Arial，画幅为16:9，
PNG已进行视觉复核。完成左右标题对齐调整后重新生成并检查。PowerPoint桌面端尚未复核。
右图中的周期数为概念示例，共用箭头概括Host对各节点的操作，不表示FPGA转发Host控制命令。

## 第7页制作记录（2026-10-28）

采用用户确认的第二版设计：左侧三个方法小节为Global Snapshot、FPGA Restore和Software RTL Replay，
突出`by partition`和`state mapping`；右侧替换为真实波形对照图，下方保留一句实验结论。
不添加流程图，不展开实验周期和操作步骤。图上保留简短的Cosim来源标签，讲稿备注区分
软件重放截图、作者确认的板级检查点对照和FPGA恢复结果，不把它们合并成全状态或全周期等价证明。

- 页面源：`scripts/midterm_pptx/slide_07.py`。
- 设计参考：`figure/presentation-reference/midterm-state-replay-07-v2.png`。
- 图片源：`experiments/figure/picorv32-cosim-vs-replay-state-tick42080.png`。
- PPTX：`pptx/midterm/REMUS_Progress_Slide_7.pptx`。
- 预览：`figure/presentation-preview/midterm-progress-07.png`。
- 在沙箱外执行`/usr/bin/python3 scripts/build_midterm_pptx.py --slide 7`，默认产物位于`build/pptx/`。

包含17个原生可编辑形状和1张独立图片；图内文字及波形属于原始截图，不能作为可编辑文字处理。
原图按1275:522等比嵌入，嵌入数据与源文件SHA-256一致，不裁剪或重绘实验结果。
标题30pt、小节标题24pt、正文18pt、结论20pt；全部原生文字为Arial，画幅16:9。
增加正文文本框高度及行距后重新生成，OpenXML校验通过、`view issues`为0；对象边界检查及
独立PNG视觉复核通过。截图细小信号文字需放大查看，不以拉伸图片换取版面填满。
PowerPoint桌面端尚未复核。

## 第10页制作记录（2026-10-28）

采用用户确认的“左侧实物平台、右侧运行结果、底部性能数据”布局。
左侧裁取真实双NM37实物照片，去掉上方示波器并保留Host内两块板卡；右侧两行可编辑表格列出
PicoRV32/Rocket裸机负载及Nanhu/KMH的OpenSBI/Linux负载，下方使用KMH实际Linux Shell截图。
截图保留完整的`cat /proc/cpuinfo`、`uname -a`与Shell提示符，不重绘终端文字。

- 页面源：`scripts/midterm_pptx/slide_10.py`。
- PPTX：`pptx/midterm/REMUS_Prototype_Slide_10.pptx`。
- 预览：`figure/presentation-preview/midterm-prototype-10.png`。
- 图片源：`figure/remus-2fpga-hw.jpg`、`experiments/figure/kmh-2fpga-linux-cli.png`。
- 在沙箱外执行`/usr/bin/python3 scripts/build_midterm_pptx.py --slide 10`，默认产物位于`build/pptx/`。

底部依次展示PicoRV32约0.327 MHz、KMH约0.322 MHz、Host可见全局暂停约0.8–1.1 ms。
脚注注明运行窗口及Host计时口径，讲稿记录精确数据、来源、样本数量和适用范围。
KMH频率为保存检查点前的运行片段，不作为完整Linux启动或进入CLI后的频率。
本页为PCIe直连原型，不作为Fabric板级验证证据。

页面包含29个原生可编辑形状和2张图片；表格由可编辑文本单元格及分隔线组成。
标题30pt、分区标题22pt、平台与表格文字17pt、Linux结论18pt、性能数值22pt；原生文字均为Arial。
两张嵌入图片与源文件SHA-256一致，PPT原生裁剪保持可见区域比例。修正终端截图边缘及数字框高度后，
OpenXML校验通过、`view issues`为0，对象边界和图片比例检查、独立PNG视觉复核通过。
既有交付PPTX哈希未变；PowerPoint桌面端尚未复核。

## 第11页制作记录（2026-10-28）

采用已确认的四行Future Work布局，将当前问题融入后续计划：Fabric上板与四FPGA集成、
性能分析与运行时优化、划分优化与评价、论文写作。以上均为后续工作，讲稿明确划分优化的
实际性能收益仍需实验评价。按用户最新要求，将参考图中的大号双位编号改为`1.`至`4.`，
与条目标题同为22pt。左侧标题、右侧说明及浅灰分隔线均为原生可编辑元素。

- 页面源：`scripts/midterm_pptx/slide_11.py`。
- 设计参考：`figure/presentation-reference/midterm-future-work-11-v1.png`。
- PPTX：`pptx/midterm/REMUS_Future_Work_Slide_11.pptx`。
- 预览：`figure/presentation-preview/midterm-future-work-11.png`。
- 在沙箱外执行`/usr/bin/python3 scripts/build_midterm_pptx.py --slide 11`，默认产物位于`build/pptx/`。

页面包含18个原生形状，无图片。标题32pt、编号与条目标题22pt、正文18pt，字体均为Arial。
视觉复核后收紧右侧正文行距至1.25倍，重新生成并通过OpenXML校验、OfficeCLI问题检查
（0项）、字体/编号/对象边界检查及独立PNG视觉复核。既有10份交付PPTX哈希未变；
检查报告保存在`build/pptx/slide-11-artifact-check.json`。PowerPoint桌面端尚未复核。

## 封面、旧目录与感谢页改色（2026-10-29）

在thesis的`main`工作树中更新`pptx/midterm/REMUS-midterm.pptx`的三页原稿。
标题改为深蓝`183B56`，分隔线改为青绿`008C95`，正文采用`20354A`，
日期说明采用`607184`；主题及显式英文字体统一为Arial。校徽与研究所标识保持原始图片和颜色。
此次只统一视觉样式，保留原文字、对象位置、表格和页码：封面的“开题答辩”及旧六项目录
尚未同步为当前中期内容；本文件不代表11页正文已合并。

- 修改入口：`scripts/restyle_midterm_frontmatter.py`，按仓库要求在沙箱外执行。
- 原稿备份：`build/pptx/restyle-midterm/REMUS-midterm-original.pptx`。
- 预览：`figure/presentation-preview/REMUS-midterm-cover.png`、`REMUS-midterm-contents.png`、`REMUS-midterm-thanks.png`。
- 检查：OpenXML通过、OfficeCLI问题检查0项，三页独立视觉复核通过；原文字、对象几何、
  图片字节及原有关系保持一致。修复了工具处理XML时丢弃独立空格的问题，并重新渲染确认。
- PowerPoint桌面端尚未复核；感谢页原有信息表较拥挤，此次未调整布局。

## 完整演示文稿合并（2026-10-29）

`scripts/merge_midterm_pptx.py`读取当前交付文件，生成
`pptx/midterm/REMUS_Midterm_Final.pptx`，默认顺序为14页：

1. `REMUS-midterm.pptx`第1页封面。
2. `REMUS_Midterm_Contents.pptx`新版目录。
3. `REMUS_Background_Slide_1.pptx`至`REMUS_Background_Slide_5.pptx`。
4. `REMUS_Progress_Slide_6.pptx`至`REMUS_Progress_Slide_9.pptx`。
5. `REMUS_Prototype_Slide_10.pptx`与`REMUS_Future_Work_Slide_11.pptx`。
6. `REMUS-midterm.pptx`第3页感谢页。

原三页文件中的旧目录不进入最终演示文稿。脚本保留源文字、布局、静态页码、可编辑形状、
原生图表、图片、主题与讲稿备注；动态页码字段按合并后的位置显示。此次不修订封面的
“开题答辩”及源页面中已有的旧内容，也不重新生成单页。

在仓库根目录执行（OfficeCLI调用按约定在沙箱外运行）：

```bash
# 仅检查输入文件、页数、画幅和合并顺序
/usr/bin/python3 thesis/scripts/merge_midterm_pptx.py --dry-run

# 首次生成；已有输出时需要显式添加--force
/usr/bin/python3 thesis/scripts/merge_midterm_pptx.py --force

# 同时导出逐页预览
/usr/bin/python3 thesis/scripts/merge_midterm_pptx.py --force \
  --preview-dir thesis/figure/presentation-preview/REMUS_Midterm_Final
```

可用`--input-dir`指定单页目录、`--output`指定输出路径、`--officecli`指定工具路径。
合并使用Python标准库处理PPTX依赖关系，不重绘页面；OfficeCLI负责OpenXML校验、问题检查
和可选PNG预览。每个源文件使用独立部件名称，避免母版、图片、图表或备注相互覆盖。
输出先在临时文件中验证，再原子替换目标。即使使用`--force`，也拒绝把任何输入文件当作输出。
同名`.manifest.json`记录14页的来源、源页号、SHA-256和校验结果。

已实际生成14页PPTX，OpenXML校验通过、OfficeCLI问题检查0项，并导出全部页面预览。
已验证`--dry-run`、拒绝默认覆盖已有输出、拒绝覆盖源文件，以及失败时已有最终文件保持不变。
PowerPoint桌面端尚未复核。

逐页重新渲染当前源文件并与合并预览比较：第1–13页像素完全一致，第14页仅右下角动态页码
由3变为14。源幻灯片、图表、图片、主题及备注XML/数据按字节保留；仅依赖路径和母版布局ID
按合并所需重映射。原始单页文件的SHA-256在合并前后保持一致。

## 2026-10-29：同步最终稿的手动调整

本节记录作者手动修改后的14页最终稿，优先于上文较早的页面制作记录。此次以
`pptx/midterm/REMUS_Midterm_Final.pptx`为参照，将文字、字号、富文本、位置、图片裁剪、
图表格式、删除对象及新增箭头同步到Python；封面改为“硕士研究生中期答辩”，未来工作保留
作者调整后的三项。未额外改写作者的英文表述或改变实验数据。

- `scripts/midterm_pptx/manual_adjustments.py`保存按稳定对象名组织的可编辑属性和富文本。
  后续修改已经覆盖的对象，应编辑此文件；原`slide_*.py`继续提供资产、基础结构和讲稿备注。
- `scripts/midterm_pptx/manual_revision.py`执行覆盖、标题行距和图表标签样式，并添加出处。
  `build_midterm_pptx.py`已接入该步骤，重新生成不依赖最终PPTX或其截图。
- 文件中的页号沿用正文编号：0为目录，1–11对应最终稿第3–13页。封面文字同步在
  `restyle_midterm_frontmatter.py`中；合并仍使用`merge_midterm_pptx.py`。
- 最终稿第6页的两组名称加上`Related work:`；第8页的`[1]`对应
  `reference.bib`中的`zhu_duohuafen_2024`，第9页的`[1]`对应`chen_remu_2023`。
  两条出处均置于左下角，并在讲稿备注中补充来源。

已从Python重新生成目录及11张正文页，更新三页封面来源文件，再合并为14页最终稿。
通过OpenXML校验，并用OfficeCLI渲染全部页面与手动原稿比较：除第6页新增前缀和第8、9页
新增出处区域外，其余页面像素一致。OfficeCLI仍报告原稿已有的10项启发式排版告警；
对应页面的实际渲染未新增裁切或碰撞，未为消除告警擅自改变手动排版。未在PowerPoint
桌面端复核。手动原稿备份位于`build/pptx/manual-sync/manual-original.pptx`。
