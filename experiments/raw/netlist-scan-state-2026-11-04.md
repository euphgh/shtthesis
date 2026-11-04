# 网表划分RTL扫描状态参数原始摘录：2026-11-04

来源：`serve41:/home/huguanghui/remu`，采集时间：`2026-11-04T04:18:18Z`（UTC）。采集时checkout：`vivado2024.2` / `828600a0f8bbf2a93040156aafff1ddbb218d504`。范围为15组配置、45个Part；只读检索生成RTL，没有重跑实验。返回[逐Part统计](../netlist-scan-state.md)。

本批对应**基于网表划分**之后的RTL，与[2026-10-27自适应划分批次](scan-state-2026-10-27.md)的目录名相同但构建不同，两组数值不可混用。

每段代码块为定向`rg -n -B 1 -A 2`匹配结果：含`FF_COUNT`的命中行使用“行号:”，上下文使用“行号-”，保留`MEM_COUNT`和`EmuScanCtrl`实例上下文。文件SHA-256由远端`sha256sum`计算，**对应完整EMU_SYSTEM_i.v，不是本地摘录代码块的哈希**；本次没有复制完整RTL，不能以本地摘录重算完整文件哈希。

采集模式：

```text
rg -n -B 1 -A 2 '^[[:space:]]*\.FF_COUNT[[:space:]]*\(' <EMU_SYSTEM_i.v>
sha256sum <EMU_SYSTEM_i.v>
```

同一源码生成路径的名称不代替具体构建版本核对。FF_COUNT和MEM_COUNT按源码定义均以bit计；下面保留原始64位十六进制字面值。

## picorv32_part2 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part2/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-11-03 14:58:07 CST`。

完整RTL SHA-256：`b4effc3c7f241996dc3d13e48eba2d82e897ac8915daf2332bb78efad844db75`。

```text
512-  EmuScanCtrl #(
513:    .FF_COUNT(64'h00000000000003a2),
514-    .MEM_COUNT(64'h0000000000034fe0)
515-  ) emu_scan_ctrl (
```

## picorv32_part2 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part2/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-11-03 14:58:08 CST`。

完整RTL SHA-256：`1ba0c37360fdaf8030f8951f87c91fc24050af295402f0f2deacc02f0ddb2b1f`。

```text
364-  EmuScanCtrl #(
365:    .FF_COUNT(64'h00000000000002c1),
366-    .MEM_COUNT(64'h0000000000000400)
367-  ) emu_scan_ctrl (
```

## picorv32_part3 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part3/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-28 20:19:21 CST`。

完整RTL SHA-256：`cbf53069bc64082df5ab8e17bb377b11368400e7595f1c322117d85f55319d4f`。

```text
539-  EmuScanCtrl #(
540:    .FF_COUNT(64'h00000000000003ff),
541-    .MEM_COUNT(64'h00000000000353e0)
542-  ) emu_scan_ctrl (
```

## picorv32_part3 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part3/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-28 20:19:21 CST`。

完整RTL SHA-256：`4daf9b79df080f88fa507df27675cfd4fb1a977a9e6de915a1fc84cf2532cd59`。

```text
382-  EmuScanCtrl #(
383:    .FF_COUNT(64'h00000000000000f5),
384-    .MEM_COUNT(64'h0000000000000000)
385-  ) emu_scan_ctrl (
```

## picorv32_part3 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part3/part2/EMU_SYSTEM_2.v`。

远端mtime：`2026-10-28 20:19:21 CST`。

完整RTL SHA-256：`32d28e3322c082331bfe1f52c1067397b5b7f76bf820bf96ceb3a6685274e520`。

```text
382-  EmuScanCtrl #(
383:    .FF_COUNT(64'h000000000000016f),
384-    .MEM_COUNT(64'h0000000000000000)
385-  ) emu_scan_ctrl (
```

## picorv32_part4 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part4/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-28 20:19:27 CST`。

完整RTL SHA-256：`bb539826031cf822a80998c327e04b7ff0192ef3fa3ac2f57506df9941dd1c57`。

```text
556-  EmuScanCtrl #(
557:    .FF_COUNT(64'h0000000000000310),
558-    .MEM_COUNT(64'h0000000000034fe0)
559-  ) emu_scan_ctrl (
```

## picorv32_part4 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part4/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-28 20:19:27 CST`。

完整RTL SHA-256：`c0e6ffce951ab3e6644ba95772e60e595bf97c1508ef1e5a5fab4292267322e5`。

