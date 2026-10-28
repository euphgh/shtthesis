# 实验图片

此目录供存放实验曲线、资源分布图、运行截图及重放波形等图片。已整理的图片由作者提供，原有四张见[板级运行记录](../board-execution.md)，2026-10-28三张见[非零检查点软件RTL重放案例](../picorv32-cosim-replay.md)，另两张见[单Part与双Part同周期状态对照](../picorv32-cosim-cycle-state.md)。中期报告1.6引用原有四图，1.2引用`picorv32-cosim-1part-vs-2part-state-tick42080.png`，1.3引用`picorv32-rtl-replay-from-tick2048.png`和`picorv32-cosim-vs-replay-state-tick42080.png`。两张Cosim运行终端图继续保留为详细操作记录；作者新确认的板级检查点一致性单独说明，不改变这些图的Cosim身份。

| 图片 | 内容与使用边界 |
| --- | --- |
| [picorv32-2fpga-baremetal-uart.png](picorv32-2fpga-baremetal-uart.png) | PicoRV32手写裸机负载：名称、素数列表与Echo交互；不代表Rocket记录或全部10轮交互完成 |
| [kmh-2fpga-opensbi-console.png](kmh-2fpga-opensbi-console.png) | KMH运行OpenSBI v1.6及单HART平台信息；末尾为一次中断停止 |
| [kmh-2fpga-checkpoint-linux-boot.png](kmh-2fpga-checkpoint-linux-boot.png) | tick 1099913暂停保存、继续运行及Linux 6.12.0+早期启动；尚无CLI结果，不单凭该图推断Restore/Replay |
| [kmh-2fpga-linux-cli.png](kmh-2fpga-linux-cli.png) | Linux执行`/init`并出现命令行，执行`cat /proc/cpuinfo`及`uname -a`；不能仅由截图与早期启动图计算全程Host耗时或证明同一会话 |
| [picorv32-cosim-2part-run-checkpoint.png](picorv32-cosim-2part-run-checkpoint.png) | 双Part Cosim复位64周期后保存2048周期检查点，继续运行至42080暂停保存；不是物理双板记录 |
| [picorv32-rtl-replay-from-tick2048.png](picorv32-rtl-replay-from-tick2048.png) | Icarus Verilog从2048检查点恢复重放100000周期并生成FST；日志提示2048之后输入无新轨迹、保持不变 |
| [picorv32-cosim-vs-replay-state-tick42080.png](picorv32-cosim-vs-replay-state-tick42080.png) | 42080周期检查点解码值与重放相对40032周期处六项信号值一致；不代表全状态或全区间逐周期比较 |
| [picorv32-cosim-1part-run-checkpoint.png](picorv32-cosim-1part-run-checkpoint.png) | 单Part Cosim复位64周期后运行至2048、42080并保存；串口名称与素数前缀和双Part记录相同 |
| [picorv32-cosim-1part-vs-2part-state-tick42080.png](picorv32-cosim-1part-vs-2part-state-tick42080.png) | 左双Part、右单Part，42080周期四个共同可见寄存器值一致；层次名称经展开、重新打包后不同 |

## 命名约定

运行与状态验证图片采用`<dut>-<环境>-<实验内容>[-tick<周期>].png`，使用小写字母和连字符：

- `2fpga`表示物理双FPGA上板，`cosim-1part`、`cosim-2part`分别表示单Part、双Part协同仿真，`rtl-replay`表示软件RTL重放。
- `baremetal-uart`、`opensbi-console`、`checkpoint-linux-boot`和`linux-cli`区分程序输出、固件输出、保存后继续启动及命令行交互。
- `cosim-1part-vs-2part-state`表示两种划分配置的状态对照，`cosim-vs-replay-state`表示Cosim检查点与重放波形的状态对照。
- `tick42080`表示对照的绝对逻辑周期；`from-tick2048`表示重放起点，不是持续周期数。不同批次重名时追加日期或批次标识。

资源或性能图按实验类别和指标命名，例如`partitioning-cut-size-2026-10-27.png`；图片较多时可按类别创建子目录。相应实验Markdown中应注明来源数据、配置、坐标单位和比较范围；派生图保留使用的数据批次，不将概念示意图当作实测波形。本次仅统一文件名与引用，图片内容及归档的SHA-256校验值保持不变。

返回[实验归档入口](../README.md)或[划分结果](../partitioning.md)。
