# 网表划分EMU_SYSTEM综合资源原始报告：2026-11-04

来源：`serve41:/home/huguanghui/remu`，采集时间：`2026-11-04T04:18:18Z`（UTC）。共5个DUT、40份`synth_emu_system_util.rpt`，全部为`Design State : Synthesized`。报告根目录`fpga/work_farm/fpga/vivado_out/`。返回[整理结果](../netlist-synthesis-utilization.md)。

采集时远端checkout：`vivado2024.2` / `828600a0f8bbf2a93040156aafff1ddbb218d504`。这些报告属于**基于网表划分**之后的构建批次（最早2026-10-28 20:40，最晚2026-11-04 11:28），与[2026-10-27自适应划分批次](synthesis-utilization-2026-10-27.md)的`target_picorv32_part0/part1`目录不是同一批产物。

本批不是完整45个Part：`target_picorv32_0th_part4`、`target_rocket_1th_part3`、`target_rocket_1th_part4`、`target_rocket_2th_part4`、`target_rocket_3th_part4`在采集时没有`synth_emu_system_util.rpt`。缺失项不填0、不外推。

各代码块保存对应报告**完整原文**，包括头部、全部资源表和警告。SHA-256对应代码块内原始文件内容（含末尾换行），不包含Markdown围栏。未重跑Vivado；采集checkout不能替代每份报告实际构建版本的核对。

## 文件校验值

| 目标目录 | SHA-256 |
| --- | --- |
| kmh_0th_part2 | `891ca4d007b0bd80f8518a443a728eb9891ce502e209f21d4643de17bffc5768` |
| kmh_0th_part3 | `253670936ac1bdc80dbc6a940c78ae3867b81d393b9b4f75ad7fc386830647d0` |
| kmh_0th_part4 | `2ac6c11aa414af9a409a2d21a4ebd1965b5203f0b47f14ad99b4703c5eb3b0ea` |
| kmh_1th_part2 | `ed205ee7d2659ea2d4ad4d093492db422ee46bedbfd25f2efe063c9d2c6598ab` |
| kmh_1th_part3 | `87880906a4c0abb10ccbf11bfbba4e92414ae7bd222c3f16bbd004b038018411` |
| kmh_1th_part4 | `d50b1855f528eb0c4ead597871e656119533a57eb8c19421b05a54292c3da11c` |
| kmh_2th_part3 | `6bfce2cefb623696b493fbd2d07c655876884e387977a6a2ad1739240e8908be` |
| kmh_2th_part4 | `4f943af639bb686b7d4eef7d71d4031a75391144fe54ba9dd3d7685b7e81e7ef` |
| kmh_3th_part4 | `e96712c5b0953ab0d6ce45dad08cfdc4105a1d458e1b0606e6bdfe0bb2902121` |
| nanhu-g_0th_part2 | `5a7b1adbfab29fa2b069bf6f4460b822f21050087f2f8ab3af8e20e0c358c9f1` |
| nanhu-g_0th_part3 | `021c787b82e527153b808c5167a1ac51b81f8a8cdc347fb46185d9de3c272e5f` |
| nanhu-g_0th_part4 | `e2e5af98499cf88a9ad1c9dde41a69b08258177c92026b8e0bb7a3d0a66f1d1c` |
| nanhu-g_1th_part2 | `b7fcd802bb5769c14f59b0d46dcdcd9fbefe3dbcb13a9c25c7d112abcb770a3e` |
| nanhu-g_1th_part3 | `aa61f465d3167f6197d232dd88f0b2fd033fe846849e3d85427ffe51a3080596` |
| nanhu-g_1th_part4 | `6fbfe11c2105c5166116a3c85ffb350cc72e55dcab46cdffe5d55b8da343a3f0` |
| nanhu-g_2th_part3 | `6fa03d4ef98155edb8302c59c74f076900e1705654a30e83df477a5c005fdba6` |
| nanhu-g_2th_part4 | `7f4ff15485376842a45be35688987d67037b51e58bd83e25e3d9db674013fef0` |
| nanhu-g_3th_part4 | `7ebd90b635507946319054f11d87685eca5d31a5bd1795b746436b6565c3513c` |
| picorv32_0th_part2 | `1a2cd73c531b6c4bfb7c0b6aeb31106712834c14f5177dee2f3caa29cb34fb08` |
| picorv32_0th_part3 | `788fb1e20465c13d9f8da00bf17461b4cbc6e34dbeed5d826eec78db5086105b` |
| picorv32_1th_part2 | `611a91d8323aa698218f9221952ec0f394e705e3bf558d55fc8be140eaeef5ad` |
| picorv32_1th_part3 | `52083ff0baaa24de984a90fb421bccbbaac2d5f8eb84321c8f374660978de0a4` |
| picorv32_1th_part4 | `b2152d3193834e0187e98307a542993ad1e922fa938871dad1cf17f921c84247` |
| picorv32_2th_part3 | `d24f49e54860a95696b57791887696fd3a394bece1337041f8cc0dd0dbedd85b` |
| picorv32_2th_part4 | `cce0bde3639e40252aa0b9123d456a7684d37571b270bb1dbf0637b5895125c8` |
| picorv32_3th_part4 | `5ae6b165143a1301ef5b865e9017ce10dccf652ea1b9993e65c006eb2e3287ee` |
| rocket_0th_part2 | `8e463ea5a08772dee49cdc7abd5f21d73445608efef194f9c97137450d42109c` |
| rocket_0th_part3 | `25aa9f71f36c57ff451bc099ba24a1a159e84b2979b930dd88cb21b7ba4ecb81` |
| rocket_0th_part4 | `72a9e5add88fa3cec4f8973cb2e62723bf685561f98860698fabdfdf9527dd63` |
| rocket_1th_part2 | `1539620e755f486c5ba94848511b944c748687b4e5e260b9b17e50945b58704a` |
| rocket_2th_part3 | `1598d54f1fff0c729861270d5b5c5c4510b005cf5bdd4cb7f2d5a5d32ff2995c` |
| xs-minimal_0th_part2 | `e10f41ba3c84de5312236e2a5e40b5510aab250716dd3de9173e044bcf2a0cbc` |
| xs-minimal_0th_part3 | `1a6253718dde83a4a7fa277a57932de1ca291c25ed7182a18448451227483e34` |
| xs-minimal_0th_part4 | `bcc5c98e3bcc5d54b6887e48cfd4b6f056b1a56ffe67d47792dba29aad96245f` |
| xs-minimal_1th_part2 | `673c9a2e9b46ae05c691863e8cb14454e7a67d1ae5830006dc121766730fefa8` |
| xs-minimal_1th_part3 | `c4f3d9b7e3341842ee839f5ec09ef2e421a5c74c23718f06a46191383787bd22` |
| xs-minimal_1th_part4 | `3ac44343f67d9a702dbb7930b9cbaf1af127f0681259792370630cd966603a14` |
| xs-minimal_2th_part3 | `b8e7395946915de4f5ffcdccdb782cc43634e41fe742ab79adf24d8d921de60a` |
| xs-minimal_2th_part4 | `03b1759f05936e01cb34905a04e2318404ed65fc9f32803c9f07bbece6acff2d` |
| xs-minimal_3th_part4 | `ccfd8e909177411f424a3ec86adda445007172d279e74c80a9378e43bc9a00ec` |

## kmh / Part 0（2分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_kmh_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-04 02:56:21 CST`。

SHA-256：`891ca4d007b0bd80f8518a443a728eb9891ce502e209f21d4643de17bffc5768`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Nov  4 02:56:21 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_kmh_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 878943 |     0 |          0 |   1303680 | 67.42 |
|   LUT as Logic             | 869712 |     0 |          0 |   1303680 | 66.71 |
|   LUT as Memory            |   9231 |     0 |          0 |    600960 |  1.54 |
|     LUT as Distributed RAM |   9204 |     0 |            |           |       |
|     LUT as Shift Register  |     27 |     0 |            |           |       |
| CLB Registers              | 320226 |     0 |          0 |   2607360 | 12.28 |
|   Register as Flip Flop    | 320226 |     0 |          0 |   2607360 | 12.28 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   5535 |     0 |          0 |    162960 |  3.40 |
| F7 Muxes                   |  51162 |     0 |          0 |    651840 |  7.85 |
| F8 Muxes                   |  16548 |     0 |          0 |    325920 |  5.08 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 1888   |          Yes |         Set |            - |
| 318338 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+-------+-------+------------+-----------+-------+
|     Site Type     |  Used | Fixed | Prohibited | Available | Util% |
+-------------------+-------+-------+------------+-----------+-------+
| Block RAM Tile    | 200.5 |     0 |          0 |      2016 |  9.95 |
|   RAMB36/FIFO*    |   168 |     0 |          0 |      2016 |  8.33 |
|     RAMB36E2 only |   168 |       |            |           |       |
|   RAMB18          |    65 |     0 |          0 |      4032 |  1.61 |
|     RAMB18E2 only |    65 |       |            |           |       |
| URAM              |    13 |     0 |          0 |       960 |  1.35 |
+-------------------+-------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| DSPs           |    3 |     0 |          0 |      9024 |  0.03 |
|   DSP48E2 only |    3 |       |            |           |       |
+----------------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| LUT6     | 424544 |                 CLB |
| FDRE     | 318338 |            Register |
| LUT3     | 253514 |                 CLB |
| LUT5     | 221577 |                 CLB |
| LUT4     |  95784 |                 CLB |
| MUXF7    |  51162 |                 CLB |
| LUT2     |  40714 |                 CLB |
| MUXF8    |  16548 |                 CLB |
| RAMD32   |   5654 |                 CLB |
| CARRY8   |   5535 |                 CLB |
| RAMD64E  |   5520 |                 CLB |
| LUT1     |   3583 |                 CLB |
| FDSE     |   1888 |            Register |
| RAMS32   |    674 |                 CLB |
| RAMB36E2 |    168 |            BLOCKRAM |
| RAMB18E2 |     65 |            BLOCKRAM |
| SRLC32E  |     27 |                 CLB |
| URAM288  |     13 |            BLOCKRAM |
| BUFGCE   |      5 |               Clock |
| DSP48E2  |      3 |          Arithmetic |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## kmh / Part 0（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_kmh_0th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-04 05:09:21 CST`。

SHA-256：`253670936ac1bdc80dbc6a940c78ae3867b81d393b9b4f75ad7fc386830647d0`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Nov  4 05:09:21 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_kmh_0th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 870854 |     0 |          0 |   1303680 | 66.80 |
|   LUT as Logic             | 855897 |     0 |          0 |   1303680 | 65.65 |
|   LUT as Memory            |  14957 |     0 |          0 |    600960 |  2.49 |
|     LUT as Distributed RAM |  14916 |     0 |            |           |       |
|     LUT as Shift Register  |     41 |     0 |            |           |       |
| CLB Registers              | 436905 |     0 |          0 |   2607360 | 16.76 |
|   Register as Flip Flop    | 436905 |     0 |          0 |   2607360 | 16.76 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   9383 |     0 |          0 |    162960 |  5.76 |
| F7 Muxes                   |  32816 |     0 |          0 |    651840 |  5.03 |
| F8 Muxes                   |   7424 |     0 |          0 |    325920 |  2.28 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 4294   |          Yes |         Set |            - |
| 432611 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+-------+-------+------------+-----------+-------+
|     Site Type     |  Used | Fixed | Prohibited | Available | Util% |
+-------------------+-------+-------+------------+-----------+-------+
| Block RAM Tile    | 340.5 |     0 |          0 |      2016 | 16.89 |
|   RAMB36/FIFO*    |   288 |     0 |          0 |      2016 | 14.29 |
|     RAMB36E2 only |   288 |       |            |           |       |
|   RAMB18          |   105 |     0 |          0 |      4032 |  2.60 |
|     RAMB18E2 only |   105 |       |            |           |       |
| URAM              |    13 |     0 |          0 |       960 |  1.35 |
+-------------------+-------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| FDRE     | 432611 |            Register |
| LUT6     | 326206 |                 CLB |
| LUT3     | 308085 |                 CLB |
| LUT5     | 256370 |                 CLB |
| LUT4     | 125505 |                 CLB |
| LUT2     |  34009 |                 CLB |
| MUXF7    |  32816 |                 CLB |
| RAMD64E  |  10504 |                 CLB |
| CARRY8   |   9383 |                 CLB |
| MUXF8    |   7424 |                 CLB |
| RAMD32   |   6778 |                 CLB |
| FDSE     |   4294 |            Register |
| LUT1     |   2286 |                 CLB |
| RAMS32   |    838 |                 CLB |
| RAMB36E2 |    288 |            BLOCKRAM |
| RAMB18E2 |    105 |            BLOCKRAM |
| SRLC32E  |     27 |                 CLB |
| SRL16E   |     14 |                 CLB |
| URAM288  |     13 |            BLOCKRAM |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## kmh / Part 0（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_kmh_0th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-04 01:52:58 CST`。

