# AGENTS.md

本文件为在仓库根目录工作的AI编码与文档Agent提供项目约定。执行具体任务时，以用户的最新要求和仓库中实际存在的文件为准。

## 项目定位

- 本仓库基于上海科技大学的非官方LaTeX学位论文模板`shtthesis`，同时承载多FPGA硬件仿真课题的开题报告、中期报告大纲、参考文献、插图和答辩PPT。
- 后续论文使用的系统名称为**REMUS**（Replay EMUlation System），承接课题组已有的单FPGA系统REMU（Replay EMUlation）；**SMART**（Scalable Multi-FPGA Automated Replayable Technology）是开题阶段的工作名称。研究重点不是单纯构建可运行的多FPGA原型验证系统，而是在多FPGA环境中实现**周期精确运行、全局一致暂停、分布式Scan Dump状态提取、状态恢复与确定性重放**。
- 自动化电路划分（包括自适应粒度、资源平衡、Cut Size和PPD）与可扩展的Fabric/Runtime是支撑上述目标的关键技术。
- `src/midterm/outline.md`包含阶段性成果、正在进行的工作和后续计划；**大纲中的计划、目标及待验证项目不能直接当作已实现或已测得的结果**。

## 仓库结构与修改位置

| 路径 | 用途 |
| --- | --- |
| `proposal.tex` | 当前开题报告的LaTeX顶层入口；通过`\input{src/proposal/main.tex}`载入正文 |
| `src/proposal/main.tex` | 开题报告章节汇总入口 |
| `src/proposal/*.tex` | 开题报告研究背景、目标、技术路线、实验与进度的正文 |
| `src/proposal/outline.md` | 开题报告大纲与写作材料 |
| `src/midterm/outline.md` | 中期报告大纲；目前仓库中尚无独立的`midterm.tex`编译入口 |
| `docs/thesis-writing-guidelines.md` | 中期与最终学位论文共用的研究定位、命名和写作指导 |
| `reference.bib` | BibLaTeX文献数据库 |
| `figure/` | 论文与PPT共用的插图资产，统一存放独立PNG及其他图像（包括部分SVG原稿） |
| `pptx/` | 答辩PPTX文件；共用插图从`figure/`复用 |
| `shtthesis.cls`、`shtthesis-user-guide.tex` | 模板类文件和用户手册，非日常论文正文 |
| `Makefile`、`.vscode/settings.json` | 本地编译命令和编辑器配置 |
| `.github/workflows/build.yaml` | GitHub Actions构建配置，当前主要编译模板用户手册 |

修改论文内容时，优先编辑对应的`src/`文件，而不是改动模板类文件。除非明确需要修改模板实现，否则不要修改`shtthesis.cls`、用户手册、校徽文件或工作流。

注意：`proposal.tex`的`\shtsetup`中仍保留部分模板示例字段；不要把这些字段当作已核实的作者、导师、关键词等正式信息，也不要在无明确要求时擅自改写。

## 学术内容与写作约定

- **长期写作指导**：编写或修改中期报告、学位论文及相关答辩材料前，先阅读[学位论文研究定位与写作指导](docs/thesis-writing-guidelines.md)，遵循其中关于REMUS命名、系统与学术贡献区分、术语引入位置及成果组织的约定。不要未经要求批量替换开题阶段已有的SMART名称。

- **区分问题、方法、证据与计划**：例如资源平衡、Cut Size、PPD、自动化和划分粒度选择是划分问题的约束或评价维度；自适应粒度划分是所采用的方法。已完成内容、初步结果和后续目标必须分开描述。
- **突出课题差异**：多FPGA原型验证主要解决大规模设计的部署与运行；本课题进一步关注同一DUT逻辑周期的一致暂停、跨FPGA全局状态聚合、Snapshot/Restore、Replay及波形观测。
- **遵循既定中期叙事**：研究背景与目标之后，依次介绍周期精确执行与一致暂停、分布式状态提取/恢复/重放、自动化电路划分、可扩展运行控制与状态传输、双FPGA系统实验、阶段总结。不要未经要求回退到旧的“划分→集成→互连”章节顺序。
- **简洁、面向读者**：大纲直接表达论点及因果关系，不写“本节建议介绍”“建议控制在几字”等面向写作者的提示。减少重复与长句，但不牺牲技术逻辑。
- **术语准确**：区分DUT逻辑时钟和FPGA物理时钟；区分局部Scan Dump和Global Snapshot；PPD指分区传播深度。首次引入陌生缩写时给出全称。
- **语言与格式**：中文论文和大纲默认使用中文，按照现有中期大纲的习惯，不在中文与相邻英文缩写之间额外插入空格（如`多FPGA`、`RTL设计`）；英文单词之间仍应保留正常空格。答辩PPT的页面标题和正文使用英文，除非用户另行要求。
- **文献与数据**：新增文献引用应核实`reference.bib`中是否存在相应key，沿用LaTeX正文已有的`\cite{...}`约定。不得编造论文、实验结果、性能数字、DUT测试状态或已经实现的功能；未核实内容应明确标记为计划或待验证。
- **控制改动范围**：原则上只修改用户指定的章节、文件和必要依赖。不因局部写作任务批量改写其余章节或全仓格式。

