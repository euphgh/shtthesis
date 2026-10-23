# 1.5 可扩展的多FPGA运行控制与状态传输：详细大纲

## 本节论点与章节衔接

1.2说明如何协调各分区在同一DUT逻辑周期暂停，1.3说明如何组织局部扫描状态与全局检查点。本节解决这些操作在物理上如何到达各FPGA：Host如何访问未与其直连的分区，如何读取远端控制寄存器与状态内存，以及如何将电路划分结果连接到实际板间链路。

Fabric提供面向分区的统一访问与通信设施。Host通过参考节点Ref接入系统，使用目标Part和局部地址访问各节点；CSR、内存与DUT边界数据共享报文传输和路由设施。周期协调由1.2中的控制算法完成，全局检查点由1.3中的状态映射组织，两者通过Fabric访问远端资源。

## 工作梳理

| 工作方向 | 已有实现 | 本节解释的问题 |
| --- | --- | --- |
| 拓扑描述与绑定 | 物理拓扑、Shell端口映射、Part放置、逻辑边绑定及出口路由生成 | 逻辑分区如何连接到实际FPGA和物理端口 |
| 统一报文与路由 | FabricPacket、Router、DATA封装与重组 | 不同用途的通信如何共享板间链路 |
| 远端控制访问 | Ref/Part Initiator、AccessAgent、CSR frontend与target | Host如何访问各分区的控制器 |
| 远端内存访问 | GlobalMemoryFrontend、MemoryAccessTarget、请求与响应编码 | Host如何加载、收集和写回各分区数据 |
| Driver适配 | 面向Part的虚拟寄存器与内存对象，共享Ref transport | 如何保留上层控制与检查点操作方式 |
| 集成与验证环境 | 双Part Role、AXI VIP、DPI/IPC、组件与软件测试 | 如何逐层检查请求是否经过真实RTL路径 |

## 1.5.1 多FPGA管理需求与Fabric总体架构

### 从独立节点访问到统一入口

- 多FPGA运行需要访问各分区的运行控制寄存器、周期计数、扫描缓冲区及模型内存。
- 若每个节点都要求独立Host直连，系统扩展会增加主机接口与平台配置需求。采用一个Ref作为Host入口，使远端节点可以复用板间链路接收控制与状态访问请求。
- 以Host只直连FPGA A、需读取FPGA B周期计数和扫描数据为例，引出小数据控制访问与大块状态访问两类需求。

### Ref与普通节点的职责

- 每个FPGA承载一个Part，包含DUT、局部控制寄存器、内存及Fabric接入组件。
- Ref提供Host接入和全局管理窗口；普通节点通过Fabric接受远端访问。
- Initiator将访问请求转换为报文并匹配响应；Router负责排队、仲裁和目标投递；AccessAgent通过本地AXI接口执行CSR或内存操作。
- 本地与远端普通访问采用相同的请求—响应组织方式，本地请求经Router回环投递。Ref全局管理窗口由本地frontend单独处理。

### 不同用途的通信共享基础设施

- CSR用于运行控制和状态查询，memory用于程序、模型内存与扫描数据传输，DATA承载DUT跨分区边界数据。
- IRQ作为已有配套组件简述，不单独展开为本节主线。
- 功能上区分控制访问、状态传输与DUT通信，物理上可以共享FabricLink。

## 1.5.2 拓扑描述、分区绑定与统一通信

### 分离物理连接、板级接口和逻辑分区

- 物理拓扑描述FPGA身份、Host连接与板间端口连线；Shell映射描述物理端口在Role边界暴露的接口及方向。
- 电路划分产生Part集合和跨Part逻辑连接，Transform据此生成Part到FPGA的放置、逻辑连接到物理链路的绑定及出口路由。
- 区分DUT逻辑连接和物理连接：没有DUT DATA连接的节点之间，仍需要控制访问可达性。
- 当前采用全连接物理拓扑，一个FPGA一个Part，Part0放置于Host直连FPGA；其他Part按确定顺序放置。当前方法不涉及带宽感知放置优化或多跳路径搜索。