SHA-256：`2ac6c11aa414af9a409a2d21a4ebd1965b5203f0b47f14ad99b4703c5eb3b0ea`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Nov  4 01:52:58 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_kmh_0th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 701385 |     0 |          0 |   1303680 | 53.80 |
|   LUT as Logic             | 691542 |     0 |          0 |   1303680 | 53.05 |
|   LUT as Memory            |   9843 |     0 |          0 |    600960 |  1.64 |
|     LUT as Distributed RAM |   9812 |     0 |            |           |       |
|     LUT as Shift Register  |     31 |     0 |            |           |       |
| CLB Registers              | 372825 |     0 |          0 |   2607360 | 14.30 |
|   Register as Flip Flop    | 372825 |     0 |          0 |   2607360 | 14.30 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   7961 |     0 |          0 |    162960 |  4.89 |
| F7 Muxes                   |  26637 |     0 |          0 |    651840 |  4.09 |
| F8 Muxes                   |   7224 |     0 |          0 |    325920 |  2.22 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 3381   |          Yes |         Set |            - |
| 369444 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+-------+-------+------------+-----------+-------+
|     Site Type     |  Used | Fixed | Prohibited | Available | Util% |
+-------------------+-------+-------+------------+-----------+-------+
| Block RAM Tile    | 328.5 |     0 |          0 |      2016 | 16.29 |
|   RAMB36/FIFO*    |   288 |     0 |          0 |      2016 | 14.29 |
|     RAMB36E2 only |   288 |       |            |           |       |
|   RAMB18          |    81 |     0 |          0 |      4032 |  2.01 |
|     RAMB18E2 only |    81 |       |            |           |       |
| URAM              |    13 |     0 |          0 |       960 |  1.35 |
+-------------------+-------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| FDRE     | 369444 |            Register |
| LUT6     | 257257 |                 CLB |
| LUT3     | 252548 |                 CLB |
| LUT5     | 215039 |                 CLB |
| LUT4     | 104660 |                 CLB |
| MUXF7    |  26637 |                 CLB |
| LUT2     |  24096 |                 CLB |
| CARRY8   |   7961 |                 CLB |
| MUXF8    |   7224 |                 CLB |
| RAMD32   |   6620 |                 CLB |
| RAMD64E  |   5576 |                 CLB |
| FDSE     |   3381 |            Register |
| LUT1     |   1306 |                 CLB |
| RAMS32   |    812 |                 CLB |
| RAMB36E2 |    288 |            BLOCKRAM |
| RAMB18E2 |     81 |            BLOCKRAM |
| SRLC32E  |     27 |                 CLB |
| URAM288  |     13 |            BLOCKRAM |
| BUFGCE   |      5 |               Clock |
| SRL16E   |      4 |                 CLB |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## kmh / Part 1（2分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_kmh_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-04 11:28:57 CST`。

SHA-256：`ed205ee7d2659ea2d4ad4d093492db422ee46bedbfd25f2efe063c9d2c6598ab`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Nov  4 11:28:56 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_kmh_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+---------+-------+------------+-----------+-------+
|          Site Type         |   Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+---------+-------+------------+-----------+-------+
| CLB LUTs*                  | 1168827 |     0 |          0 |   1303680 | 89.66 |
|   LUT as Logic             | 1162777 |     0 |          0 |   1303680 | 89.19 |
|   LUT as Memory            |    6050 |     0 |          0 |    600960 |  1.01 |
|     LUT as Distributed RAM |    6032 |     0 |            |           |       |
|     LUT as Shift Register  |      18 |     0 |            |           |       |
| CLB Registers              |  341231 |     0 |          0 |   2607360 | 13.09 |
|   Register as Flip Flop    |  341231 |     0 |          0 |   2607360 | 13.09 |
|   Register as Latch        |       0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |    8988 |     0 |          0 |    162960 |  5.52 |
| F7 Muxes                   |   54208 |     0 |          0 |    651840 |  8.32 |
| F8 Muxes                   |   15149 |     0 |          0 |    325920 |  4.65 |
| F9 Muxes                   |       0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+---------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 4915   |          Yes |         Set |            - |
| 336316 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |  140 |     0 |          0 |      2016 |  6.94 |
|   RAMB36/FIFO*    |  120 |     0 |          0 |      2016 |  5.95 |
|     RAMB36E2 only |  120 |       |            |           |       |
|   RAMB18          |   40 |     0 |          0 |      4032 |  0.99 |
|     RAMB18E2 only |   40 |       |            |           |       |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| LUT6     | 566119 |                 CLB |
| FDRE     | 336316 |            Register |
| LUT3     | 306536 |                 CLB |
| LUT5     | 290274 |                 CLB |
| LUT4     | 161214 |                 CLB |
| LUT2     |  70613 |                 CLB |
| MUXF7    |  54208 |                 CLB |
| MUXF8    |  15149 |                 CLB |
| CARRY8   |   8988 |                 CLB |
| RAMD64E  |   4984 |                 CLB |
| FDSE     |   4915 |            Register |
| LUT1     |   2418 |                 CLB |
| RAMD32   |   1684 |                 CLB |
| RAMS32   |    244 |                 CLB |
| RAMB36E2 |    120 |            BLOCKRAM |
| RAMB18E2 |     40 |            BLOCKRAM |
| SRL16E   |     18 |                 CLB |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## kmh / Part 1（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_kmh_1th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-04 00:10:48 CST`。

SHA-256：`87880906a4c0abb10ccbf11bfbba4e92414ae7bd222c3f16bbd004b038018411`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Nov  4 00:10:48 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_kmh_1th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 447588 |     0 |          0 |   1303680 | 34.33 |
|   LUT as Logic             | 446996 |     0 |          0 |   1303680 | 34.29 |
|   LUT as Memory            |    592 |     0 |          0 |    600960 |  0.10 |
|     LUT as Distributed RAM |    592 |     0 |            |           |       |
|     LUT as Shift Register  |      0 |     0 |            |           |       |
| CLB Registers              |  84208 |     0 |          0 |   2607360 |  3.23 |
|   Register as Flip Flop    |  84208 |     0 |          0 |   2607360 |  3.23 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   4071 |     0 |          0 |    162960 |  2.50 |
| F7 Muxes                   |  35527 |     0 |          0 |    651840 |  5.45 |
| F8 Muxes                   |  12562 |     0 |          0 |    325920 |  3.85 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 56    |          Yes |         Set |            - |
| 84152 |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| Block RAM Tile |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB36/FIFO* |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18       |    0 |     0 |          0 |      4032 |  0.00 |
| URAM           |    0 |     0 |          0 |       960 |  0.00 |
+----------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| DSPs           |    1 |     0 |          0 |      9024 |  0.01 |
|   DSP48E2 only |    1 |       |            |           |       |
+----------------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| LUT6     | 276230 |                 CLB |
| LUT5     |  89911 |                 CLB |
| FDRE     |  84152 |            Register |
| LUT3     |  61443 |                 CLB |
| LUT4     |  47968 |                 CLB |
| MUXF7    |  35527 |                 CLB |
| LUT2     |  26842 |                 CLB |
| MUXF8    |  12562 |                 CLB |
| CARRY8   |   4071 |                 CLB |
| LUT1     |   1769 |                 CLB |
| RAMD32   |   1036 |                 CLB |
| RAMS32   |    148 |                 CLB |
| FDSE     |     56 |            Register |
| BUFGCE   |      5 |               Clock |
| DSP48E2  |      1 |          Arithmetic |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## kmh / Part 1（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_kmh_1th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-04 02:47:00 CST`。

SHA-256：`d50b1855f528eb0c4ead597871e656119533a57eb8c19421b05a54292c3da11c`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Nov  4 02:47:00 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_kmh_1th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 514354 |     0 |          0 |   1303680 | 39.45 |
|   LUT as Logic             | 507780 |     0 |          0 |   1303680 | 38.95 |
|   LUT as Memory            |   6574 |     0 |          0 |    600960 |  1.09 |
|     LUT as Distributed RAM |   6564 |     0 |            |           |       |
|     LUT as Shift Register  |     10 |     0 |            |           |       |
| CLB Registers              | 159657 |     0 |          0 |   2607360 |  6.12 |
|   Register as Flip Flop    | 159657 |     0 |          0 |   2607360 |  6.12 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   1496 |     0 |          0 |    162960 |  0.92 |
| F7 Muxes                   |  16656 |     0 |          0 |    651840 |  2.56 |
| F8 Muxes                   |   2724 |     0 |          0 |    325920 |  0.84 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 3053   |          Yes |         Set |            - |
| 156604 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |   12 |     0 |          0 |      2016 |  0.60 |
|   RAMB36/FIFO*    |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18          |   24 |     0 |          0 |      4032 |  0.60 |
|     RAMB18E2 only |   24 |       |            |           |       |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| LUT6     | 256583 |                 CLB |
| FDRE     | 156604 |            Register |
| LUT3     | 120085 |                 CLB |
| LUT5     | 114541 |                 CLB |
| LUT4     |  70610 |                 CLB |
| LUT2     |  31621 |                 CLB |
| MUXF7    |  16656 |                 CLB |
| RAMD64E  |   4928 |                 CLB |
| FDSE     |   3053 |            Register |
| MUXF8    |   2724 |                 CLB |
| RAMD32   |   2712 |                 CLB |
| CARRY8   |   1496 |                 CLB |
| LUT1     |   1138 |                 CLB |
| RAMS32   |    392 |                 CLB |
| RAMB18E2 |     24 |            BLOCKRAM |
| SRL16E   |     10 |                 CLB |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## kmh / Part 2（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_kmh_2th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 23:32:49 CST`。

SHA-256：`6bfce2cefb623696b493fbd2d07c655876884e387977a6a2ad1739240e8908be`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 23:32:48 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_kmh_2th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 618874 |     0 |          0 |   1303680 | 47.47 |
|   LUT as Logic             | 617986 |     0 |          0 |   1303680 | 47.40 |
|   LUT as Memory            |    888 |     0 |          0 |    600960 |  0.15 |
|     LUT as Distributed RAM |    888 |     0 |            |           |       |
|     LUT as Shift Register  |      0 |     0 |            |           |       |
| CLB Registers              | 140144 |     0 |          0 |   2607360 |  5.37 |
|   Register as Flip Flop    | 140144 |     0 |          0 |   2607360 |  5.37 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   1248 |     0 |          0 |    162960 |  0.77 |
| F7 Muxes                   |  36238 |     0 |          0 |    651840 |  5.56 |
| F8 Muxes                   |  14511 |     0 |          0 |    325920 |  4.45 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 3178   |          Yes |         Set |            - |
| 136966 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| Block RAM Tile |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB36/FIFO* |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18       |    0 |     0 |          0 |      4032 |  0.00 |
| URAM           |    0 |     0 |          0 |       960 |  0.00 |
+----------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| LUT6     | 325433 |                 CLB |
| FDRE     | 136966 |            Register |
| LUT4     | 136633 |                 CLB |
| LUT5     | 128834 |                 CLB |
| LUT3     |  66770 |                 CLB |
| MUXF7    |  36238 |                 CLB |
| LUT2     |  23092 |                 CLB |
| MUXF8    |  14511 |                 CLB |
| FDSE     |   3178 |            Register |
| RAMD32   |   1554 |                 CLB |
| CARRY8   |   1248 |                 CLB |
| LUT1     |    475 |                 CLB |
| RAMS32   |    222 |                 CLB |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## kmh / Part 2（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_kmh_2th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 23:31:36 CST`。

SHA-256：`4f943af639bb686b7d4eef7d71d4031a75391144fe54ba9dd3d7685b7e81e7ef`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 23:31:36 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_kmh_2th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 393113 |     0 |          0 |   1303680 | 30.15 |
|   LUT as Logic             | 392225 |     0 |          0 |   1303680 | 30.09 |
|   LUT as Memory            |    888 |     0 |          0 |    600960 |  0.15 |
|     LUT as Distributed RAM |    888 |     0 |            |           |       |
|     LUT as Shift Register  |      0 |     0 |            |           |       |
| CLB Registers              |  73913 |     0 |          0 |   2607360 |  2.83 |
|   Register as Flip Flop    |  73913 |     0 |          0 |   2607360 |  2.83 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   3435 |     0 |          0 |    162960 |  2.11 |
| F7 Muxes                   |  34903 |     0 |          0 |    651840 |  5.35 |
| F8 Muxes                   |  12489 |     0 |          0 |    325920 |  3.83 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 55    |          Yes |         Set |            - |
| 73858 |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| Block RAM Tile |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB36/FIFO* |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18       |    0 |     0 |          0 |      4032 |  0.00 |
| URAM           |    0 |     0 |          0 |       960 |  0.00 |
+----------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| LUT6     | 247631 |                 CLB |
| LUT5     |  75622 |                 CLB |
| FDRE     |  73858 |            Register |
| LUT3     |  46522 |                 CLB |
| LUT4     |  44089 |                 CLB |
| MUXF7    |  34903 |                 CLB |
| LUT2     |  21889 |                 CLB |
| MUXF8    |  12489 |                 CLB |
| CARRY8   |   3435 |                 CLB |
| LUT1     |   1581 |                 CLB |
| RAMD32   |   1554 |                 CLB |
| RAMS32   |    222 |                 CLB |
| FDSE     |     55 |            Register |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## kmh / Part 3（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_kmh_3th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 23:42:05 CST`。

SHA-256：`e96712c5b0953ab0d6ce45dad08cfdc4105a1d458e1b0606e6bdfe0bb2902121`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 23:42:05 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_kmh_3th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 320520 |     0 |          0 |   1303680 | 24.59 |
|   LUT as Logic             | 319632 |     0 |          0 |   1303680 | 24.52 |
|   LUT as Memory            |    888 |     0 |          0 |    600960 |  0.15 |
|     LUT as Distributed RAM |    888 |     0 |            |           |       |
|     LUT as Shift Register  |      0 |     0 |            |           |       |
| CLB Registers              |  63180 |     0 |          0 |   2607360 |  2.42 |
|   Register as Flip Flop    |  63180 |     0 |          0 |   2607360 |  2.42 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   1877 |     0 |          0 |    162960 |  1.15 |
| F7 Muxes                   |  23444 |     0 |          0 |    651840 |  3.60 |
| F8 Muxes                   |  10687 |     0 |          0 |    325920 |  3.28 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 424   |          Yes |         Set |            - |
| 62756 |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| Block RAM Tile |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB36/FIFO* |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18       |    0 |     0 |          0 |      4032 |  0.00 |
| URAM           |    0 |     0 |          0 |       960 |  0.00 |
+----------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| DSPs           |    1 |     0 |          0 |      9024 |  0.01 |
|   DSP48E2 only |    1 |       |            |           |       |
+----------------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| LUT6     | 163821 |                 CLB |
| LUT4     |  81673 |                 CLB |
| FDRE     |  62756 |            Register |
| LUT5     |  53778 |                 CLB |
| LUT3     |  42802 |                 CLB |
| MUXF7    |  23444 |                 CLB |
| LUT2     |  16593 |                 CLB |
| MUXF8    |  10687 |                 CLB |
| CARRY8   |   1877 |                 CLB |
| RAMD32   |   1554 |                 CLB |
| LUT1     |   1136 |                 CLB |
| FDSE     |    424 |            Register |
| RAMS32   |    222 |                 CLB |
| BUFGCE   |      5 |               Clock |
| DSP48E2  |      1 |          Arithmetic |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## nanhu-g / Part 0（2分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_nanhu-g_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-04 01:52:19 CST`。

