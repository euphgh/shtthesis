# 扫描状态参数原始摘录：2026-10-27

来源：`serve41:/home/huguanghui/remu`，采集时间：`2026-10-27T13:08:57Z`（UTC）。采集时checkout：`vivado2024.2` / `e924d0eabbc6a3a38b01339b00da55b25faf7a00`。范围为15组配置、45个Part；只读检索生成RTL，没有重跑实验。返回[逐Part统计](../scan-state.md)。

每段代码块为定向`rg -n -B 1 -A 2`匹配结果：含`FF_COUNT`的命中行使用“行号:”，上下文使用“行号-”，并保留`MEM_COUNT`和`EmuScanCtrl`实例上下文。文件SHA-256由远端`sha256sum`计算，**对应完整EMU_SYSTEM_i.v，不是本地摘录代码块的哈希**；本次没有复制完整RTL，不能以本地摘录重算完整文件哈希。

采集模式：

```text
rg -n -B 1 -A 2 '^[[:space:]]*\.FF_COUNT[[:space:]]*\(' <EMU_SYSTEM_i.v>
sha256sum <EMU_SYSTEM_i.v>
```

同一源码生成路径的名称不代替具体构建版本核对。FF_COUNT和MEM_COUNT按源码定义均以bit计；下面保留原始64位十六进制字面值。

## picorv32_part2 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part2/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`33baf5aa6a6e8c7d3e7c6fb98cfb414ef256ca6b6ad9089b52501a24d5c8a3f6`。

```text
521-  EmuScanCtrl #(
522:    .FF_COUNT(64'h00000000000003a7),
523-    .MEM_COUNT(64'h0000000000034fe0)
524-  ) emu_scan_ctrl (
```

## picorv32_part2 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part2/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`df88f4de4860b03ada264f377339e4a044d656bbe111740e7149d8c23ee73e2f`。

```text
374-  EmuScanCtrl #(
375:    .FF_COUNT(64'h00000000000002bc),
376-    .MEM_COUNT(64'h0000000000000400)
377-  ) emu_scan_ctrl (
```

## picorv32_part3 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part3/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`f976ac9ce9e3555824a752d3a2bb4688e4652743725a976b43e757e332545133`。

```text
539-  EmuScanCtrl #(
540:    .FF_COUNT(64'h000000000000039b),
541-    .MEM_COUNT(64'h00000000000353e0)
542-  ) emu_scan_ctrl (
```

## picorv32_part3 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part3/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`19b75821cae42b045d89bb6355b573c6e5f57d54468bf2b72bc5e3b9c399b757`。

```text
382-  EmuScanCtrl #(
383:    .FF_COUNT(64'h00000000000000d9),
384-    .MEM_COUNT(64'h0000000000000000)
385-  ) emu_scan_ctrl (
```

## picorv32_part3 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part3/part2/EMU_SYSTEM_2.v`。

完整RTL SHA-256：`64e8c73efa29b246484a4ac973eea983655480bd6629d91b0db4233aba714a3e`。

```text
382-  EmuScanCtrl #(
383:    .FF_COUNT(64'h00000000000001ef),
384-    .MEM_COUNT(64'h0000000000000000)
385-  ) emu_scan_ctrl (
```

## picorv32_part4 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part4/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`2c83d29e685b66cd7da42e1b475e4e7cf7caff910440c151018dc7b23521c10d`。

```text
556-  EmuScanCtrl #(
557:    .FF_COUNT(64'h000000000000030b),
558-    .MEM_COUNT(64'h0000000000034fe0)
559-  ) emu_scan_ctrl (
```

## picorv32_part4 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part4/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`3e9d583cf54e2e7fc208cd93feb7313f288d6bf01c97db71af87a12de514dc13`。

```text
410-  EmuScanCtrl #(
411:    .FF_COUNT(64'h000000000000013e),
412-    .MEM_COUNT(64'h0000000000000400)
413-  ) emu_scan_ctrl (
```

