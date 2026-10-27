# 实验图片

此目录供存放实验曲线、资源分布图、运行截图及重放波形等图片。当前四张截图由作者提供，内容已在[板级运行记录](../board-execution.md)中按代码预期、截图可见信息和作者说明分别整理。中期报告1.6直接引用这些原图。

| 图片 | 内容与使用边界 |
| --- | --- |
| [picorv32-2fpga.png](picorv32-2fpga.png) | PicoRV32手写裸机负载：名称、素数列表与Echo交互；不代表Rocket记录或全部10轮交互完成 |
| [kmh-2fpga-opensbi.png](kmh-2fpga-opensbi.png) | KMH运行OpenSBI v1.6及单HART平台信息；末尾为一次中断停止 |
| [kmh-2fpga-linux.png](kmh-2fpga-linux.png) | tick 1099913暂停保存、继续运行及Linux 6.12.0+早期启动；尚无CLI结果，不单凭该图推断Restore/Replay |
| [kmh-linux-cli.png](kmh-linux-cli.png) | Linux执行`/init`并出现命令行，执行`cat /proc/cpuinfo`及`uname -a`；不能仅由截图与早期启动图计算全程Host耗时或证明同一会话 |

建议文件名体现实验类别与内容，例如`partitioning-cut-size-2026-10-27.png`；图片较多时可按类别创建子目录。相应实验Markdown中应注明来源数据、配置、坐标单位和比较范围；派生图保留使用的数据批次，不将概念示意图当作实测波形。

返回[实验归档入口](../README.md)或[划分结果](../partitioning.md)。