SHA-256：`5a7b1adbfab29fa2b069bf6f4460b822f21050087f2f8ab3af8e20e0c358c9f1`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Nov  4 01:52:18 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_nanhu-g_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 701064 |     0 |          0 |   1303680 | 53.78 |
|   LUT as Logic             | 685637 |     0 |          0 |   1303680 | 52.59 |
|   LUT as Memory            |  15427 |     0 |          0 |    600960 |  2.57 |
|     LUT as Distributed RAM |  15346 |     0 |            |           |       |
|     LUT as Shift Register  |     81 |     0 |            |           |       |
| CLB Registers              | 430497 |     0 |          0 |   2607360 | 16.51 |
|   Register as Flip Flop    | 430497 |     0 |          0 |   2607360 | 16.51 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   1100 |     0 |          0 |    162960 |  0.68 |
| F7 Muxes                   |   5713 |     0 |          0 |    651840 |  0.88 |
| F8 Muxes                   |   1887 |     0 |          0 |    325920 |  0.58 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 6524   |          Yes |         Set |            - |
| 423973 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |  233 |     0 |          0 |      2016 | 11.56 |
|   RAMB36/FIFO*    |  112 |     0 |          0 |      2016 |  5.56 |
|     RAMB36E2 only |  112 |       |            |           |       |
|   RAMB18          |  242 |     0 |          0 |      4032 |  6.00 |
|     RAMB18E2 only |  242 |       |            |           |       |
| URAM              |  141 |     0 |          0 |       960 | 14.69 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| FDRE     | 423973 |            Register |
| LUT5     | 258050 |                 CLB |
| LUT6     | 228285 |                 CLB |
| LUT3     | 198631 |                 CLB |
| LUT4     |  98637 |                 CLB |
| LUT2     |  18342 |                 CLB |
| RAMD32   |  14682 |                 CLB |
| RAMD64E  |   6746 |                 CLB |
| FDSE     |   6524 |            Register |
| MUXF7    |   5713 |                 CLB |
| RAMS32   |   2286 |                 CLB |
| LUT1     |   2090 |                 CLB |
| MUXF8    |   1887 |                 CLB |
| CARRY8   |   1100 |                 CLB |
| RAMB18E2 |    242 |            BLOCKRAM |
| URAM288  |    141 |            BLOCKRAM |
| RAMB36E2 |    112 |            BLOCKRAM |
| SRLC32E  |     71 |                 CLB |
| SRL16E   |     10 |                 CLB |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## nanhu-g / Part 0（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_nanhu-g_0th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-04 00:03:22 CST`。

SHA-256：`021c787b82e527153b808c5167a1ac51b81f8a8cdc347fb46185d9de3c272e5f`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Nov  4 00:03:22 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_nanhu-g_0th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 540840 |     0 |          0 |   1303680 | 41.49 |
|   LUT as Logic             | 532293 |     0 |          0 |   1303680 | 40.83 |
|   LUT as Memory            |   8547 |     0 |          0 |    600960 |  1.42 |
|     LUT as Distributed RAM |   8466 |     0 |            |           |       |
|     LUT as Shift Register  |     81 |     0 |            |           |       |
| CLB Registers              | 343299 |     0 |          0 |   2607360 | 13.17 |
|   Register as Flip Flop    | 343299 |     0 |          0 |   2607360 | 13.17 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |    795 |     0 |          0 |    162960 |  0.49 |
| F7 Muxes                   |   1362 |     0 |          0 |    651840 |  0.21 |
| F8 Muxes                   |     21 |     0 |          0 |    325920 | <0.01 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 5555   |          Yes |         Set |            - |
| 337744 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |  182 |     0 |          0 |      2016 |  9.03 |
|   RAMB36/FIFO*    |   96 |     0 |          0 |      2016 |  4.76 |
|     RAMB36E2 only |   96 |       |            |           |       |
|   RAMB18          |  172 |     0 |          0 |      4032 |  4.27 |
|     RAMB18E2 only |  172 |       |            |           |       |
| URAM              |  141 |     0 |          0 |       960 | 14.69 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| FDRE     | 337744 |            Register |
| LUT5     | 192876 |                 CLB |
| LUT6     | 170774 |                 CLB |
| LUT3     | 165928 |                 CLB |
| LUT4     |  83566 |                 CLB |
| LUT2     |  14913 |                 CLB |
| RAMD32   |  14292 |                 CLB |
| FDSE     |   5555 |            Register |
| RAMS32   |   2160 |                 CLB |
| LUT1     |   1456 |                 CLB |
| MUXF7    |   1362 |                 CLB |
| CARRY8   |    795 |                 CLB |
| RAMB18E2 |    172 |            BLOCKRAM |
| URAM288  |    141 |            BLOCKRAM |
| RAMD64E  |    138 |                 CLB |
| RAMB36E2 |     96 |            BLOCKRAM |
| SRLC32E  |     71 |                 CLB |
| MUXF8    |     21 |                 CLB |
| SRL16E   |     10 |                 CLB |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## nanhu-g / Part 0（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_nanhu-g_0th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 23:17:57 CST`。

SHA-256：`e2e5af98499cf88a9ad1c9dde41a69b08258177c92026b8e0bb7a3d0a66f1d1c`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 23:17:57 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_nanhu-g_0th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 360038 |     0 |          0 |   1303680 | 27.62 |
|   LUT as Logic             | 355731 |     0 |          0 |   1303680 | 27.29 |
|   LUT as Memory            |   4307 |     0 |          0 |    600960 |  0.72 |
|     LUT as Distributed RAM |   4226 |     0 |            |           |       |
|     LUT as Shift Register  |     81 |     0 |            |           |       |
| CLB Registers              | 241297 |     0 |          0 |   2607360 |  9.25 |
|   Register as Flip Flop    | 241297 |     0 |          0 |   2607360 |  9.25 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |    428 |     0 |          0 |    162960 |  0.26 |
| F7 Muxes                   |    662 |     0 |          0 |    651840 |  0.10 |
| F8 Muxes                   |     26 |     0 |          0 |    325920 | <0.01 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 3061   |          Yes |         Set |            - |
| 238236 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |   74 |     0 |          0 |      2016 |  3.67 |
|   RAMB36/FIFO*    |   28 |     0 |          0 |      2016 |  1.39 |
|     RAMB36E2 only |   28 |       |            |           |       |
|   RAMB18          |   92 |     0 |          0 |      4032 |  2.28 |
|     RAMB18E2 only |   92 |       |            |           |       |
| URAM              |  141 |     0 |          0 |       960 | 14.69 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| FDRE     | 238236 |            Register |
| LUT5     | 148506 |                 CLB |
| LUT3     | 112215 |                 CLB |
| LUT6     | 103927 |                 CLB |
| LUT4     |  46320 |                 CLB |
| RAMD32   |   7226 |                 CLB |
| LUT2     |   6813 |                 CLB |
| FDSE     |   3061 |            Register |
| RAMS32   |   1090 |                 CLB |
| LUT1     |    837 |                 CLB |
| MUXF7    |    662 |                 CLB |
| CARRY8   |    428 |                 CLB |
| URAM288  |    141 |            BLOCKRAM |
| RAMB18E2 |     92 |            BLOCKRAM |
| SRLC32E  |     71 |                 CLB |
| RAMB36E2 |     28 |            BLOCKRAM |
| MUXF8    |     26 |                 CLB |
| SRL16E   |     10 |                 CLB |
| RAMD64E  |     10 |                 CLB |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## nanhu-g / Part 1（2分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_nanhu-g_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-04 01:47:30 CST`。

SHA-256：`b7fcd802bb5769c14f59b0d46dcdcd9fbefe3dbcb13a9c25c7d112abcb770a3e`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Nov  4 01:47:30 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_nanhu-g_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 819798 |     0 |          0 |   1303680 | 62.88 |
|   LUT as Logic             | 819165 |     0 |          0 |   1303680 | 62.83 |
|   LUT as Memory            |    633 |     0 |          0 |    600960 |  0.11 |
|     LUT as Distributed RAM |    612 |     0 |            |           |       |
|     LUT as Shift Register  |     21 |     0 |            |           |       |
| CLB Registers              | 288325 |     0 |          0 |   2607360 | 11.06 |
|   Register as Flip Flop    | 288325 |     0 |          0 |   2607360 | 11.06 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   8900 |     0 |          0 |    162960 |  5.46 |
| F7 Muxes                   |   9614 |     0 |          0 |    651840 |  1.47 |
| F8 Muxes                   |   1427 |     0 |          0 |    325920 |  0.44 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 2701   |          Yes |         Set |            - |
| 285624 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+-------+-------+------------+-----------+-------+
|     Site Type     |  Used | Fixed | Prohibited | Available | Util% |
+-------------------+-------+-------+------------+-----------+-------+
| Block RAM Tile    | 159.5 |     0 |          0 |      2016 |  7.91 |
|   RAMB36/FIFO*    |   149 |     0 |          0 |      2016 |  7.39 |
|     RAMB36E2 only |   149 |       |            |           |       |
|   RAMB18          |    21 |     0 |          0 |      4032 |  0.52 |
|     RAMB18E2 only |    21 |       |            |           |       |
| URAM              |     0 |     0 |          0 |       960 |  0.00 |
+-------------------+-------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| LUT6     | 326144 |                 CLB |
| FDRE     | 285624 |            Register |
| LUT3     | 240257 |                 CLB |
| LUT5     | 190686 |                 CLB |
| LUT4     | 185200 |                 CLB |
| LUT2     |  40274 |                 CLB |
| MUXF7    |   9614 |                 CLB |
| CARRY8   |   8900 |                 CLB |
| FDSE     |   2701 |            Register |
| LUT1     |   1495 |                 CLB |
| MUXF8    |   1427 |                 CLB |
| RAMD32   |   1068 |                 CLB |
| RAMS32   |    152 |                 CLB |
| RAMB36E2 |    149 |            BLOCKRAM |
| RAMB18E2 |     21 |            BLOCKRAM |
| SRLC32E  |     16 |                 CLB |
| SRL16E   |      5 |                 CLB |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## nanhu-g / Part 1（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_nanhu-g_1th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-04 00:18:41 CST`。

SHA-256：`aa61f465d3167f6197d232dd88f0b2fd033fe846849e3d85427ffe51a3080596`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Nov  4 00:18:40 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_nanhu-g_1th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 472202 |     0 |          0 |   1303680 | 36.22 |
|   LUT as Logic             | 463550 |     0 |          0 |   1303680 | 35.56 |
|   LUT as Memory            |   8652 |     0 |          0 |    600960 |  1.44 |
|     LUT as Distributed RAM |   8652 |     0 |            |           |       |
|     LUT as Shift Register  |      0 |     0 |            |           |       |
| CLB Registers              | 196761 |     0 |          0 |   2607360 |  7.55 |
|   Register as Flip Flop    | 196761 |     0 |          0 |   2607360 |  7.55 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   5535 |     0 |          0 |    162960 |  3.40 |
| F7 Muxes                   |  11014 |     0 |          0 |    651840 |  1.69 |
| F8 Muxes                   |   2478 |     0 |          0 |    325920 |  0.76 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 2256   |          Yes |         Set |            - |
| 194505 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |  171 |     0 |          0 |      2016 |  8.48 |
|   RAMB36/FIFO*    |  128 |     0 |          0 |      2016 |  6.35 |
|     RAMB36E2 only |  128 |       |            |           |       |
|   RAMB18          |   86 |     0 |          0 |      4032 |  2.13 |
|     RAMB18E2 only |   86 |       |            |           |       |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| FDRE     | 194505 |            Register |
| LUT6     | 175978 |                 CLB |
| LUT3     | 160332 |                 CLB |
| LUT4     | 107112 |                 CLB |
| LUT5     | 103524 |                 CLB |
| LUT2     |  29157 |                 CLB |
| MUXF7    |  11014 |                 CLB |
| RAMD64E  |   6608 |                 CLB |
| CARRY8   |   5535 |                 CLB |
| RAMD32   |   3488 |                 CLB |
| MUXF8    |   2478 |                 CLB |
| FDSE     |   2256 |            Register |
| LUT1     |   1471 |                 CLB |
| RAMS32   |    568 |                 CLB |
| RAMB36E2 |    128 |            BLOCKRAM |
| RAMB18E2 |     86 |            BLOCKRAM |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## nanhu-g / Part 1（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_nanhu-g_1th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 23:45:55 CST`。