## picorv32_part4 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part4/part2/EMU_SYSTEM_2.v`。

完整RTL SHA-256：`473937d51a2716ed759baeddbb883f7721d44dc35a1759e6aafb2e878b6360ff`。

```text
400-  EmuScanCtrl #(
401:    .FF_COUNT(64'h00000000000000cb),
402-    .MEM_COUNT(64'h0000000000000000)
403-  ) emu_scan_ctrl (
```

## picorv32_part4 / Part 3

远端路径：`/home/huguanghui/remu/examples/build/picorv32_part4/part3/EMU_SYSTEM_3.v`。

完整RTL SHA-256：`9d616bb35b236e0f1f2b9fefaca213abf70c112880b20d6248cccf8766ae4ea9`。

```text
399-  EmuScanCtrl #(
400:    .FF_COUNT(64'h000000000000014f),
401-    .MEM_COUNT(64'h0000000000000000)
402-  ) emu_scan_ctrl (
```

## rocket_part2 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/rocket_part2/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`012ab795632146c17be66fb1dd90bdb21adbfb7bdeaf2892d15c8ddf6e7562e9`。

```text
521-  EmuScanCtrl #(
522:    .FF_COUNT(64'h00000000000019a4),
523-    .MEM_COUNT(64'h000000000006816e)
524-  ) emu_scan_ctrl (
```

## rocket_part2 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/rocket_part2/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`bcd5d142db2f47198fc5f503e918b33b7745d589d509159db1ec1c00af792144`。

```text
349-  EmuScanCtrl #(
350:    .FF_COUNT(64'h0000000000003919),
351-    .MEM_COUNT(64'h0000000000043ce0)
352-  ) emu_scan_ctrl (
```

## rocket_part3 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/rocket_part3/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`48511dd4e453e7b8eb49e25f8027d6bb7c336fc02f45cf3c9ca196b7c256d7b9`。

```text
538-  EmuScanCtrl #(
539:    .FF_COUNT(64'h000000000000158d),
540-    .MEM_COUNT(64'h000000000006816e)
541-  ) emu_scan_ctrl (
```

## rocket_part3 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/rocket_part3/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`a29885e55a27c2339bf7ed89321127c3b56e9ab8771f5d32fdf55dc200c222c4`。

```text
392-  EmuScanCtrl #(
393:    .FF_COUNT(64'h000000000000205f),
394-    .MEM_COUNT(64'h0000000000042d00)
395-  ) emu_scan_ctrl (
```

## rocket_part3 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/rocket_part3/part2/EMU_SYSTEM_2.v`。

完整RTL SHA-256：`af870b70808dc48eaeeee61f3953d3879db11eff4c7ef7370be5e12d1eb8e022`。

```text
366-  EmuScanCtrl #(
367:    .FF_COUNT(64'h0000000000001ca6),
368-    .MEM_COUNT(64'h0000000000000fe0)
369-  ) emu_scan_ctrl (
```

## rocket_part4 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/rocket_part4/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`f0a0a11d02fab10f3550eb2aec463a6464b7d9a66d591ab45ec2d9327cb40337`。

```text
557-  EmuScanCtrl #(
558:    .FF_COUNT(64'h0000000000002762),
559-    .MEM_COUNT(64'h000000000008986e)
560-  ) emu_scan_ctrl (
```

## rocket_part4 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/rocket_part4/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`ca67e1cf7cc501313192274d13f5505ff06d7efe2872cbece77edd39ade9d343`。

```text
383-  EmuScanCtrl #(
384:    .FF_COUNT(64'h000000000000107e),
385-    .MEM_COUNT(64'h0000000000000820)
386-  ) emu_scan_ctrl (
```

## rocket_part4 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/rocket_part4/part2/EMU_SYSTEM_2.v`。

完整RTL SHA-256：`341f2d835574b5e4f69e4591eef34ae53064a215e0eefedfb08ad4962c5d5d6c`。

