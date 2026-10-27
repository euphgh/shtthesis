# EMU_SYSTEM双分区综合资源原始报告：2026-10-27

来源：`serve41:/home/huguanghui/remu`，采集时间：`2026-10-27T13:15:57Z`（UTC）。采集时checkout：`vivado2024.2` / `e924d0eabbc6a3a38b01339b00da55b25faf7a00`。共五个DUT、各两个Part、10份`synth_emu_system_util.rpt`；均为Synthesized状态，不包含3/4分区。返回[整理结果](../synthesis-utilization.md)。

各代码块保存对应报告的**完整原文**，包括头部、全部资源表和警告。SHA-256对应代码块内原始文件内容（含末尾换行），不包含Markdown围栏。未重跑Vivado；采集checkout不能替代每份报告实际构建版本的核对。

## 文件校验值

| DUT目录名 | Part ID | SHA-256 |
| --- | --- | --- |
| picorv32 | 0 | `7e9ee8854e7e2fc4ef93311a02e3119eb5a420de98b22b13f2c4e2701f83545d` |
| picorv32 | 1 | `df5a7283bd758b8c863474afb52b61b78e28ef67f990cf9627bce1917ac318e5` |
| rocket | 0 | `4350d69312344ce3d9a1c89c092d50bfe6b1c66bdac02394c14eee43f78f99b2` |
| rocket | 1 | `6cdf847419a8e8d7744a30a1d032405872b1005844385ad475ea5e402db1be86` |
| xs-minimal | 0 | `9e8758ac8a726c7cb439ac877f2c7d8fcb70e5016095678c337479f6458178ed` |
| xs-minimal | 1 | `39f8fdb5861ade567fd58925aa0094792e0b7e51b77b4808ae6b1f87c9383596` |
| nanhu-g | 0 | `22ede151d62402cc7a32cf00714dc002167059f17ec25e8585d8b6021536ff26` |
| nanhu-g | 1 | `aab6fc08ae4f05761fcfda15f0d7eb05b0f45cf99fb16a005cdba9d5d02d07b6` |
| kmh | 0 | `945d442f74215c95da38ef62323981c509058984045de24ab56f489cedd77a57` |
| kmh | 1 | `ae959b6054f9564ba16a56e22e9c8d8efceaa0543db93be1b4f7be22507d697d` |

## picorv32 / Part 0

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_picorv32_part0_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Oct 27 15:55:38 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_picorv32_part0_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
| CLB LUTs*                  | 3833 |     0 |          0 |   1303680 |  0.29 |
|   LUT as Logic             | 3689 |     0 |          0 |   1303680 |  0.28 |
|   LUT as Memory            |  144 |     0 |          0 |    600960 |  0.02 |
|     LUT as Distributed RAM |  144 |     0 |            |           |       |
|     LUT as Shift Register  |    0 |     0 |            |           |       |
| CLB Registers              | 2869 |     0 |          0 |   2607360 |  0.11 |
|   Register as Flip Flop    | 2869 |     0 |          0 |   2607360 |  0.11 |
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
| 2774  |          Yes |       Reset |            - |
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
| FDRE     | 2774 |            Register |
| LUT6     | 1259 |                 CLB |
| LUT3     | 1166 |                 CLB |
| LUT4     |  705 |                 CLB |
| LUT2     |  533 |                 CLB |
| LUT5     |  497 |                 CLB |
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

## picorv32 / Part 1

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_picorv32_part1_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Oct 27 15:51:13 2026
| Host         : node41 running 64-bit Ubuntu 22.04.5 LTS
| Command      : report_utilization -cells [get_cells -quiet role_i/ClockResetCore_0/emu_system] -file /home/huguanghui/remu/fpga/work_farm/fpga/scripts/../vivado_out/target_picorv32_part1_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt
| Design       : role_top
| Device       : xcvu37p_CIV-fsvh2892-2L-e
| Speed File   : -2L
| Design State : Synthesized
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
| CLB LUTs*                  | 2654 |     0 |          0 |   1303680 |  0.20 |
|   LUT as Logic             | 2614 |     0 |          0 |   1303680 |  0.20 |
|   LUT as Memory            |   40 |     0 |          0 |    600960 | <0.01 |
|     LUT as Distributed RAM |   40 |     0 |            |           |       |
|     LUT as Shift Register  |    0 |     0 |            |           |       |
| CLB Registers              | 2076 |     0 |          0 |   2607360 |  0.08 |
|   Register as Flip Flop    | 2076 |     0 |          0 |   2607360 |  0.08 |
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
| 2035  |          Yes |       Reset |            - |
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
| FDRE     | 2035 |            Register |
| LUT3     |  824 |                 CLB |
| LUT6     |  761 |                 CLB |
| LUT1     |  539 |                 CLB |
| LUT4     |  465 |                 CLB |
| LUT2     |  451 |                 CLB |
| LUT5     |  200 |                 CLB |
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

