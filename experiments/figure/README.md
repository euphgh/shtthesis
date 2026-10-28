# 实验图片

此目录供存放实验曲线、资源分布图、运行截图及重放波形等图片。已整理的图片由作者提供，原有四张见[板级运行记录](../board-execution.md)，2026-10-28三张见[非零检查点软件RTL重放案例](../picorv32-cosim-replay.md)，另两张见[单Part与双Part同周期状态对照](../picorv32-cosim-cycle-state.md)。中期报告1.6引用原有四图，1.2引用`single-vs-part2.png`，1.3引用`picorv32-replay.png`和`ckpt-vs-wave.png`。两张Cosim运行终端图继续保留为详细操作记录；作者新确认的板级检查点一致性单独说明，不改变这些图的Cosim身份。

| 图片 | 内容与使用边界 |
| --- | --- |
| [picorv32-2fpga.png](picorv32-2fpga.png) | PicoRV32手写裸机负载：名称、素数列表与Echo交互；不代表Rocket记录或全部10轮交互完成 |
| [kmh-2fpga-opensbi.png](kmh-2fpga-opensbi.png) | KMH运行OpenSBI v1.6及单HART平台信息；末尾为一次中断停止 |
| [kmh-2fpga-linux.png](kmh-2fpga-linux.png) | tick 1099913暂停保存、继续运行及Linux 6.12.0+早期启动；尚无CLI结果，不单凭该图推断Restore/Replay |
| [kmh-linux-cli.png](kmh-linux-cli.png) | Linux执行`/init`并出现命令行，执行`cat /proc/cpuinfo`及`uname -a`；不能仅由截图与早期启动图计算全程Host耗时或证明同一会话 |
| [picorv32-cosim.png](picorv32-cosim.png) | 双Part Cosim复位64周期后保存2048周期检查点，继续运行至42080暂停保存；不是物理双板记录 |
| [picorv32-replay.png](picorv32-replay.png) | Icarus Verilog从2048检查点恢复重放100000周期并生成FST；日志提示2048之后输入无新轨迹、保持不变 |
| [ckpt-vs-wave.png](ckpt-vs-wave.png) | 42080周期检查点解码值与重放相对40032周期处六项信号值一致；不代表全状态或全区间逐周期比较 |
| [picorv32-single-run.png](picorv32-single-run.png) | 单Part Cosim复位64周期后运行至2048、42080并保存；串口名称与素数前缀和双Part记录相同 |
| [single-vs-part2.png](single-vs-part2.png) | 左双Part、右单Part，42080周期四个共同可见寄存器值一致；层次名称经展开、重新打包后不同 |

建议文件名体现实验类别与内容，例如`partitioning-cut-size-2026-10-27.png`；图片较多时可按类别创建子目录。相应实验Markdown中应注明来源数据、配置、坐标单位和比较范围；派生图保留使用的数据批次，不将概念示意图当作实测波形。

返回[实验归档入口](../README.md)或[划分结果](../partitioning.md)。
