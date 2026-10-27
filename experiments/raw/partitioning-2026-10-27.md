# 划分实验原始汇总：2026-10-27

来源：`serve41:/home/huguanghui/remu`。采集时间：`2026-10-27T09:44:37Z`。本文件保存12份已完成summary的原文，不包含KMH；只读复制，未重新运行实验。返回[整理结果](../partitioning.md)。

采集时远端checkout：`vivado2024.2` / `212bd4bf60af332c0491ce8bef0ae2704ab185e9`。此标识不替代每次实验构建版本的核对。以下校验值对应各代码块内的原始文件内容，包括末尾换行，不包含Markdown围栏或路径说明。

## 文件校验值

| 实验目录 | SHA-256 |
| --- | --- |
| picorv32_part2 | `760d30ef2bddc51353f61834291e1f1f16e000f34d475929993bbad84c3c8ea7` |
| picorv32_part3 | `903dbd9b322c8193a74f774e0225d4d325a78d4ae96702fd181ac2e41c9112e4` |
| picorv32_part4 | `9c39b464d2cd4eaa268bd0d1c66eb2591df5b0c4ed09e02c9f7c42ad81fca379` |
| rocket_part2 | `e5571064fa96cbce3982f76b57e32b21ef361e1d484297cc21121b7f55ee5543` |
| rocket_part3 | `151c95a04ea4ad1985b8b8d21f7f104914469757f376e8c9ccb2f703f8b517e6` |
| rocket_part4 | `f33d94ccea4361370bfe57d3edba7af9d0425b3928be4a4e438e7e95bf845be8` |
| xs-minimal_part2 | `8b2da926053e7e8855284782d1c714af63e22976b77f2da977dc52b390370879` |
| xs-minimal_part3 | `e8b205708302a1d31ce2110d0b029293199479530f6fb5a59f3b0ce30f4f6834` |
| xs-minimal_part4 | `21217cc3fa783c086dfec07c77219569fe31d24a6849f326bf5a380d3f2445f5` |
| nanhu-g_part2 | `0a713a37008a67b10e969508edcca6cecb37d14020b6df5666bc238df12ba001` |
| nanhu-g_part3 | `044d9e80ba58ad5bbbde561a6a5552ef1be64f314d5b89da3d4e541509611b58` |
| nanhu-g_part4 | `d247b8972c81b87b25869156efc53f87975de905eb45ac8ed5fe1ad8a422c496` |

## picorv32_part2

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part2/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/picorv32_part2/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 2 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=1136 hyperedges=1223
[partition] solver_wall_ms=161.995971
[partition] part=0 vertices=964 total_weight=2706 cell_weight=2704 port_weight=2
[partition] part=1 vertices=172 total_weight=3102 cell_weight=3102 port_weight=0
[partition] cut_edges=85 cut_size=215 km1=215
[partition] max_path_cuts=4 boundary_ppd=5 required_stages=5
[partition] critical_boundary_path=see_ppd_report
```

## picorv32_part3

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part3/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/picorv32_part3/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 3 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=1140 hyperedges=1225
[partition] solver_wall_ms=236.071124
[partition] part=0 vertices=264 total_weight=2125 cell_weight=2123 port_weight=2
[partition] part=1 vertices=751 total_weight=1624 cell_weight=1624 port_weight=0
[partition] part=2 vertices=125 total_weight=2059 cell_weight=2059 port_weight=0
[partition] cut_edges=112 cut_size=330 km1=333
[partition] max_path_cuts=3 boundary_ppd=4 required_stages=4
[partition] critical_boundary_path=see_ppd_report
```