## rocket / Part 0

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_rocket_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Oct 27 18:09:04 2026
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
| CLB LUTs*                  | 16005 |     0 |          0 |   1303680 |  1.23 |
|   LUT as Logic             | 15446 |     0 |          0 |   1303680 |  1.18 |
|   LUT as Memory            |   559 |     0 |          0 |    600960 |  0.09 |
|     LUT as Distributed RAM |   552 |     0 |            |           |       |
|     LUT as Shift Register  |     7 |     0 |            |           |       |
| CLB Registers              |  9745 |     0 |          0 |   2607360 |  0.37 |
|   Register as Flip Flop    |  9745 |     0 |          0 |   2607360 |  0.37 |
|   Register as Latch        |     0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   119 |     0 |          0 |    162960 |  0.07 |
| F7 Muxes                   |   267 |     0 |          0 |    651840 |  0.04 |
| F8 Muxes                   |     2 |     0 |          0 |    325920 | <0.01 |
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
| 224   |          Yes |         Set |            - |
| 9521  |          Yes |       Reset |            - |
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
| FDRE     | 9521 |            Register |
| LUT6     | 5880 |                 CLB |
| LUT5     | 4101 |                 CLB |
| LUT3     | 3804 |                 CLB |
| LUT4     | 2973 |                 CLB |
| RAMD32   |  902 |                 CLB |
| LUT2     |  725 |                 CLB |
| LUT1     |  617 |                 CLB |
| MUXF7    |  267 |                 CLB |
| FDSE     |  224 |            Register |
| RAMS32   |  150 |                 CLB |
| CARRY8   |  119 |                 CLB |
| SRL16E   |    7 |                 CLB |
| BUFGCE   |    5 |               Clock |
| RAMB36E2 |    4 |            BLOCKRAM |
| URAM288  |    2 |            BLOCKRAM |
| MUXF8    |    2 |                 CLB |
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

## rocket / Part 1

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_rocket_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Oct 27 18:05:54 2026
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
| CLB LUTs*                  | 39465 |     0 |          0 |   1303680 |  3.03 |
|   LUT as Logic             | 39167 |     0 |          0 |   1303680 |  3.00 |
|   LUT as Memory            |   298 |     0 |          0 |    600960 |  0.05 |
|     LUT as Distributed RAM |   296 |     0 |            |           |       |
|     LUT as Shift Register  |     2 |     0 |            |           |       |
| CLB Registers              | 19718 |     0 |          0 |   2607360 |  0.76 |
|   Register as Flip Flop    | 19718 |     0 |          0 |   2607360 |  0.76 |
|   Register as Latch        |     0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   501 |     0 |          0 |    162960 |  0.31 |
| F7 Muxes                   |  1212 |     0 |          0 |    651840 |  0.19 |
| F8 Muxes                   |   348 |     0 |          0 |    325920 |  0.11 |
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
| 289   |          Yes |         Set |            - |
| 19429 |          Yes |       Reset |            - |
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
| BUFGCE     |    3 |     0 |          0 |       288 |  1.04 |
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
| FDRE     | 19429 |            Register |
| LUT6     | 17579 |                 CLB |
| LUT3     | 13805 |                 CLB |
| LUT5     |  7660 |                 CLB |
| LUT4     |  5918 |                 CLB |
| LUT2     |  3318 |                 CLB |
| MUXF7    |  1212 |                 CLB |
| LUT1     |   562 |                 CLB |
| CARRY8   |   501 |                 CLB |
| MUXF8    |   348 |                 CLB |
| FDSE     |   289 |            Register |
| RAMD64E  |   216 |                 CLB |
| RAMD32   |   140 |                 CLB |
| RAMB18E2 |    40 |            BLOCKRAM |
| RAMS32   |    20 |                 CLB |
| DSP48E2  |    15 |          Arithmetic |
| BUFGCE   |     3 |               Clock |
| SRLC32E  |     2 |                 CLB |
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