```text
400-  EmuScanCtrl #(
401:    .FF_COUNT(64'h00000000000000cb),
402-    .MEM_COUNT(64'h0000000000000000)
403-  ) emu_scan_ctrl (
```

## picorv32_part4 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part4/part2/EMU_SYSTEM_2.v`。

远端mtime：`2026-10-28 20:19:28 CST`。

完整RTL SHA-256：`f76b861da7a8144063bca90ba39814851b62c80ef12f3c036477ec0de7be19b3`。

```text
410-  EmuScanCtrl #(
411:    .FF_COUNT(64'h0000000000000145),
412-    .MEM_COUNT(64'h0000000000000400)
413-  ) emu_scan_ctrl (
```

## picorv32_part4 / Part 3

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part4/part3/EMU_SYSTEM_3.v`。

远端mtime：`2026-10-28 20:19:28 CST`。

完整RTL SHA-256：`d54ecc73769c9503e7ab6747af749ad5906bd9109c1834b8a5d6dca0c262fc14`。

```text
399-  EmuScanCtrl #(
400:    .FF_COUNT(64'h0000000000000143),
401-    .MEM_COUNT(64'h0000000000000000)
402-  ) emu_scan_ctrl (
```

## rocket_part2 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/rocket_part2/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-28 20:22:01 CST`。

完整RTL SHA-256：`9a35a3355ddcf4d10c05ea2b2cd0d23233c29846561d5412a3b42190e55a9eb9`。

```text
521-  EmuScanCtrl #(
522:    .FF_COUNT(64'h00000000000018d0),
523-    .MEM_COUNT(64'h000000000006816e)
524-  ) emu_scan_ctrl (
```

## rocket_part2 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/rocket_part2/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-28 20:22:28 CST`。

完整RTL SHA-256：`084cebbce1459c6f1e5316c009195bdb9caf27f0e874e872c53a4c4a491d7502`。

```text
374-  EmuScanCtrl #(
375:    .FF_COUNT(64'h00000000000036e0),
376-    .MEM_COUNT(64'h0000000000043ce0)
377-  ) emu_scan_ctrl (
```

## rocket_part3 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/rocket_part3/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-28 20:21:42 CST`。

完整RTL SHA-256：`8875aeb7401336c5c167a183af8b8b7cc414b7255cd09ec43558886cb58ab4a6`。

```text
539-  EmuScanCtrl #(
540:    .FF_COUNT(64'h0000000000002192),
541-    .MEM_COUNT(64'h00000000000a898e)
542-  ) emu_scan_ctrl (
```

## rocket_part3 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/rocket_part3/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-28 20:21:46 CST`。

完整RTL SHA-256：`da5742c61cc2ab86aecc5533477172a9da148bd383304c3403008f27700c1cf4`。

```text
381-  EmuScanCtrl #(
382:    .FF_COUNT(64'h000000000000051e),
383-    .MEM_COUNT(64'h0000000000000000)
384-  ) emu_scan_ctrl (
```

## rocket_part3 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/rocket_part3/part2/EMU_SYSTEM_2.v`。

远端mtime：`2026-10-28 20:22:02 CST`。

完整RTL SHA-256：`1c3a235d2d4253d8f62203c3f58a536e00c222e5cec45ddfbe2d684c228d9288`。

```text
391-  EmuScanCtrl #(
392:    .FF_COUNT(64'h0000000000002900),
393-    .MEM_COUNT(64'h00000000000034c0)
394-  ) emu_scan_ctrl (
```

## rocket_part4 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/rocket_part4/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-28 20:22:03 CST`。

完整RTL SHA-256：`2c41a50caf1d3911d105a574e2e05cd7348c31a15d7fb676d22ae3f3f1539bfa`。

```text
557-  EmuScanCtrl #(
558:    .FF_COUNT(64'h00000000000016f9),
559-    .MEM_COUNT(64'h000000000006816e)
560-  ) emu_scan_ctrl (
```

## rocket_part4 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/rocket_part4/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-28 20:22:05 CST`。

完整RTL SHA-256：`a311a9dd9651c16f03ecfb59376ee6bf65fbe2d4b99866ec9aa4aa286d1f19b4`。

```text
371-  EmuScanCtrl #(
372:    .FF_COUNT(64'h0000000000000000),
373-    .MEM_COUNT(64'h0000000000000000)
374-  ) emu_scan_ctrl (
```

## rocket_part4 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/rocket_part4/part2/EMU_SYSTEM_2.v`。

远端mtime：`2026-10-28 20:22:16 CST`。

完整RTL SHA-256：`d3bc28a03d011117571bb4a2f5c872709b6df5decbcc29f197d615c6fc8aa9c0`。

```text
408-  EmuScanCtrl #(
409:    .FF_COUNT(64'h0000000000001ac7),
410-    .MEM_COUNT(64'h0000000000021dc0)
411-  ) emu_scan_ctrl (
```

## rocket_part4 / Part 3

远端路径：`/home/huguanghui/remu/examples/build/rocket_part4/part3/EMU_SYSTEM_3.v`。

远端mtime：`2026-10-28 20:22:29 CST`。

完整RTL SHA-256：`fc890ffbc5f7705840246ad6d2736adbe650abe6519fce136fb1df72b5959c9f`。

```text
408-  EmuScanCtrl #(
409:    .FF_COUNT(64'h0000000000001df0),
410-    .MEM_COUNT(64'h0000000000021f20)
411-  ) emu_scan_ctrl (
```

## xs-minimal_part2 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part2/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-29 09:29:33 CST`。

完整RTL SHA-256：`7352d0b0d94c507beb72ac30923b29ee42569cf64438e117964e6cf2fa7db86a`。

```text
521-  EmuScanCtrl #(
522:    .FF_COUNT(64'h000000000003a7ca),
523-    .MEM_COUNT(64'h00000000006c4165)
524-  ) emu_scan_ctrl (
```

## xs-minimal_part2 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part2/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-29 09:39:13 CST`。

完整RTL SHA-256：`05760cf4635253e3c6b6c4a6eeecd5a11dab0310a79c5f6db7936459c3b0ecfc`。

```text
374-  EmuScanCtrl #(
375:    .FF_COUNT(64'h000000000001c571),
376-    .MEM_COUNT(64'h000000000007f0c8)
377-  ) emu_scan_ctrl (
```

## xs-minimal_part3 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part3/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-29 06:39:10 CST`。

完整RTL SHA-256：`420e3ed7ae48a27d4125233b21ecb1be8e4ec8a47bf8aaa3662d8d30e842fd27`。

```text
539-  EmuScanCtrl #(
540:    .FF_COUNT(64'h000000000001f1cc),
541-    .MEM_COUNT(64'h00000000006d4b7b)
542-  ) emu_scan_ctrl (
```

## xs-minimal_part3 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part3/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-29 06:44:34 CST`。

完整RTL SHA-256：`ccdb1674ee8482948c72ecbecc80b42ab084e8e346433ae6cff102c0273c7b2f`。

```text
392-  EmuScanCtrl #(
393:    .FF_COUNT(64'h00000000000108be),
394-    .MEM_COUNT(64'h0000000000000080)
395-  ) emu_scan_ctrl (
```

## xs-minimal_part3 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part3/part2/EMU_SYSTEM_2.v`。

远端mtime：`2026-10-29 06:50:29 CST`。

完整RTL SHA-256：`ab32e935792d6f0208642edd4a85da80caf3aa863ba7d0325efbc8bf38df67ea`。

```text
392-  EmuScanCtrl #(
393:    .FF_COUNT(64'h00000000000272b1),
394-    .MEM_COUNT(64'h000000000006e632)
395-  ) emu_scan_ctrl (
```

## xs-minimal_part4 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part4/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-29 05:13:07 CST`。

完整RTL SHA-256：`8b6987fd66d5fe46e56217d235b994fa1c2399dcd34db5cec0d4acb29823e744`。

```text
557-  EmuScanCtrl #(
558:    .FF_COUNT(64'h000000000001a2d0),
559-    .MEM_COUNT(64'h0000000000655b33)
560-  ) emu_scan_ctrl (
```

## xs-minimal_part4 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part4/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-29 05:16:46 CST`。

完整RTL SHA-256：`81d5c9d7fcf606fef00e809e81d7526dd3a5ede05add8b23fe76a35bc8cb8109`。

```text
410-  EmuScanCtrl #(
411:    .FF_COUNT(64'h0000000000019e4b),
412-    .MEM_COUNT(64'h000000000004cb32)
413-  ) emu_scan_ctrl (
```

## xs-minimal_part4 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part4/part2/EMU_SYSTEM_2.v`。

远端mtime：`2026-10-29 05:22:30 CST`。

完整RTL SHA-256：`1141ec0199ba68b9920786d3395f87b6be4dbcc18df968d624b3585ee4913c0f`。

```text
410-  EmuScanCtrl #(
411:    .FF_COUNT(64'h0000000000016054),
412-    .MEM_COUNT(64'h00000000000a0b48)
413-  ) emu_scan_ctrl (
```

## xs-minimal_part4 / Part 3

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part4/part3/EMU_SYSTEM_3.v`。

远端mtime：`2026-10-29 05:27:08 CST`。

完整RTL SHA-256：`203a184ca1ce894bbe781ef7c94b36ed5318d44d17bc2c9f10fdfda7142b3128`。

```text
410-  EmuScanCtrl #(
411:    .FF_COUNT(64'h000000000000cbcc),
412-    .MEM_COUNT(64'h0000000000000080)
413-  ) emu_scan_ctrl (
```

## nanhu-g_part2 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part2/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-30 19:58:11 CST`。

完整RTL SHA-256：`ebe900bec35213e6aec6b704e6ae587960b8add489c8322208dd5b3a7ff8a226`。

```text
521-  EmuScanCtrl #(
522:    .FF_COUNT(64'h000000000005bf80),
523-    .MEM_COUNT(64'h0000000001171518)
524-  ) emu_scan_ctrl (
```

## nanhu-g_part2 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part2/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-30 20:18:19 CST`。

完整RTL SHA-256：`1dab3feb61a0069e4d3d00d7419545c3b570d4e344d9db04509737981fe5626b`。

```text
374-  EmuScanCtrl #(
375:    .FF_COUNT(64'h0000000000042501),
376-    .MEM_COUNT(64'h000000000006f932)
377-  ) emu_scan_ctrl (
```

## nanhu-g_part3 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part3/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-30 07:14:12 CST`。

完整RTL SHA-256：`1436a7afe704ab03cc70f57f6c6b67ef7a0d946dd51320e5a4c7cd829ce24ab0`。

```text
539-  EmuScanCtrl #(
540:    .FF_COUNT(64'h0000000000049130),
541-    .MEM_COUNT(64'h00000000011094e0)
542-  ) emu_scan_ctrl (
```

## nanhu-g_part3 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part3/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-30 07:27:38 CST`。

完整RTL SHA-256：`f133c98ec6057258d4e6a53002a870eaa26501fd3474db5b457a0bc5cd5d7501`。

```text
392-  EmuScanCtrl #(
393:    .FF_COUNT(64'h000000000002a4bb),
394-    .MEM_COUNT(64'h000000000008d62a)
395-  ) emu_scan_ctrl (
```

## nanhu-g_part3 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part3/part2/EMU_SYSTEM_2.v`。

远端mtime：`2026-10-30 07:38:57 CST`。

完整RTL SHA-256：`04efc324a72681f832abe2230614f58bc1e3d2a9305b666fe92180bbd4acb7c2`。

```text
392-  EmuScanCtrl #(
393:    .FF_COUNT(64'h000000000002ae8a),
394-    .MEM_COUNT(64'h000000000004a340)
395-  ) emu_scan_ctrl (
```

## nanhu-g_part4 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part4/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-30 02:50:20 CST`。

完整RTL SHA-256：`e8ce0458c523e689b7cb08cbdd645549a86f2f89e50717b870ae7a4a75241934`。

```text
557-  EmuScanCtrl #(
558:    .FF_COUNT(64'h0000000000034887),
559-    .MEM_COUNT(64'h0000000000ed7434)
560-  ) emu_scan_ctrl (
```

## nanhu-g_part4 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part4/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-30 02:58:30 CST`。

完整RTL SHA-256：`69cd7aa4c050c01590ca9b01dc1c2d537d4fffd526a409591b5c2751b0ca4840`。

```text
410-  EmuScanCtrl #(
411:    .FF_COUNT(64'h0000000000028304),
412-    .MEM_COUNT(64'h000000000029a0e4)
413-  ) emu_scan_ctrl (
```

## nanhu-g_part4 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part4/part2/EMU_SYSTEM_2.v`。

远端mtime：`2026-10-30 03:10:30 CST`。

完整RTL SHA-256：`1e8adc261baf5dbeb33e66593fac45cd726c51cea0501709db3a00fc7d653f60`。

```text
410-  EmuScanCtrl #(
411:    .FF_COUNT(64'h0000000000024927),
412-    .MEM_COUNT(64'h0000000000026932)
413-  ) emu_scan_ctrl (
```

## nanhu-g_part4 / Part 3

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part4/part3/EMU_SYSTEM_3.v`。

远端mtime：`2026-10-30 03:17:13 CST`。

完整RTL SHA-256：`212be564035648723e9ef0ad811d2a7ebd70bcda9bec3bb26a995babf2e56fe2`。

```text
410-  EmuScanCtrl #(
411:    .FF_COUNT(64'h000000000001cfcf),
412-    .MEM_COUNT(64'h0000000000049000)
413-  ) emu_scan_ctrl (
```

## kmh_part2 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/kmh_part2/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-31 19:30:20 CST`。

完整RTL SHA-256：`30ca3e659fe43c621753ff28d03ca2bbfcc42adfecf8cac8ac7f48940cb0ef5d`。

```text
521-  EmuScanCtrl #(
522:    .FF_COUNT(64'h0000000000047e7a),
523-    .MEM_COUNT(64'h00000000007d9f4c)
524-  ) emu_scan_ctrl (
```

## kmh_part2 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/kmh_part2/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-31 20:10:23 CST`。

完整RTL SHA-256：`d33bd280dcccc0239e0eca80c5cca03635754ccba37fb0a1579884c7cc0664d2`。

```text
374-  EmuScanCtrl #(
375:    .FF_COUNT(64'h000000000004d911),
376-    .MEM_COUNT(64'h0000000000055950)
377-  ) emu_scan_ctrl (
```

## kmh_part3 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/kmh_part3/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-31 02:54:01 CST`。

完整RTL SHA-256：`bc75ca654ab77da2a8d75a6fb68e8cf03b17688906e1181e848e4c1dac2b017c`。

```text
539-  EmuScanCtrl #(
540:    .FF_COUNT(64'h0000000000062102),
541-    .MEM_COUNT(64'h000000000082f89c)
542-  ) emu_scan_ctrl (
```

## kmh_part3 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/kmh_part3/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-31 02:55:22 CST`。

完整RTL SHA-256：`b1756193a6a511f6e5a4f5a885d0c9636240a9c42a9216c147fc181d8ed4ee2c`。

```text
382-  EmuScanCtrl #(
383:    .FF_COUNT(64'h0000000000013400),
384-    .MEM_COUNT(64'h0000000000000000)
385-  ) emu_scan_ctrl (
```

## kmh_part3 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/kmh_part3/part2/EMU_SYSTEM_2.v`。

远端mtime：`2026-10-31 02:58:32 CST`。

完整RTL SHA-256：`98f03b4829b3ff51433866793606e77c6d204e64111077ce91dbe98d230cbbf5`。

```text
382-  EmuScanCtrl #(
383:    .FF_COUNT(64'h0000000000020289),
384-    .MEM_COUNT(64'h0000000000000000)
385-  ) emu_scan_ctrl (
```

## kmh_part4 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/kmh_part4/part0/EMU_SYSTEM_0.v`。

远端mtime：`2026-10-30 21:26:20 CST`。

完整RTL SHA-256：`a1640721516fb57d623c04d8228ce258dc8ac2a15452b016a5f6d5ae68a4746f`。

```text
557-  EmuScanCtrl #(
558:    .FF_COUNT(64'h00000000000537ad),
559-    .MEM_COUNT(64'h00000000007f7524)
560-  ) emu_scan_ctrl (
```

## kmh_part4 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/kmh_part4/part1/EMU_SYSTEM_1.v`。

远端mtime：`2026-10-30 21:46:18 CST`。

完整RTL SHA-256：`2f0705feeae855380ff25d401a5564dd3822c5523c9d244e03e5e311c28ae3a8`。

```text
410-  EmuScanCtrl #(
411:    .FF_COUNT(64'h0000000000023ad0),
412-    .MEM_COUNT(64'h0000000000038378)
413-  ) emu_scan_ctrl (
```

## kmh_part4 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/kmh_part4/part2/EMU_SYSTEM_2.v`。

远端mtime：`2026-10-30 21:47:33 CST`。

完整RTL SHA-256：`7208d12dd6e82098fe302debe1514b9cb83cb77e3bf38e194c7e9c14ebeb181c`。

```text
400-  EmuScanCtrl #(
401:    .FF_COUNT(64'h00000000000109b0),
402-    .MEM_COUNT(64'h0000000000000000)
403-  ) emu_scan_ctrl (
```

## kmh_part4 / Part 3

远端路径：`/home/huguanghui/remu/examples/build/kmh_part4/part3/EMU_SYSTEM_3.v`。

远端mtime：`2026-10-30 21:48:54 CST`。

完整RTL SHA-256：`dfea26d6d7f5e730287359abf7e884b9ccfe80b72af647b4faba698a2555e08f`。

```text
400-  EmuScanCtrl #(
401:    .FF_COUNT(64'h000000000000db5e),
402-    .MEM_COUNT(64'h0000000000000000)
403-  ) emu_scan_ctrl (
```