SHA-256：`6fbfe11c2105c5166116a3c85ffb350cc72e55dcab46cdffe5d55b8da343a3f0`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 23:45:55 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_nanhu-g_1th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 346956 |     0 |          0 |   1303680 | 26.61 |
|   LUT as Logic             | 334492 |     0 |          0 |   1303680 | 25.66 |
|   LUT as Memory            |  12464 |     0 |          0 |    600960 |  2.07 |
|     LUT as Distributed RAM |  12464 |     0 |            |           |       |
|     LUT as Shift Register  |      0 |     0 |            |           |       |
| CLB Registers              | 197256 |     0 |          0 |   2607360 |  7.57 |
|   Register as Flip Flop    | 197256 |     0 |          0 |   2607360 |  7.57 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |    717 |     0 |          0 |    162960 |  0.44 |
| F7 Muxes                   |   5348 |     0 |          0 |    651840 |  0.82 |
| F8 Muxes                   |   2035 |     0 |          0 |    325920 |  0.62 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 3518   |          Yes |         Set |            - |
| 193738 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |  159 |     0 |          0 |      2016 |  7.89 |
|   RAMB36/FIFO*    |   84 |     0 |          0 |      2016 |  4.17 |
|     RAMB36E2 only |   84 |       |            |           |       |
|   RAMB18          |  150 |     0 |          0 |      4032 |  3.72 |
|     RAMB18E2 only |  150 |       |            |           |       |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| FDRE     | 193738 |            Register |
| LUT6     | 122999 |                 CLB |
| LUT5     | 112515 |                 CLB |
| LUT3     | 103513 |                 CLB |
| LUT4     |  46269 |                 CLB |
| LUT2     |  13487 |                 CLB |
| RAMD32   |   9808 |                 CLB |
| RAMD64E  |   6736 |                 CLB |
| MUXF7    |   5348 |                 CLB |
| FDSE     |   3518 |            Register |
| MUXF8    |   2035 |                 CLB |
| RAMS32   |   1532 |                 CLB |
| LUT1     |   1391 |                 CLB |
| CARRY8   |    717 |                 CLB |
| RAMB18E2 |    150 |            BLOCKRAM |
| RAMB36E2 |     84 |            BLOCKRAM |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## nanhu-g / Part 2（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_nanhu-g_2th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 23:41:48 CST`。

SHA-256：`6fa03d4ef98155edb8302c59c74f076900e1705654a30e83df477a5c005fdba6`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 23:41:47 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_nanhu-g_2th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 496134 |     0 |          0 |   1303680 | 38.06 |
|   LUT as Logic             | 495049 |     0 |          0 |   1303680 | 37.97 |
|   LUT as Memory            |   1085 |     0 |          0 |    600960 |  0.18 |
|     LUT as Distributed RAM |   1064 |     0 |            |           |       |
|     LUT as Shift Register  |     21 |     0 |            |           |       |
| CLB Registers              | 184392 |     0 |          0 |   2607360 |  7.07 |
|   Register as Flip Flop    | 184392 |     0 |          0 |   2607360 |  7.07 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   3717 |     0 |          0 |    162960 |  2.28 |
| F7 Muxes                   |   4275 |     0 |          0 |    651840 |  0.66 |
| F8 Muxes                   |   1016 |     0 |          0 |    325920 |  0.31 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 1187   |          Yes |         Set |            - |
| 183205 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    | 39.5 |     0 |          0 |      2016 |  1.96 |
|   RAMB36/FIFO*    |   37 |     0 |          0 |      2016 |  1.84 |
|     RAMB36E2 only |   37 |       |            |           |       |
|   RAMB18          |    5 |     0 |          0 |      4032 |  0.12 |
|     RAMB18E2 only |    5 |       |            |           |       |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| LUT6     | 183611 |                 CLB |
| FDRE     | 183205 |            Register |
| LUT3     | 154220 |                 CLB |
| LUT5     | 132702 |                 CLB |
| LUT4     | 103347 |                 CLB |
| LUT2     |  18207 |                 CLB |
| MUXF7    |   4275 |                 CLB |
| CARRY8   |   3717 |                 CLB |
| RAMD32   |   1862 |                 CLB |
| FDSE     |   1187 |            Register |
| MUXF8    |   1016 |                 CLB |
| LUT1     |    930 |                 CLB |
| RAMS32   |    266 |                 CLB |
| RAMB36E2 |     37 |            BLOCKRAM |
| SRLC32E  |     16 |                 CLB |
| SRL16E   |      5 |                 CLB |
| RAMB18E2 |      5 |            BLOCKRAM |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## nanhu-g / Part 2（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_nanhu-g_2th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-04 00:16:31 CST`。

SHA-256：`7f4ff15485376842a45be35688987d67037b51e58bd83e25e3d9db674013fef0`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Nov  4 00:16:31 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_nanhu-g_2th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 463696 |     0 |          0 |   1303680 | 35.57 |
|   LUT as Logic             | 462567 |     0 |          0 |   1303680 | 35.48 |
|   LUT as Memory            |   1129 |     0 |          0 |    600960 |  0.19 |
|     LUT as Distributed RAM |   1124 |     0 |            |           |       |
|     LUT as Shift Register  |      5 |     0 |            |           |       |
| CLB Registers              | 165604 |     0 |          0 |   2607360 |  6.35 |
|   Register as Flip Flop    | 165604 |     0 |          0 |   2607360 |  6.35 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   7710 |     0 |          0 |    162960 |  4.73 |
| F7 Muxes                   |   7876 |     0 |          0 |    651840 |  1.21 |
| F8 Muxes                   |   1010 |     0 |          0 |    325920 |  0.31 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 1923   |          Yes |         Set |            - |
| 163681 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |  123 |     0 |          0 |      2016 |  6.10 |
|   RAMB36/FIFO*    |  114 |     0 |          0 |      2016 |  5.65 |
|     RAMB36E2 only |  114 |       |            |           |       |
|   RAMB18          |   18 |     0 |          0 |      4032 |  0.45 |
|     RAMB18E2 only |   18 |       |            |           |       |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| LUT6     | 181101 |                 CLB |
| FDRE     | 163681 |            Register |
| LUT3     | 129674 |                 CLB |
| LUT4     | 115355 |                 CLB |
| LUT5     | 105846 |                 CLB |
| LUT2     |  29602 |                 CLB |
| MUXF7    |   7876 |                 CLB |
| CARRY8   |   7710 |                 CLB |
| RAMD32   |   1964 |                 CLB |
| FDSE     |   1923 |            Register |
| MUXF8    |   1010 |                 CLB |
| LUT1     |    957 |                 CLB |
| RAMS32   |    280 |                 CLB |
| RAMB36E2 |    114 |            BLOCKRAM |
| RAMB18E2 |     18 |            BLOCKRAM |
| SRL16E   |      5 |                 CLB |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## nanhu-g / Part 3（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_nanhu-g_3th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 23:04:30 CST`。

SHA-256：`7ebd90b635507946319054f11d87685eca5d31a5bd1795b746436b6565c3513c`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 23:04:30 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_nanhu-g_3th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 357800 |     0 |          0 |   1303680 | 27.45 |
|   LUT as Logic             | 357016 |     0 |          0 |   1303680 | 27.39 |
|   LUT as Memory            |    784 |     0 |          0 |    600960 |  0.13 |
|     LUT as Distributed RAM |    768 |     0 |            |           |       |
|     LUT as Shift Register  |     16 |     0 |            |           |       |
| CLB Registers              | 126616 |     0 |          0 |   2607360 |  4.86 |
|   Register as Flip Flop    | 126616 |     0 |          0 |   2607360 |  4.86 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   1248 |     0 |          0 |    162960 |  0.77 |
| F7 Muxes                   |   2621 |     0 |          0 |    651840 |  0.40 |
| F8 Muxes                   |    475 |     0 |          0 |    325920 |  0.15 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 716    |          Yes |         Set |            - |
| 125900 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    | 36.5 |     0 |          0 |      2016 |  1.81 |
|   RAMB36/FIFO*    |   35 |     0 |          0 |      2016 |  1.74 |
|     RAMB36E2 only |   35 |       |            |           |       |
|   RAMB18          |    3 |     0 |          0 |      4032 |  0.07 |
|     RAMB18E2 only |    3 |       |            |           |       |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| LUT6     | 145303 |                 CLB |
| FDRE     | 125900 |            Register |
| LUT3     | 112353 |                 CLB |
| LUT5     |  88951 |                 CLB |
| LUT4     |  66911 |                 CLB |
| LUT2     |  12194 |                 CLB |
| MUXF7    |   2621 |                 CLB |
| RAMD32   |   1344 |                 CLB |
| CARRY8   |   1248 |                 CLB |
| FDSE     |    716 |            Register |
| LUT1     |    715 |                 CLB |
| MUXF8    |    475 |                 CLB |
| RAMS32   |    192 |                 CLB |
| RAMB36E2 |     35 |            BLOCKRAM |
| SRLC32E  |     16 |                 CLB |
| BUFGCE   |      5 |               Clock |
| RAMB18E2 |      3 |            BLOCKRAM |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## picorv32 / Part 0（2分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_picorv32_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-10-29 00:30:19 CST`。

SHA-256：`1a2cd73c531b6c4bfb7c0b6aeb31106712834c14f5177dee2f3caa29cb34fb08`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Thu Oct 29 00:30:19 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_picorv32_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+------+-------+------------+-----------+-------+
|          Site Type         | Used | Fixed | Prohibited | Available | Util% |
+----------------------------+------+-------+------------+-----------+-------+
| CLB LUTs*                  | 3810 |     0 |          0 |   1303680 |  0.29 |
|   LUT as Logic             | 3666 |     0 |          0 |   1303680 |  0.28 |
|   LUT as Memory            |  144 |     0 |          0 |    600960 |  0.02 |
|     LUT as Distributed RAM |  144 |     0 |            |           |       |
|     LUT as Shift Register  |    0 |     0 |            |           |       |
| CLB Registers              | 2856 |     0 |          0 |   2607360 |  0.11 |
|   Register as Flip Flop    | 2856 |     0 |          0 |   2607360 |  0.11 |
|   Register as Latch        |    0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   65 |     0 |          0 |    162960 |  0.04 |
| F7 Muxes                   |    0 |     0 |          0 |    651840 |  0.00 |
| F8 Muxes                   |    0 |     0 |          0 |    325920 |  0.00 |
| F9 Muxes                   |    0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 95    |          Yes |         Set |            - |
| 2761  |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |  6.5 |     0 |          0 |      2016 |  0.32 |
|   RAMB36/FIFO*    |    6 |     0 |          0 |      2016 |  0.30 |
|     RAMB36E2 only |    6 |       |            |           |       |
|   RAMB18          |    1 |     0 |          0 |      4032 |  0.02 |
|     RAMB18E2 only |    1 |       |            |           |       |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+------+---------------------+
| Ref Name | Used | Functional Category |
+----------+------+---------------------+
| FDRE     | 2761 |            Register |
| LUT6     | 1253 |                 CLB |
| LUT3     | 1179 |                 CLB |
| LUT4     |  699 |                 CLB |
| LUT2     |  531 |                 CLB |
| LUT5     |  473 |                 CLB |
| LUT1     |  432 |                 CLB |
| RAMD32   |  242 |                 CLB |
| FDSE     |   95 |            Register |
| CARRY8   |   65 |                 CLB |
| RAMS32   |   34 |                 CLB |
| RAMB36E2 |    6 |            BLOCKRAM |
| BUFGCE   |    5 |               Clock |
| RAMB18E2 |    1 |            BLOCKRAM |
+----------+------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## picorv32 / Part 0（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_picorv32_0th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-10-28 20:42:04 CST`。

SHA-256：`788fb1e20465c13d9f8da00bf17461b4cbc6e34dbeed5d826eec78db5086105b`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Oct 28 20:42:03 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_picorv32_0th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+------+-------+------------+-----------+-------+
|          Site Type         | Used | Fixed | Prohibited | Available | Util% |
+----------------------------+------+-------+------------+-----------+-------+
| CLB LUTs*                  | 4366 |     0 |          0 |   1303680 |  0.33 |
|   LUT as Logic             | 4182 |     0 |          0 |   1303680 |  0.32 |
|   LUT as Memory            |  184 |     0 |          0 |    600960 |  0.03 |
|     LUT as Distributed RAM |  184 |     0 |            |           |       |
|     LUT as Shift Register  |    0 |     0 |            |           |       |
| CLB Registers              | 3268 |     0 |          0 |   2607360 |  0.13 |
|   Register as Flip Flop    | 3268 |     0 |          0 |   2607360 |  0.13 |
|   Register as Latch        |    0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |  100 |     0 |          0 |    162960 |  0.06 |
| F7 Muxes                   |    0 |     0 |          0 |    651840 |  0.00 |
| F8 Muxes                   |    0 |     0 |          0 |    325920 |  0.00 |
| F9 Muxes                   |    0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 93    |          Yes |         Set |            - |
| 3175  |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |  6.5 |     0 |          0 |      2016 |  0.32 |
|   RAMB36/FIFO*    |    6 |     0 |          0 |      2016 |  0.30 |
|     RAMB36E2 only |    6 |       |            |           |       |
|   RAMB18          |    1 |     0 |          0 |      4032 |  0.02 |
|     RAMB18E2 only |    1 |       |            |           |       |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+------+---------------------+
| Ref Name | Used | Functional Category |
+----------+------+---------------------+
| FDRE     | 3175 |            Register |
| LUT3     | 1434 |                 CLB |
| LUT6     | 1267 |                 CLB |
| LUT4     |  834 |                 CLB |
| LUT2     |  691 |                 CLB |
| LUT1     |  467 |                 CLB |
| LUT5     |  428 |                 CLB |
| RAMD32   |  310 |                 CLB |
| CARRY8   |  100 |                 CLB |
| FDSE     |   93 |            Register |
| RAMS32   |   46 |                 CLB |
| RAMB36E2 |    6 |            BLOCKRAM |
| BUFGCE   |    5 |               Clock |
| RAMB18E2 |    1 |            BLOCKRAM |
+----------+------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## picorv32 / Part 1（2分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_picorv32_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-10-29 00:29:09 CST`。