## xs-minimal / Part 0

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_xs-minimal_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Oct 27 18:43:06 2026
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
| CLB LUTs*                  | 528098 |     0 |          0 |   1303680 | 40.51 |
|   LUT as Logic             | 510082 |     0 |          0 |   1303680 | 39.13 |
|   LUT as Memory            |  18016 |     0 |          0 |    600960 |  3.00 |
|     LUT as Distributed RAM |  17964 |     0 |            |           |       |
|     LUT as Shift Register  |     52 |     0 |            |           |       |
| CLB Registers              | 309532 |     0 |          0 |   2607360 | 11.87 |
|   Register as Flip Flop    | 309532 |     0 |          0 |   2607360 | 11.87 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   5728 |     0 |          0 |    162960 |  3.51 |
| F7 Muxes                   |  11233 |     0 |          0 |    651840 |  1.72 |
| F8 Muxes                   |   3904 |     0 |          0 |    325920 |  1.20 |
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
| 3791   |          Yes |         Set |            - |
| 305741 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+-------+-------+------------+-----------+-------+
|     Site Type     |  Used | Fixed | Prohibited | Available | Util% |
+-------------------+-------+-------+------------+-----------+-------+
| Block RAM Tile    | 320.5 |     0 |          0 |      2016 | 15.90 |
|   RAMB36/FIFO*    |   263 |     0 |          0 |      2016 | 13.05 |
|     RAMB36E2 only |   263 |       |            |           |       |
|   RAMB18          |   115 |     0 |          0 |      4032 |  2.85 |
|     RAMB18E2 only |   115 |       |            |           |       |
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
| FDRE     | 305741 |            Register |
| LUT5     | 179049 |                 CLB |
| LUT6     | 169694 |                 CLB |
| LUT3     | 154664 |                 CLB |
| LUT4     |  88745 |                 CLB |
| LUT2     |  18866 |                 CLB |
| RAMD64E  |  14768 |                 CLB |
| MUXF7    |  11233 |                 CLB |
| CARRY8   |   5728 |                 CLB |
| RAMD32   |   5356 |                 CLB |
| MUXF8    |   3904 |                 CLB |
| FDSE     |   3791 |            Register |
| LUT1     |   1668 |                 CLB |
| RAMS32   |    852 |                 CLB |
| RAMB36E2 |    263 |            BLOCKRAM |
| RAMB18E2 |    115 |            BLOCKRAM |
| SRLC32E  |     49 |                 CLB |
| URAM288  |     13 |            BLOCKRAM |
| BUFGCE   |      5 |               Clock |
| SRL16E   |      3 |                 CLB |
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

## xs-minimal / Part 1

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_xs-minimal_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Oct 27 18:26:28 2026
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
| CLB LUTs*                  | 343605 |     0 |          0 |   1303680 | 26.36 |
|   LUT as Logic             | 343013 |     0 |          0 |   1303680 | 26.31 |
|   LUT as Memory            |    592 |     0 |          0 |    600960 |  0.10 |
|     LUT as Distributed RAM |    592 |     0 |            |           |       |
|     LUT as Shift Register  |      0 |     0 |            |           |       |
| CLB Registers              | 104227 |     0 |          0 |   2607360 |  4.00 |
|   Register as Flip Flop    | 104227 |     0 |          0 |   2607360 |  4.00 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |    899 |     0 |          0 |    162960 |  0.55 |
| F7 Muxes                   |   2438 |     0 |          0 |    651840 |  0.37 |
| F8 Muxes                   |    570 |     0 |          0 |    325920 |  0.17 |
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
| 1132   |          Yes |         Set |            - |
| 103095 |          Yes |       Reset |            - |
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
| LUT6     | 171917 |                 CLB |
| FDRE     | 103095 |            Register |
| LUT5     |  75001 |                 CLB |
| LUT4     |  72361 |                 CLB |
| LUT3     |  48255 |                 CLB |
| LUT2     |  10107 |                 CLB |
| MUXF7    |   2438 |                 CLB |
| FDSE     |   1132 |            Register |
| RAMD32   |   1036 |                 CLB |
| CARRY8   |    899 |                 CLB |
| LUT1     |    612 |                 CLB |
| MUXF8    |    570 |                 CLB |
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