### 统一报文与端点适配

- 用源Part、目标Part、消息类型和事务标识描述访问，路由组件无需解释具体寄存器或状态数据含义。
- 当前FabricPacket为512位，包含128位头部与384位载荷；正文以概念结构说明为主，具体字段编码留在实现文档。
- DATA桥完成DUT流接口与Fabric报文之间的封装、分片和重组，并保持有效字节、消息边界及反压关系。
- Role/Shell负责位宽、时钟域和物理接口适配。统一流式边界为更换底层链路提供接口基础；Ethernet、跨服务器部署及任意拓扑不作为当前已验证能力。

### 路由、仲裁与反压

- 根据目标Part选择本地投递或物理出口，将请求、响应和DATA送往对应端点。
- 使用队列与valid/ready握手吸收暂时等待；报文在被接受前保持稳定，避免反压时被其他来源替换。
- 当前按memory、CSR、DATA、IRQ进行优先级仲裁，memory消息占用某输出后保持至消息结束，其他独立输出仍可推进。
- 此策略提供明确的实现次序，公平性、持续竞争和运行性能仍需实验分析，不提前声称无饥饿或最优吞吐。

## 1.5.3 面向运行控制与检查点的统一访问

### 面向Part的寄存器与内存视图

- 上层Driver继续使用各Part的寄存器与内存对象；Fabric后端将目标Part与局部偏移组合成全局地址，共享Ref传输入口。
- CSR和memory采用各自的地址布局与范围检查；Ref全局管理空间和Part0局部控制空间分别处理。
- 用读取Part1周期计数的完整路径解释：Driver定位Part→Ref编码请求→Router跨片转发→远端Agent访问控制寄存器→响应返回Driver。
- 请求成功以目标侧访问完成和响应返回为依据；错误和超时向软件传播。

### 高层运行命令与远端CSR访问

- Run、Step、Pause等操作由Driver组合控制寄存器访问完成；Fabric传递这些访问及其响应。
- 一致暂停仍采用1.2的接收屏障、稳定周期采样和共同目标周期，不依赖Host请求同时到达各节点。
- Fabric使相同的协调算法可以访问远端分区，本节引用1.2而不重复推导暂停协议。

### 分布式状态收集与写回

- Scan Dump先将各分区扫描数据写入本地FPGA内存；Host经Ref读取目标Part内存，交给1.3中的检查点保存与解码流程。
- 恢复时，Host按分区写回局部内存，再由已有扫描控制执行Scanin。Fabric负责数据可达与传输完成，状态映射和共同周期由前述机制保证。
- 以Part1扫描缓冲区为例说明收集和写回的双向路径，避免将状态汇聚误写成硬件自动归约或跨片串行扫描链。
- 大块传输在Driver侧按页边界拆分；RTL将内存请求转换为局部AXI访问。Role完成外部512位总线与内部256位memory接口适配。
- 中途失败可能留下部分写入，当前实现报告错误，不提供事务回滚或透明重试。

## 1.5.4 阶段性实现与验证范围

### 已有工程实现

- 拓扑读取与绑定、统一报文、Router、访问发起与执行组件、DATA桥、Driver Fabric后端均已有源码实现。
- 已建立双Part Role工程和双进程VCS验证环境；每个进程运行独立Role，Host仅连接Ref，请求经过VIP和实际Role RTL。
- DPI/IPC提供有界队列与链路数据交换，支持反压和会话管理。两进程独立推进本地时间，该环境用于功能验证，不直接提供物理板间延迟测量。

### 分层证据与功能验收

- 组件测试检查编码解码、目标访问、路由、分片重组、反压及错误处理；已有记录与本次实际重跑结果分别注明。
- 软件测试检查地址映射、共享传输和请求生命周期；软件mock通过不能代替远端RTL访问通过。
- Role工程创建和checker已有通过记录；它们证明工程结构及连接检查完成，不证明DUT已正常运行。
- 联合验收依次检查本地/远端CSR、不同Part内存写入回读、检查点加载与回读、DUT通信和程序输出，以及异常关闭。
- 截至当前进展记录，完整双PartVCS/Driver联合验收、自动Fabric接入生成及上板验收仍待完成；正文据后续实际结果更新。