SHA-256：`611a91d8323aa698218f9221952ec0f394e705e3bf558d55fc8be140eaeef5ad`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Thu Oct 29 00:29:09 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_picorv32_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+------+-------+------------+-----------+-------+
|          Site Type         | Used | Fixed | Prohibited | Available | Util% |
+----------------------------+------+-------+------------+-----------+-------+
| CLB LUTs*                  | 2652 |     0 |          0 |   1303680 |  0.20 |
|   LUT as Logic             | 2612 |     0 |          0 |   1303680 |  0.20 |
|   LUT as Memory            |   40 |     0 |          0 |    600960 | <0.01 |
|     LUT as Distributed RAM |   40 |     0 |            |           |       |
|     LUT as Shift Register  |    0 |     0 |            |           |       |
| CLB Registers              | 2015 |     0 |          0 |   2607360 |  0.08 |
|   Register as Flip Flop    | 2015 |     0 |          0 |   2607360 |  0.08 |
|   Register as Latch        |    0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   96 |     0 |          0 |    162960 |  0.06 |
| F7 Muxes                   |    0 |     0 |          0 |    651840 |  0.00 |
| F8 Muxes                   |    0 |     0 |          0 |    325920 |  0.00 |
| F9 Muxes                   |    0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 41    |          Yes |         Set |            - |
| 1974  |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| Block RAM Tile |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB36/FIFO* |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18       |    0 |     0 |          0 |      4032 |  0.00 |
| URAM           |    0 |     0 |          0 |       960 |  0.00 |
+----------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| DSPs           |    4 |     0 |          0 |      9024 |  0.04 |
|   DSP48E2 only |    4 |       |            |           |       |
+----------------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+------+---------------------+
| Ref Name | Used | Functional Category |
+----------+------+---------------------+
| FDRE     | 1974 |            Register |
| LUT3     |  842 |                 CLB |
| LUT6     |  744 |                 CLB |
| LUT1     |  570 |                 CLB |
| LUT2     |  442 |                 CLB |
| LUT4     |  434 |                 CLB |
| LUT5     |  208 |                 CLB |
| CARRY8   |   96 |                 CLB |
| RAMD32   |   68 |                 CLB |
| FDSE     |   41 |            Register |
| RAMS32   |   12 |                 CLB |
| BUFGCE   |    5 |               Clock |
| DSP48E2  |    4 |          Arithmetic |
+----------+------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## picorv32 / Part 1（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_picorv32_1th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-10-28 20:40:22 CST`。

SHA-256：`52083ff0baaa24de984a90fb421bccbbaac2d5f8eb84321c8f374660978de0a4`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Oct 28 20:40:21 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_picorv32_1th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+-------------------------+------+-------+------------+-----------+-------+
|        Site Type        | Used | Fixed | Prohibited | Available | Util% |
+-------------------------+------+-------+------------+-----------+-------+
| CLB LUTs*               | 1729 |     0 |          0 |   1303680 |  0.13 |
|   LUT as Logic          | 1729 |     0 |          0 |   1303680 |  0.13 |
|   LUT as Memory         |    0 |     0 |          0 |    600960 |  0.00 |
| CLB Registers           | 1170 |     0 |          0 |   2607360 |  0.04 |
|   Register as Flip Flop | 1170 |     0 |          0 |   2607360 |  0.04 |
|   Register as Latch     |    0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                  |   18 |     0 |          0 |    162960 |  0.01 |
| F7 Muxes                |    0 |     0 |          0 |    651840 |  0.00 |
| F8 Muxes                |    0 |     0 |          0 |    325920 |  0.00 |
| F9 Muxes                |    0 |     0 |          0 |    162960 |  0.00 |
+-------------------------+------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 37    |          Yes |         Set |            - |
| 1133  |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| Block RAM Tile |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB36/FIFO* |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18       |    0 |     0 |          0 |      4032 |  0.00 |
| URAM           |    0 |     0 |          0 |       960 |  0.00 |
+----------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+------+---------------------+
| Ref Name | Used | Functional Category |
+----------+------+---------------------+
| FDRE     | 1133 |            Register |
| LUT2     |  478 |                 CLB |
| LUT1     |  472 |                 CLB |
| LUT6     |  467 |                 CLB |
| LUT3     |  317 |                 CLB |
| LUT5     |  201 |                 CLB |
| LUT4     |  158 |                 CLB |
| FDSE     |   37 |            Register |
| CARRY8   |   18 |                 CLB |
| BUFGCE   |    5 |               Clock |
+----------+------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## picorv32 / Part 1（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_picorv32_1th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-10-28 20:40:40 CST`。

SHA-256：`b2152d3193834e0187e98307a542993ad1e922fa938871dad1cf17f921c84247`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Oct 28 20:40:40 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_picorv32_1th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+-------------------------+------+-------+------------+-----------+-------+
|        Site Type        | Used | Fixed | Prohibited | Available | Util% |
+-------------------------+------+-------+------------+-----------+-------+
| CLB LUTs*               | 1797 |     0 |          0 |   1303680 |  0.14 |
|   LUT as Logic          | 1797 |     0 |          0 |   1303680 |  0.14 |
|   LUT as Memory         |    0 |     0 |          0 |    600960 |  0.00 |
| CLB Registers           | 1223 |     0 |          0 |   2607360 |  0.05 |
|   Register as Flip Flop | 1223 |     0 |          0 |   2607360 |  0.05 |
|   Register as Latch     |    0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                  |   21 |     0 |          0 |    162960 |  0.01 |
| F7 Muxes                |    0 |     0 |          0 |    651840 |  0.00 |
| F8 Muxes                |    0 |     0 |          0 |    325920 |  0.00 |
| F9 Muxes                |    0 |     0 |          0 |    162960 |  0.00 |
+-------------------------+------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 37    |          Yes |         Set |            - |
| 1186  |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| Block RAM Tile |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB36/FIFO* |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18       |    0 |     0 |          0 |      4032 |  0.00 |
| URAM           |    0 |     0 |          0 |       960 |  0.00 |
+----------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+------+---------------------+
| Ref Name | Used | Functional Category |
+----------+------+---------------------+
| FDRE     | 1186 |            Register |
| LUT6     |  543 |                 CLB |
| LUT3     |  449 |                 CLB |
| LUT1     |  436 |                 CLB |
| LUT2     |  420 |                 CLB |
| LUT5     |  190 |                 CLB |
| LUT4     |  148 |                 CLB |
| FDSE     |   37 |            Register |
| CARRY8   |   21 |                 CLB |
| BUFGCE   |    5 |               Clock |
+----------+------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## picorv32 / Part 2（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_picorv32_2th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-10-28 20:40:32 CST`。

SHA-256：`d24f49e54860a95696b57791887696fd3a394bece1337041f8cc0dd0dbedd85b`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Oct 28 20:40:32 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_picorv32_2th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+-------------------------+------+-------+------------+-----------+-------+
|        Site Type        | Used | Fixed | Prohibited | Available | Util% |
+-------------------------+------+-------+------------+-----------+-------+
| CLB LUTs*               | 1950 |     0 |          0 |   1303680 |  0.15 |
|   LUT as Logic          | 1950 |     0 |          0 |   1303680 |  0.15 |
|   LUT as Memory         |    0 |     0 |          0 |    600960 |  0.00 |
| CLB Registers           | 1325 |     0 |          0 |   2607360 |  0.05 |
|   Register as Flip Flop | 1325 |     0 |          0 |   2607360 |  0.05 |
|   Register as Latch     |    0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                  |   68 |     0 |          0 |    162960 |  0.04 |
| F7 Muxes                |    0 |     0 |          0 |    651840 |  0.00 |
| F8 Muxes                |    0 |     0 |          0 |    325920 |  0.00 |
| F9 Muxes                |    0 |     0 |          0 |    162960 |  0.00 |
+-------------------------+------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 34    |          Yes |         Set |            - |
| 1291  |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| Block RAM Tile |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB36/FIFO* |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18       |    0 |     0 |          0 |      4032 |  0.00 |
| URAM           |    0 |     0 |          0 |       960 |  0.00 |
+----------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| DSPs           |    4 |     0 |          0 |      9024 |  0.04 |
|   DSP48E2 only |    4 |       |            |           |       |
+----------------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+------+---------------------+
| Ref Name | Used | Functional Category |
+----------+------+---------------------+
| FDRE     | 1291 |            Register |
| LUT1     |  684 |                 CLB |
| LUT6     |  470 |                 CLB |
| LUT3     |  405 |                 CLB |
| LUT4     |  349 |                 CLB |
| LUT2     |  324 |                 CLB |
| LUT5     |   91 |                 CLB |
| CARRY8   |   68 |                 CLB |
| FDSE     |   34 |            Register |
| BUFGCE   |    5 |               Clock |
| DSP48E2  |    4 |          Arithmetic |
+----------+------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## picorv32 / Part 2（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_picorv32_2th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-10-28 20:40:39 CST`。

SHA-256：`cce0bde3639e40252aa0b9123d456a7684d37571b270bb1dbf0637b5895125c8`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Oct 28 20:40:38 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_picorv32_2th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+------+-------+------------+-----------+-------+
|          Site Type         | Used | Fixed | Prohibited | Available | Util% |
+----------------------------+------+-------+------------+-----------+-------+
| CLB LUTs*                  | 2319 |     0 |          0 |   1303680 |  0.18 |
|   LUT as Logic             | 2279 |     0 |          0 |   1303680 |  0.17 |
|   LUT as Memory            |   40 |     0 |          0 |    600960 | <0.01 |
|     LUT as Distributed RAM |   40 |     0 |            |           |       |
|     LUT as Shift Register  |    0 |     0 |            |           |       |
| CLB Registers              | 1859 |     0 |          0 |   2607360 |  0.07 |
|   Register as Flip Flop    | 1859 |     0 |          0 |   2607360 |  0.07 |
|   Register as Latch        |    0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   55 |     0 |          0 |    162960 |  0.03 |
| F7 Muxes                   |    0 |     0 |          0 |    651840 |  0.00 |
| F8 Muxes                   |    0 |     0 |          0 |    325920 |  0.00 |
| F9 Muxes                   |    0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 72    |          Yes |         Set |            - |
| 1787  |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| Block RAM Tile |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB36/FIFO* |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18       |    0 |     0 |          0 |      4032 |  0.00 |
| URAM           |    0 |     0 |          0 |       960 |  0.00 |
+----------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+------+---------------------+
| Ref Name | Used | Functional Category |
+----------+------+---------------------+
| FDRE     | 1787 |            Register |
| LUT6     |  613 |                 CLB |
| LUT3     |  608 |                 CLB |
| LUT1     |  516 |                 CLB |
| LUT2     |  402 |                 CLB |
| LUT4     |  313 |                 CLB |
| LUT5     |  279 |                 CLB |
| FDSE     |   72 |            Register |
| RAMD32   |   68 |                 CLB |
| CARRY8   |   55 |                 CLB |
| RAMS32   |   12 |                 CLB |
| BUFGCE   |    5 |               Clock |
+----------+------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## picorv32 / Part 3（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_picorv32_3th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-10-28 20:40:32 CST`。

SHA-256：`5ae6b165143a1301ef5b865e9017ce10dccf652ea1b9993e65c006eb2e3287ee`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Oct 28 20:40:32 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_picorv32_3th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+-------------------------+------+-------+------------+-----------+-------+
|        Site Type        | Used | Fixed | Prohibited | Available | Util% |
+-------------------------+------+-------+------------+-----------+-------+
| CLB LUTs*               | 1942 |     0 |          0 |   1303680 |  0.15 |
|   LUT as Logic          | 1942 |     0 |          0 |   1303680 |  0.15 |
|   LUT as Memory         |    0 |     0 |          0 |    600960 |  0.00 |
| CLB Registers           | 1399 |     0 |          0 |   2607360 |  0.05 |
|   Register as Flip Flop | 1399 |     0 |          0 |   2607360 |  0.05 |
|   Register as Latch     |    0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                  |   73 |     0 |          0 |    162960 |  0.04 |
| F7 Muxes                |    0 |     0 |          0 |    651840 |  0.00 |
| F8 Muxes                |    0 |     0 |          0 |    325920 |  0.00 |
| F9 Muxes                |    0 |     0 |          0 |    162960 |  0.00 |
+-------------------------+------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 34    |          Yes |         Set |            - |
| 1365  |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| Block RAM Tile |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB36/FIFO* |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18       |    0 |     0 |          0 |      4032 |  0.00 |
| URAM           |    0 |     0 |          0 |       960 |  0.00 |
+----------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+------+---------------------+
| Ref Name | Used | Functional Category |
+----------+------+---------------------+
| FDRE     | 1365 |            Register |
| LUT1     |  684 |                 CLB |
| LUT3     |  582 |                 CLB |
| LUT6     |  375 |                 CLB |
| LUT4     |  240 |                 CLB |
| LUT2     |  227 |                 CLB |
| LUT5     |  140 |                 CLB |
| CARRY8   |   73 |                 CLB |
| FDSE     |   34 |            Register |
| BUFGCE   |    5 |               Clock |
+----------+------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## rocket / Part 0（2分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_rocket_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-10-28 20:42:51 CST`。

SHA-256：`8e463ea5a08772dee49cdc7abd5f21d73445608efef194f9c97137450d42109c`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Oct 28 20:42:51 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_rocket_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+-------+-------+------------+-----------+-------+
|          Site Type         |  Used | Fixed | Prohibited | Available | Util% |
+----------------------------+-------+-------+------------+-----------+-------+
| CLB LUTs*                  | 16149 |     0 |          0 |   1303680 |  1.24 |
|   LUT as Logic             | 15585 |     0 |          0 |   1303680 |  1.20 |
|   LUT as Memory            |   564 |     0 |          0 |    600960 |  0.09 |
|     LUT as Distributed RAM |   552 |     0 |            |           |       |
|     LUT as Shift Register  |    12 |     0 |            |           |       |
| CLB Registers              |  9537 |     0 |          0 |   2607360 |  0.37 |
|   Register as Flip Flop    |  9537 |     0 |          0 |   2607360 |  0.37 |
|   Register as Latch        |     0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   121 |     0 |          0 |    162960 |  0.07 |
| F7 Muxes                   |   190 |     0 |          0 |    651840 |  0.03 |
| F8 Muxes                   |    48 |     0 |          0 |    325920 |  0.01 |
| F9 Muxes                   |     0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+-------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 166   |          Yes |         Set |            - |
| 9371  |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |  4.5 |     0 |          0 |      2016 |  0.22 |
|   RAMB36/FIFO*    |    4 |     0 |          0 |      2016 |  0.20 |
|     RAMB36E2 only |    4 |       |            |           |       |
|   RAMB18          |    1 |     0 |          0 |      4032 |  0.02 |
|     RAMB18E2 only |    1 |       |            |           |       |
| URAM              |    2 |     0 |          0 |       960 |  0.21 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+------+---------------------+
| Ref Name | Used | Functional Category |
+----------+------+---------------------+
| FDRE     | 9371 |            Register |
| LUT6     | 6128 |                 CLB |
| LUT3     | 5533 |                 CLB |
| LUT4     | 3153 |                 CLB |
| LUT5     | 2734 |                 CLB |
| RAMD32   |  902 |                 CLB |
| LUT2     |  805 |                 CLB |
| LUT1     |  616 |                 CLB |
| MUXF7    |  190 |                 CLB |
| FDSE     |  166 |            Register |
| RAMS32   |  150 |                 CLB |
| CARRY8   |  121 |                 CLB |
| MUXF8    |   48 |                 CLB |
| SRL16E   |   12 |                 CLB |
| BUFGCE   |    5 |               Clock |
| RAMB36E2 |    4 |            BLOCKRAM |
| URAM288  |    2 |            BLOCKRAM |
| RAMB18E2 |    1 |            BLOCKRAM |
+----------+------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## rocket / Part 0（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_rocket_0th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-10-28 20:43:16 CST`。