## nanhu-g / Part 0

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_nanhu-g_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Oct 27 18:55:09 2026
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
| CLB LUTs*                  | 872861 |     0 |          0 |   1303680 | 66.95 |
|   LUT as Logic             | 854005 |     0 |          0 |   1303680 | 65.51 |
|   LUT as Memory            |  18856 |     0 |          0 |    600960 |  3.14 |
|     LUT as Distributed RAM |  18766 |     0 |            |           |       |
|     LUT as Shift Register  |     90 |     0 |            |           |       |
| CLB Registers              | 524416 |     0 |          0 |   2607360 | 20.11 |
|   Register as Flip Flop    | 524416 |     0 |          0 |   2607360 | 20.11 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   6376 |     0 |          0 |    162960 |  3.91 |
| F7 Muxes                   |  14369 |     0 |          0 |    651840 |  2.20 |
| F8 Muxes                   |   4924 |     0 |          0 |    325920 |  1.51 |
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
| 8061   |          Yes |         Set |            - |
| 516355 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+------+-------+------------+-----------+-------+
|     Site Type     | Used | Fixed | Prohibited | Available | Util% |
+-------------------+------+-------+------------+-----------+-------+
| Block RAM Tile    |  340 |     0 |          0 |      2016 | 16.87 |
|   RAMB36/FIFO*    |  212 |     0 |          0 |      2016 | 10.52 |
|     RAMB36E2 only |  212 |       |            |           |       |
|   RAMB18          |  256 |     0 |          0 |      4032 |  6.35 |
|     RAMB18E2 only |  256 |       |            |           |       |
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
| FDRE     | 516355 |            Register |
| LUT5     | 317901 |                 CLB |
| LUT6     | 288668 |                 CLB |
| LUT3     | 241944 |                 CLB |
| LUT4     | 127512 |                 CLB |
| LUT2     |  31619 |                 CLB |
| RAMD32   |  15954 |                 CLB |
| MUXF7    |  14369 |                 CLB |
| RAMD64E  |   9402 |                 CLB |
| FDSE     |   8061 |            Register |
| CARRY8   |   6376 |                 CLB |
| MUXF8    |   4924 |                 CLB |
| LUT1     |   2692 |                 CLB |
| RAMS32   |   2466 |                 CLB |
| RAMB18E2 |    256 |            BLOCKRAM |
| RAMB36E2 |    212 |            BLOCKRAM |
| URAM288  |    141 |            BLOCKRAM |
| SRLC32E  |     80 |                 CLB |
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

## nanhu-g / Part 1

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_nanhu-g_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Oct 27 18:39:31 2026
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
| CLB LUTs*                  | 662769 |     0 |          0 |   1303680 | 50.84 |
|   LUT as Logic             | 661860 |     0 |          0 |   1303680 | 50.77 |
|   LUT as Memory            |    909 |     0 |          0 |    600960 |  0.15 |
|     LUT as Distributed RAM |    888 |     0 |            |           |       |
|     LUT as Shift Register  |     21 |     0 |            |           |       |
| CLB Registers              | 225610 |     0 |          0 |   2607360 |  8.65 |
|   Register as Flip Flop    | 225610 |     0 |          0 |   2607360 |  8.65 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   4052 |     0 |          0 |    162960 |  2.49 |
| F7 Muxes                   |   6216 |     0 |          0 |    651840 |  0.95 |
| F8 Muxes                   |   1532 |     0 |          0 |    325920 |  0.47 |
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
| 2300   |          Yes |         Set |            - |
| 223310 |          Yes |       Reset |            - |
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
| LUT6     | 299036 |                 CLB |
| FDRE     | 223310 |            Register |
| LUT4     | 160986 |                 CLB |
| LUT5     | 149523 |                 CLB |
| LUT3     | 117338 |                 CLB |
| LUT2     |  17063 |                 CLB |
| MUXF7    |   6216 |                 CLB |
| CARRY8   |   4052 |                 CLB |
| FDSE     |   2300 |            Register |
| MUXF8    |   1532 |                 CLB |
| RAMD32   |   1332 |                 CLB |
| LUT1     |    820 |                 CLB |
| RAMS32   |    148 |                 CLB |
| RAMB36E2 |     35 |            BLOCKRAM |
| SRLC32E  |     16 |                 CLB |
| SRL16E   |      5 |                 CLB |
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