### 扩展条件与后续评价

- 当前Transform要求全连接拓扑，Driver v1 profile最多支持Part0/1；参数化RTL和更宽Part字段不能直接证明多节点系统已验证。
- 自动Role接入生成、多节点/多跳、跨服务器和硬件部署作为后续工作。
- 后续测量CSR访问延迟、远端内存有效吞吐、状态收集时间、资源开销及DATA竞争影响，解释统一入口的收益与瓶颈。
- 明确区分Cosim功能结果、组件测量与真实板卡性能；系统级DUT实验集中在1.6。

## 图表安排

- 一张Fabric总体架构图：Host、Ref、普通Part及板间链路；标出Initiator、Router、Agent、DUT、局部内存，分别展示CSR、memory和DATA路径。
- 一张拓扑绑定图：物理连线与Shell映射、逻辑分区图共同形成placement、logical links及egress routes。图中采用当前双节点或全连接示例。
- 一张验证范围表：组件、软件、Role工程、联合功能、上板，逐项填写证据来源与当前状态。

## 写作取证索引

本大纲依据主仓库`thesis`分支当前源码及Fabric文档整理；论文子仓库为`main`。Fabric进展页标注的历史基线为`vivado2024.2`，其测试记录需保留原有时间与范围。本轮只读代码与文档，未运行功能测试。

| 论点 | 代码或文档入口（相对主仓库根目录） |
| --- | --- |
| 架构职责与本地/远端访问 | `docs/source/project-notes/fabric/specs/architecture.md` |
| 拓扑校验、放置和路由生成 | `transform/src/topo/topology.cc`、`transform/src/emu_and_part.cc` |
| topology模式Part接口 | `transform/src/partition/part_io_fifo.cc` |
| 报文定义与路由 | `fabric/common/rtl/FabricPkg.sv`、`fabric/components/fabric_router/rtl/FabricRouter.sv` |
| DATA封装与重组 | `fabric/components/axis_to_fabric_bridge/rtl/AxisToFabricBridge.sv`、`fabric/components/fabric_to_axis_bridge/rtl/FabricToAxisBridge.sv` |
| 请求发起与本地执行 | `fabric/components/fabric_access_initiator/rtl/RefFabricAccessInitiator.sv`、`fabric/components/fabric_access_agent/rtl/FabricAccessAgent.sv` |
| 全局内存访问 | `fabric/components/fabric_access_initiator/rtl/GlobalMemoryFrontend.sv`、`fabric/components/fabric_access_agent/rtl/MemoryAccessTarget.sv` |
| Driver地址与传输适配 | `driver/uma_fabric.cc`、`driver/uma_fabric.h` |
| 远端控制与检查点调用方 | `driver/controller.cc`、`driver/driver.cc` |
| Role集成 | `fpga/role/fpga/wrapper/fabric/`、`tests/fabric-integrate/fabric-role/` |
| 联合仿真边界 | `docs/source/project-notes/fabric/implementation/role-cosim.md`、`fpga/role/fpga/sources/simulation/tb_topology_remus_role_top.sv` |
| 历史结果、当前缺口与验收要求 | `docs/source/project-notes/fabric/status.md`、`docs/source/project-notes/fabric/specs/driver-cosim.md` |

## 与已有文稿的衔接调整

- 将原1.5.1中的Ethernet、跨服务器、多节点支持改为接口扩展方向，当前实现按全连接和双Part验证范围描述。
- 将“分发高层命令并保证一致边界”具体化为“远端CSR访问承载1.2的控制算法”。
- 将“完成状态传输验证”改为分层进展与联合验收状态，等待实际实验记录后填写结果。
- 详细大纲先独立保存；本轮不覆盖总大纲和TeX骨架，便于审阅章节安排。
