# 双分区EMU_SYSTEM综合资源结果

## 1. 采集范围与来源

- 服务器：`serve41`；远端仓库：`/home/huguanghui/remu`。
- 报告根目录：`fpga/work_farm/fpga/vivado_out/`。
- 采集时间：`2026-10-27T13:15:57Z`（UTC）。
- 采集时远端checkout：`vivado2024.2` / `e924d0eabbc6a3a38b01339b00da55b25faf7a00`。这不替代每个综合工程所用RTL、约束、未提交改动和构建版本的核对。
- 本地整理基于主仓库`thesis`分支、论文仓库`main`分支；本轮只读收集报告，未运行Vivado、重新综合或上板。

本批覆盖`picorv32`、`rocket`、`xs-minimal`、`nanhu-g`、`kmh`五个DUT目录的**双分区配置**，每个DUT各Part 0、Part 1，共10份报告。没有3、4分区综合结果；不能将它们填成0或由两分区结果外推。

[10份完整报告及SHA-256](raw/synthesis-utilization-2026-10-27.md)保留报告原文、表格、头部工具/器件/日期信息及源路径。本文只抽取相关字段，不替代原报告。

### 1.1 目标目录与Part映射

普通命名为：

`target_<DUT>_<i>th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`

其中`part2`表示划分为2个Part，`0th/1th`对应Part 0/1，而不是“第2个Part”。

PicoRV32按作者指定的特殊命名对应双分区的两个Part：

- Part 0：`target_picorv32_part0_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。
- Part 1：`target_picorv32_part1_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

各报告的完整远端路径在原始归档中逐份记录，避免用通用模板误拼PicoRV32路径。

## 2. 工具、统计层次与计量口径

10份报告的共同头部信息：

| 字段 | 报告值 |
| --- | --- |
| Tool Version | Vivado v.2024.2 (lin64) Build 5239630 |
| Host | node41 running 64-bit Ubuntu 22.04.5 LTS |
| Design | role_top |
| Device | xcvu37p_CIV-fsvh2892-2L-e |
| Speed File | -2L |
| Design State | Synthesized |
| 统计对象 | `role_i/ClockResetCore_0/emu_system` |

报告命令均为：

```tcl
report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file <报告路径>
```

本轮还读取了远端`fpga/role/fpga/scripts/flow/synth.tcl`：该脚本要求该层次恰好匹配一个cell，再生成本报告；另有统计整个设计的`synth_util.rpt`，两者不能混用。

因此这些数据是**EMU_SYSTEM层次及其子层次的综合资源占用**，不是纯DUT净占用，也不是整片FPGA或整个Role/Shell的总占用。系统插入逻辑未从该层次中扣除，不能直接将资源值解释为扫描链或通信逻辑的独立增量开销。

### 2.1 核心资源定义

| 本文列名 | 原报告行 | 单位/说明 |
| --- | --- | --- |
| LUT | `CLB LUTs*` | 物理LUT计数，包含逻辑及存储用途；不使用Primitives中LUT1—LUT6数量直接相加代替 |
| FF | `Register as Flip Flop` | 综合后物理触发器计数；本批Latch均为0，因此与CLB Registers相同 |
| BRAM Tile | `Block RAM Tile` | 36 Kb Tile口径，允许0.5；本批等于RAMB36/FIFO + RAMB18/2 |
| URAM | `URAM` | 报告中的URAM数量 |
| DSP | `DSPs` | 报告中的DSP数量 |

利用率直接转录报告`Util%`列，保留其两位小数；不是按两块板合并计算。10份报告对应的`Available`均为：

| 资源 | Available |
| --- | ---: |
| CLB LUTs | 1303680 |
| CLB Registers / Flip Flop | 2607360 |
| Block RAM Tile | 2016 |
| URAM | 960 |
| DSPs | 9024 |

这些分母是报告给出的器件资源容量，并不表示扣除Shell、其他Role逻辑和预留资源后的Part可用预算。低于100%不单独证明完整工程可部署。