SHA-256：`25aa9f71f36c57ff451bc099ba24a1a159e84b2979b930dd88cb21b7ba4ecb81`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Oct 28 20:43:16 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_rocket_0th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+-------+-------+------------+-----------+-------+
|          Site Type         |  Used | Fixed | Prohibited | Available | Util% |
+----------------------------+-------+-------+------------+-----------+-------+
| CLB LUTs*                  | 31496 |     0 |          0 |   1303680 |  2.42 |
|   LUT as Logic             | 30941 |     0 |          0 |   1303680 |  2.37 |
|   LUT as Memory            |   555 |     0 |          0 |    600960 |  0.09 |
|     LUT as Distributed RAM |   552 |     0 |            |           |       |
|     LUT as Shift Register  |     3 |     0 |            |           |       |
| CLB Registers              | 16053 |     0 |          0 |   2607360 |  0.62 |
|   Register as Flip Flop    | 16053 |     0 |          0 |   2607360 |  0.62 |
|   Register as Latch        |     0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   287 |     0 |          0 |    162960 |  0.18 |
| F7 Muxes                   |  1076 |     0 |          0 |    651840 |  0.17 |
| F8 Muxes                   |   131 |     0 |          0 |    325920 |  0.04 |
| F9 Muxes                   |     0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+-------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 159   |          Yes |         Set |            - |
| 15894 |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    | 24.5 |     0 |          0 |      2016 |  1.22 |
|   RAMB36/FIFO*    |    4 |     0 |          0 |      2016 |  0.20 |
|     RAMB36E2 only |    4 |       |            |           |       |
|   RAMB18          |   41 |     0 |          0 |      4032 |  1.02 |
|     RAMB18E2 only |   41 |       |            |           |       |
| URAM              |    2 |     0 |          0 |       960 |  0.21 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| DSPs           |   11 |     0 |          0 |      9024 |  0.12 |
|   DSP48E2 only |   11 |       |            |           |       |
+----------------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+-------+---------------------+
| Ref Name |  Used | Functional Category |
+----------+-------+---------------------+
| FDRE     | 15894 |            Register |
| LUT6     | 13081 |                 CLB |
| LUT3     |  9090 |                 CLB |
| LUT5     |  6687 |                 CLB |
| LUT4     |  5281 |                 CLB |
| LUT2     |  2099 |                 CLB |
| MUXF7    |  1076 |                 CLB |
| RAMD32   |   902 |                 CLB |
| LUT1     |   633 |                 CLB |
| CARRY8   |   287 |                 CLB |
| FDSE     |   159 |            Register |
| RAMS32   |   150 |                 CLB |
| MUXF8    |   131 |                 CLB |
| RAMB18E2 |    41 |            BLOCKRAM |
| DSP48E2  |    11 |          Arithmetic |
| BUFGCE   |     5 |               Clock |
| RAMB36E2 |     4 |            BLOCKRAM |
| SRLC32E  |     3 |                 CLB |
| URAM288  |     2 |            BLOCKRAM |
+----------+-------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## rocket / Part 0（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_rocket_0th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-10-28 20:42:36 CST`。

SHA-256：`72a9e5add88fa3cec4f8973cb2e62723bf685561f98860698fabdfdf9527dd63`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Oct 28 20:42:35 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_rocket_0th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+-------+-------+------------+-----------+-------+
|          Site Type         |  Used | Fixed | Prohibited | Available | Util% |
+----------------------------+-------+-------+------------+-----------+-------+
| CLB LUTs*                  | 15570 |     0 |          0 |   1303680 |  1.19 |
|   LUT as Logic             | 15006 |     0 |          0 |   1303680 |  1.15 |
|   LUT as Memory            |   564 |     0 |          0 |    600960 |  0.09 |
|     LUT as Distributed RAM |   552 |     0 |            |           |       |
|     LUT as Shift Register  |    12 |     0 |            |           |       |
| CLB Registers              |  9569 |     0 |          0 |   2607360 |  0.37 |
|   Register as Flip Flop    |  9569 |     0 |          0 |   2607360 |  0.37 |
|   Register as Latch        |     0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   119 |     0 |          0 |    162960 |  0.07 |
| F7 Muxes                   |    20 |     0 |          0 |    651840 | <0.01 |
| F8 Muxes                   |     1 |     0 |          0 |    325920 | <0.01 |
| F9 Muxes                   |     0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+-------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 164   |          Yes |         Set |            - |
| 9405  |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |  4.5 |     0 |          0 |      2016 |  0.22 |
|   RAMB36/FIFO*    |    4 |     0 |          0 |      2016 |  0.20 |
|     RAMB36E2 only |    4 |       |            |           |       |
|   RAMB18          |    1 |     0 |          0 |      4032 |  0.02 |
|     RAMB18E2 only |    1 |       |            |           |       |
| URAM              |    2 |     0 |          0 |       960 |  0.21 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+------+---------------------+
| Ref Name | Used | Functional Category |
+----------+------+---------------------+
| FDRE     | 9405 |            Register |
| LUT6     | 5072 |                 CLB |
| LUT3     | 5049 |                 CLB |
| LUT5     | 3330 |                 CLB |
| LUT4     | 3207 |                 CLB |
| RAMD32   |  902 |                 CLB |
| LUT2     |  896 |                 CLB |
| LUT1     |  588 |                 CLB |
| FDSE     |  164 |            Register |
| RAMS32   |  150 |                 CLB |
| CARRY8   |  119 |                 CLB |
| MUXF7    |   20 |                 CLB |
| SRL16E   |   12 |                 CLB |
| BUFGCE   |    5 |               Clock |
| RAMB36E2 |    4 |            BLOCKRAM |
| URAM288  |    2 |            BLOCKRAM |
| RAMB18E2 |    1 |            BLOCKRAM |
| MUXF8    |    1 |                 CLB |
+----------+------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## rocket / Part 1（2分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_rocket_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-10-28 20:44:07 CST`。

SHA-256：`1539620e755f486c5ba94848511b944c748687b4e5e260b9b17e50945b58704a`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Oct 28 20:44:07 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_rocket_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+-------+-------+------------+-----------+-------+
|          Site Type         |  Used | Fixed | Prohibited | Available | Util% |
+----------------------------+-------+-------+------------+-----------+-------+
| CLB LUTs*                  | 39041 |     0 |          0 |   1303680 |  2.99 |
|   LUT as Logic             | 38742 |     0 |          0 |   1303680 |  2.97 |
|   LUT as Memory            |   299 |     0 |          0 |    600960 |  0.05 |
|     LUT as Distributed RAM |   296 |     0 |            |           |       |
|     LUT as Shift Register  |     3 |     0 |            |           |       |
| CLB Registers              | 19097 |     0 |          0 |   2607360 |  0.73 |
|   Register as Flip Flop    | 19097 |     0 |          0 |   2607360 |  0.73 |
|   Register as Latch        |     0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   493 |     0 |          0 |    162960 |  0.30 |
| F7 Muxes                   |  1159 |     0 |          0 |    651840 |  0.18 |
| F8 Muxes                   |   152 |     0 |          0 |    325920 |  0.05 |
| F9 Muxes                   |     0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+-------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 436   |          Yes |         Set |            - |
| 18661 |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |   20 |     0 |          0 |      2016 |  0.99 |
|   RAMB36/FIFO*    |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18          |   40 |     0 |          0 |      4032 |  0.99 |
|     RAMB18E2 only |   40 |       |            |           |       |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| DSPs           |   15 |     0 |          0 |      9024 |  0.17 |
|   DSP48E2 only |   15 |       |            |           |       |
+----------------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+-------+---------------------+
| Ref Name |  Used | Functional Category |
+----------+-------+---------------------+
| FDRE     | 18661 |            Register |
| LUT6     | 16538 |                 CLB |
| LUT3     | 13060 |                 CLB |
| LUT5     |  8209 |                 CLB |
| LUT4     |  6410 |                 CLB |
| LUT2     |  3055 |                 CLB |
| MUXF7    |  1159 |                 CLB |
| LUT1     |   559 |                 CLB |
| CARRY8   |   493 |                 CLB |
| FDSE     |   436 |            Register |
| RAMD64E  |   216 |                 CLB |
| MUXF8    |   152 |                 CLB |
| RAMD32   |   140 |                 CLB |
| RAMB18E2 |    40 |            BLOCKRAM |
| RAMS32   |    20 |                 CLB |
| DSP48E2  |    15 |          Arithmetic |
| BUFGCE   |     5 |               Clock |
| SRLC32E  |     3 |                 CLB |
+----------+-------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## rocket / Part 2（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_rocket_2th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-10-28 20:41:51 CST`。

SHA-256：`1598d54f1fff0c729861270d5b5c5c4510b005cf5bdd4cb7f2d5a5d32ff2995c`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Oct 28 20:41:51 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_rocket_2th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+-------+-------+------------+-----------+-------+
|          Site Type         |  Used | Fixed | Prohibited | Available | Util% |
+----------------------------+-------+-------+------------+-----------+-------+
| CLB LUTs*                  | 21331 |     0 |          0 |   1303680 |  1.64 |
|   LUT as Logic             | 21035 |     0 |          0 |   1303680 |  1.61 |
|   LUT as Memory            |   296 |     0 |          0 |    600960 |  0.05 |
|     LUT as Distributed RAM |   296 |     0 |            |           |       |
|     LUT as Shift Register  |     0 |     0 |            |           |       |
| CLB Registers              | 13091 |     0 |          0 |   2607360 |  0.50 |
|   Register as Flip Flop    | 13091 |     0 |          0 |   2607360 |  0.50 |
|   Register as Latch        |     0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   320 |     0 |          0 |    162960 |  0.20 |
| F7 Muxes                   |   113 |     0 |          0 |    651840 |  0.02 |
| F8 Muxes                   |    14 |     0 |          0 |    325920 | <0.01 |
| F9 Muxes                   |     0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+-------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 275   |          Yes |         Set |            - |
| 12816 |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| Block RAM Tile |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB36/FIFO* |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18       |    0 |     0 |          0 |      4032 |  0.00 |
| URAM           |    0 |     0 |          0 |       960 |  0.00 |
+----------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| DSPs           |    4 |     0 |          0 |      9024 |  0.04 |
|   DSP48E2 only |    4 |       |            |           |       |
+----------------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+-------+---------------------+
| Ref Name |  Used | Functional Category |
+----------+-------+---------------------+
| FDRE     | 12816 |            Register |
| LUT3     | 10099 |                 CLB |
| LUT6     |  7086 |                 CLB |
| LUT5     |  4316 |                 CLB |
| LUT4     |  3477 |                 CLB |
| LUT2     |  2736 |                 CLB |
| CARRY8   |   320 |                 CLB |
| FDSE     |   275 |            Register |
| RAMD64E  |   216 |                 CLB |
| LUT1     |   216 |                 CLB |
| RAMD32   |   140 |                 CLB |
| MUXF7    |   113 |                 CLB |
| RAMS32   |    20 |                 CLB |
| MUXF8    |    14 |                 CLB |
| BUFGCE   |     5 |               Clock |
| DSP48E2  |     4 |          Arithmetic |
+----------+-------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## xs-minimal / Part 0（2分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_xs-minimal_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-04 00:01:24 CST`。

SHA-256：`e10f41ba3c84de5312236e2a5e40b5510aab250716dd3de9173e044bcf2a0cbc`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Wed Nov  4 00:01:23 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_xs-minimal_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 444387 |     0 |          0 |   1303680 | 34.09 |
|   LUT as Logic             | 437914 |     0 |          0 |   1303680 | 33.59 |
|   LUT as Memory            |   6473 |     0 |          0 |    600960 |  1.08 |
|     LUT as Distributed RAM |   6432 |     0 |            |           |       |
|     LUT as Shift Register  |     41 |     0 |            |           |       |
| CLB Registers              | 262410 |     0 |          0 |   2607360 | 10.06 |
|   Register as Flip Flop    | 262410 |     0 |          0 |   2607360 | 10.06 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   5340 |     0 |          0 |    162960 |  3.28 |
| F7 Muxes                   |   5177 |     0 |          0 |    651840 |  0.79 |
| F8 Muxes                   |    389 |     0 |          0 |    325920 |  0.12 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 2571   |          Yes |         Set |            - |
| 259839 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+-------+-------+------------+-----------+-------+
|     Site Type     |  Used | Fixed | Prohibited | Available | Util% |
+-------------------+-------+-------+------------+-----------+-------+
| Block RAM Tile    | 282.5 |     0 |          0 |      2016 | 14.01 |
|   RAMB36/FIFO*    |   259 |     0 |          0 |      2016 | 12.85 |
|     RAMB36E2 only |   259 |       |            |           |       |
|   RAMB18          |    47 |     0 |          0 |      4032 |  1.17 |
|     RAMB18E2 only |    47 |       |            |           |       |
| URAM              |    13 |     0 |          0 |       960 |  1.35 |
+-------------------+-------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| FDRE     | 259839 |            Register |
| LUT6     | 146493 |                 CLB |
| LUT3     | 141732 |                 CLB |
| LUT5     | 135285 |                 CLB |
| LUT4     |  87456 |                 CLB |
| LUT2     |  22149 |                 CLB |
| CARRY8   |   5340 |                 CLB |
| MUXF7    |   5177 |                 CLB |
| RAMD64E  |   4736 |                 CLB |
| RAMD32   |   2882 |                 CLB |
| FDSE     |   2571 |            Register |
| LUT1     |    953 |                 CLB |
| RAMS32   |    418 |                 CLB |
| MUXF8    |    389 |                 CLB |
| RAMB36E2 |    259 |            BLOCKRAM |
| RAMB18E2 |     47 |            BLOCKRAM |
| SRLC32E  |     40 |                 CLB |
| URAM288  |     13 |            BLOCKRAM |
| BUFGCE   |      5 |               Clock |
| SRL16E   |      1 |                 CLB |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## xs-minimal / Part 0（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_xs-minimal_0th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 23:26:07 CST`。

