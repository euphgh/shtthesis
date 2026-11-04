# 网表划分实验原始汇总：2026-11-04

来源：`serve41:/home/huguanghui/remu`。采集时间：`2026-11-04T04:18:18Z`（UTC，即北京时间2026-11-04 12:18:18）。本文件保存15份已完成summary的原文，只读复制，未重新运行实验。返回[整理结果](../netlist-partitioning.md)。

采集时远端checkout：`vivado2024.2` / `828600a0f8bbf2a93040156aafff1ddbb218d504`。此时`transform/src/partition/decomposer.cc`存在未提交改动（关闭自适应展开阈值分支），与[2026-10-27自适应划分批次](partitioning-2026-10-27.md)不是同一划分算法；两批数据不可混用或直接拼表。

以下校验值对应代码块内的原始文件内容（含末尾换行），不包含Markdown围栏或路径说明；每个代码块前的mtime与SHA-256均为采集时远端`sha256sum`结果。

## 文件校验值

| 实验目录 | SHA-256 |
| --- | --- |
| picorv32_part2 | `6c420d5a94dd874d8d93a3b38d0262bbb490e149e6b2e4f2153979a570aacfd7` |
| picorv32_part3 | `73de694065c5c2acc1b423a13598842b8a207786f845ac24b516391fc225fe46` |
| picorv32_part4 | `b561b3746d5331d1675a4764fa082e47d1a528cce10120c8981f2cb207c5de20` |
| rocket_part2 | `acfa22706231f4576aa2bc3ba697babc5ce21cb73a2daef9b8ff50335ba37d41` |
| rocket_part3 | `8360b078462a56f7e7fab423dbb21f46fdae7ee6f5efea8b42dcd0dfcdcc4cce` |
| rocket_part4 | `341370eabc8b5d4b07cb2377ffa23de4be01ffa9a852b701280cc9d96af2604b` |
| xs-minimal_part2 | `6b8aabef0a1acaf8d59552631752c8d43e05aa48fb1a4dd7c6c19fdb644cdace` |
| xs-minimal_part3 | `1802f55a27ab5cb373b89b8a4dec1233cfdc5a891c554cfebf70107a33ccfd05` |
| xs-minimal_part4 | `e537d694219906214bfc96f9c09076eb208e11da476fd0a777aaf08c0845fca3` |
| nanhu-g_part2 | `36ff89cfeaef5fd7bea2a56a8b7b630f4ec114aa07c34c20d5dde723970f6ac8` |
| nanhu-g_part3 | `744c0380126c8c741c43ed9b05fbd54f5b9a70de7a37dbfa76d01b4fde533bd6` |
| nanhu-g_part4 | `bdca86a29d8f425d5d536e7e3777f905e61f96ca0cb359041fa7711aaa0827af` |
| kmh_part2 | `3681aa13364e80c735d4634ce7762bd171ecc4caa356eee140987c77d4f3b1fd` |
| kmh_part3 | `e1d7108370ece48130bdaabff8ce9fdd76a6a1e362913998295569fab8eb835a` |
| kmh_part4 | `ab283b69c7124c6fbb3af2b17047c111a3fa8d24276d8e3fdbe1d2133fc0cba5` |

## picorv32_part2

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part2/partition/summary.txt`。

远端mtime：`2026-11-03 14:58:06 CST`；SHA-256：`6c420d5a94dd874d8d93a3b38d0262bbb490e149e6b2e4f2153979a570aacfd7`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/picorv32_part2/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 2 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=1169 hyperedges=1244
[partition] solver_wall_ms=162.80219099999999
[partition] part=0 vertices=987 total_weight=2621 cell_weight=2619 port_weight=2
[partition] part=1 vertices=182 total_weight=3187 cell_weight=3187 port_weight=0
[partition] cut_edges=85 cut_size=211 km1=211
[partition] max_path_cuts=4 boundary_ppd=5 required_stages=5
[partition] critical_boundary_path=see_ppd_report
```