## picorv32_part4

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part4/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/picorv32_part4/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 4 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=1140 hyperedges=1225
[partition] solver_wall_ms=270.085666
[partition] part=0 vertices=280 total_weight=1415 cell_weight=1413 port_weight=2
[partition] part=1 vertices=69 total_weight=1436 cell_weight=1436 port_weight=0
[partition] part=2 vertices=684 total_weight=1478 cell_weight=1478 port_weight=0
[partition] part=3 vertices=107 total_weight=1479 cell_weight=1479 port_weight=0
[partition] cut_edges=105 cut_size=380 km1=418
[partition] max_path_cuts=4 boundary_ppd=5 required_stages=5
[partition] critical_boundary_path=see_ppd_report
```

## rocket_part2

远端路径：`/home/huguanghui/remu/examples/build/rocket_part2/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/rocket_part2/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 2 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=2945 hyperedges=3218
[partition] solver_wall_ms=136.11485400000001
[partition] part=0 vertices=2585 total_weight=87099 cell_weight=87097 port_weight=2
[partition] part=1 vertices=360 total_weight=96010 cell_weight=96010 port_weight=0
[partition] cut_edges=4 cut_size=357 km1=357
[partition] max_path_cuts=2 boundary_ppd=3 required_stages=3
[partition] critical_boundary_path=see_ppd_report
```

## rocket_part3

远端路径：`/home/huguanghui/remu/examples/build/rocket_part3/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/rocket_part3/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 3 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=7030 hyperedges=7963
[partition] solver_wall_ms=847.38457800000003
[partition] part=0 vertices=466 total_weight=64398 cell_weight=64396 port_weight=2
[partition] part=1 vertices=4898 total_weight=53608 cell_weight=53608 port_weight=0
[partition] part=2 vertices=1666 total_weight=65030 cell_weight=65030 port_weight=0
[partition] cut_edges=181 cut_size=1120 km1=1120
[partition] max_path_cuts=3 boundary_ppd=4 required_stages=4
[partition] critical_boundary_path=see_ppd_report
```

## rocket_part4

远端路径：`/home/huguanghui/remu/examples/build/rocket_part4/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/rocket_part4/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 4 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=11449 hyperedges=13029
[partition] solver_wall_ms=1442.3987360000001
[partition] part=0 vertices=2320 total_weight=49790 cell_weight=49788 port_weight=2
[partition] part=1 vertices=2026 total_weight=33940 cell_weight=33940 port_weight=0
[partition] part=2 vertices=5368 total_weight=50098 cell_weight=50098 port_weight=0
[partition] part=3 vertices=1735 total_weight=49111 cell_weight=49111 port_weight=0
[partition] cut_edges=238 cut_size=1317 km1=1325
[partition] max_path_cuts=4 boundary_ppd=5 required_stages=5
[partition] critical_boundary_path=see_ppd_report
```

## xs-minimal_part2

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part2/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/xs-minimal_part2/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 2 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=71664 hyperedges=73589
[partition] solver_wall_ms=4374.3883530000003
[partition] part=0 vertices=4798 total_weight=1457641 cell_weight=1457639 port_weight=2
[partition] part=1 vertices=66866 total_weight=1194971 cell_weight=1194971 port_weight=0
[partition] cut_edges=275 cut_size=2763 km1=2763
[partition] max_path_cuts=3 boundary_ppd=4 required_stages=4
[partition] critical_boundary_path=see_ppd_report
```

## xs-minimal_part3

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part3/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/xs-minimal_part3/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 3 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=81087 hyperedges=86550
[partition] solver_wall_ms=3896.166635
[partition] part=0 vertices=6182 total_weight=961365 cell_weight=961363 port_weight=2
[partition] part=1 vertices=72782 total_weight=784023 cell_weight=784023 port_weight=0
[partition] part=2 vertices=2123 total_weight=907229 cell_weight=907229 port_weight=0
[partition] cut_edges=453 cut_size=4752 km1=4756
[partition] max_path_cuts=2 boundary_ppd=3 required_stages=3
[partition] critical_boundary_path=see_ppd_report
```

## xs-minimal_part4

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part4/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/xs-minimal_part4/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 4 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=93963 hyperedges=101694
[partition] solver_wall_ms=6699.0347229999998
[partition] part=0 vertices=6010 total_weight=625604 cell_weight=625602 port_weight=2
[partition] part=1 vertices=6065 total_weight=715593 cell_weight=715593 port_weight=0
[partition] part=2 vertices=845 total_weight=589010 cell_weight=589010 port_weight=0
[partition] part=3 vertices=81043 total_weight=722410 cell_weight=722410 port_weight=0
[partition] cut_edges=562 cut_size=6508 km1=6628
[partition] max_path_cuts=4 boundary_ppd=5 required_stages=5
[partition] critical_boundary_path=see_ppd_report
```

## nanhu-g_part2

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part2/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/nanhu-g_part2/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 2 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=5867 hyperedges=8017
[partition] solver_wall_ms=549.53933099999995
[partition] part=0 vertices=5020 total_weight=2602068 cell_weight=2602066 port_weight=2
[partition] part=1 vertices=847 total_weight=2214758 cell_weight=2214758 port_weight=0
[partition] cut_edges=159 cut_size=4395 km1=4395
[partition] max_path_cuts=2 boundary_ppd=3 required_stages=3
[partition] critical_boundary_path=see_ppd_report
```

## nanhu-g_part3

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part3/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/nanhu-g_part3/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 3 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=95166 hyperedges=100831
[partition] solver_wall_ms=5855.9918710000002
[partition] part=0 vertices=74850 total_weight=1408682 cell_weight=1408680 port_weight=2
[partition] part=1 vertices=2567 total_weight=1762537 cell_weight=1762537 port_weight=0
[partition] part=2 vertices=17749 total_weight=1645603 cell_weight=1645603 port_weight=0
[partition] cut_edges=803 cut_size=5808 km1=5821
[partition] max_path_cuts=4 boundary_ppd=5 required_stages=5
[partition] critical_boundary_path=see_ppd_report
```

## nanhu-g_part4

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part4/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/nanhu-g_part4/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 4 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=99781 hyperedges=106720
[partition] solver_wall_ms=8121.8141390000001
[partition] part=0 vertices=859 total_weight=1176282 cell_weight=1176280 port_weight=2
[partition] part=1 vertices=15899 total_weight=1304901 cell_weight=1304901 port_weight=0
[partition] part=2 vertices=79268 total_weight=1030466 cell_weight=1030466 port_weight=0
[partition] part=3 vertices=3755 total_weight=1305178 cell_weight=1305178 port_weight=0
[partition] cut_edges=1097 cut_size=8015 km1=8153
[partition] max_path_cuts=3 boundary_ppd=4 required_stages=4
[partition] critical_boundary_path=see_ppd_report
```

