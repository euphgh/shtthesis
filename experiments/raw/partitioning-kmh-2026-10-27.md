# KMH划分实验原始汇总：2026-10-27增补

来源：`serve41:/home/huguanghui/remu`。采集时间：`2026-10-27T13:01:21Z`（UTC，即北京时间2026-10-27 21:01:21）。本文件保存KMH的2、3、4分区summary原文，共3组，均为`kahypar status=success`。本轮只读复制，未重新运行实验。返回[整理结果](../partitioning.md)。

采集时远端checkout：`vivado2024.2` / `e924d0eabbc6a3a38b01339b00da55b25faf7a00`。该HEAD不同于[此前12组原始归档](partitioning-2026-10-27.md)的采集时HEAD；采集checkout不替代每次实验构建版本及未提交改动的核对。两次HEAD之间`transform/src/partition/report.cc`与`statistics.cc`无提交差异，且本轮重新读取了统计实现；不能据此推断其余变换代码、资源估计和输入配置均未变化。

原始summary中的命令仍使用`-e 0.1 --seed 0 -o km1 -m direct -w true`及相同路径的KaHyPar配置文件。详细统计口径及标量负载派生值见汇总；求解成功不等于相应板数已通过运行验证，也不更新Linux进入CLI的状态。

以下校验值对应代码块内的原始文件内容，包括末尾换行，不包含Markdown围栏或路径说明。

## 文件校验值

| 实验目录 | SHA-256 |
| --- | --- |
| kmh_part2 | `9cda14f0e02c9d85186635f58cdbd491caa92c424d2f948455b13babd97393ab` |
| kmh_part3 | `c44a9d0b0c91a91620facd205ea26427ad4bbec4c7910c71d4e595ac04bc5deb` |
| kmh_part4 | `aa229dd4cacb5e8e991f00f0b297d559d1a9b1dee7cdac7d8fd6d4b205a63d57` |

## kmh_part2

远端路径：`/home/huguanghui/remu/examples/build/kmh_part2/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/kmh_part2/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 2 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=9620 hyperedges=18149
[partition] solver_wall_ms=611.22587599999997
[partition] part=0 vertices=8793 total_weight=2521969 cell_weight=2521967 port_weight=2
[partition] part=1 vertices=827 total_weight=3054737 cell_weight=3054737 port_weight=0
[partition] cut_edges=414 cut_size=7615 km1=7615
[partition] max_path_cuts=3 boundary_ppd=4 required_stages=4
[partition] critical_boundary_path=see_ppd_report
```

## kmh_part3

远端路径：`/home/huguanghui/remu/examples/build/kmh_part3/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/kmh_part3/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 3 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=35101 hyperedges=46834
[partition] solver_wall_ms=3633.1936099999998
[partition] part=0 vertices=9848 total_weight=2027266 cell_weight=2027264 port_weight=2
[partition] part=1 vertices=13988 total_weight=1541417 cell_weight=1541417 port_weight=0
[partition] part=2 vertices=11265 total_weight=2008071 cell_weight=2008071 port_weight=0
[partition] cut_edges=1618 cut_size=15980 km1=15993
[partition] max_path_cuts=3 boundary_ppd=4 required_stages=4
[partition] critical_boundary_path=see_ppd_report
```

## kmh_part4

远端路径：`/home/huguanghui/remu/examples/build/kmh_part4/partition/summary.txt`。

```text
[partition] summary_version=1 scope=solver_input_hypergraph
[partition] solver=kahypar status=success
[partition] command="cd /home/huguanghui/remu/examples/build/kmh_part4/partition && KaHyPar -h inputs.hgr -f inputs.fix -k 4 -e 0.1 --seed 0 -o km1 -m direct -w true -p /home/huguanghui/remu/transform/resources/km1_kKaHyPar_sea20.ini --quiet=1 "
[partition] vertices=35670 hyperedges=47502
[partition] solver_wall_ms=5543.6536980000001
[partition] part=0 vertices=1581 total_weight=1020719 cell_weight=1020717 port_weight=2
[partition] part=1 vertices=4292 total_weight=1533595 cell_weight=1533595 port_weight=0
[partition] part=2 vertices=20308 total_weight=1514652 cell_weight=1514652 port_weight=0
[partition] part=3 vertices=9489 total_weight=1507756 cell_weight=1507756 port_weight=0
[partition] cut_edges=2008 cut_size=18879 km1=19135
[partition] max_path_cuts=5 boundary_ppd=6 required_stages=6
[partition] critical_boundary_path=see_ppd_report
```