## kmh / Part 0

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_kmh_0th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Oct 27 19:00:57 2026
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
| CLB LUTs*                  | 953991 |     0 |          0 |   1303680 | 73.18 |
|   LUT as Logic             | 936355 |     0 |          0 |   1303680 | 71.82 |
|   LUT as Memory            |  17636 |     0 |          0 |    600960 |  2.93 |
|     LUT as Distributed RAM |  17584 |     0 |            |           |       |
|     LUT as Shift Register  |     52 |     0 |            |           |       |
| CLB Registers              | 460539 |     0 |          0 |   2607360 | 17.66 |
|   Register as Flip Flop    | 460539 |     0 |          0 |   2607360 | 17.66 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |  11097 |     0 |          0 |    162960 |  6.81 |
| F7 Muxes                   |  29665 |     0 |          0 |    651840 |  4.55 |
| F8 Muxes                   |   6430 |     0 |          0 |    325920 |  1.97 |
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
| 4995   |          Yes |         Set |            - |
| 455544 |          Yes |       Reset |            - |
+--------+--------------+-------------+--------------+


2. BLOCKRAM
-----------

+-------------------+-------+-------+------------+-----------+-------+
|     Site Type     |  Used | Fixed | Prohibited | Available | Util% |
+-------------------+-------+-------+------------+-----------+-------+
| Block RAM Tile    | 288.5 |     0 |          0 |      2016 | 14.31 |
|   RAMB36/FIFO*    |   248 |     0 |          0 |      2016 | 12.30 |
|     RAMB36E2 only |   248 |       |            |           |       |
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
| FDRE     | 455544 |            Register |
| LUT6     | 381320 |                 CLB |
| LUT5     | 281204 |                 CLB |
| LUT3     | 271027 |                 CLB |
| LUT4     | 151192 |                 CLB |
| LUT2     |  35682 |                 CLB |
| MUXF7    |  29665 |                 CLB |
| RAMD64E  |  13608 |                 CLB |
| CARRY8   |  11097 |                 CLB |
| MUXF8    |   6430 |                 CLB |
| RAMD32   |   6338 |                 CLB |
| FDSE     |   4995 |            Register |
| LUT1     |   3471 |                 CLB |
| RAMS32   |    842 |                 CLB |
| RAMB36E2 |    248 |            BLOCKRAM |
| RAMB18E2 |     81 |            BLOCKRAM |
| SRLC32E  |     35 |                 CLB |
| SRL16E   |     17 |                 CLB |
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

## kmh / Part 1

远端路径：`/home/huguanghui/remu/fpga/work_farm/fpga/vivado_out/target_kmh_1th_part2_direct_remus_nm37_aurora/synth_rpt/synth_emu_system_util.rpt`。

```text
Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
| Date         : Tue Oct 27 18:59:57 2026
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

+----------------------------+--------+-------+------------+-----------+-------+
|          Site Type         |  Used  | Fixed | Prohibited | Available | Util% |
+----------------------------+--------+-------+------------+-----------+-------+
| CLB LUTs*                  | 987830 |     0 |          0 |   1303680 | 75.77 |
|   LUT as Logic             | 987235 |     0 |          0 |   1303680 | 75.73 |
|   LUT as Memory            |    595 |     0 |          0 |    600960 |  0.10 |
|     LUT as Distributed RAM |    592 |     0 |            |           |       |
|     LUT as Shift Register  |      3 |     0 |            |           |       |
| CLB Registers              | 212936 |     0 |          0 |   2607360 |  8.17 |
|   Register as Flip Flop    | 212936 |     0 |          0 |   2607360 |  8.17 |
|   Register as Latch        |      0 |     0 |          0 |   2607360 |  0.00 |
| CARRY8                     |   3904 |     0 |          0 |    162960 |  2.40 |
| F7 Muxes                   |  68693 |     0 |          0 |    651840 | 10.54 |
| F8 Muxes                   |  31555 |     0 |          0 |    325920 |  9.68 |
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
| 3290   |          Yes |         Set |            - |
| 209646 |          Yes |       Reset |            - |
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
| LUT6     | 548749 |                 CLB |
| FDRE     | 209646 |            Register |
| LUT5     | 202104 |                 CLB |
| LUT4     | 190777 |                 CLB |
| LUT3     | 111773 |                 CLB |
| MUXF7    |  68693 |                 CLB |
| LUT2     |  39930 |                 CLB |
| MUXF8    |  31555 |                 CLB |
| CARRY8   |   3904 |                 CLB |
| FDSE     |   3290 |            Register |
| LUT1     |   1319 |                 CLB |
| RAMD32   |   1036 |                 CLB |
| RAMS32   |    148 |                 CLB |
| BUFGCE   |      5 |               Clock |
| SRL16E   |      3 |                 CLB |
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