```text
383-  EmuScanCtrl #(
384:    .FF_COUNT(64'h0000000000001a52),
385-    .MEM_COUNT(64'h0000000000021dc0)
386-  ) emu_scan_ctrl (
```

## rocket_part4 / Part 3

远端路径：`/home/huguanghui/remu/examples/build/rocket_part4/part3/EMU_SYSTEM_3.v`。

完整RTL SHA-256：`ca21a9ea5062c97ccf1295aa2023bd47cceb1148baeda7f07323b91e6fed84c2`。

```text
371-  EmuScanCtrl #(
372:    .FF_COUNT(64'h0000000000000000),
373-    .MEM_COUNT(64'h0000000000000000)
374-  ) emu_scan_ctrl (
```

## xs-minimal_part2 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part2/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`c0401316b66349a5cf3cf0f87c4b729b997109612bebcc1dfb9e4946f74d648f`。

```text
521-  EmuScanCtrl #(
522:    .FF_COUNT(64'h000000000004309b),
523-    .MEM_COUNT(64'h0000000000747ecd)
524-  ) emu_scan_ctrl (
```

## xs-minimal_part2 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part2/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`cd70c53e4d2f7a3502e54389dfc519f7ab8e6d3b6419a4540099966a4cb86fd3`。

```text
374-  EmuScanCtrl #(
375:    .FF_COUNT(64'h0000000000018460),
376-    .MEM_COUNT(64'h0000000000000080)
377-  ) emu_scan_ctrl (
```

## xs-minimal_part3 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part3/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`293f2145dd7c2b5db5c4654979fdfd793b4fbbab0dc0f30049e6759ee61d3e69`。

```text
539-  EmuScanCtrl #(
540:    .FF_COUNT(64'h000000000002ac7c),
541-    .MEM_COUNT(64'h00000000006a3853)
542-  ) emu_scan_ctrl (
```

## xs-minimal_part3 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part3/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`f6b29def0cec0715a36915db56281d11af79cd5fc07c1bcc25a52900bf37b31a`。

```text
392-  EmuScanCtrl #(
393:    .FF_COUNT(64'h000000000001c563),
394-    .MEM_COUNT(64'h00000000000a467a)
395-  ) emu_scan_ctrl (
```

## xs-minimal_part3 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part3/part2/EMU_SYSTEM_2.v`。

完整RTL SHA-256：`297d3bd06de85317b194a48aebd6f3c3eee046bc55023bf92151507e13227943`。

```text
392-  EmuScanCtrl #(
393:    .FF_COUNT(64'h0000000000014317),
394-    .MEM_COUNT(64'h0000000000000080)
395-  ) emu_scan_ctrl (
```

## xs-minimal_part4 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part4/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`4041a005c01b939778cd7e18722d3449dda22918b1bbe75574ac089f95e0032b`。

```text
556-  EmuScanCtrl #(
557:    .FF_COUNT(64'h000000000001eaa1),
558-    .MEM_COUNT(64'h000000000065e385)
559-  ) emu_scan_ctrl (
```

## xs-minimal_part4 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part4/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`e1a82411f520096b5cc2409e8e98965e32bc77a33fd3f7f9a70e2d5696e91c6b`。

```text
410-  EmuScanCtrl #(
411:    .FF_COUNT(64'h0000000000019830),
412-    .MEM_COUNT(64'h0000000000049080)
413-  ) emu_scan_ctrl (
```

## xs-minimal_part4 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part4/part2/EMU_SYSTEM_2.v`。

完整RTL SHA-256：`549cfa701cec52cd84329013043f1c2e70290a6c3ffd97243d12c387625ace52`。

```text
399-  EmuScanCtrl #(
400:    .FF_COUNT(64'h000000000000b156),
401-    .MEM_COUNT(64'h0000000000000000)
402-  ) emu_scan_ctrl (
```

## xs-minimal_part4 / Part 3

远端路径：`/home/huguanghui/remu/examples/build/xs-minimal_part4/part3/EMU_SYSTEM_3.v`。