## picorv32_part3

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part3/partition/summary.txt`。

远端mtime：`2026-10-28 20:19:19 CST`；SHA-256：`73de694065c5c2acc1b423a13598842b8a207786f845ac24b516391fc225fe46`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/picorv32_part3/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 3 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=1169 hyperedges=1244
[partition] solver_wall_ms=160.02303599999999
[partition] part=0 vertices=143 total_weight=2124 cell_weight=2122 port_weight=2
[partition] part=1 vertices=908 total_weight=1946 cell_weight=1946 port_weight=0
[partition] part=2 vertices=118 total_weight=1738 cell_weight=1738 port_weight=0
[partition] cut_edges=114 cut_size=311 km1=315
[partition] max_path_cuts=3 boundary_ppd=4 required_stages=4
[partition] critical_boundary_path=see_ppd_report
```

## picorv32_part4

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part4/partition/summary.txt`。

远端mtime：`2026-10-28 20:19:26 CST`；SHA-256：`b561b3746d5331d1675a4764fa082e47d1a528cce10120c8981f2cb207c5de20`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/picorv32_part4/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 4 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=1169 hyperedges=1244
[partition] solver_wall_ms=297.54493100000002
[partition] part=0 vertices=302 total_weight=1229 cell_weight=1227 port_weight=2
[partition] part=1 vertices=709 total_weight=1573 cell_weight=1573 port_weight=0
[partition] part=2 vertices=92 total_weight=1572 cell_weight=1572 port_weight=0
[partition] part=3 vertices=66 total_weight=1434 cell_weight=1434 port_weight=0
[partition] cut_edges=116 cut_size=378 km1=448
[partition] max_path_cuts=3 boundary_ppd=4 required_stages=4
[partition] critical_boundary_path=see_ppd_report
```

## rocket_part2

远端路径：`/home/huguanghui/remu/examples/build/rocket_part2/partition/summary.txt`。

远端mtime：`2026-10-28 20:21:26 CST`；SHA-256：`acfa22706231f4576aa2bc3ba697babc5ce21cb73a2daef9b8ff50335ba37d41`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/rocket_part2/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 2 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=26290 hyperedges=34019
[partition] solver_wall_ms=2184.1372670000001
[partition] part=0 vertices=13325 total_weight=85870 cell_weight=85868 port_weight=2
[partition] part=1 vertices=12965 total_weight=93843 cell_weight=93843 port_weight=0
[partition] cut_edges=45 cut_size=341 km1=341
[partition] max_path_cuts=2 boundary_ppd=3 required_stages=3
[partition] critical_boundary_path=see_ppd_report
```

## rocket_part3

远端路径：`/home/huguanghui/remu/examples/build/rocket_part3/partition/summary.txt`。

远端mtime：`2026-10-28 20:21:22 CST`；SHA-256：`8360b078462a56f7e7fab423dbb21f46fdae7ee6f5efea8b42dcd0dfcdcc4cce`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/rocket_part3/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 3 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=26290 hyperedges=34019
[partition] solver_wall_ms=2899.2935080000002
[partition] part=0 vertices=13093 total_weight=60079 cell_weight=60077 port_weight=2
[partition] part=1 vertices=3892 total_weight=57672 cell_weight=57672 port_weight=0
[partition] part=2 vertices=9305 total_weight=61962 cell_weight=61962 port_weight=0
[partition] cut_edges=202 cut_size=741 km1=743
[partition] max_path_cuts=4 boundary_ppd=5 required_stages=5
[partition] critical_boundary_path=see_ppd_report
```

## rocket_part4

远端路径：`/home/huguanghui/remu/examples/build/rocket_part4/partition/summary.txt`。

远端mtime：`2026-10-28 20:21:41 CST`；SHA-256：`341370eabc8b5d4b07cb2377ffa23de4be01ffa9a852b701280cc9d96af2604b`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/rocket_part4/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 4 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=26290 hyperedges=34019
[partition] solver_wall_ms=3997.016177
[partition] part=0 vertices=11478 total_weight=49381 cell_weight=49379 port_weight=2
[partition] part=1 vertices=1022 total_weight=33215 cell_weight=33215 port_weight=0
[partition] part=2 vertices=7342 total_weight=49369 cell_weight=49369 port_weight=0
[partition] part=3 vertices=6448 total_weight=47748 cell_weight=47748 port_weight=0
[partition] cut_edges=309 cut_size=1127 km1=1199
[partition] max_path_cuts=5 boundary_ppd=6 required_stages=6
[partition] critical_boundary_path=see_ppd_report
```

## xs-minimal_part2

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part2/partition/summary.txt`。