## 3. 各Part核心资源占用

### 3.1 Used数量

| DUT目录名 | Part ID | LUT | FF | BRAM Tile | URAM | DSP |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| picorv32 | 0 | 3833 | 2869 | 6.5 | 0 | 0 |
| picorv32 | 1 | 2654 | 2076 | 0 | 0 | 4 |
| rocket | 0 | 16005 | 9745 | 4.5 | 2 | 0 |
| rocket | 1 | 39465 | 19718 | 20 | 0 | 15 |
| xs-minimal | 0 | 528098 | 309532 | 320.5 | 13 | 0 |
| xs-minimal | 1 | 343605 | 104227 | 0 | 0 | 0 |
| nanhu-g | 0 | 872861 | 524416 | 340 | 141 | 0 |
| nanhu-g | 1 | 662769 | 225610 | 36.5 | 0 | 0 |
| kmh | 0 | 953991 | 460539 | 288.5 | 13 | 0 |
| kmh | 1 | 987830 | 212936 | 0 | 0 | 1 |

0为原报告明确值。BRAM Tile的0.5计数保留，不向上取整，也不与RAMB36或RAMB18重复相加。

### 3.2 对应Util%

| DUT目录名 | Part ID | LUT/% | FF/% | BRAM Tile/% | URAM/% | DSP/% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| picorv32 | 0 | 0.29 | 0.11 | 0.32 | 0.00 | 0.00 |
| picorv32 | 1 | 0.20 | 0.08 | 0.00 | 0.00 | 0.04 |
| rocket | 0 | 1.23 | 0.37 | 0.22 | 0.21 | 0.00 |
| rocket | 1 | 3.03 | 0.76 | 0.99 | 0.00 | 0.17 |
| xs-minimal | 0 | 40.51 | 11.87 | 15.90 | 1.35 | 0.00 |
| xs-minimal | 1 | 26.36 | 4.00 | 0.00 | 0.00 | 0.00 |
| nanhu-g | 0 | 66.95 | 20.11 | 16.87 | 14.69 | 0.00 |
| nanhu-g | 1 | 50.84 | 8.65 | 1.81 | 0.00 | 0.00 |
| kmh | 0 | 73.18 | 17.66 | 14.31 | 1.35 | 0.00 |
| kmh | 1 | 75.77 | 8.17 | 0.00 | 0.00 | 0.01 |

## 4. 资源细分

### 4.1 存储映射相关资源

| DUT目录名 | Part ID | LUT as Memory | Distributed RAM LUT | Shift Register LUT | RAMB36/FIFO | RAMB18 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| picorv32 | 0 | 144 | 144 | 0 | 6 | 1 |
| picorv32 | 1 | 40 | 40 | 0 | 0 | 0 |
| rocket | 0 | 559 | 552 | 7 | 4 | 1 |
| rocket | 1 | 298 | 296 | 2 | 0 | 40 |
| xs-minimal | 0 | 18016 | 17964 | 52 | 263 | 115 |
| xs-minimal | 1 | 592 | 592 | 0 | 0 | 0 |
| nanhu-g | 0 | 18856 | 18766 | 90 | 212 | 256 |
| nanhu-g | 1 | 909 | 888 | 21 | 35 | 3 |
| kmh | 0 | 17636 | 17584 | 52 | 248 | 81 |
| kmh | 1 | 595 | 592 | 3 | 0 | 0 |

`LUT as Memory`内部还区分Distributed RAM和Shift Register；该列是主LUT计数的一部分，不能再加到LUT总数上。BRAM Tile、RAMB36/FIFO和RAMB18是汇总与分项关系，不是三类独立资源。

### 4.2 逻辑LUT与寄存器细分

