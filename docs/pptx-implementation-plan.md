# 中期PPT构建与维护

本页面向修改、构建和交付中期答辩PPT的作者。唯一交付文件是
`pptx/midterm/REMUS_Midterm_Final.pptx`，固定使用Academic Red主题，共14页。

## 一条命令构建

在REMUS仓库根目录执行：

```bash
make -C thesis pptx
```

也可在任意目录执行`python3 /path/to/thesis/scripts/build_midterm_pptx.py`。
需要Python 3和OfficeCLI；Python构建代码仅使用标准库。
OfficeCLI从PATH或`~/.local/bin/officecli`查找，也可用`--officecli /path/to/officecli`指定。
Agent执行OfficeCLI及调用它的脚本时，必须在沙箱外运行。

命令依次打包封面与感谢页模板、生成Contents及11页正文、合成14页演示稿，
执行OpenXML校验并导出全部PNG预览。所有步骤成功后才替换最终文件。
构建失败时旧最终稿保留，终端会指出失败日志。OfficeCLI的版式启发式提示会保存供人工复核，
不能把结构校验成功等同于没有文字溢出。

## 文件职责与Git边界

| 路径 | 内容 | Git |
| --- | --- | --- |
| `scripts/midterm_pptx/slide_contents.py`、`slide_01.py`至`slide_11.py` | 逐页文字、布局、图表、脚注和备注 | 跟踪 |
| `scripts/midterm_pptx/common.py`、`theme.py` | 公共绘图逻辑和唯一红色主题 | 跟踪 |
| `scripts/midterm_pptx/frontmatter/` | 封面和感谢页的展开OpenXML模板及校徽；保留原生可编辑文字、母版和布局 | 跟踪 |
| `figure/ppt-assets/*.png`、`figure/midterm-pause-timing.png`、实际实验图 | 构建输入资产 | 跟踪 |
| `pptx/midterm/REMUS_Midterm_Final.pptx` | 唯一最终演示稿 | 跟踪 |
| `build/pptx/midterm/` | 本次成功构建的单页、预览、清单、检查日志 | 忽略 |
| `build/pptx/midterm-run-*/` | 构建过程或失败现场 | 忽略 |
| `figure/presentation-preview/`、`figure/presentation-reference/` | 历史预览和设计草稿；不是构建输入 | 忽略 |
| `figure/ppt-assets/navy-teal/`、其他PPTX | 历史配色备份、单页或旧稿 | 忽略 |

新克隆不需要旧最终稿、旧单页PPTX或本地缓存也能构建。
历史文件已取消Git跟踪，本地副本可继续查看；不重写Git历史。
论文正在引用的`figure/fpga-rtl-workflow.png`和`figure/checkpoint-and-replay.png`
属于正式插图输入，保留跟踪，不与临时预览混放。

## 修改与单页调试

各页的`LAYOUT_EDITS`记录作者确认的手动调整，优先于同页基础布局。
修改已调整对象时编辑该字典；脚注和备注也在本页模块中。不要重新引入集中存放所有页面内容的覆盖文件。
`theme.py`在布局调整之后应用红色配色，旧颜色值仅作为既有绘图参数的映射输入。

只调试正文第7页：

```bash
python3 scripts/build_midterm_pptx.py --slide 7
```

`--slide 0`表示Contents；正文编号1至11对应最终文件第3至13页。
单页调试只写`build/pptx/`，完成修改后仍运行完整构建命令更新最终稿。
封面和感谢页分别来自模板中的第1、2页；模板源文件清单见其README。
合并工具`merge_midterm_pptx.py`由统一入口调用，日常无需手动复制单页或运行合并命令。

## 内容与检查

- 内容组织：[逐页大纲](midterm-presentation-outline.md)。
- 颜色、字体、图像：[视觉规范](presentation-style-guide.md)。
- 讲述重点与证据边界：[讲稿提纲](midterm-speaking-outline.md)。
- 实验依据：`experiments/`与`src/midterm/`，不能用示意图或规划证明实验完成。

交付前查看`build/pptx/midterm/preview/slide-01.png`至`slide-14.png`，
核对页面顺序、引用、文字裁切和最新资产。检查结果保存在同目录的`logs/`和
`REMUS_Midterm_Final.manifest.json`。PowerPoint桌面端显示效果仍需在实际答辩设备上确认。