远端mtime：`2026-10-29 09:19:03 CST`；SHA-256：`6b8aabef0a1acaf8d59552631752c8d43e05aa48fb1a4dd7c6c19fdb644cdace`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/xs-minimal_part2/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 2 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=642184 hyperedges=832484
[partition] solver_wall_ms=98980.751355
[partition] part=0 vertices=332708 total_weight=1297010 cell_weight=1297008 port_weight=2
[partition] part=1 vertices=309476 total_weight=1224282 cell_weight=1224282 port_weight=0
[partition] cut_edges=713 cut_size=1955 km1=1955
[partition] max_path_cuts=2 boundary_ppd=3 required_stages=3
[partition] critical_boundary_path=see_ppd_report
```

## xs-minimal_part3

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part3/partition/summary.txt`。

远端mtime：`2026-10-29 06:31:39 CST`；SHA-256：`1802f55a27ab5cb373b89b8a4dec1233cfdc5a891c554cfebf70107a33ccfd05`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/xs-minimal_part3/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 3 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=642184 hyperedges=832484
[partition] solver_wall_ms=82373.276945999998
[partition] part=0 vertices=307920 total_weight=749018 cell_weight=749016 port_weight=2
[partition] part=1 vertices=161095 total_weight=890641 cell_weight=890641 port_weight=0
[partition] part=2 vertices=173169 total_weight=881633 cell_weight=881633 port_weight=0
[partition] cut_edges=1158 cut_size=3105 km1=3108
[partition] max_path_cuts=3 boundary_ppd=4 required_stages=4
[partition] critical_boundary_path=see_ppd_report
```

## xs-minimal_part4

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part4/partition/summary.txt`。

远端mtime：`2026-10-29 05:07:26 CST`；SHA-256：`e537d694219906214bfc96f9c09076eb208e11da476fd0a777aaf08c0845fca3`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/xs-minimal_part4/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 4 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=642184 hyperedges=832484
[partition] solver_wall_ms=186937.13997399999
[partition] part=0 vertices=215468 total_weight=686723 cell_weight=686721 port_weight=2
[partition] part=1 vertices=106163 total_weight=578082 cell_weight=578082 port_weight=0
[partition] part=2 vertices=183436 total_weight=571324 cell_weight=571324 port_weight=0
[partition] part=3 vertices=137117 total_weight=685163 cell_weight=685163 port_weight=0
[partition] cut_edges=1344 cut_size=4525 km1=4533
[partition] max_path_cuts=3 boundary_ppd=4 required_stages=4
[partition] critical_boundary_path=see_ppd_report
```

## nanhu-g_part2

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part2/partition/summary.txt`。

远端mtime：`2026-10-30 19:38:38 CST`；SHA-256：`36ff89cfeaef5fd7bea2a56a8b7b630f4ec114aa07c34c20d5dde723970f6ac8`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/nanhu-g_part2/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 2 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=1214292 hyperedges=1623676
[partition] solver_wall_ms=160273.53423799999
[partition] part=0 vertices=704959 total_weight=2137392 cell_weight=2137390 port_weight=2
[partition] part=1 vertices=509333 total_weight=2499674 cell_weight=2499674 port_weight=0
[partition] cut_edges=290 cut_size=2400 km1=2400
[partition] max_path_cuts=3 boundary_ppd=4 required_stages=4
[partition] critical_boundary_path=see_ppd_report
```

## nanhu-g_part3

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part3/partition/summary.txt`。

远端mtime：`2026-10-30 06:57:41 CST`；SHA-256：`744c0380126c8c741c43ed9b05fbd54f5b9a70de7a37dbfa76d01b4fde533bd6`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/nanhu-g_part3/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 3 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=1214292 hyperedges=1623676
[partition] solver_wall_ms=493179.03226100001
[partition] part=0 vertices=511464 total_weight=1694294 cell_weight=1694292 port_weight=2
[partition] part=1 vertices=410730 total_weight=1329521 cell_weight=1329521 port_weight=0
[partition] part=2 vertices=292098 total_weight=1613251 cell_weight=1613251 port_weight=0
[partition] cut_edges=1394 cut_size=4532 km1=4534
[partition] max_path_cuts=5 boundary_ppd=6 required_stages=6
[partition] critical_boundary_path=see_ppd_report
```

## nanhu-g_part4

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part4/partition/summary.txt`。