SHA-256：`1a6253718dde83a4a7fa277a57932de1ca291c25ed7182a18448451227483e34`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 23:26:06 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_xs-minimal_0th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 260652 |     0 |          0 |   1303680 | 19.99 |
|   LUT as Logic             | 251440 |     0 |          0 |   1303680 | 19.29 |
|   LUT as Memory            |   9212 |     0 |          0 |    600960 |  1.53 |
|     LUT as Distributed RAM |   9188 |     0 |            |           |       |
|     LUT as Shift Register  |     24 |     0 |            |           |       |
| CLB Registers              | 145500 |     0 |          0 |   2607360 |  5.58 |
|   Register as Flip Flop    | 145500 |     0 |          0 |   2607360 |  5.58 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |    540 |     0 |          0 |    162960 |  0.33 |
| F7 Muxes                   |   5226 |     0 |          0 |    651840 |  0.80 |
| F8 Muxes                   |   1949 |     0 |          0 |    325920 |  0.60 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 1539   |          Yes |         Set |            - |
| 143961 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+-------+-------+------------+-----------+-------+
|     Site Type     |  Used | Fixed | Prohibited | Available | Util% |
+-------------------+-------+-------+------------+-----------+-------+
| Block RAM Tile    | 213.5 |     0 |          0 |      2016 | 10.59 |
|   RAMB36/FIFO*    |   152 |     0 |          0 |      2016 |  7.54 |
|     RAMB36E2 only |   152 |       |            |           |       |
|   RAMB18          |   123 |     0 |          0 |      4032 |  3.05 |
|     RAMB18E2 only |   123 |       |            |           |       |
| URAM              |    13 |     0 |          0 |       960 |  1.35 |
+-------------------+-------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| FDRE     | 143961 |            Register |
| LUT5     |  96089 |                 CLB |
| LUT6     |  87388 |                 CLB |
| LUT3     |  66895 |                 CLB |
| LUT4     |  34371 |                 CLB |
| LUT2     |   8149 |                 CLB |
| RAMD64E  |   6608 |                 CLB |
| MUXF7    |   5226 |                 CLB |
| RAMD32   |   4330 |                 CLB |
| MUXF8    |   1949 |                 CLB |
| FDSE     |   1539 |            Register |
| LUT1     |   1089 |                 CLB |
| RAMS32   |    714 |                 CLB |
| CARRY8   |    540 |                 CLB |
| RAMB36E2 |    152 |            BLOCKRAM |
| RAMB18E2 |    123 |            BLOCKRAM |
| SRLC32E  |     24 |                 CLB |
| URAM288  |     13 |            BLOCKRAM |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## xs-minimal / Part 0（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_xs-minimal_0th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 22:55:56 CST`。

SHA-256：`bcc5c98e3bcc5d54b6887e48cfd4b6f056b1a56ffe67d47792dba29aad96245f`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 22:55:56 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_xs-minimal_0th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 206835 |     0 |          0 |   1303680 | 15.87 |
|   LUT as Logic             | 205431 |     0 |          0 |   1303680 | 15.76 |
|   LUT as Memory            |   1404 |     0 |          0 |    600960 |  0.23 |
|     LUT as Distributed RAM |   1380 |     0 |            |           |       |
|     LUT as Shift Register  |     24 |     0 |            |           |       |
| CLB Registers              | 116875 |     0 |          0 |   2607360 |  4.48 |
|   Register as Flip Flop    | 116875 |     0 |          0 |   2607360 |  4.48 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |    649 |     0 |          0 |    162960 |  0.40 |
| F7 Muxes                   |    328 |     0 |          0 |    651840 |  0.05 |
| F8 Muxes                   |     41 |     0 |          0 |    325920 |  0.01 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 941    |          Yes |         Set |            - |
| 115934 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+-------+-------+------------+-----------+-------+
|     Site Type     |  Used | Fixed | Prohibited | Available | Util% |
+-------------------+-------+-------+------------+-----------+-------+
| Block RAM Tile    | 154.5 |     0 |          0 |      2016 |  7.66 |
|   RAMB36/FIFO*    |   136 |     0 |          0 |      2016 |  6.75 |
|     RAMB36E2 only |   136 |       |            |           |       |
|   RAMB18          |    37 |     0 |          0 |      4032 |  0.92 |
|     RAMB18E2 only |    37 |       |            |           |       |
| URAM              |    13 |     0 |          0 |       960 |  1.35 |
+-------------------+-------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| FDRE     | 115934 |            Register |
| LUT5     |  84877 |                 CLB |
| LUT3     |  59786 |                 CLB |
| LUT6     |  59322 |                 CLB |
| LUT4     |  31128 |                 CLB |
| LUT2     |   6176 |                 CLB |
| RAMD32   |   2332 |                 CLB |
| FDSE     |    941 |            Register |
| LUT1     |    726 |                 CLB |
| CARRY8   |    649 |                 CLB |
| RAMS32   |    340 |                 CLB |
| MUXF7    |    328 |                 CLB |
| RAMB36E2 |    136 |            BLOCKRAM |
| MUXF8    |     41 |                 CLB |
| RAMB18E2 |     37 |            BLOCKRAM |
| SRLC32E  |     24 |                 CLB |
| URAM288  |     13 |            BLOCKRAM |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## xs-minimal / Part 1（2分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_xs-minimal_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 23:45:54 CST`。

SHA-256：`673c9a2e9b46ae05c691863e8cb14454e7a67d1ae5830006dc121766730fefa8`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 23:45:54 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_xs-minimal_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 415287 |     0 |          0 |   1303680 | 31.85 |
|   LUT as Logic             | 407183 |     0 |          0 |   1303680 | 31.23 |
|   LUT as Memory            |   8104 |     0 |          0 |    600960 |  1.35 |
|     LUT as Distributed RAM |   8104 |     0 |            |           |       |
|     LUT as Shift Register  |      0 |     0 |            |           |       |
| CLB Registers              | 129855 |     0 |          0 |   2607360 |  4.98 |
|   Register as Flip Flop    | 129855 |     0 |          0 |   2607360 |  4.98 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   1093 |     0 |          0 |    162960 |  0.67 |
| F7 Muxes                   |   7437 |     0 |          0 |    651840 |  1.14 |
| F8 Muxes                   |   2312 |     0 |          0 |    325920 |  0.71 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 1515   |          Yes |         Set |            - |
| 128340 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |   59 |     0 |          0 |      2016 |  2.93 |
|   RAMB36/FIFO*    |   16 |     0 |          0 |      2016 |  0.79 |
|     RAMB36E2 only |   16 |       |            |           |       |
|   RAMB18          |   86 |     0 |          0 |      4032 |  2.13 |
|     RAMB18E2 only |   86 |       |            |           |       |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| LUT6     | 184282 |                 CLB |
| FDRE     | 128340 |            Register |
| LUT3     | 105116 |                 CLB |
| LUT5     | 103328 |                 CLB |
| LUT4     |  65764 |                 CLB |
| LUT2     |  14963 |                 CLB |
| MUXF7    |   7437 |                 CLB |
| RAMD64E  |   6608 |                 CLB |
| RAMD32   |   2516 |                 CLB |
| MUXF8    |   2312 |                 CLB |
| FDSE     |   1515 |            Register |
| LUT1     |   1456 |                 CLB |
| CARRY8   |   1093 |                 CLB |
| RAMS32   |    448 |                 CLB |
| RAMB18E2 |     86 |            BLOCKRAM |
| RAMB36E2 |     16 |            BLOCKRAM |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## xs-minimal / Part 1（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_xs-minimal_1th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 22:57:19 CST`。

SHA-256：`c4f3d9b7e3341842ee839f5ec09ef2e421a5c74c23718f06a46191383787bd22`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 22:57:19 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_xs-minimal_1th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 272878 |     0 |          0 |   1303680 | 20.93 |
|   LUT as Logic             | 272286 |     0 |          0 |   1303680 | 20.89 |
|   LUT as Memory            |    592 |     0 |          0 |    600960 |  0.10 |
|     LUT as Distributed RAM |    592 |     0 |            |           |       |
|     LUT as Shift Register  |      0 |     0 |            |           |       |
| CLB Registers              |  71051 |     0 |          0 |   2607360 |  2.73 |
|   Register as Flip Flop    |  71051 |     0 |          0 |   2607360 |  2.73 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |    727 |     0 |          0 |    162960 |  0.45 |
| F7 Muxes                   |   2705 |     0 |          0 |    651840 |  0.41 |
| F8 Muxes                   |    309 |     0 |          0 |    325920 |  0.09 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 796   |          Yes |         Set |            - |
| 70255 |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| Block RAM Tile |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB36/FIFO* |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18       |    0 |     0 |          0 |      4032 |  0.00 |
| URAM           |    0 |     0 |          0 |       960 |  0.00 |
+----------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| LUT6     | 119113 |                 CLB |
| FDRE     |  70255 |            Register |
| LUT5     |  68497 |                 CLB |
| LUT3     |  63958 |                 CLB |
| LUT4     |  51056 |                 CLB |
| LUT2     |  10421 |                 CLB |
| MUXF7    |   2705 |                 CLB |
| RAMD32   |   1036 |                 CLB |
| FDSE     |    796 |            Register |
| CARRY8   |    727 |                 CLB |
| LUT1     |    726 |                 CLB |
| MUXF8    |    309 |                 CLB |
| RAMS32   |    148 |                 CLB |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## xs-minimal / Part 1（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_xs-minimal_1th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 23:17:53 CST`。

SHA-256：`3ac44343f67d9a702dbb7930b9cbaf1af127f0681259792370630cd966603a14`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 23:17:53 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_xs-minimal_1th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 207154 |     0 |          0 |   1303680 | 15.89 |
|   LUT as Logic             | 201493 |     0 |          0 |   1303680 | 15.46 |
|   LUT as Memory            |   5661 |     0 |          0 |    600960 |  0.94 |
|     LUT as Distributed RAM |   5644 |     0 |            |           |       |
|     LUT as Shift Register  |     17 |     0 |            |           |       |
| CLB Registers              | 121094 |     0 |          0 |   2607360 |  4.64 |
|   Register as Flip Flop    | 121094 |     0 |          0 |   2607360 |  4.64 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   2643 |     0 |          0 |    162960 |  1.62 |
| F7 Muxes                   |   2901 |     0 |          0 |    651840 |  0.45 |
| F8 Muxes                   |    297 |     0 |          0 |    325920 |  0.09 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 1596   |          Yes |         Set |            - |
| 119498 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |   65 |     0 |          0 |      2016 |  3.22 |
|   RAMB36/FIFO*    |   65 |     0 |          0 |      2016 |  3.22 |
|     RAMB36E2 only |   65 |       |            |           |       |
|   RAMB18          |    0 |     0 |          0 |      4032 |  0.00 |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| FDRE     | 119498 |            Register |
| LUT3     |  74483 |                 CLB |
| LUT6     |  67844 |                 CLB |
| LUT5     |  51734 |                 CLB |
| LUT4     |  44370 |                 CLB |
| LUT2     |  14101 |                 CLB |
| RAMD64E  |   4736 |                 CLB |
| MUXF7    |   2901 |                 CLB |
| CARRY8   |   2643 |                 CLB |
| FDSE     |   1596 |            Register |
| RAMD32   |   1586 |                 CLB |
| LUT1     |    463 |                 CLB |
| MUXF8    |    297 |                 CLB |
| RAMS32   |    226 |                 CLB |
| RAMB36E2 |     65 |            BLOCKRAM |
| SRLC32E  |     16 |                 CLB |
| BUFGCE   |      5 |               Clock |
| SRL16E   |      1 |                 CLB |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## xs-minimal / Part 2（3分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_xs-minimal_2th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 23:37:06 CST`。