完整RTL SHA-256：`0c2d40478e8ab9dfc6bb70f922d10e90f828d3ed26ee4a86701df25653ffb6fd`。

```text
410-  EmuScanCtrl #(
411:    .FF_COUNT(64'h00000000000180cf),
412-    .MEM_COUNT(64'h00000000000a0b48)
413-  ) emu_scan_ctrl (
```

## nanhu-g_part2 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part2/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`524130f579b01a9a6819323c3ef22d83556fdc31e6fcc33dfa27c59350f455fe`。

```text
521-  EmuScanCtrl #(
522:    .FF_COUNT(64'h00000000000703ed),
523-    .MEM_COUNT(64'h000000000119bf5a)
524-  ) emu_scan_ctrl (
```

## nanhu-g_part2 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part2/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`9566281234c55c99efff0308d9cad19113555200ac541504a73f46117f055619`。

```text
374-  EmuScanCtrl #(
375:    .FF_COUNT(64'h0000000000034abc),
376-    .MEM_COUNT(64'h000000000004a400)
377-  ) emu_scan_ctrl (
```

## nanhu-g_part3 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part3/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`7a41174904d36bc6af11507a22683cd6147855a144ccb27197bf39776175b7d6`。

```text
539-  EmuScanCtrl #(
540:    .FF_COUNT(64'h0000000000038636),
541-    .MEM_COUNT(64'h0000000000edc4c4)
542-  ) emu_scan_ctrl (
```

## nanhu-g_part3 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part3/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`4260e5189237631d3e3028772c3d63f739c49ca9f9ad179219942a6bdd186698`。

```text
392-  EmuScanCtrl #(
393:    .FF_COUNT(64'h000000000002c045),
394-    .MEM_COUNT(64'h000000000004a400)
395-  ) emu_scan_ctrl (
```

## nanhu-g_part3 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part3/part2/EMU_SYSTEM_2.v`。

完整RTL SHA-256：`513975a69c9c868525adb8b784e7cdb124f86fb16255a8971371c754e428e5b2`。

```text
392-  EmuScanCtrl #(
393:    .FF_COUNT(64'h0000000000040829),
394-    .MEM_COUNT(64'h00000000002bfa96)
395-  ) emu_scan_ctrl (
```

## nanhu-g_part4 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part4/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`01c7dec382bbb69cf5c85711dd934dacaec1c953b422d9a57323867c41250d12`。

```text
554-  EmuScanCtrl #(
555:    .FF_COUNT(64'h0000000000035870),
556-    .MEM_COUNT(64'h0000000000edc4c4)
557-  ) emu_scan_ctrl (
```

## nanhu-g_part4 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part4/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`69e8432ec63e90ffd718bafd4138fca3417d3123761c0edd2c590c0a33e2a4be`。

```text
410-  EmuScanCtrl #(
411:    .FF_COUNT(64'h000000000003a504),
412-    .MEM_COUNT(64'h00000000002bfa96)
413-  ) emu_scan_ctrl (
```

## nanhu-g_part4 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part4/part2/EMU_SYSTEM_2.v`。

完整RTL SHA-256：`1f7a37ec0b800e4dc60e648029a7e0ace1e248fd7f85834b787678bfcc93c37e`。

```text
408-  EmuScanCtrl #(
409:    .FF_COUNT(64'h000000000001db4d),
410-    .MEM_COUNT(64'h000000000004a280)
411-  ) emu_scan_ctrl (
```

## nanhu-g_part4 / Part 3

远端路径：`/home/huguanghui/remu/examples/build/nanhu-g_part4/part3/EMU_SYSTEM_3.v`。

完整RTL SHA-256：`01d915326a10cfdfef3fb7c5115e41e599493fcb8939e6f2616aa5bcf5b957e8`。

```text
409-  EmuScanCtrl #(
410:    .FF_COUNT(64'h00000000000175e1),
411-    .MEM_COUNT(64'h0000000000000180)
412-  ) emu_scan_ctrl (
```