远端mtime：`2026-10-30 02:40:02 CST`；SHA-256：`bdca86a29d8f425d5d536e7e3777f905e61f96ca0cb359041fa7711aaa0827af`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/nanhu-g_part4/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 4 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=1214292 hyperedges=1623676
[partition] solver_wall_ms=275371.99617100001
[partition] part=0 vertices=381843 total_weight=1152325 cell_weight=1152323 port_weight=2
[partition] part=1 vertices=329032 total_weight=998998 cell_weight=998998 port_weight=0
[partition] part=2 vertices=349820 total_weight=1273208 cell_weight=1273208 port_weight=0
[partition] part=3 vertices=153597 total_weight=1212535 cell_weight=1212535 port_weight=0
[partition] cut_edges=1949 cut_size=5953 km1=5958
[partition] max_path_cuts=4 boundary_ppd=5 required_stages=5
[partition] critical_boundary_path=see_ppd_report
```

## kmh_part2

远端路径：`/home/huguanghui/remu/examples/build/kmh_part2/partition/summary.txt`。

远端mtime：`2026-10-31 19:13:39 CST`；SHA-256：`3681aa13364e80c735d4634ce7762bd171ecc4caa356eee140987c77d4f3b1fd`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/kmh_part2/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 2 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=1067041 hyperedges=1294157
[partition] solver_wall_ms=163119.658994
[partition] part=0 vertices=364505 total_weight=2649404 cell_weight=2649402 port_weight=2
[partition] part=1 vertices=702536 total_weight=2838131 cell_weight=2838131 port_weight=0
[partition] cut_edges=1468 cut_size=4740 km1=4740
[partition] max_path_cuts=4 boundary_ppd=5 required_stages=5
[partition] critical_boundary_path=see_ppd_report
```

## kmh_part3

远端路径：`/home/huguanghui/remu/examples/build/kmh_part3/partition/summary.txt`。

远端mtime：`2026-10-31 02:36:31 CST`；SHA-256：`e1d7108370ece48130bdaabff8ce9fdd76a6a1e362913998295569fab8eb835a`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/kmh_part3/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 3 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=1067041 hyperedges=1294157
[partition] solver_wall_ms=177793.68789
[partition] part=0 vertices=439580 total_weight=1925907 cell_weight=1925905 port_weight=2
[partition] part=1 vertices=127824 total_weight=1659363 cell_weight=1659363 port_weight=0
[partition] part=2 vertices=499637 total_weight=1902265 cell_weight=1902265 port_weight=0
[partition] cut_edges=1360 cut_size=5328 km1=5355
[partition] max_path_cuts=6 boundary_ppd=7 required_stages=7
[partition] critical_boundary_path=see_ppd_report
```

## kmh_part4

远端路径：`/home/huguanghui/remu/examples/build/kmh_part4/partition/summary.txt`。

远端mtime：`2026-10-30 21:12:45 CST`；SHA-256：`ab283b69c7124c6fbb3af2b17047c111a3fa8d24276d8e3fdbe1d2133fc0cba5`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/kmh_part4/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 4 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=1067041 hyperedges=1294157
[partition] solver_wall_ms=250964.65951100001
[partition] part=0 vertices=357920 total_weight=1490882 cell_weight=1490880 port_weight=2
[partition] part=1 vertices=477784 total_weight=1507194 cell_weight=1507194 port_weight=0
[partition] part=2 vertices=105431 total_weight=1422155 cell_weight=1422155 port_weight=0
[partition] part=3 vertices=125906 total_weight=1067304 cell_weight=1067304 port_weight=0
[partition] cut_edges=1773 cut_size=7763 km1=7820
[partition] max_path_cuts=7 boundary_ppd=8 required_stages=8
[partition] critical_boundary_path=see_ppd_report
```