| DUT目录名 | Part ID | LUT as Logic | CLB Registers | Flip Flop | Latch |
| --- | ---: | ---: | ---: | ---: | ---: |
| picorv32 | 0 | 3689 | 2869 | 2869 | 0 |
| picorv32 | 1 | 2614 | 2076 | 2076 | 0 |
| rocket | 0 | 15446 | 9745 | 9745 | 0 |
| rocket | 1 | 39167 | 19718 | 19718 | 0 |
| xs-minimal | 0 | 510082 | 309532 | 309532 | 0 |
| xs-minimal | 1 | 343013 | 104227 | 104227 | 0 |
| nanhu-g | 0 | 854005 | 524416 | 524416 | 0 |
| nanhu-g | 1 | 661860 | 225610 | 225610 | 0 |
| kmh | 0 | 936355 | 460539 | 460539 | 0 |
| kmh | 1 | 987235 | 212936 | 212936 | 0 |

这些综合FF数量不等于[扫描状态统计](scan-state.md)中的FF_COUNT。后者是扫描条目的状态位数，前者是当前EMU_SYSTEM层次综合映射后的物理资源计数。同理，MEM_COUNT是扫描存储位数，不是本表的BRAM/URAM实例数；存储映射还可能使用LUT资源。

## 5. 由本批数据支持的观察

- `xs-minimal`的BRAM Tile为Part 0的320.5与Part 1的0，URAM为13与0。
- `kmh`的BRAM Tile为Part 0的288.5与Part 1的0，URAM为13与0；DSP则为0与1。
- `nanhu-g`的BRAM Tile为340与36.5，URAM为141与0。
- `picorv32`的BRAM Tile为6.5与0，DSP为0与4；`rocket`的BRAM Tile为4.5与20，URAM为2与0，DSP为0与15。

这些结果说明本批双分区综合工程中存在分项资源分布差异，不能用“标量总权重接近”替代实际资源检查。若与[KaHyPar标量权重](partitioning.md)结合分析，仍需核对两者是否对应同一次生成RTL与构建；本次仅按DUT目录名和分区数建立候选对应关系，不假定不同批次产物完全匹配。

本报告是**综合阶段**资源结果，不是布局布线后资源结果，也没有提供实现后WNS/TNS。原报告还提示物理优化及后续实现可能改变LUT计数。因此不能据此填写实现后时序通过、最终bitstream资源或运行频率。

## 6. 报告日期与后续回填

下面保留各报告头部`Date`字段原样。字段本身没有注明时区，不将它直接标为UTC；采集时间另见第1节。

| DUT目录名 | Part ID | 报告Date字段（原样） |
| --- | ---: | ---: |
| picorv32 | 0 | Tue Oct 27 15:55:38 2026 |
| picorv32 | 1 | Tue Oct 27 15:51:13 2026 |
| rocket | 0 | Tue Oct 27 18:09:04 2026 |
| rocket | 1 | Tue Oct 27 18:05:54 2026 |
| xs-minimal | 0 | Tue Oct 27 18:43:06 2026 |
| xs-minimal | 1 | Tue Oct 27 18:26:28 2026 |
| nanhu-g | 0 | Tue Oct 27 18:55:09 2026 |
| nanhu-g | 1 | Tue Oct 27 18:39:31 2026 |
| kmh | 0 | Tue Oct 27 19:00:57 2026 |
| kmh | 1 | Tue Oct 27 18:59:57 2026 |

| 报告位置 | 可回填数据 | 使用前仍需核对 |
| --- | --- | --- |
| 1.4资源分布评价 | 双分区各Part综合后的LUT/FF/BRAM/URAM/DSP | 与划分参数、权重、生成RTL的匹配关系x |
| 1.6资源开销 | 本批EMU_SYSTEM层次综合数量及利用率 | 明确为综合/选定层次，不能冒充完整平台或实现后结果 |
| 2.1标量资源权重问题 | 某个DUT两Part分项资源差异的现状证据 | 同版本标量权重x，以及DUT与系统插入逻辑的统计边界 |

实际综合命令/约束、生成RTL与bitstream版本、ILA配置、实现后报告和物理资源预算等尚未由本批文件完整给出，待补为x。原始完整报告已保存，可在需要时进一步提取其他资源项。本轮未修改报告正文或既有原始批次。
