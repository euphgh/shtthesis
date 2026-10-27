# FPGA板级性能日志原始摘录：2026-10-27

原始输入：[perf.txt](perf.txt)，由作者从remu-driver日志使用grep摘录。该文本不是完整运行日志，行首数字为原始日志行号。数据覆盖PicoRV32和KMH，计时与单位解释见[性能整理](../board-performance.md)。

原始文本SHA-256：`52e1c3bf624bb27da1fa84ae154805d4c293e0ed18bed48f7a652a386751a26f`。以下代码块逐字保留原始58行文本（含空行和末尾换行）；校验值对应代码块内部，不包含Markdown围栏。本轮未修改原始`perf.txt`、未重新采集或运行实验。

```text
picorv32:
79:[2026-10-27 08:28:37.372086 UTC] [debug] [perf] load memory elapsed_s=0.0133662 status=completed bytes=98304 payload_bytes=98304
420:[2026-10-27 08:28:37.377252 UTC] [debug] [perf] load design state elapsed_s=0.00514643 status=completed
421:[2026-10-27 08:28:37.377269 UTC] [debug] [perf] load checkpoint total elapsed_s=0.0189032 status=completed bytes=98304 payload_bytes=98304
464:[2026-10-27 08:28:40.388663 UTC] [debug] [perf] load memory elapsed_s=0.0198311 status=completed bytes=98304 payload_bytes=98304
641:[2026-10-27 08:28:40.394539 UTC] [debug] [perf] load design state elapsed_s=0.00583279 status=completed
642:[2026-10-27 08:28:40.394569 UTC] [debug] [perf] load checkpoint total elapsed_s=0.0268912 status=completed bytes=98304 payload_bytes=98304
686:[2026-10-27 08:28:49.497490 UTC] [debug] [perf] run emulation elapsed_s=0.00210355 status=completed cycles=64 rate_mhz=0.0304248
825:[2026-10-27 08:28:58.460248 UTC] [debug] [perf] run emulation elapsed_s=0.00776128 status=completed cycles=1984 rate_mhz=0.255628
957:[2026-10-27 08:29:00.044904 UTC] [debug] [perf] save design state elapsed_s=0.00736113 status=completed
976:[2026-10-27 08:29:00.119548 UTC] [debug] [perf] save memory elapsed_s=0.0745898 status=completed bytes=102400 payload_bytes=98304
977:[2026-10-27 08:29:00.120909 UTC] [debug] [perf] save checkpoint total elapsed_s=0.0840378 status=completed bytes=102400 payload_bytes=98304
92375:[2026-10-27 08:29:03.447212 UTC] [debug] [perf] run emulation elapsed_s=1.43391 status=completed cycles=469496 rate_mhz=0.327423
92507:[2026-10-27 08:29:10.085743 UTC] [debug] [perf] save design state elapsed_s=0.00737647 status=completed
92526:[2026-10-27 08:29:10.160412 UTC] [debug] [perf] save memory elapsed_s=0.0746148 status=completed bytes=102400 payload_bytes=98304
92527:[2026-10-27 08:29:10.161533 UTC] [debug] [perf] save checkpoint total elapsed_s=0.0837636 status=completed bytes=102400 payload_bytes=98304
683329:[2026-10-27 08:29:20.621604 UTC] [debug] [perf] run emulation elapsed_s=9.11789 status=completed cycles=2979192 rate_mhz=0.326741

92361:[2026-10-27 08:29:03.446968 UTC] [debug] [controller] synchronized pause completed tick=471544 parts=2 elapsed_ms=0.925013
114645:[2026-10-27 08:29:11.866917 UTC] [debug] [controller] synchronized pause completed tick=590182 parts=2 elapsed_ms=0.815245
119614:[2026-10-27 08:29:11.943397 UTC] [debug] [controller] synchronized pause completed tick=614782 parts=2 elapsed_ms=0.892565
130853:[2026-10-27 08:29:12.116385 UTC] [debug] [controller] synchronized pause completed tick=671064 parts=2 elapsed_ms=0.805101
140940:[2026-10-27 08:29:12.271977 UTC] [debug] [controller] synchronized pause completed tick=721603 parts=2 elapsed_ms=0.816228
150799:[2026-10-27 08:29:12.424552 UTC] [debug] [controller] synchronized pause completed tick=771173 parts=2 elapsed_ms=0.840611
160742:[2026-10-27 08:29:12.578233 UTC] [debug] [controller] synchronized pause completed tick=821099 parts=2 elapsed_ms=0.881133
177009:[2026-10-27 08:29:12.828537 UTC] [debug] [controller] synchronized pause completed tick=902714 parts=2 elapsed_ms=0.815051
184390:[2026-10-27 08:29:12.942776 UTC] [debug] [controller] synchronized pause completed tick=939706 parts=2 elapsed_ms=0.84804
193025:[2026-10-27 08:29:13.076272 UTC] [debug] [controller] synchronized pause completed tick=983015 parts=2 elapsed_ms=0.822549
200496:[2026-10-27 08:29:13.192026 UTC] [debug] [controller] synchronized pause completed tick=1020528 parts=2 elapsed_ms=0.813268
206749:[2026-10-27 08:29:13.288212 UTC] [debug] [controller] synchronized pause completed tick=1051613 parts=2 elapsed_ms=0.814178
216866:[2026-10-27 08:29:13.444036 UTC] [debug] [controller] synchronized pause completed tick=1102253 parts=2 elapsed_ms=0.812024
495690:[2026-10-27 08:29:17.735103 UTC] [debug] [controller] synchronized pause completed tick=2508540 parts=2 elapsed_ms=0.818873
502315:[2026-10-27 08:29:17.836715 UTC] [debug] [controller] synchronized pause completed tick=2541407 parts=2 elapsed_ms=0.813674
510242:[2026-10-27 08:29:17.958515 UTC] [debug] [controller] synchronized pause completed tick=2580904 parts=2 elapsed_ms=0.806736
519657:[2026-10-27 08:29:18.103407 UTC] [debug] [controller] synchronized pause completed tick=2627965 parts=2 elapsed_ms=0.805613
528874:[2026-10-27 08:29:18.244657 UTC] [debug] [controller] synchronized pause completed tick=2673814 parts=2 elapsed_ms=0.817001
539429:[2026-10-27 08:29:18.407381 UTC] [debug] [controller] synchronized pause completed tick=2726720 parts=2 elapsed_ms=0.813029
548538:[2026-10-27 08:29:18.547566 UTC] [debug] [controller] synchronized pause completed tick=2772239 parts=2 elapsed_ms=0.812975
552505:[2026-10-27 08:29:18.608533 UTC] [debug] [controller] synchronized pause completed tick=2791784 parts=2 elapsed_ms=0.803824
566870:[2026-10-27 08:29:18.829542 UTC] [debug] [controller] synchronized pause completed tick=2863791 parts=2 elapsed_ms=0.806946
683315:[2026-10-27 08:29:20.621367 UTC] [debug] [controller] synchronized pause completed tick=3450736 parts=2 elapsed_ms=0.806811


kmh:
154:[2026-10-27 09:00:18.442597 UTC] [debug] [perf] load memory elapsed_s=8.26399 status=completed bytes=2148638720 payload_bytes=2148638720
12467:[2026-10-27 09:00:18.626709 UTC] [debug] [perf] load design state elapsed_s=0.18409 status=completed
12468:[2026-10-27 09:00:18.626727 UTC] [debug] [perf] load checkpoint total elapsed_s=8.44846 status=completed bytes=2148638720 payload_bytes=2148638720
12586:[2026-10-27 09:00:55.012612 UTC] [debug] [perf] load memory elapsed_s=8.1737 status=completed bytes=2148638720 payload_bytes=2148638720
24859:[2026-10-27 09:00:55.196704 UTC] [debug] [perf] load design state elapsed_s=0.184071 status=completed
24860:[2026-10-27 09:00:55.196721 UTC] [debug] [perf] load checkpoint total elapsed_s=8.35907 status=completed bytes=2148638720 payload_bytes=2148638720
24904:[2026-10-27 09:01:08.698633 UTC] [debug] [perf] run emulation elapsed_s=0.00209189 status=completed cycles=64 rate_mhz=0.0305944
25163:[2026-10-27 09:01:14.876779 UTC] [debug] [perf] run emulation elapsed_s=0.0143843 status=completed cycles=4032 rate_mhz=0.280305
234569:[2026-10-27 09:01:23.742971 UTC] [debug] [perf] run emulation elapsed_s=3.40238 status=completed cycles=1095817 rate_mhz=0.322073
245493:[2026-10-27 09:01:25.873846 UTC] [debug] [perf] save design state elapsed_s=0.185341 status=completed
245587:[2026-10-27 09:02:45.818606 UTC] [debug] [perf] save memory elapsed_s=79.9447 status=completed bytes=2149613568 payload_bytes=2148638720
245588:[2026-10-27 09:02:45.823441 UTC] [debug] [perf] save checkpoint total elapsed_s=80.1357 status=completed bytes=2149613568 payload_bytes=2148638720

234555:[2026-10-27 09:01:23.742713 UTC] [debug] [controller] synchronized pause completed tick=1099913 parts=2 elapsed_ms=1.04744
```