## kmh_part2 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/kmh_part2/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`87cb1effcb8133ceeb1d4c127843fc30c9d89079af8cfadac6c4db1f944dfbe2`。

```text
521-  EmuScanCtrl #(
522:    .FF_COUNT(64'h00000000000669a0),
523-    .MEM_COUNT(64'h000000000082f89c)
524-  ) emu_scan_ctrl (
```

## kmh_part2 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/kmh_part2/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`999035161babad230b05b231c213a6ae28684ed1a83a430b66f7b63792cf8686`。

```text
364-  EmuScanCtrl #(
365:    .FF_COUNT(64'h0000000000030a40),
366-    .MEM_COUNT(64'h0000000000000000)
367-  ) emu_scan_ctrl (
```

## kmh_part3 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/kmh_part3/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`88008c3b7b036f960964e758ecce216c40f45d89301c9517413e5404b679ae84`。

```text
539-  EmuScanCtrl #(
540:    .FF_COUNT(64'h0000000000058f86),
541-    .MEM_COUNT(64'h0000000000829fc4)
542-  ) emu_scan_ctrl (
```

## kmh_part3 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/kmh_part3/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`b4d09e18f061e8f9ffcc6fe676e31c809f862e705c29dd7d84247ffd4ecb5e09`。

```text
392-  EmuScanCtrl #(
393:    .FF_COUNT(64'h000000000001a251),
394-    .MEM_COUNT(64'h00000000000058d8)
395-  ) emu_scan_ctrl (
```

## kmh_part3 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/kmh_part3/part2/EMU_SYSTEM_2.v`。

完整RTL SHA-256：`eab0d4aae950dacf01c3bb65561f9af2c2aac75a0349c813c31f9c9258b6aec6`。

```text
382-  EmuScanCtrl #(
383:    .FF_COUNT(64'h0000000000024207),
384-    .MEM_COUNT(64'h0000000000000000)
385-  ) emu_scan_ctrl (
```

## kmh_part4 / Part 0

远端路径：`/home/huguanghui/remu/examples/build/kmh_part4/part0/EMU_SYSTEM_0.v`。

完整RTL SHA-256：`71c81568cd9bd8cabdef3cccd11a3e9b4d6e17bce92141a2cb2ffe04570cadef`。

```text
557-  EmuScanCtrl #(
558:    .FF_COUNT(64'h00000000000370d7),
559-    .MEM_COUNT(64'h00000000007cc7c4)
560-  ) emu_scan_ctrl (
```

## kmh_part4 / Part 1

远端路径：`/home/huguanghui/remu/examples/build/kmh_part4/part1/EMU_SYSTEM_1.v`。

完整RTL SHA-256：`b93f23130889b29eca908085785f3330fc0203616833fe5ebc4c31709462d4e1`。

```text
400-  EmuScanCtrl #(
401:    .FF_COUNT(64'h000000000001e270),
402-    .MEM_COUNT(64'h0000000000000000)
403-  ) emu_scan_ctrl (
```

## kmh_part4 / Part 2

远端路径：`/home/huguanghui/remu/examples/build/kmh_part4/part2/EMU_SYSTEM_2.v`。

完整RTL SHA-256：`0d4c74ba5bc5085dd0bfbb0ff79772c5e547c64c9a00422993354324379b11f3`。

```text
410-  EmuScanCtrl #(
411:    .FF_COUNT(64'h0000000000030468),
412-    .MEM_COUNT(64'h00000000000630d8)
413-  ) emu_scan_ctrl (
```

## kmh_part4 / Part 3

远端路径：`/home/huguanghui/remu/examples/build/kmh_part4/part3/EMU_SYSTEM_3.v`。

完整RTL SHA-256：`91094691bf9fce10d5e0bf6d6770bcb5e0312c7a456aed1e796a2b85e96b3c5c`。

```text
400-  EmuScanCtrl #(
401:    .FF_COUNT(64'h0000000000011c0e),
402-    .MEM_COUNT(64'h0000000000000000)
403-  ) emu_scan_ctrl (
```