## LaTeX构建与检查

本仓库使用`shtthesis`文档类，依赖现代TeX Live/MacTeX及相关中文字体和宏包；不支持pdfLaTeX。首选XeLaTeX，部分模板手册场景也支持LuaLaTeX。

```bash
# 在仓库根目录编译开题报告；对应Makefile的默认目标
make proposal.pdf

# 等价的直接编译命令
latexmk -pdfxe -shell-escape -interaction=nonstopmode proposal.tex

# 编译模板用户手册（README中也给出LuaLaTeX方式）
latexmk -pdfxe shtthesis-user-guide.tex

# 清理LaTeX辅助文件，注意这是全局清理命令
make clean
```

- `Makefile`中的`proposal-with-cover.pdf`目标依赖`resource/proposal-cover.pdf`；当前仓库树中没有该文件，因此**不要假定合并封面的目标可以直接运行**。
- VSCode的LaTeX Workshop配置默认使用`latexmk -pdfxe`并输出到`build/`。
- `DEPENDS.txt`列出部分TeX依赖。遇到缺少字体、宏包、biber或TeX引擎时应报告环境问题，不要为使构建通过而删除原有中文排版或参考文献配置。
- `proposal.tex`通过`\makebiblio`输出文献，引用配置来自`\shtsetup`中的`bib-resource = {reference.bib}`。
- `figure/`图像引用使用相对仓库根目录的路径；在`src/`编辑正文时保持该路径约定。
- GitHub Actions的现有构建任务主要针对`shtthesis-user-guide.tex`，不能用它的成功代替`proposal.tex`或未来中期报告的完整验证。
- Markdown大纲变动可检查标题层级、术语、表格和链接，不必因此强制重新编译无关LaTeX文档。新增或修改LaTeX时优先编译相应入口，并检查日志中未定义引用、缺失文件和排版警告。

## PPT与图像资产

- `pptx/`存放英文答辩PPTX；FPGA芯片、波形显示器、数据库快照等独立PNG资产统一存放在`figure/`，供论文与PPT复用，不在`pptx/`保留重复副本。PPTX内部嵌入的图片保留，以保证演示文稿可独立打开。
- 延续已采用的**16:9、白底、红色标题、橙色分隔线、低文字密度**的学术展示风格。
- PPT中的标题、说明、图形框、箭头等尽量保持可编辑；复杂插图可作为独立的高分辨率图片嵌入。已有插图应优先复用，避免同一种符号在不同页出现不一致的样式。
- 不把生成的整页图片当成唯一PPT内容来代替可编辑文件；交付PPTX时尽量同时检查渲染预览、文字溢出、图片透明背景、对齐与长宽比。
- 图表和测试结果只能依据已有数据绘制；示意图应与实际系统架构或明确的规划相符。

## 提交前检查

1. 查看最新仓库文件及本次变更范围，避免覆盖用户近期的修改。
2. 检查技术名词、章节顺序、引用路径和“已完成/计划中”的状态是否与原始材料一致。
3. 对修改过的LaTeX入口运行适当的`latexmk`构建；对于仅修改大纲或说明文档的任务，检查Markdown结构即可。
4. 不提交`*.aux`、`*.log`、`*.bcf`等辅助文件，也不要误提交生成的PDF。`.gitignore`目前默认忽略根目录的PDF（校徽和模板手册除外）；如需追踪新的PDF资产，应先核对忽略规则。
5. 保持提交聚焦，并在交付说明中明确修改的文件、实际执行的验证以及未验证的部分。