SHA-256：`b8e7395946915de4f5ffcdccdb782cc43634e41fe742ab79adf24d8d921de60a`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 23:37:05 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_xs-minimal_2th_part3_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 324377 |     0 |          0 |   1303680 | 24.88 |
|   LUT as Logic             | 318452 |     0 |          0 |   1303680 | 24.43 |
|   LUT as Memory            |   5925 |     0 |          0 |    600960 |  0.99 |
|     LUT as Distributed RAM |   5908 |     0 |            |           |       |
|     LUT as Shift Register  |     17 |     0 |            |           |       |
| CLB Registers              | 179045 |     0 |          0 |   2607360 |  6.87 |
|   Register as Flip Flop    | 179045 |     0 |          0 |   2607360 |  6.87 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   5206 |     0 |          0 |    162960 |  3.19 |
| F7 Muxes                   |   5835 |     0 |          0 |    651840 |  0.90 |
| F8 Muxes                   |    315 |     0 |          0 |    325920 |  0.10 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 1758   |          Yes |         Set |            - |
| 177287 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |  128 |     0 |          0 |      2016 |  6.35 |
|   RAMB36/FIFO*    |  123 |     0 |          0 |      2016 |  6.10 |
|     RAMB36E2 only |  123 |       |            |           |       |
|   RAMB18          |   10 |     0 |          0 |      4032 |  0.25 |
|     RAMB18E2 only |   10 |       |            |           |       |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| FDRE     | 177287 |            Register |
| LUT3     | 121763 |                 CLB |
| LUT6     | 106763 |                 CLB |
| LUT5     |  79471 |                 CLB |
| LUT4     |  72820 |                 CLB |
| LUT2     |  20762 |                 CLB |
| MUXF7    |   5835 |                 CLB |
| CARRY8   |   5206 |                 CLB |
| RAMD64E  |   4736 |                 CLB |
| RAMD32   |   2048 |                 CLB |
| FDSE     |   1758 |            Register |
| LUT1     |    754 |                 CLB |
| MUXF8    |    315 |                 CLB |
| RAMS32   |    292 |                 CLB |
| RAMB36E2 |    123 |            BLOCKRAM |
| SRLC32E  |     16 |                 CLB |
| RAMB18E2 |     10 |            BLOCKRAM |
| BUFGCE   |      5 |               Clock |
| SRL16E   |      1 |                 CLB |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## xs-minimal / Part 2（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_xs-minimal_2th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 23:08:45 CST`。

SHA-256：`03b1759f05936e01cb34905a04e2318404ed65fc9f32803c9f07bbece6acff2d`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 23:08:45 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_xs-minimal_2th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 229049 |     0 |          0 |   1303680 | 17.57 |
|   LUT as Logic             | 221289 |     0 |          0 |   1303680 | 16.97 |
|   LUT as Memory            |   7760 |     0 |          0 |    600960 |  1.29 |
|     LUT as Distributed RAM |   7760 |     0 |            |           |       |
|     LUT as Shift Register  |      0 |     0 |            |           |       |
| CLB Registers              | 108864 |     0 |          0 |   2607360 |  4.18 |
|   Register as Flip Flop    | 108864 |     0 |          0 |   2607360 |  4.18 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   2945 |     0 |          0 |    162960 |  1.81 |
| F7 Muxes                   |   8077 |     0 |          0 |    651840 |  1.24 |
| F8 Muxes                   |   2227 |     0 |          0 |    325920 |  0.68 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+--------+--------------+-------------+--------------+
|  Total | Clock Enable | Synchronous | Asynchronous |
+--------+--------------+-------------+--------------+
| 0      |            _ |           - |            - |
| 0      |            _ |           - |          Set |
| 0      |            _ |           - |        Reset |
| 0      |            _ |         Set |            - |
| 0      |            _ |       Reset |            - |
| 0      |          Yes |           - |            - |
| 0      |          Yes |           - |          Set |
| 0      |          Yes |           - |        Reset |
| 1073   |          Yes |         Set |            - |
| 107791 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |  122 |     0 |          0 |      2016 |  6.05 |
|   RAMB36/FIFO*    |   74 |     0 |          0 |      2016 |  3.67 |
|     RAMB36E2 only |   74 |       |            |           |       |
|   RAMB18          |   96 |     0 |          0 |      4032 |  2.38 |
|     RAMB18E2 only |   96 |       |            |           |       |
| URAM              |    0 |     0 |          0 |       960 |  0.00 |
+-------------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+--------+---------------------+
| Ref Name |  Used  | Functional Category |
+----------+--------+---------------------+
| FDRE     | 107791 |            Register |
| LUT6     |  78729 |                 CLB |
| LUT3     |  78551 |                 CLB |
| LUT5     |  54514 |                 CLB |
| LUT4     |  50476 |                 CLB |
| LUT2     |  13883 |                 CLB |
| MUXF7    |   8077 |                 CLB |
| RAMD64E  |   6608 |                 CLB |
| CARRY8   |   2945 |                 CLB |
| MUXF8    |   2227 |                 CLB |
| RAMD32   |   1914 |                 CLB |
| LUT1     |   1237 |                 CLB |
| FDSE     |   1073 |            Register |
| RAMS32   |    362 |                 CLB |
| RAMB18E2 |     96 |            BLOCKRAM |
| RAMB36E2 |     74 |            BLOCKRAM |
| BUFGCE   |      5 |               Clock |
+----------+--------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

## xs-minimal / Part 3（4分区）

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_xs-minimal_3th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

远端mtime：`2026-11-03 22:52:19 CST`。

SHA-256：`ccfd8e909177411f424a3ec86adda445007172d279e74c80a9378e43bc9a00ec`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Nov  3 22:52:19 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_xs-minimal_3th_part4_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. CLB Logic
1.1 Summary of Registers by Type
2. BLOCKRAM
3. ARITHMETIC
4. I/O
5. CLOCK
6. ADVANCED
7. CONFIGURATION
8. Primitives
9. Black Boxes
10. Instantiated Netlists
11. SLR Connectivity
12. SLR Connectivity Matrix
13. SLR IO Utilization

1. CLB Logic
------------

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 210346 |     0 |          0 |   1303680 | 16.13 |
|   LUT as Logic             | 210050 |     0 |          0 |   1303680 | 16.11 |
|   LUT as Memory            |    296 |     0 |          0 |    600960 |  0.05 |
|     LUT as Distributed RAM |    296 |     0 |            |           |       |
|     LUT as Shift Register  |      0 |     0 |            |           |       |
| CLB Registers              |  57844 |     0 |          0 |   2607360 |  2.22 |
|   Register as Flip Flop    |  57844 |     0 |          0 |   2607360 |  2.22 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |    290 |     0 |          0 |    162960 |  0.18 |
| F7 Muxes                   |   3174 |     0 |          0 |    651840 |  0.49 |
| F8 Muxes                   |    281 |     0 |          0 |    325920 |  0.09 |
| F9 Muxes                   |      0 |     0 |          0 |    162960 |  0.00 |
+----------------------------+--------+-------+------------+-----------+-------+
* Warning! The Final LUT count, after physical optimizations and full implementation, is typically lower. Run opt_design after synthesis, if not already completed, for a more realistic count.
Warning! LUT value is adjusted to account for LUT combining.
Warning! For any ECO changes, please run place_design if there are unplaced instances


1.1 Summary of Registers by Type
--------------------------------

+-------+--------------+-------------+--------------+
| Total | Clock Enable | Synchronous | Asynchronous |
+-------+--------------+-------------+--------------+
| 0     |            _ |           - |            - |
| 0     |            _ |           - |          Set |
| 0     |            _ |           - |        Reset |
| 0     |            _ |         Set |            - |
| 0     |            _ |       Reset |            - |
| 0     |          Yes |           - |            - |
| 0     |          Yes |           - |          Set |
| 0     |          Yes |           - |        Reset |
| 698   |          Yes |         Set |            - |
| 57146 |          Yes |       Reset |            - |
+-------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+----------------+------+-------+------------+-----------+-------+
|    Site Type   | Used | Fixed | Prohibited | Available | Util% |
+----------------+------+-------+------------+-----------+-------+
| Block RAM Tile |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB36/FIFO* |    0 |     0 |          0 |      2016 |  0.00 |
|   RAMB18       |    0 |     0 |          0 |      4032 |  0.00 |
| URAM           |    0 |     0 |          0 |       960 |  0.00 |
+----------------+------+-------+------------+-----------+-------+
* Note: Each Block RAM Tile only has one FIFO logic available and therefore can accommodate only one FIFO36E2 or one FIFO18E2. However, if a FIFO18E2 occupies a Block RAM Tile, that tile can still accommodate a RAMB18E2


3. ARITHMETIC
-------------

+-----------+------+-------+------------+-----------+-------+
| Site Type | Used | Fixed | Prohibited | Available | Util% |
+-----------+------+-------+------------+-----------+-------+
| DSPs      |    0 |     0 |          0 |      9024 |  0.00 |
+-----------+------+-------+------------+-----------+-------+


4. I/O
------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| Bonded IOB |    0 |     0 |          0 |       624 |  0.00 |
+------------+------+-------+------------+-----------+-------+


5. CLOCK
--------

+------------+------+-------+------------+-----------+-------+
|  Site Type | Used | Fixed | Prohibited | Available | Util% |
+------------+------+-------+------------+-----------+-------+
| BUFGCE     |    5 |     0 |          0 |       288 |  1.74 |
| BUFGCE_DIV |    0 |     0 |          0 |        48 |  0.00 |
| BUFG_GT    |    0 |     0 |          0 |       576 |  0.00 |
| BUFGCTRL*  |    0 |     0 |          0 |        96 |  0.00 |
| PLL        |    0 |     0 |          0 |        24 |  0.00 |
| MMCM       |    0 |     0 |          0 |        12 |  0.00 |
+------------+------+-------+------------+-----------+-------+
* Note: Each used BUFGCTRL counts as two GLOBAL CLOCK BUFFERs. This table does not include global clocking resources, only buffer cell usage. See the Clock Utilization Report (report_clock_utilization) for detailed accounting of global clocking resource availability.


6. ADVANCED
-----------

+----------------------+------+-------+------------+-----------+-------+
|       Site Type      | Used | Fixed | Prohibited | Available | Util% |
+----------------------+------+-------+------------+-----------+-------+
| CMACE4               |    0 |     0 |          0 |         8 |  0.00 |
| GTYE4_CHANNEL        |    0 |     0 |          0 |        96 |  0.00 |
| GTYE4_COMMON         |    0 |     0 |          0 |        24 |  0.00 |
| HBM_REF_CLK          |    0 |     0 |          0 |         2 |  0.00 |
| HBM_SNGLBLI_INTF_APB |    0 |     0 |          0 |        32 |  0.00 |
| HBM_SNGLBLI_INTF_AXI |    0 |     0 |          0 |        32 |  0.00 |
| ILKNE4               |    0 |     0 |          0 |         4 |  0.00 |
| OBUFDS_GTE4          |    0 |     0 |          0 |        48 |  0.00 |
| OBUFDS_GTE4_ADV      |    0 |     0 |          0 |        48 |  0.00 |
| PCIE40E4             |    0 |     0 |          0 |         2 |  0.00 |
| PCIE4CE4             |    0 |     0 |          0 |         4 |  0.00 |
| SYSMONE4             |    0 |     0 |          0 |         3 |  0.00 |
+----------------------+------+-------+------------+-----------+-------+


7. CONFIGURATION
----------------

+-------------+------+-------+------------+-----------+-------+
|  Site Type  | Used | Fixed | Prohibited | Available | Util% |
+-------------+------+-------+------------+-----------+-------+
| BSCANE2     |    0 |     0 |          0 |        12 |  0.00 |
| DNA_PORTE2  |    0 |     0 |          0 |         3 |  0.00 |
| EFUSE_USR   |    0 |     0 |          0 |         3 |  0.00 |
| FRAME_ECCE4 |    0 |     0 |          0 |         3 |  0.00 |
| ICAPE3      |    0 |     0 |          0 |         6 |  0.00 |
| MASTER_JTAG |    0 |     0 |          0 |         3 |  0.00 |
| STARTUPE3   |    0 |     0 |          0 |         3 |  0.00 |
+-------------+------+-------+------------+-----------+-------+


8. Primitives
-------------

+----------+-------+---------------------+
| Ref Name |  Used | Functional Category |
+----------+-------+---------------------+
| LUT6     | 90762 |                 CLB |
| FDRE     | 57146 |            Register |
| LUT5     | 56058 |                 CLB |
| LUT3     | 50140 |                 CLB |
| LUT4     | 36802 |                 CLB |
| LUT2     |  7846 |                 CLB |
| MUXF7    |  3174 |                 CLB |
| FDSE     |   698 |            Register |
| RAMD32   |   518 |                 CLB |
| LUT1     |   436 |                 CLB |
| CARRY8   |   290 |                 CLB |
| MUXF8    |   281 |                 CLB |
| RAMS32   |    74 |                 CLB |
| BUFGCE   |     5 |               Clock |
+----------+-------+---------------------+


9. Black Boxes
--------------

+----------+------+
| Ref Name | Used |
+----------+------+


10. Instantiated Netlists
-------------------------

+----------+------+
| Ref Name | Used |
+----------+------+


11. SLR Connectivity
--------------------

+----------------------------------+------+-------+-----------+-------+
|                                  | Used | Fixed | Available | Util% |
+----------------------------------+------+-------+-----------+-------+
| SLR2 <-> SLR1                    |    0 |       |     23040 |  0.00 |
|   SLR1 -> SLR2                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR2 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
| SLR1 <-> SLR0                    |    0 |       |     23040 |  0.00 |
|   SLR0 -> SLR1                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
|   SLR1 -> SLR0                   |    0 |       |           |  0.00 |
|     Using TX_REG only            |    0 |     0 |           |       |
|     Using RX_REG only            |    0 |     0 |           |       |
|     Using Both TX_REG and RX_REG |    0 |     0 |           |       |
+----------------------------------+------+-------+-----------+-------+
| Total SLLs Used                  |    0 |       |           |       |
+----------------------------------+------+-------+-----------+-------+


12. SLR Connectivity Matrix
---------------------------

+-----------+------+------+------+
| FROM \ TO | SLR2 | SLR1 | SLR0 |
+-----------+------+------+------+
| SLR2      |    0 |    0 |    0 |
| SLR1      |    0 |    0 |    0 |
| SLR0      |    0 |    0 |    0 |
+-----------+------+------+------+


13. SLR IO Utilization
----------------------

+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR Index | Used IOBs | (%)IOBs | Used IPADs | (%)IPADs | Used OPADs | (%)OPADs | GTs |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| SLR2      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR1      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
| SLR0      |         0 |    0.00 |          0 |     0.00 |          0 |     0.00 |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+
| Total     |         0 |         |          0 |          |          0 |          |   0 |
+-----------+-----------+---------+------------+----------+------------+----------+-----+


```

