上海证券交易所
交易网关 STEP 接口规格说明书
（竞价平台）
V0.5 <span style="color:blue">7</span> <span style="color:red">6</span>
2023 年 <span style="color:blue">9</span> <span style="color:red">4</span> 月

交易网关数据接口规范
文档版本
日期
版本
说明
2021-04-15
0.10
创建文档。
2021-06-08
0.20
1. 更新业务范围描述
2. 增加指定、撤指定业务相关接口
3. 更新应用消息内各接口的部分字段约束说明
4. 更新竞价平台标识为 0
2021-07-05
0.30
1. 更新指定撤指定、网络密码服务的 SET 分区信息
2. 配股、配转债包含成交确认
3. 更新 ReportIndex 的 tag 值
2021-07-19
0.40
1. 更新“申报拒绝”的 MsgType
2. 更新“新订单申报”的字段描述
3. 更新“分区序号同步”的约束描述
2021-12-01
0.50
1. 更新“注册处理”和“网络密码服务”应用消息；
2. 更新“信用标签”的填写说明；
3. 新增错误码 5016 ；
4. 更新 OrdRejReason 的类型为 N5 ；
5. 更新“网络密码服务申报响应”消息；
6. 更新开放式基金分红设置取值；
7. 更新 BCAN 信息填写说明；
8. 更新结算会员代码填写说明；
9. 更新申报数量取值范围；
10. 更新网络密码服务申报 ValidationCode 填写说明；
11. 更新消息头的填写说明；
12. 更新订阅机制订阅数限制；
13. 更新 branchID 的填写说明；
14. 更新开放式基金转托管的填写说明；
15. 补充融资融券业务说明；
16. 补充“成交金额”的溢出场景说明；
2022-02-11
0.51
1. 补充“注册处理”消息流图；
2. 更新登录消息描述说明；
2022-03-04
0.52
1. 更新“成交金额”溢出场景的说明描述；
2022-06-17
0.53
1. 补充“ TrdCnfmID （成交编号）”的填写说明；
2023-01-04
0.54
1. 补充“现金选择权”业务的申报填写说明；
2. 删除“指定登记”、“指定撤销”业务的申报填写说
明；
2023-04-07
0.55
1. 修订新订单申报接口中“ Price ”、“ OrdType ”字段的填
写说明；
<span style="color:blue">2023-07-12</span>
<span style="color:blue">0.56</span>
<span style="color:blue">根据技术规划，要约（要约预受、要约撤销）</span> <span style="color:blue">/</span> <span style="color:blue">现金选择权、</span>
<span style="color:blue">开放式基金相关业务（申赎、分红选择、份额转出）、融</span>
2

交易网关数据接口规范
<span style="color:blue">资融券非交易业务（余券划转、还券划转、担保品划入、</span>
<span style="color:blue">担保品划出、券源划入、券源划出）、网络密码服务（密</span>
<span style="color:blue">码激活（注销）），将从竞价撮合平台迁移至互联网交易</span>
<span style="color:blue">平台。</span>
<span style="color:blue">1.</span>
<span style="color:blue">[删除] 删除相关申报填写说明，待迁移业务的申报说明，请</span>
<span style="color:blue">参见《</span> <span style="color:blue">IS122</span> <span style="color:blue">上海证券交易所交易网关</span> <span style="color:blue">STEP</span> <span style="color:blue">接口规格说</span>
<span style="color:blue">明书（互联网交易平台）</span> <span style="color:blue">1.13</span> <span style="color:blue">版（技术开发稿）》。</span>
<span style="color:blue">2.</span>
<span style="color:blue">[删除] 删除待下线业务的填写说明，包括开放式基金认购</span>
<span style="color:blue">（含货币市场基金实时申赎业务的认购）。</span>
<span style="color:blue">根据技术规划，要约（要约预受、要约撤销）</span> <span style="color:blue">/</span> <span style="color:blue">现金选择权、</span>
<span style="color:blue">开放式基金相关业务（申赎、分红选择、份额转出）、融</span>
<span style="color:blue">资融券非交易业务（余券划转、还券划转、担保品划入、</span>
<span style="color:blue">担保品划出、券源划入、券源划出）、网络密码服务（密</span>
<span style="color:blue">码激活（注销）），将从竞价撮合平台迁移至互联网交易</span>
<span style="color:blue">平台。</span>
<span style="color:blue">1.</span>
<span style="color:blue">[删除] 删除待迁移业务的填写说明，待迁移业务在互联网交</span>
<span style="color:blue">2023-09-26</span>
<span style="color:blue">0.57</span>
<span style="color:blue">易平台的填写说明，请参见《</span> <span style="color:blue">IS122</span> <span style="color:blue">上海证券交易所交易</span>
<span style="color:blue">网关</span> <span style="color:blue">STEP</span> <span style="color:blue">接口规格说明书（互联网交易平台）</span> <span style="color:blue">1.14</span> <span style="color:blue">版（竞</span>
<span style="color:blue">价非交易迁移互联网</span> <span style="color:blue">_</span> <span style="color:blue">技术开发稿）》。</span>
<span style="color:blue">2.</span>
<span style="color:blue">保留开放式基金相关业务和融资融券非交易业务的</span>
<span style="color:blue">业务字段（开放式基金转托管的目标方代理人、分红选择</span>
<span style="color:blue">方式、转入的标的产品代码），调整为预留字段，暂不启</span>
<span style="color:blue">用。</span>
3

交易网关数据接口规范
目录
第一章 前言 ................................................................................................................................... <span style="color:blue">6</span> 5
1.1 目的 ................................................................................................................................. <span style="color:blue">6</span> 5
1.2 术语和定义 ...................................................................................................................... <span style="color:blue">6</span> 5
1.3 参考文档 .......................................................................................................................... <span style="color:blue">6</span> 5
1.4 联系方式 .......................................................................................................................... <span style="color:blue">7</span> 6
第二章 系统简介 ........................................................................................................................... <span style="color:blue">8</span> 7
2.1 系统接入 ........................................................................................................................... <span style="color:blue">8</span> 7
2.2 业务范围 ........................................................................................................................... <span style="color:blue">8</span> 7
第三章 交互机制 ......................................................................................................................... <span style="color:blue">10</span> 9
3.1 会话机制 ......................................................................................................................... <span style="color:blue">10</span> 9
3.1.1 建立会话 .............................................................................................................. <span style="color:blue">10</span> 9
3.1.2 关闭会话 .............................................................................................................. <span style="color:blue">10</span> 9
3.1.3 维持会话 ............................................................................................................ <span style="color:blue">11</span> 10
3.1.4 其他约定 ............................................................................................................ <span style="color:blue">11</span> 10
3.2 申报与回报 ................................................................................................................... <span style="color:blue">11</span> 10
3.2.1 业务类型 ............................................................................................................ <span style="color:blue">12</span> 11
3.2.2 消息流图 ............................................................................................................ <span style="color:blue">15</span> 14
3.2.3 平台状态 ................................................................................................................ 18
3.2.4 重复订单 ............................................................................................................ <span style="color:blue">20</span> 19
3.2.5 执行报告 ................................................................................................................ 20
3.3 恢复场景 .......................................................................................................................... 22
3.4 订阅机制 ...................................................................................................................... <span style="color:blue">23</span> 22
第四章 消息定义 ........................................................................................................................... 24
4.1 消息结构与约定 ............................................................................................................... 24
4.1.1 数据类型 ............................................................................................................... 24
4.1.2 STEP 格式约定 ....................................................................................................... 25
4.1.3 STEP 消息头 ........................................................................................................... 25
4.1.4 STEP 消息尾 ........................................................................................................... 26
4.1.5 STEP 消息完整性 ................................................................................................... 26
4.2 会话消息 ........................................................................................................................... 26
4.2.1 登录消息（ MsgType=A ） .................................................................................... 26
4.2.2 注销消息（ MsgType=5 ） .................................................................................... 27
4.2.3 心跳消息（ MsgType=0 ） .................................................................................... 28
4.2.4 测试请求消息（ MsgType=1 ） ............................................................................ 28
4.2.5 重发请求消息（ MsgType=2 ） ............................................................................ 29
4.2.6 会话拒绝消息（ MsgType=3 ） ............................................................................ 29
4.2.7 序号重设消息（ MsgType=4 ） ............................................................................ 29
4.3 应用消息 - 新订单 ............................................................................................................. 30
4.3.1 新订单申报 New Order Single .............................................................................. 30
4.3.2 撤单申报 Order Cancel .......................................................................................... 35
4.3.3 执行报告 Execution Report ................................................................................... 36
4.3.3.1 申报响应、成交回报及撤单成功响应 ............................................................. 36
4.3.3.2 撤单失败执行报告 ......................................................................................... <span style="color:blue">39</span> 38
4

交易网关数据接口规范
4.4 应用消息 - 网络密码服务 ............................................................................................. <span style="color:blue">40</span> 39
4.4.1 网络密码服务申报 ............................................................................................ <span style="color:blue">40</span> 39
4.4.1 网络密码服务申报响应 .................................................................................... <span style="color:blue">41</span> 40
4.5 其他消息 ....................................................................................................................... <span style="color:blue">43</span> 42
4.5.1 申报拒绝 Order Reject ...................................................................................... <span style="color:blue">43</span> 42
4.5.2 平台状态 PlatformState .................................................................................... <span style="color:blue">43</span> 42
4.5.3 执行报告分区信息 ExecRptInfo ........................................................................ <span style="color:blue">43</span> 42
4.5.4 分区序号同步 ExecRptSync .............................................................................. <span style="color:blue">44</span> 43
4.5.5 分区序号同步响应 ExecRptSyncRsp ................................................................. <span style="color:blue">44</span> 43
4.5.6 分区执行报告结束 ExecRptEndOfStream ........................................................ <span style="color:blue">45</span> 44
第五章 附录 ............................................................................................................................. <span style="color:blue">46</span> 45
5.1 附一 计算校验和 ....................................................................................................... <span style="color:blue">46</span> 45
5.2 附二 PBU 及说明 ....................................................................................................... <span style="color:blue">46</span> 45
5.3 附三 错误代码说明 ................................................................................................... <span style="color:blue">47</span> 46
5.4 附四 “用户私有信息”说明 ................................................................................... <span style="color:blue">47</span> 46
5.5 附五 价格数量字段说明 ........................................................................................... <span style="color:blue">48</span> 47
5.6 附六 融资融券 ........................................................................................................... <span style="color:blue">48</span> 47
5

交易网关数据接口规范
第一章 前言
1.1 目的
本接口规范描述了上海证券交易所（以下称本所）交易网关与市场参与者系统之间以
STEP 协议进行交易数据交换时所采用的交互机制、消息格式、消息定义和数据内容。目前，
本接口规范仅适用于本所竞价平台提供的各类业务。
文档采用的术语及消息内容与 STEP 数据接口规范具有对应关系，可互为参考。
1.2 术语和定义
名词
含义
TDGW
TraDing GateWay
交易网关
OMS
Order Management System
用户订单管理系统
会员等市场参与者通过 OMS 接入 TDGW 并进行交易数据交换
PBU
Participant Business Unit
市场参与者交易业务单元
EzCS
Easy Communication Server
轻型化通信服务器
STEP
Securities Trading Exchange Protocol
证券交易数据交换协议
1.3 参考文档
名称
《 IS101 上海证券交易所竞价撮合平台市场参与者接口规格说明书》
《 IS111 上海证券交易所报盘软件错误代码表》
6

交易网关数据接口规范
1.4 联系方式
技术服务 QQ 群： 298643611
技术服务电话 : 4008888400-2(8:00-20:00)
电子邮件： tech_support@sse.com.cn
技术服务微信公众号： SSE-TechService ( 回复 00 进入
人工服务 )
7

交易网关数据接口规范
第二章 系统简介
2.1 系统接入
为满足业务发展需求和提升交易服务水平，本所通过交易网关（ TDGW ）对接竞价平台
交易系统，提供实时交易流接口。 TDGW 对接交易系统及市场参与者系统（ OMS ）的示意图
如下：
TDGW 通过数字证书和交易业务单元（ PBU ）登录并接入交易系统，证书及 PBU 的配置
由用户提前在 TDGW 端完成。
TDGW 每个平台开放一个端口供 OMS 建立会话， TDGW 仅接受 OMS 为每个平台建立一
个 TCP/IP 连接，每个连接仅允许建立一个有效的会话。该会话既用于接收 OMS 的业务申报，
又向 OMS 推送交易所接收申报后产生的回报数据。
OMS 与 TDGW 间的连接为标准 TCP/IP 连接，由 OMS 负责发起。 OMS 与 TDGW 之间传
输的数据是非加密的，数据传输的安全性由部署的网络予以保证。
附录二对术语 PBU 在不同场景下的使用进行了说明。
2.2 业务范围
目前支持竞价平台相关业务：
平台
业务
业务申报时间
竞价
现货竞价交易（股票 A/B 股、基金、国债分
09:15 – 09:25
8

交易网关数据接口规范
<span style="color:red">竞价</span>
<span style="color:red">竞价</span>
销 / 公司债分销）
09:30 – 11:30
13:00 – 15:00
配股 / 科创板配售、配转债
09:30 – 11:30
13:00 – 15:00
发行（股票、可转债、可交换债、 ETF ） <span style="color:red">、</span>
<span style="color:red">要约收购</span> <span style="color:red">/</span> <span style="color:red">现金选择权的登记及注销、开放</span>
<span style="color:red">式基金业务（申购、赎回、认购、转托管、</span>
<span style="color:red">分红设置、转换）、余券划转、还券划转、</span>
<span style="color:red">担保品划转、券源划转、网络密码服务</span>
<span style="color:red">注：开放式基金认购，其中包括货币市场基金实时申赎业务的认购。</span>
9

交易网关数据接口规范
第三章 交互机制
3.1 会话机制
OMS 与 TDGW 间的会话消息包括登录 Logon 、注销 Logout 和心跳 Heartbeat 等消息。
3.1.1 建立会话
OMS 负责发起到交易网关的 TCP 连接，并在连接建立后发送 Logon 消息。 OMS 连接后
的首个消息必须是 Logon 消息。如果登录成功， TDGW 返回一个 Logon 消息作为确认；如果
失败， TDGW 返回一个含失败原因的 Logout 消息，并由 OMS 关闭连接。 OMS 只应在收到
TDGW 的登录成功确认后才能发送其他消息。
3.1.2 关闭会话
会话建立成功后，连接双方均可发送 Logout 注销消息，告知对端将关闭会话，一般地，
接收方应回复一个 Logout 消息作为回应。 Logout 的发起方在收到回应后关闭连接。如果超
过 5 秒没有收到对方回传的 Logout 消息，注销发起方也可直接关闭连接。连接双方在发送
1

交易网关数据接口规范
Logout 消息后不应再发送任何消息。
3.1.3 维持会话
在消息交换的空闲期间，连接双方通过 Heartbeat 心跳消息维持会话，即连接的任何一
方在心跳时间间隔内若没有发送任何消息，需要产生并发送一个 Heartbeat 消息。
心跳间隔通过登录过程进行协商，以登录成功后 TDGW 返回的登录确认消息中的
HeartBtInt 域为准。一般地，当 OMS 发送 Logon 消息中的 HeartBtInt 取值属于 [5,60] 时， TDGW
返回原值，否则取边界值（ 5 或 60 ）。
接收方接收到任何消息（不仅仅是心跳）可重置读心跳间隔计数。若接收方在 2 个心跳
间隔内未收到任何消息，则可以认为会话出现异常并立即关闭连接。 OMS 关闭连接后，可
重新发起会话或切换至其他 TDGW 。
3.1.4 其他约定
TDGW 在未成功登录至交易系统时， OMS 将无法成功与 TDGW 建立会话； TDGW 与 EzCS
连接断开时， TDGW 将注销与 OMS 间的会话，此时 OMS 应稍后尝试重建会话，或切换至备
用 TDGW 服务。
此外， TDGW 在以下情况下会主动断开与 OMS 间的连接：
⚫
OMS 与 TDGW 建立 TCP 连接之后，超过 5 秒未完成登录；
⚫
OMS 在登录失败之后，未在 5 秒内关闭连接；
⚫
OMS 在发起注销后，未在 5 秒内关闭连接；
⚫
OMS 未能及时处理 TDGW 下行消息，导致 TDGW 内积压的待发送消息超过特定阈
值；
⚫
TDGW 与 EzCS 间的连接已经断开；
3.2 申报与回报
OMS 进行的新订单申报（ New Order Single ），本所交易系统会进行前置检查，若检查
未通过将返回订单拒绝（ Order Reject ）消息。
对于通过前置校验的申报，交易系统根据业务的不同，向 OMS 返回相应的执行报告
1

交易网关数据接口规范
（ Execution Report ）消息。执行报告包括对申报的确认，如对新订单的确认或拒绝响应 1 、撤
单响应等；如产生成交时，执行报告中会包含成交确认。
总体示意图如下：
3.2.1 业务类型
订单申报需要指定业务类型（ ApplID ），其产生的回报以不同的执行报告分区（ PartitionNo ）
划分为多个逻辑上相互独立的数据流。根据具体业务的不同，下表给出业务类型、分区的对
应关系，并明确业务相关属性。
业务
业务类型
(ApplID)
执行报告分区
(PartitionNo)
支持撤单
申报确认 成交确认
现货竞价
交易
100010
1-6，20
Y
Y
Y
发行
300010
991
注1
Y
N
1 除前置检查未通过返回Reject 外，执行报告中也包含有因业务校验未通过产生的拒绝响应Execution
Report（ExecType=8）。
1

交易网关数据接口规范
配股/科创
板配售
300020
991
N
Y
Y
配转债
300021
991
N
Y
Y
<span style="color:red">要约预受/</span>
<span style="color:red">现金选择</span>
<span style="color:red">300030</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">权登记</span>
<span style="color:red">要约撤销/</span>
<span style="color:red">现金选择</span>
<span style="color:red">300031</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">权撤销</span>
<span style="color:red">开放式基</span>
<span style="color:red">金申购</span>
<span style="color:red">300040</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">开放式基</span>
<span style="color:red">金赎回</span>
<span style="color:red">300041</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">开放式基</span>
<span style="color:red">金认购</span>
<span style="color:red">300050</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">开放式基</span>
<span style="color:red">金转托管</span>
<span style="color:red">300060</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">开放式基</span>
<span style="color:red">金分红设</span>
<span style="color:red">300070</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">置</span>
<span style="color:red">开放式基</span>
<span style="color:red">金转换</span>
<span style="color:red">300080</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
1

交易网关数据接口规范
<span style="color:red">余券划转</span>
<span style="color:red">300090</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">还券划转</span>
<span style="color:red">300091</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">担保品划</span>
<span style="color:red">入</span>
<span style="color:red">300092</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">担保品划</span>
<span style="color:red">出</span>
<span style="color:red">300093</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">券源划入</span>
<span style="color:red">300094</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">券源划出</span>
<span style="color:red">300095</span>
<span style="color:red">991</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">网络密码</span>
<span style="color:red">服务</span>
<span style="color:red">300100</span>
<span style="color:red">注2</span>
<span style="color:red">N</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
注1：发行业务中，ETF 认购可撤单，其他不可撤单；
<span style="color:red">注2：网络密码服务业务，申报消息不进行重单校验，申报响应消息不进执行报告；</span>
注 <span style="color:blue">2</span> <span style="color:red">3</span> ：Y 为是，N 为否。
1

交易网关数据接口规范
3.2.2 消息流图
3.2.2.1 新订单申报
1 、限价订单（ OrdType=2 ）消息流如下：
OMS
OMS
TDGW
TDGW
限价申报（ New Order Single ）
订单拒绝（ Order Reject, OrdRejReason=xxx ）
前置校验失败
限价申报（ New Order Single ）
申报响应（ Execution Report, ExecType=8 ）
业务校验失败
限价申报（ New Order Single ）
申报响应（ Execution Report, ExecType=0 ）
业务校验通过后，
先返回申报响应，
然后根据不同的业
务规则和订单执行
情况返回成交回报
成交回报（ Execution Report, ExecType=F ）
2 、市转撤订单（ OrdType=1 ）消息流如下：
1

交易网关数据接口规范
OMS
OMS
TDGW
TDGW
市转撤申报（ New Order Single ）
订单拒绝（ Order Reject, OrdRejReason=xxx ）
前置校验失败
市转撤申报（ New Order Single ）
申报响应（ Execution Report, ExecType=8 ）
业务校验失败
市转撤申报（ New Order Single ）
申报响应（ Execution Report, ExecType=0 ）
业务校验通过后，
先返回申报响应（并
携带剩余未成交数
量），再返回成交回
报
成交回报（ Execution Report, ExecType=F ）
3 、市转限订单（ OrdType=3 ）、本方最优（ OrdType=4 ）、对手方最优（ OrdType=5 ）消
息流如下：
1

交易网关数据接口规范
OMS
OMS
TDGW
TDGW
市转限申报（ New Order Single ）
订单拒绝（ Order Reject, OrdRejReason=xxx ）
前置校验失败
市转限申报（ New Order Single ）
申报响应（ Execution Report, ExecType=8 ）
业务校验失败
市转限申报（ New Order Single ）
申报响应（ Execution Report, ExecType=0 ）
成交回报（ Execution Report, ExecType=F ）
业务校验通过后，
先返回申报响应
（携带剩余转限价
数量），如有成
交，再返回成交回
报
3.2.2.2 新订单撤单
支持撤单的业务类型见前述章节业务类型表。
1

交易网关数据接口规范
OMS
OMS
TDGW
TDGW
撤单申报（ Order Cancel ）
前置校验失败
订单拒绝（ Order Reject, OrdRejReason=xxx ）
撤单申报（ Order Cancel ）
撤单失败
撤单失败响应（ Execution Report,
CxlRejReason=xxx ）
撤单申报（ Order Cancel ）
撤单成功响应（ Execution Report, ExecType=4 ）
撤单成功
<span style="color:red">3.2.2.3</span> <span style="color:red">网络密码服务</span>
OMS
OMS
TDGW
TDGW
网络密码服务申报
前置校验失败
订单拒绝（ Order Reject, OrdRejReason=xxx ）
网络密码服务申报
业务处理
网络密码服务申报响应
3.2.3 平台状态
OMS 向 TDGW 进行申报应符合交易时间表 2 要求。 TDGW 依据交易时间表对平台状态进
行了划分，示意图如下。
2 时间表以本所交易规则为准。
1

交易网关数据接口规范
处于 NotOpen 、 Break 、 Close 状态时不接收申报， TDGW 返回 Order Reject
（ OrdRejReason=5009 ）予以拒绝。 PreOpen 3 状态下， TDGW 提前接收 OMS 的申报，并在 Open
时向交易系统转发。 PreOpen 及 Open 状态下 TDGW 接收的申报是否被交易系统主机接受，
OMS 应以申报确认为准。
在 OMS 与 TDGW 交易通道建立会话成功后， TDGW 向 OMS 发送一条平台状态
PlatformState 消息。当平台状态发生变化时， TDGW 也向已建立会话的 OMS 发送一条平台
状态消息予以通知。
OMS
TDGW
Logon
Logon
PlatformState
登录后及状态变化时以
PlatformState 通知 OMS
ExecRptInfo
执行报告分区信息（包
含 PBU 和 SetID 信息）
New Order Single
NotOpen/Break/Close 时
拒绝申报（ 5009 ）
Order Reject
New Order Single
PreOpen/Open 时
TDGW 接收申报
Order Reject
/Execution Report
3 目前，设置 PreOpen 为各交易时段 Open 前的 5 秒。以交易时段 9:15-9:25 为例， 9:14:55TDGW 转为 PreOpen ， 9:15:00 TDGW
转为 Open 状态。
1

交易网关数据接口规范
3.2.4 重复订单
交易系统依据申报中的业务 PBU + 会员内部订单编号组合的取值判断申报是否为重复
订单：
其中，业务 PBU 取 Parties 组件中 PartyID 字段（当 PartyRole=1 ）。
会员内部订单编号取消息类型相应字段：
申报类型
会员内部订单编号字段
New Order Single
ClOrdID
Order Cancel
ClOrdID
对于重复订单， TDGW 返回拒绝消息（ Order Reject ）。
OMS
TDGW
新申报
New Order Single
ClOrdID=10  Pbu=20001
Execution Report,ExecType=0
申报确认
重复申报
New Order Single
ClOrdID=10  Pbu=20001
拒绝响应
Order Reject
OrdRejReason=11270
3.2.5 执行报告
每笔执行报告消息都包含 PBU 、分区（ PartitionNo ）和序号（ ReportIndex ）信息。
PBU 字段表明了该执行报告是在哪一个登录 PBU 上进行申报所产生的回报数据，一般
为 OMS 所连接的 TDGW 上正在登录的 PBU ；若 TDGW 配置了订阅，该字段取值也可能为被
订阅的其他 PBU ，详见后续订阅章节的说明。
在每个 PBU 下，执行报告根据分区（ PartitionNo ）划分为多个编号相互独立的数据流。
2

交易网关数据接口规范
在一个交易日内，每个执行报告流中的 ReportIndex 由 1 开始连续递增。多个不同业务可以
属于同一个分区 4 ，从而在同一个流中按序发送。
OMS 与 TDGW 建立会话后， TDGW 会向 OMS 推送执行报告分区信息（ ExecRptInfo ）消
息，其中包含 PBU 列表和分区列表， OMS 应根据此信息维护多个逻辑上的执行报告流。
OMS 与 TDGW 建立会话后，应根据 ExecRptInfo 中的信息，向 TDGW 发送各个执行报告
流的分区序号同步（ ExecRptSync ）消息， TDGW 将返回一个分区序号同步响应消息
（ ExecRptSyncRsp ）进行回应。对于 ExecRptSync 请求校验通过的情况， TDGW 将依据其中约
定的序号 BeginReportIndex 发送后续执行报告。
OMS 若不发送序号同步消息， TDGW 将不会推动执行报告。如果 OMS 发送的序号同步
消息中， BeginReportIndex 大于实际存在的分区回报最大序号，则 TDGW 不会推送执行报告，
直至实际分区回报数确实达到 BeginReportIndex 后再开始推送。闭市后， TDGW 不再接收
OMS 申报，但可以通过序号同步消息重新获取当日历史执行报告数据。
OMS 应对 TDGW 推送的执行报告进行数据持久化操作，以减少 OMS 异常时从交易系统
恢复的执行报告数量。同时， OMS 应具备识别重复执行报告的能力，避免重复处理。
4 比如，发行（ BizID=300010 ）和配股 / 科创板配售（ BizID=300020 ）均属于 PartitionNo =991 的分区。
2

交易网关数据接口规范
OMS
TDGW
Logon
登录
Logon
PlatformState
平台状态
ExecRptInfo
执行报告分区信息
Pbu=20001, SetID=1
ExecRptSync
序号同步请求
20001, 1, NextRptIndex=1
20001, <span style="color:red">2</span> , NextRptIndex=100
ExecRptSyncRsp
序号同步响应
20001, 1, 1, 10, RejReason=0
20001, <span style="color:red">2</span> , 100, 200, RejReason= <span style="color:red">5010</span>
Execution Report
执行报告
20001, 1, 1
20001, 1, 2
…
3.3 恢复场景
OMS 与 TDGW 断开
在 OMS 重新与 TDGW 建立会话后，由于断连期间可能存在传输中的消息丢失， OMS 应
对上下行两个方向的消息进行恢复。建议 OMS 先对执行报告进行恢复，以尽可能更新断连
前申报订单的状态。 OMS 可在恢复一段时间后，对仍然处于“已报但未确认”状态的订单进
行重新申报。
2

交易网关数据接口规范
TDGW 与 EzCS 断开
TDGW 与 EzCS 间连接断开时， TDGW 将通过 Logout （ SessionStatus=5006 ）消息注销与
OMS 间的会话，并尝试切换备用 EzCS 。在 TDGW 未登录至交易系统期间， OMS 发起到 TDGW
的会话将无法成功。 TDGW 恢复登录，且 OMS 重建与 TDGW 间的会话后， OMS 对消息的恢
复处理可与上一节描述相同。
3.4 订阅机制
通过在 TDGW 端进行配置， OMS 可通过与一个 TDGW 间的会话，接收到其他 TDGW 上
登录的另一 PBU 所产生的执行报告数据。
TDGW 端登录的 PBU-B ，若需订阅另一 TDGW 上登录的 PBU-A 所产生的执行报告， PBU-
B 与 PBU-A 需要属于同一市场参与者机构。
目前，交易系统限制每个登录 PBU 可被最多 2 个其他登录 PBU 订阅成功。为减少订阅
对登录 PBU 自身回报数据处理的影响， TDGW 将优先发送登录 PBU 自身的回报数据。
在同一市场参与者机构的范围内，订阅的配置和管理由市场参与者机构负责，市场参与
者机构在充分利用订阅形成 TDGW 互备的同时，也应做好订阅权限和数据权限的控制。
2

交易网关数据接口规范
第四章 消息定义
4.1 消息结构与约定
每一条 STEP 消息由消息头、消息体和消息尾组成，消息最大长度为 4K 字节。
4.1.1 数据类型
数据类型相关说明如下：
1. 字符串类型用 CX 表示， X 表示字符串最大字节数，除特别声明，字符串只包含数字、
大写字母、小写字母以及空格；字符串实际长度小于字段类型最大长度时可以不补空格；字
符串统一采用 ASCII 编码。
2. 十进制整数用 NX 表示， X 表示整数最大位数（不包括正负号），除特殊说明，整数
类型均有正负。
3. 浮点数用 NX （ Y ）表示， X 表示整数与小数总计位数（不包括小数点及正负号）， Y 表
示小数位数，小数位数不足时必须在后面补 0 ，除非特殊说明，浮点数类型均有正负。
4. 数值类型字段默认填 0 值，字符串类型默认填空格；针对“暂不启用”字段，填写默
认值。
5. 针对部分字段填写固定值的场景，固定值根据实际字段类型进行填写。如字段要求
“固定填 1 ”，若字段类型为 N13(5) ，则实际填写 1.00000 ；若字段类型为 C1 ，则实际填写
字符‘ 1 ’ .
6. 为简化描述，定义部分业务类型如下：
字段名
类型
说明
price
N13(5)
价格
quantity
N15(3)
数量
amount
N18(5)
金额
当前时区日期，格式 YYYYMMDD ，
YYYY 为年，取值范围 0000-9999 ， MM
date
C8
为月，取值范围 01-12 ， DD 为日，取
值范围 01-31
ntime
C13
当
前
时
区
时
间
，
格
式
HHMMSSsssnnnn ， HH 为小时，取值范
2

交易网关数据接口规范
围 00-23 ， MM 为分钟，取值范围 00-
59 ， SS 为秒，取值范围 00-59 ， sss 为
毫秒，取值范围 000-999 ， nnnn 为百纳
秒，取值 0000-9999
Boolean
C1
代表该字符串内容为布尔值，有效取
值是 Y 或者 N 。
4.1.2 STEP 格式约定
STEP 结构均采用依次排列“标签 = 字段取值 <SOH> ”的方式组织，标签为数字字符，前
后无空格，除非特别声明外，字段取值均为可打印 ASCII 码字符串表示，不得采用全角字母
字符， <SOH> 为字段界定符，值为不可打印 ASCII 码字符：十六进制的 0x01 。
STEP 结构中重复组部分的字段需严格遵循接口规格中定义的先后顺序；字符型字段用
空格表示空值，即采用“标签 = <SOH> ”的方式表示（等号后与分隔符间有一个空格），数
值型字段用 0 表示空值，即“标签 =0<SOH> ”（注：含小数数值型字段空值需符合格式要求，
例 N13 （ 5 ）空值表示为“标签 =0.00000<SOH> ”）。
4.1.3 STEP 消息头
每一个会话或应用消息都有一个消息头，该消息头指明消息类型、消息体长度、消息序
号及发送时间等信息。
消息头格式如下：
Tag
域名
必须
说明
类型
8
BeginString
Y
起始串，固定为 FIXT.1.1
C16
9
BodyLength
Y
消息体长度
N9
35
MsgType
Y
消息类型
C16
49
SenderCompID
Y
发送方代码
C32
接收方代码。 OMS 发出的消息
56
TargetCompID
Y
C32
中填写“ TDGW ”。
34
MsgSeqNum
Y
消息序号
N18
43
PossDupFlag
N
会话层可能重传标志
Boolean
97
PossResend
N
应用层可能重传标志
Boolean
2

交易网关数据接口规范
52
SendingTime
Y
发送时间，格式： YYYYMMDD-
HH:MM:SS.sss
C21
347
MessageEncoding
N
字符编码类型
C16
4.1.4 STEP 消息尾
每一个会话或应用消息都有一个消息尾，并以此终止。消息尾可分隔多个消息，包含有
3 位数的校验和值。
消息尾格式如下：
Tag
域名
必须
说明
类型
10
CheckSum
Y
校验和，消息的最末域
C3
4.1.5 STEP 消息完整性
STEP 消息完整性通过两个方法保证：消息体长度及校验和的验证。
消息长度通过 BodyLength 域记录，表示 BodyLength 域值之后第一个域界定符 <SOH> （不
包括）与 CheckSum 域号前的最后一个域界定符 <SOH> （包括）之间的字符个数。
校验和是把每个字符的 ASCII 码值从消息开头‘ 8= ’中的‘ 8 ’开始相加，一直加到紧靠
在 CheckSum 域号‘ 10= ’之前的域界定符，然后取按 256 取模得到的结果。计算校验和的
代码段可参考附录一“计算校验和”。
4.2 会话消息
会话消息将在以下各节中予以介绍，并定义会话消息格式，会话层消息机制兼容《 LFIXT
会话协议接口规范》。
4.2.1 登录消息（ MsgType=A ）
登录消息（ Logon ）应是 OMS 建立连接后发送的首个消息。
会话发起方，如需序号重置，则需设置 ResetSeqNumFlag 为 ’Y’ 、 NextExpectedMsgSeqNum
2

交易网关数据接口规范
为 1.
对于 DefaultCstmApplVerID ，会话接收方将返回最低接入协议版本号。
登录请求消息格式如下：
Tag
域名
必须
说明
类型
标准消息头
MsgType = A
98
EncryptMethod
Y
加密方法，固定为 0
N8
108
HeartBtInt
Y
心跳间隔，单位为秒
N8
141
ResetSeqNumFlag N
双方序号重置为 1 的标记
Boolean
接收方期望得到的下一条消
NextExpectedMsg
789
N
N18
SeqNum
息序号。若无，默认设置为 1.
553
Username
N
用户名（预留）
C32
554
Password
N
密码（预留）
C32
本次会话中使用的 FIX 消息的
1137
DefaultApplVerID
Y
C8
缺省版本
本次会话中使用的 FIX 消息的
1407
DefaultApplExtID
N
N8
缺省扩展包
本次会话中 FIX 消息的缺省
自定义应用版本。填写格式为
STEP1.20_SH_n.xy 其中 n.xy
为接入协议版本号，如接入协
DefaultCstmAppl
1408
Y
C32
议版本号为 1.70 时， 则填写：
VerID
STEP1.20_SH_1.70 。
（ TDGW 将
限制接入的协议版本。当前最
低接入协议版本要求为 0.50
版）
标准消息尾
4.2.2 注销消息（ MsgType=5 ）
注销消息是发起或确认会话终止的消息。连接双方在发送注销消息之后不应发送任何消
2

交易网关数据接口规范
息。
注销消息格式如下：
Tag
域名
必须
说明
类型
标准消息头
MsgType = 5
1409
SessionStatus
N
注销状态码
N4
58
Text
N
文本
C1024
标准消息尾
4.2.3 心跳消息（ MsgType=0 ）
心跳消息用于监控通信连接的状况。如果接收方在 2 倍心跳时间间隔内未收到任何消
息的时候，可认定会话出现异常，可以立即关闭 TCP 连接。
心跳消息格式如下：
Tag
域名
必需
说明
类型
标准消息头
Y
MsgType = 0
112
TestReqID
N
C32
如是对测试请求消息（ 4.2.4 ）而发送
的心跳消息，则需包含本域，否则不
包含本域。本域的内容复制于测试请
求消息（ 4.2.4 ）的 TestReqID 内容
标准消息尾
Y
4.2.4 测试请求消息（ MsgType=1 ）
测试请求消息能强制对方发出心跳消息。测试请求消息的作用是检查对方消息序号和检
查通信线路的状况。对方用带有测试请求标识符（ TestReqID ）的心跳作应答。 TDGW 不会主
动发送此消息，但会遵循 FIX 标准引擎规则而响应 OMS 发送的该请求。
测试请求消息格式如下：
Tag
域名
必须
说明
类型
标准消息头
MsgType =1
112
TestReqID
N
测试请求标识符
C32
标准消息尾
2

交易网关数据接口规范
4.2.5 重发请求消息（ MsgType=2 ）
TDGW 不会主动发送此消息，但会遵循 FIX 标准引擎规则而响应 OMS 发送的该请求。
TDGW 接收到重发请求消息，通过序号重设消息（ 4.2.7 ）响应。
重发请求消息格式如下：
Tag
域名
必须
说明
类型
标准消息头
MsgType = 2
7
BeginSeqNo
Y
起始消息序号
N18
16
EndSeqNo
Y
结束消息序号
N18
标准消息尾
4.2.6 会话拒绝消息（ MsgType=3 ）
当接收方收到一条违反会话层规则而不能正确处理的消息时，应该发出会话拒绝消息。
TDGW 不会主动发送此消息。
会话拒绝消息格式如下：
Tag
域名
必需
说明
类型
标准消息头
Y
MsgType = 3
45
RefSeqNum
Y
关联消息的序号，即被拒绝消息的序号 N18
371
RefTagID
N
相关错误消息中，出现错误的 FIX 域号 N6
372
RefMsgType
N
相关错误消息的 MsgType
C16
373
SessionRejectR
eason
N
会话拒绝原因编号
N5
58
Text
N
文本，拒绝的原因描述
C1024
标准消息尾
Y
4.2.7 序号重设消息（ MsgType=4 ）
序号重设消息用于告知接收方下一个消息的消息序号。序号重设消息的 MsgSeqNum 按
标准 FIX 协议规定可以任意填写且接收方不会检查，建议固定填写为 1 。 TDGW 不会主动发
送此消息，但会遵循 FIX 标准引擎规则而响应 OMS 发送的重发请求消息（ 4.2.5 ）。当 TDGW
收到用户序号重设消息，则重置入向消息序号 NxtIn = NewSeqNo 。
序号重设消息格式如下：
Tag
域名
必需
说明
类型
标准消息头
Y
MsgType = 4
123
GapFillFlag
N
缺口填补标志
Boolean
2

交易网关数据接口规范
36
NewSeqNo
Y
新消息序号
N18
标准消息尾
Y
4.3 应用消息 - 新订单
4.3.1 新订单申报 New Order Single
标签
字段名
字段描述
必须
类型
消息
头
MsgType = D
1180
ApplID
业务类型
Y
C6
11
ClOrdID
会员内部订单编号
Y
C10
48
SecurityID
产品代码
Y
C12
522
OwnerType
订单所有者类型
Y
N3
54
Side
买卖方向，取值： 1 表示买， 2 表示卖
Y
C1
44
Price
申报价格
Y
price
38
OrderQty
申报数量
Y
quantity
40
OrdType
订单类型： 1= 市转撤， 2= 限价， 3= 市转限， 4= 本
方最优， 5= 对手方最优
Y
C1
59
TimeInForce
订单有效时间类型，取值范围： 0 表示当日有效
（ GFD ）
Y
C1
60
TransactTime
订单申报时间
Y
ntime
544
CashMargin
N
C2
信用标签，用于现货竞价交易业务的信用交易，
取值： XY= 担保品买卖、 RZ= 融资交易、 RQ= 融券
交易、 PC= 平仓交易
其他业务填写默认值，无意义。
58
Text
用户私有信息，前 12 位有效
N
C32
453
NoPartyIDs
Y
N2
参与方个数，取值 =5 ，后接重复组，依次包含发
起方投资者账户、发起方业务交易单元号、发起
方营业部代码、结算会员代码、开放式基金转托
管的目标方。
448
PartyID
发起方投资者帐户
Y
C13
Y
N4
452
PartyRole
发起
方投
资者
账户
取 5 ，表示当前
PartyID 的取值为发
起方投资者帐户。
448
PartyID
Y
C8
发起方业务交易单
元代码，填写 5 位业
务交易单元号。
发起
方业
务交
易单
元号
452
PartyRole
取 1 ，表示当前
PartyID 的取值为发
Y
N4
3

交易网关数据接口规范
起方业务交易单元
号。
448
PartyID
发起方营业部代码
Y
C8
452
PartyRole
Y
N4
发起
方营
业部
代码
取 4001 ，表示当前
PartyID 的取值为发
起方的营业部代码。
448
PartyID
结算会员代码
Y
C8
452
PartyRole
Y
N4
结算
会员
代码
取 4 ，表示当前
PartyID 的取值为结
算会员代码。
448
PartyID
Y
C3
<span style="color:red">开放式基金转托管</span>
<span style="color:red">的目标方代理人，对</span>
<span style="color:red">方对应的销售人代</span>
<span style="color:red">码，取值</span> <span style="color:red">000-999</span> <span style="color:red">，</span>
<span style="color:red">不足</span> <span style="color:red">3</span> <span style="color:red">位左侧补</span>
<span style="color:red">0.ApplID=</span> <span style="color:red">“开放式基</span>
<span style="color:red">金转托管”时有效</span> <span style="color:blue">预</span>
<span style="color:blue">留字段，暂不启用。</span>
452
PartyRole
Y
N4
<span style="color:red">开放</span>
<span style="color:red">式基</span>
<span style="color:red">金转</span>
<span style="color:red">托管</span>
<span style="color:red">的目</span>
<span style="color:red">标方</span>
<span style="color:blue">预留</span>
<span style="color:blue">字</span>
<span style="color:blue">段，</span>
<span style="color:blue">暂不</span>
<span style="color:blue">启用</span>
<span style="color:blue">固定</span> 取 30 <span style="color:blue">。</span> <span style="color:red">，表示当</span>
<span style="color:red">前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为</span>
<span style="color:red">开放式基金转托管</span>
<span style="color:red">的目标方代理人。</span> <span style="color:blue">预</span>
<span style="color:blue">留字段，暂不启用。</span>
<span style="color:red">分红选择方式，</span> <span style="color:red">ApplID=</span> <span style="color:red">“开放式基金分红”时有</span>
8532
DividendSelect
N
C1
<span style="color:red">效，’</span> <span style="color:red">U’=红利转投；’C’=现金分红</span> <span style="color:blue">预留字</span>
<span style="color:blue">段，暂不启用。</span>
8533
DestSecurity
N
C12
<span style="color:red">转入的标的产品代码，前</span>
<span style="color:red">6</span> <span style="color:red">位有效。</span> <span style="color:red">ApplID=</span> <span style="color:red">“开放</span>
<span style="color:red">式基金基金转换”、“余</span>
<span style="color:red">券划转”、“还券划转”、</span>
<span style="color:red">“担保品划转”、“券源</span>
<span style="color:red">划转”时有效。</span> <span style="color:blue">预留字段，</span>
<span style="color:blue">暂不启用。</span>
说明：
1.
适用于业务类型如下：
业务
可选字段
Side
Price
OrderQty
SecurityID
只需填写必须字
段
1=买
2=卖
价格
数量
证券代码
现货
竞价
交易
3

交易网关数据接口规范
发行价
发行认购代码（“非交易
固定
发行
只需填写必须字
段
填1
认购数
量。以
1000 为最
业务类型”=“IN”），
买入转义为对对应证券参
（ETF
网上现
金认购
小单位。
与发行认购。
填1）
配股/
配股价
配股代码（“非交易业务
只需填写必须字
固定
配股数量/
科创
板配
段
填2
/科创
板配售
配售数量
类型”=“R1”），卖出
转义为对对应证券参与配
售
价
股。
配转债代码（“非交易业
配转
只需填写必须字
固定
债
段
填2
配债价
配债数量
务类型”=“R4”），卖
出转义为对对应证券参与
配转债
<span style="color:red">706***（“非交易业务类</span>
<span style="color:red">要约</span>
<span style="color:red">预受/</span>
<span style="color:red">型”=“FS”），与股票</span>
<span style="color:red">代码没有直接对应关系，</span>
<span style="color:red">需要根据上交所在要约收</span>
<span style="color:red">只需填写必须字</span>
<span style="color:red">固定</span>
<span style="color:red">段</span>
<span style="color:red">填2</span>
<span style="color:red">收购价</span>
<span style="color:red">收购数量</span>
<span style="color:red">现金</span>
<span style="color:red">选择</span>
<span style="color:red">权登</span>
<span style="color:red">购/现金选择权业务开始</span>
<span style="color:red">之前发布的公告决定。卖</span>
<span style="color:red">出转义为对对应的股票进</span>
<span style="color:red">记</span>
<span style="color:red">行要约收购/现金选择权</span>
<span style="color:red">706***（“非交易业务类</span>
<span style="color:red">登记。</span>
<span style="color:red">要约</span>
<span style="color:red">撤销/</span>
<span style="color:red">只需填写必须字</span>
<span style="color:red">固定</span>
<span style="color:red">型”=“FC”），买入转</span>
<span style="color:red">义为对对应的股票进行要</span>
<span style="color:red">段</span>
<span style="color:red">填1</span>
<span style="color:red">收购价</span>
<span style="color:red">收购数量</span>
<span style="color:red">约收购/现金选择权注</span>
<span style="color:red">现金</span>
<span style="color:red">选择</span>
<span style="color:red">权撤</span>
<span style="color:red">销。</span>
<span style="color:red">销</span>
<span style="color:red">519***（“非交易业务类</span>
<span style="color:red">只需填写必须字</span>
<span style="color:red">固定</span>
<span style="color:red">固定填</span>
<span style="color:red">开放</span>
<span style="color:red">式基</span>
<span style="color:red">金申</span>
<span style="color:red">段</span>
<span style="color:red">填1</span>
<span style="color:red">1</span>
<span style="color:red">型”=“OC”），买入转</span>
<span style="color:red">义为对对应的开放式基金</span>
<span style="color:red">申购金</span>
<span style="color:red">额，单位</span>
<span style="color:red">为元。目</span>
<span style="color:red">前不支持</span>
<span style="color:red">购</span>
<span style="color:red">申购</span>
<span style="color:red">小数</span>
<span style="color:red">519***（“非交易业务类</span>
<span style="color:red">只需填写必须字</span>
<span style="color:red">固定</span>
<span style="color:red">固定填</span>
<span style="color:red">开放</span>
<span style="color:red">式基</span>
<span style="color:red">金赎</span>
<span style="color:red">段</span>
<span style="color:red">填2</span>
<span style="color:red">1</span>
<span style="color:red">型”=“OR”），卖出转</span>
<span style="color:red">义为对对应的开放式基金</span>
<span style="color:red">赎回份</span>
<span style="color:red">额，单位</span>
<span style="color:red">为份。目</span>
<span style="color:red">前不支持</span>
<span style="color:red">回</span>
<span style="color:red">赎回</span>
<span style="color:red">小数</span>
<span style="color:red">521***（“非交易业务类</span>
<span style="color:red">只需填写必须字</span>
<span style="color:red">固定</span>
<span style="color:red">固定填</span>
<span style="color:red">开放</span>
<span style="color:red">式基</span>
<span style="color:red">金认</span>
<span style="color:red">段</span>
<span style="color:red">填1</span>
<span style="color:red">1</span>
<span style="color:red">型”=“OS”），买入转</span>
<span style="color:red">义为对对应的开放式基金</span>
<span style="color:red">认购金</span>
<span style="color:red">额，单位</span>
<span style="color:red">为元。目</span>
<span style="color:red">前不支持</span>
<span style="color:red">购</span>
<span style="color:red">的认购</span>
<span style="color:red">小数</span>
3

交易网关数据接口规范
<span style="color:red">522***（“非交易业务类</span>
<span style="color:red">只需填写必须字</span>
<span style="color:red">固定</span>
<span style="color:red">固定填</span>
<span style="color:red">段</span>
<span style="color:red">填2</span>
<span style="color:red">1</span>
<span style="color:red">型”=“OT”），卖出转</span>
<span style="color:red">义为对对应的开放式基金</span>
<span style="color:red">基金份</span>
<span style="color:red">额，单位</span>
<span style="color:red">为份。目</span>
<span style="color:red">前不支持</span>
<span style="color:red">开放</span>
<span style="color:red">式基</span>
<span style="color:red">金转</span>
<span style="color:red">托管</span>
<span style="color:red">的转托管转出</span>
<span style="color:red">小数</span>
<span style="color:red">523***（“非交易业务类</span>
<span style="color:red">固定</span>
<span style="color:red">固定填</span>
<span style="color:red">填1</span>
<span style="color:red">1</span>
<span style="color:red">固定填1</span>
<span style="color:red">型”=“OD”），买入转</span>
<span style="color:red">义为对对应的开放式基金</span>
<span style="color:red">开放</span>
<span style="color:red">式基</span>
<span style="color:red">金分</span>
<span style="color:red">红设</span>
<span style="color:red">DividendSelect</span>
<span style="color:red">必填，U=红利转</span>
<span style="color:red">投，C=现金分红</span>
<span style="color:red">设置分红方式</span>
<span style="color:red">置</span>
<span style="color:red">524***（“非交易业务类</span>
<span style="color:red">DestSecurity 填</span>
<span style="color:red">固定</span>
<span style="color:red">固定填</span>
<span style="color:red">开放</span>
<span style="color:red">式基</span>
<span style="color:red">金转</span>
<span style="color:red">写标的证券</span>
<span style="color:red">填2</span>
<span style="color:red">1</span>
<span style="color:red">型”=“OV”），卖出转</span>
<span style="color:red">义为对对应的开放式基金</span>
<span style="color:red">基金份</span>
<span style="color:red">额，单位</span>
<span style="color:red">为份。目</span>
<span style="color:red">前不支持</span>
<span style="color:red">换</span>
<span style="color:red">转换为其他基金</span>
<span style="color:red">小数</span>
<span style="color:red">划转数量,</span>
<span style="color:red">799981（“非交易业务类</span>
<span style="color:red">型”=“ST”）,买入转义</span>
<span style="color:red">为标的证券从“证券公司</span>
<span style="color:red">DestSecurity 填</span>
<span style="color:red">固定</span>
<span style="color:red">固定填</span>
<span style="color:red">余券</span>
<span style="color:red">划转</span>
<span style="color:red">写标的证券</span>
<span style="color:red">填1</span>
<span style="color:red">1</span>
<span style="color:red">划转数量</span>
<span style="color:red">允许零散</span>
<span style="color:red">股。</span>
<span style="color:red">融券专用账户”过户到</span>
<span style="color:red">“证券公司信用交易担保</span>
<span style="color:red">证券账户”。仅允许投资</span>
<span style="color:red">者信用账户（E 字头账</span>
<span style="color:red">户）申报。</span>
<span style="color:red">799982（“非交易业务类</span>
<span style="color:red">划转数量,</span>
<span style="color:red">型”=“SR”），卖出转</span>
<span style="color:red">义为标的证券从“证券公</span>
<span style="color:red">DestSecurity 填</span>
<span style="color:red">固定</span>
<span style="color:red">固定填</span>
<span style="color:red">还券</span>
<span style="color:red">划转</span>
<span style="color:red">写标的证券</span>
<span style="color:red">填2</span>
<span style="color:red">1</span>
<span style="color:red">划转数量</span>
<span style="color:red">允许零散</span>
<span style="color:red">股。</span>
<span style="color:red">司信用交易担保证券账</span>
<span style="color:red">户”过户到“证券公司融</span>
<span style="color:red">券专用账户”。仅允许投</span>
<span style="color:red">资者信用账户（E 字头账</span>
<span style="color:red">户）申报。</span>
<span style="color:red">799983（“非交易业务类</span>
<span style="color:red">划转数量,</span>
<span style="color:red">型”=“CI”），买入转</span>
<span style="color:red">义为标的证券从“投资者</span>
<span style="color:red">DestSecurity 填</span>
<span style="color:red">固定</span>
<span style="color:red">固定填</span>
<span style="color:red">担保</span>
<span style="color:red">品划</span>
<span style="color:red">写标的证券</span>
<span style="color:red">填1</span>
<span style="color:red">1</span>
<span style="color:red">划转数量</span>
<span style="color:red">允许零散</span>
<span style="color:red">入</span>
<span style="color:red">股。</span>
<span style="color:red">普通证券账户”过户到</span>
<span style="color:red">“证券公司信用交易担保</span>
<span style="color:red">证券账户”。仅允许投资</span>
<span style="color:red">者信用账户（E 字头账</span>
<span style="color:red">户）申报。</span>
<span style="color:red">799983（“非交易业务类</span>
<span style="color:red">划转数量,</span>
<span style="color:red">DestSecurity 填</span>
<span style="color:red">固定</span>
<span style="color:red">固定填</span>
<span style="color:red">担保</span>
<span style="color:red">品划</span>
<span style="color:red">型”=“CO”），卖出转</span>
<span style="color:red">义为标的证券从“证券公</span>
<span style="color:red">写标的证券</span>
<span style="color:red">填2</span>
<span style="color:red">1</span>
<span style="color:red">划转数量</span>
<span style="color:red">允许零散</span>
<span style="color:red">出</span>
<span style="color:red">股。</span>
<span style="color:red">司信用交易担保证券账</span>
<span style="color:red">户”过户到“投资者普通</span>
3

交易网关数据接口规范
<span style="color:red">证券账户”。仅允许投资</span>
<span style="color:red">者信用账户（E 字头账</span>
<span style="color:red">户）申报。</span>
<span style="color:red">799984（“非交易业务类</span>
<span style="color:red">划转数量,</span>
<span style="color:red">DestSecurity 填</span>
<span style="color:red">固定</span>
<span style="color:red">固定填</span>
<span style="color:red">券源</span>
<span style="color:red">划入</span>
<span style="color:red">写标的证券</span>
<span style="color:red">填1</span>
<span style="color:red">1</span>
<span style="color:red">划转数量</span>
<span style="color:red">允许零散</span>
<span style="color:red">股。</span>
<span style="color:red">型”=“SI”），买入转</span>
<span style="color:red">义为标的证券从“证券公</span>
<span style="color:red">司融券专用账户”过户到</span>
<span style="color:red">“证券公司自营账户”。</span>
<span style="color:red">仅允许证券公司自营证券</span>
<span style="color:red">账户申报。</span>
<span style="color:red">799984（“非交易业务类</span>
<span style="color:red">划转数量,</span>
<span style="color:red">DestSecurity 填</span>
<span style="color:red">固定</span>
<span style="color:red">固定填</span>
<span style="color:red">券源</span>
<span style="color:red">划出</span>
<span style="color:red">写标的证券</span>
<span style="color:red">填2</span>
<span style="color:red">1</span>
<span style="color:red">划转数量</span>
<span style="color:red">允许零散</span>
<span style="color:red">股。</span>
<span style="color:red">型”=“SO”），卖出转</span>
<span style="color:red">义为标的证券从“证券公</span>
<span style="color:red">司自营账户”过户到“证</span>
<span style="color:red">券公司融券专用账户”。</span>
<span style="color:red">仅允许证券公司自营证券</span>
<span style="color:red">账户申报。</span>
2.
SecurityID 字段：除“现货竞价交易”业务填写证券代码外，其他非交易业务根据产品
非交易基础信息接口 fiyYYYYMMDD.txt 中特定“非交易业务类型”对应的“非交易证券
代码”填写。
3. OrdType 字段：现货竞价交易业务申报请求的 OrdType 可取值 1/2/3/4/5 ，其他业务申报
请求的 OrdType 暂不启用。
1)
为 ‘1’ 表示最优五档即时成交剩余撤销的市价订单，含义为该申报在对手方实时最
优五个价位内以对手方价格为成交价逐次成交，剩余未成交部分自动撤销；
2)
为 ‘2’ 表示限价订单；
3)
为 ‘3’ 表示最优五档即时成交剩余转限价的市价订单，含义为该申报在对手方实时
五个最优价位内以对手方价格为成交价逐次成交，剩余未成交部分按本申报最新
成交价转为限价订单；如无对手方申报与该申报成交的，则按本方最优报价转为
限价订单；如无本方申报的，该市价订单自动撤销；
4)
为 ’4’ 表示以本方最优价格申报的市价订单，该申报以其进入交易主机时，集中申
报簿中本方最优报价为其申报价格。如有本方申报的，则按本方最优报价转为限
价订单；如无本方申报的，则该市价订单自动撤销。
3

交易网关数据接口规范
5)
为 ’5’ 表示以对手方最优价格申报的市价订单，该申报以其进入交易主机时，集中
申报簿中对手方最优报价为其申报价格。如有对手方申报，以对手方最优价为成
交价与对手方撮合成交，剩余未成交部分按本申报最新成交价转为限价订单；如
无对手方申报，该市价订单自动撤销。
4.
“发起方营业部代码”字段： 5 位数字表示，目前使用区间为 [00000 ， 65535] ，不足 5 位
的左侧补 0 。营业部代码可于本所网站会员专区查询，若无对应营业部代码，则该字段
填写空格。前 5 位有效。
5.
“结算会员代码”字段： B 股结算会员代码，对于非交易业务取值无意义，对于 A 股投
资者取值无意义。对于 B 股境外投资者 C9 类帐户此记录不能为空，直接填写中登公司
公布的 B 股结算会员代码，不足 5 位的左侧补 0 。对于 B 股境内投资者 C1 类帐户无意
义。前 5 位有效。
6.
Price 字段：对于交易业务，价格字段必须小于 1 万元；
针对市价订单（包括订单类型为最优五档即时成交剩余撤销市价订单、最优五档即时成
交剩余转限价市价订单、本方最优市价订单、对手方最优市价订单）：该字段为保护限
价，取值必须大于 0 且小于 1 万元，表示投资者能够接受的最高买入价或最低卖出价，
即买入申报的成交价格和转限价的价格不高于保护限价，卖出申报的成交价格和转限价的
价格不低于保护限价。
7.
“发起方业务交易单元号”字段：前 5 位有效； SecurityID 字段：前 6 位有效；“发起
方投资者账户”字段：前 10 位有效；“发起方营业部代码”字段：前 5 位有效； OrderQty
字段：取值小于 1000000000 ； DestSecurity 字段：前 6 位有效。
8.
ClOrdID 字段：会员内部订单编号，长度必须等于 10 个字符，各字符仅允许填写数字 0-
9 、大小写字母 a-z A-Z ，不允许其他字符。
9.
OwnerType 暂不启用。
10.  Text 字段：第 23 至 32 位，仅供港交所使用，用于填写沪股通业务的 BCAN 编码（香港
券商客户编码）信息。 BCAN 编码共 10 位数字，若不足 10 位，则左补空格右对齐。
4.3.2 撤单申报 Order Cancel
标签
字段名
字段描述
必须
类型
消息头
MsgType = F
3

交易网关数据接口规范
1180
ApplID
业务类型
Y
C6
11
ClOrdID
会员内部订单编号
Y
C10
48
SecurityID
证券代码
Y
C12
522
OwnerType
订单所有者类型
Y
N3
54
Side
买卖方向，取值： 1 表示买， 2 表示卖。
Y
C1
41
OrigClOrdID
原始会员内部订单编号，指待撤原订单的
ClOrdID
Y
C10
60
TransactTime
订单申报时间
Y
ntime
58
Text
用户私有信息，前 12 位有效
N
C32
453
NoPartyIDs
Y
N2
参与方个数，取值 =3 ，后接重复组，依次包含发
起方投资者账户、发起方业务交易单元号、发起
方营业部代码。
448
PartyID
发起方投资者帐户
Y
C13
发起方
投资者
账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发
起方投资者帐户。
Y
N4
448
PartyID
发起方业务交易单元代码，填写 5 位
业务交易单元号。
Y
C8
发起方
业务交
易单元
号
452
PartyRole
取 1 ，表示当前 PartyID 的取值为发
起方业务交易单元号。
Y
N4
448
PartyID
发起方营业部代码
Y
C8
发起方
营业部
代码
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为
发起方的营业部代码。
Y
N4
说明：
1.
撤单申报中， ApplID 、发起方业务交易单元号、 SecurityID 取值应与待撤原订单相同，
OrigClOrdID 的取值应与待撤原订单的 ClOrdID 相同。
2.
发起方投资者帐户、发起方营业部代码、 OwnerType 、 Side ，暂不启用。
4.3.3 执行报告 Execution Report
4.3.3.1 申报响应、成交回报及撤单成功响应
标签
字段名
字段描述
必
须
类型
消息
头
MsgType = 8
10197 PartitionNo
平台内分区号
Y
N4
10179
ReportIndex
执行报告编号，从 1 开始连续递增编号
Y
N16
1180
ApplID
业务类型
Y
C6
150
ExecType
执行报告类型，取值有：
0= 订单申报成功
Y
C1
3

交易网关数据接口规范
4= 订单撤销成功
8= 订单申报拒绝
F= 成交回报
11
ClOrdID
会员内部订单编号
Y
C10
48
SecurityID
证券代码
Y
C12
522
OwnerType
Y
N3
订单所有者类型，取值包括：
1= 个人投资者
103= 机构投资者
104= 自营交易
54
Side
买卖方向，取值： 1 表示买， 2 表示卖
Y
C1
8500
OrderEntryTime
订单申报时间， ExecType=F 时有效
N
ntime
44
Price
申报价格， ExecType=0/4/8 时有效
N
price
38
OrderQty
申报数量
Y
quantity
151
LeavesQty
剩余数量
Y
quantity
31
LastPx
成交价格， ExecType=F 时有效
N
price
32
LastQty
成交数量， ExecType=F 时有效
N
quantity
8504
TotalValueTraded
成交金额， ExecType=F 时有效
N
amount
84
CxlQty
撤单数量， ExecType=0/4 时有效
N
quantity
40
OrdType
订单类型， ExecType=0/4/8 时有效
N
C1
59
TimeInForce
订单有效时间类型， ExecType=0/4/8 时有效
N
C1
39
OrdStatus
Y
C1
当前申报的状态，取值有：
0= 已挂单未成交
1= 部分成交
2= 已成交
4= 已撤消
8= 已拒绝
N
C2
544
CashMargin
信用标签，信用交易时填写，取值： XY= 担保
品买卖、 RZ= 融资交易、 RQ= 融券交易、 PC= 平
仓交易
41
OrigClOrdID
原始会员内部订单编号， ExecType=4 时有效
N
C10
103
OrdRejReason
订单拒绝码， ExecType=8 时有效
N
N5
17
ExecID
成交编号， ExecType=F 时有效
N
C16
37
OrderID
交易所订单编号 , 取值为数字， 仅订单申报
成功 ExecType=0 时有效。
Y
C16
1080
RefOrderID
被撤订单交易所订单编号， ExecType=4 时有
效。
N
C16
75
TradeDate
交易日期
Y
date
60
TransactTime
回报时间
Y
ntime
58
Text
用户私有信息，前 12 位有效
N
C32
453
NoPartyIDs
Y
N2
参与方个数，取值 =6 ，后接重复组，依次包含
发起方投资者账户、登录或订阅交易单元、发
起方业务交易单元、发起方营业部代码、结算
会员代码、开放式基金转托管的目标方。
3

交易网关数据接口规范
448
PartyID
发起方投资者帐
户
Y
C13
452
PartyRole
Y
N4
发起
方投
资者
账户
取 5 ，表示当前
PartyID 的取值为
发起方投资者帐
户。
448
PartyID
登录或订阅交易
单元。
Y
C8
452
PartyRole
Y
N4
登录
或订
阅交
易单
元
取 17 ，表示当前
PartyID 的取值为
登录或订阅交易
单元。
448
PartyID
发起方业务交易
单元。
Y
C8
452
PartyRole
Y
N4
发起
方业
务交
易单
元
取 1 ，表示当前
PartyID 的取值为
发起方业务交易
单元。
448
PartyID
发起方营业部代
码
Y
C8
452
PartyRole
Y
N4
发起
方营
业部
代码
取 4001 ，表示当前
PartyID 的取值为
发起方的营业部
代码。
448
PartyID
结算会员代码
Y
C8
452
PartyRole
Y
N4
结算
会员
代码
取 4 ，表示当前
PartyID 的取值为
结算机构代码。
448
PartyID
Y
C3
<span style="color:red">开放式基金转托</span>
<span style="color:red">管的目标方代理</span>
<span style="color:red">人，对方对应的销</span>
<span style="color:red">售人代码，取值</span>
<span style="color:red">000-999</span> <span style="color:red">，</span> <span style="color:red">ApplID=</span>
<span style="color:red">“开放式基金转</span>
<span style="color:red">托管”时有效</span> <span style="color:blue">预留</span>
<span style="color:blue">字段，暂不启用。</span>
452
PartyRole
Y
N4
<span style="color:blue">预留</span>
<span style="color:blue">字段，</span>
<span style="color:blue">暂不</span>
<span style="color:blue">启用</span>
<span style="color:red">开放</span>
<span style="color:red">式基</span>
<span style="color:red">金转</span>
<span style="color:red">托管</span>
<span style="color:red">的目</span>
<span style="color:red">标方</span>
<span style="color:blue">固定</span> 取 30 <span style="color:blue">。</span> <span style="color:red">，表示</span>
<span style="color:red">当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取</span>
<span style="color:red">值为开放式基金</span>
<span style="color:red">转托管的目标方</span>
<span style="color:red">代理人。</span> <span style="color:blue">预留字</span>
<span style="color:blue">段，暂不启用。</span>
8532
DividendSelect <span style="color:red">分红选择方式，ApplID=“开放式基金分红”</span>
<span style="color:red">时有效，。</span> <span style="color:blue">预留字段，暂不启用。</span>
N
C3
3

交易网关数据接口规范
8533
DestSecurity
N
C12
<span style="color:red">转入的标的产品代码，</span>
<span style="color:red">前6 位有效。ApplID=</span>
<span style="color:red">“开放式基金基金转</span>
<span style="color:red">换”、“余券划转”、</span>
<span style="color:red">“还券划转”、“担保</span>
<span style="color:red">品划转”、“券源划转</span>
<span style="color:red">的划转标的证券”时有</span>
<span style="color:red">效。</span> <span style="color:blue">预留字段，暂不启</span>
<span style="color:blue">用。</span>
说明：
1. ExecType 和OrdStatus 组合取值：
申报成功响应： ExecType=0, OrdStatus=0
申报拒绝响应： ExecType=8, OrdStatus =8
撤单成功响应： ExecType=4, OrdStatus =4
成交回报：
ExecType=F, OrdStatus =1/2
2.
OwnerType 、 RefOrderID 暂不启用。
3. TotalValueTraded 字段：如果实际成交金额超过999,999,999.99999 元，则该字段返回
OxFFFFFFFFFFFFFFFF（即对应数值-1），请使用该字段的市场参与者特殊处理，柜台系统应
能识别并及时处理该字段溢出异常，可采取如自行计算或拆分调整，盘后采用登记结算数据
或其他方式处理，做好该异常的识别和处理。
4. TrdCnfmID 字段：成交编号为数字，不足 16 位左侧补 0. 例如若成交编号为 1 ，则填写
为“ 0000000000000001 ”。
4.3.3.2 撤单失败执行报告
标签
字段名
字段描述
必须
类型
消息头
MsgType = 9
10197
PartitionNo
平台内分区号
Y
N4
10179
ReportIndex
执行报告编号，从 1 开始连续递增编号
Y
N16
1180
ApplID
业务类型
Y
C6
11
ClOrdID
会员内部订单编号
Y
C10
48
SecurityID
证券代码
Y
C12
41
OrigClOrdID
原始会员内部订单编号
Y
C10
75
TradeDate
交易日期
Y
date
60
TransactTime
回报时间
Y
ntime
3

交易网关数据接口规范
103
OrdRejReason
撤单订单拒绝码
Y
N5
58
Text
用户私有信息，前 12 位有效
N
C32
453
NoPartyIDs
Y
N2
参与方个数，取值 =3 ，后接重复组，依次包含
登录或订阅交易单元、发起方业务交易单元、
发起方营业部代码。
448
PartyID
登录或订阅交易单元。
Y
C8
452
PartyRole 取 17 ，表示当前 PartyID 的取值为登
录或订阅交易单元。
Y
N4
登录或
订阅交
易单元
448
PartyID
发起方业务交易单元。
Y
C8
452
PartyRole 取 1 ，表示当前 PartyID 的取值为发
起方业务交易单元。
Y
N4
发起方
业务交
易单元
448
PartyID
发起方营业部代码
Y
C8
452
PartyRole 取 4001 ，表示当前 PartyID 的取值为
发起方的营业部代码。
Y
N4
发起方
营业部
代码
说明：
1.
发起方营业部代码暂不启用。
<span style="color:red">4.4</span> <span style="color:red">应用消息</span> <span style="color:red">-</span> <span style="color:red">网络密码服务</span>
<span style="color:red">4.4.1</span> <span style="color:red">网络密码服务申报</span>
<span style="color:red">标签</span>
<span style="color:red">字段名</span>
<span style="color:red">字段描述</span>
<span style="color:red">必须</span>
<span style="color:red">类型</span>
<span style="color:red">消息头</span>
<span style="color:red">MsgType = U006</span>
<span style="color:red">1180</span>
<span style="color:red">ApplID</span>
<span style="color:red">业务类型</span>
<span style="color:red">Y</span>
<span style="color:red">C6</span>
<span style="color:red">11</span>
<span style="color:red">ClOrdID</span>
<span style="color:red">会员内部订单编号</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">48</span>
<span style="color:red">SecurityID</span>
<span style="color:red">产品代码</span>
<span style="color:red">Y</span>
<span style="color:red">C12</span>
<span style="color:red">522</span>
<span style="color:red">OwnerType</span>
<span style="color:red">订单所有者类型</span>
<span style="color:red">Y</span>
<span style="color:red">N3</span>
<span style="color:red">60</span>
<span style="color:red">TransactTime</span>
<span style="color:red">订单申报时间</span>
<span style="color:red">Y</span>
<span style="color:red">ntime</span>
<span style="color:red">58</span>
<span style="color:red">Text</span>
<span style="color:red">用户私有信息，前</span> <span style="color:red">12</span> <span style="color:red">位有效</span>
<span style="color:red">N</span>
<span style="color:red">C32</span>
<span style="color:red">54</span>
<span style="color:red">Side</span>
<span style="color:red">1=激活；2=注销</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">8539</span>
<span style="color:red">ValidationCode</span>
<span style="color:red">投资者在上交所网站注册时所获得的激活</span>
<span style="color:red">码，取值仅在Side=1 时有意义。</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
4

交易网关数据接口规范
<span style="color:red">453</span>
<span style="color:red">NoPartyIDs</span>
<span style="color:red">Y</span>
<span style="color:red">N2</span>
<span style="color:red">参与方个数，取值</span> <span style="color:red">=3</span> <span style="color:red">，后接重复组，依次包含</span>
<span style="color:red">发起方投资者账户、发起方业务交易单元号、</span>
<span style="color:red">发起方营业部代码。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方投资者帐户</span>
<span style="color:red">Y</span>
<span style="color:red">C13</span>
<span style="color:red">发起方</span>
<span style="color:red">投资者</span>
<span style="color:red">账户</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">5</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为</span>
<span style="color:red">发起方投资者帐户。</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方业务交易单元代码，填写</span> <span style="color:red">5</span>
<span style="color:red">位业务交易单元号。</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">发起方</span>
<span style="color:red">业务交</span>
<span style="color:red">易单元</span>
<span style="color:red">号</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">1</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为</span>
<span style="color:red">发起方业务交易单元号。</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方营业部代码</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">发起方</span>
<span style="color:red">营业部</span>
<span style="color:red">代码</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">4001</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值</span>
<span style="color:red">为发起方的营业部代码。</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">说明：</span>
<span style="color:red">1.</span>
<span style="color:red">OwnerType</span> <span style="color:red">暂不启用。</span>
<span style="color:red">4.4.1</span> <span style="color:red">网络密码服务申报响应</span>
<span style="color:red">标签</span>
<span style="color:red">字段名</span>
<span style="color:red">字段描述</span>
<span style="color:red">必须</span>
<span style="color:red">类型</span>
<span style="color:red">消息头</span>
<span style="color:red">MsgType = U008</span>
<span style="color:red">1180</span>
<span style="color:red">ApplID</span>
<span style="color:red">业务类型</span>
<span style="color:red">Y</span>
<span style="color:red">C6</span>
<span style="color:red">11</span>
<span style="color:red">ClOrdID</span>
<span style="color:red">会员内部订单编号</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">48</span>
<span style="color:red">SecurityID</span>
<span style="color:red">证券代码</span>
<span style="color:red">Y</span>
<span style="color:red">C12</span>
<span style="color:red">522</span>
<span style="color:red">OwnerType</span>
<span style="color:red">订单所有者类型</span>
<span style="color:red">Y</span>
<span style="color:red">N3</span>
4

交易网关数据接口规范
<span style="color:red">103</span>
<span style="color:red">OrdRejReason</span>
<span style="color:red">订单拒绝码，当申报成功响应时返回‘0’</span>
<span style="color:red">Y</span>
<span style="color:red">N5</span>
<span style="color:red">75</span>
<span style="color:red">TradeDate</span>
<span style="color:red">交易日期</span>
<span style="color:red">Y</span>
<span style="color:red">date</span>
<span style="color:red">60</span>
<span style="color:red">TransactTime</span>
<span style="color:red">回报时间</span>
<span style="color:red">Y</span>
<span style="color:red">ntime</span>
<span style="color:red">58</span>
<span style="color:red">Text</span>
<span style="color:red">用户私有信息，前12 位有效</span>
<span style="color:red">N</span>
<span style="color:red">C32</span>
<span style="color:red">54</span>
<span style="color:red">Side</span>
<span style="color:red">1=激活；2=注销</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">8539</span>
<span style="color:red">ValidationCode</span>
<span style="color:red">投资者在上交所网站注册时所获得的激活码</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">453</span>
<span style="color:red">NoPartyIDs</span>
<span style="color:red">Y</span>
<span style="color:red">N2</span>
<span style="color:red">参与方个数，取值</span> <span style="color:red">=3</span> <span style="color:red">，后接重复组，依次包含</span>
<span style="color:red">发起方投资者账户、发起方业务交易单元、发</span>
<span style="color:red">起方营业部代码。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方投资者帐户</span>
<span style="color:red">Y</span>
<span style="color:red">C13</span>
<span style="color:red">发起方</span>
<span style="color:red">投资者</span>
<span style="color:red">账户</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">5</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发</span>
<span style="color:red">起方投资者帐户。</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方业务交易单元。</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">发起方</span>
<span style="color:red">业务交</span>
<span style="color:red">易单元</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">1</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发</span>
<span style="color:red">起方业务交易单元。</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方营业部代码</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">发起方</span>
<span style="color:red">营业部</span>
<span style="color:red">代码</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">4001</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值</span>
<span style="color:red">为发起方的营业部代码。</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">说明：</span>
<span style="color:red">1.</span>
<span style="color:red">OwnerType</span> <span style="color:red">暂不启用。</span>
4

交易网关数据接口规范
4. <span style="color:red">5</span> <span style="color:blue">4</span> 其他消息
4. <span style="color:red">5</span> <span style="color:blue">4</span> .1 申报拒绝 Order Reject
标签
字段名
字段描述
必
须
类型
消息头
MsgType = j
1180
ApplID
业务类型
Y
C6
11
ClOrdID
会员内部订单编号
Y
C10
48
SecurityID
证券代码
Y
C12
103
OrdRejReason
订单拒绝码
Y
N5
75
TradeDate
交易日期
Y
date
60
TransactTime
回报时间
Y
ntime
58
Text
用户私有信息，前 12 位有效
N
C32
453
NoPartyIDs
参与方个数，取值 =1 ，后接重复组，依次包含
发起方业务交易单元。
Y
N2
448
PartyID
发起方申报交易单元代码，填写 5
位发起方业务交易单元。
Y
C8
发起方业务
交易单元
452
PartyRole
取 1 ，表示当前 PartyID 的取值为
发起方业务交易单元。
Y
N4
4. <span style="color:red">5</span> <span style="color:blue">4</span> .2 平台状态 PlatformState
标签
字段名
字段描述
必须
类型
消息头
MsgType = U109
10180
PlatformID
平台标识：
0 = 竞价平台
Y
C1
平台状态：
0 = NotOpen ，未开放
1 = PreOpen ，预开放
10181
PlatformStatus
Y
C1
2 = Open ，开放
3 = Break ，暂停
4 = Close ，关闭
4. <span style="color:red">5</span> <span style="color:blue">4</span> .3 执行报告分区信息 ExecRptInfo
标签
字段名
字段描述
必须
类型
消息头
MsgType = U108
10180
PlatformID
平台标识：
Y
C1
4

交易网关数据接口规范
0 = 竞价平台
8561
NoGateWayPBUs
登录或订阅 PBU 数量
Y
N4
8560
→
GateWayPBU
登录或订阅 PBU
Y
C8
10196
NoPartitions
平台内分区数量
Y
N4
10197
→
PartitionNo
平台内分区号
Y
N4
执行报告分区信息提供 Pbu 和分区列表，供 OMS 对执行报告流进行初始化和维护。其
中 Pbu 可能为 OMS 所连接 TDGW 上的登录 PBU ，也可能为该 TDGW 上订阅的其他 PBU （仅
包含订阅成功的 PBU ）， TDGW 在该循环体中首先给出登录 PBU ，后给出订阅的其他 PBU （如
有）。
4. <span style="color:red">5</span> <span style="color:blue">4</span> .4 分区序号同步 ExecRptSync
标签
字段名
字段描述
必须
类型
消息头
MsgType = U106
10196
NoPartitions
循环次数
Y
N4
8560
→
GateWayPBU
登录或订阅 PBU
Y
C8
10197
→
PartitionNo
平台内分区号
Y
N4
8562
→
BeginReportIndex
分区执行报告起始序号
Y
N16
序号同步请求中 BeginReportIndex 取值应大于 0 。 OMS 应避免频繁发送“分区序号同步”
请求，禁止定时或不必要的反复同步行为。
4. <span style="color:red">5</span> <span style="color:blue">4</span> .5 分区序号同步响应 ExecRptSyncRsp
标签
字段名
字段描述
必须
类型
消息头
MsgType = U107
10196
NoPartitions
循环次数
Y
N4
8560
→
GateWayPBU
登录或订阅 PBU
Y
C8
10197
→
PartitionNo
平台内分区号
Y
N4
8562
→
BeginReportIndex
分区执行报告起始序号
Y
N16
8563
→
EndReportIndex
分区执行报告最大序号
Y
N16
103
→
OrdRejReason
分区序号同步拒绝码
Y
N5
58
→
Text
描述
Y
C64
分区序号同步响应中 OrdRejReason 为 0 时表示成功，其他取值表示错误（如 Pbu 或
PartitionNo 取值不正确）。
4

交易网关数据接口规范
4. <span style="color:red">5</span> <span style="color:blue">4</span> .6 分区执行报告结束 ExecRptEndOfStream
标签
字段名
字段描述
必须
类型
消息头
MsgType = U110
8560
GateWayPBU
交易网关登录或订阅 PBU
Y
C8
10197
PartitionNo
平台分区号
Y
N4
8563
EndReportIndex
分区执行报告最大序号，本消息编入该分区执
行报告编号序列。
Y
N16
TDGW 在闭市后向 OMS 自动发送一次，表示该执行报告流推送结束，后续该执行报告
流上的序号将不再增加，最大序号为 EndReportIndex 。
4

交易网关数据接口规范
第五章 附录
5.1 附一 计算校验和
以下为计算校验和的代码段：
uint32 CalcChecksum(const char* buffer, uint32 len)
{
uint8 checksum = 0;
uint32 i = 0;
for (i = 0; i < len; i++)
{
checksum += (uint8)buffer[i];
}
return (uint32)checksum;
}
5.2 附二 PBU 及说明
涉及 PBU 时有几种含义：
1. 配置于 TDGW 上用于登录至交易系统后台的登录单位，称为登录交易单元；
2. 在消息报文中，表明该消息所进行的业务归属单元，称为业务交易单元，接口文档中
用 BizPbu 指代；
3. 在消息报文中，表明与另一登录 PBU 间的订阅关系，称为订阅交易单元。
目前，业务交易单元必须与登录交易单元属于同一市场参与者机构，否则交易系统将拒
绝相应的业务申报请求。订阅 PBU 必须与登录 PBU 属于同一市场参与者机构，否则将订阅
失败，在执行报告分区信息 ExecRptInfo 消息中将不会包含订阅失败的交易单元。
4

交易网关数据接口规范
5.3 附三 错误代码说明
状态码 / 错误码
说明
Text （如有）
0
正常退出
Normal Logout
4012
SecurityID 错误或者业务类型 BizID 错误
5000
上行消息超过 4K
Message Exceed Max Length
5001
上行消息校验和错误
CheckSum Error
5002
心跳超时
Heartbeat Timeout
5003
平台已有 OMS 登录
Already Login, try again
5004
连接建立后 5 秒内未完成登录
Login Timeout
5005
上行消息 TargetCompId 不正确
CompId Error
5006
TDGW 未登录至交易系统，请稍后重试
Not Ready
5007
内部错误
Internal Error
5008
不能识别的消息类型
Message Type Illegal
5009
平台状态暂不接受申报
5010
PartitionNo 错误
5011
Pbu 错误
5012
首个消息非是 Logon 消息
Login First
5013
BeginReportIndex 取值错误
5014
不支持的接口协议版本
UnsupportedPrtclVersion
5015
消息数据错误
Message Data Error
5016
ClOrdID 取值错误
注：本表仅提供交易网关错误码，系统后台错误码参照每日发送的竞价平台错误码信息文
件。
5.4 附四 “用户私有信息”说明
对于应用消息中的“用户私有信息”字段，有如下规则：
1. TDGW 返回给 OMS 的下行消息中“用户私有信息”，取该条下行消息所对应的上行
消息（由 OMS 发送给 TDGW ）中的“用户私有信息”字段值。
4

交易网关数据接口规范
5.5 附五 价格数量字段说明
现货竞价交易
其他
MsgType=
8
字段
限价
市转
撤
市转
限
本方
最优
对手方
最优
其他
Price 申报价
格
申报
信息
申报
信息
申报
信息
申报
信息
申报信
息
申报信
息
OrderQty 申报
数量
申报
信息
申报
信息
申报
信息
申报
信息
申报信
息
申报成功
响应
申报信
息
LeavesQty 剩
余数量
无意
义
无意
义
转限
数量
转限
数量
转限数
量
无意义
CxlQty 撤单数
量
无意
义
撤单
数量
无意
义
无意
义
无意义
无意义
申报失败
响应
Price 申报价
格
申报信息
申报信
息
OrderQty 申报
数量
申报信息
申报信
息
LeavesQty 剩
余数量
无意义
无意义
CxlQty 撤单数
量
无意义
无意义
撤单成功
响应
Price 申报价
格
被撤原申报（市价单填0）
被撤原
申报
OrderQty 申报
数量
被撤原申报
被撤原
申报
LeavesQty 剩
余数量
无意义
无意义
CxlQty 撤单数
量
撤单数量
无意义
5.6 附六 融资融券
投资者要进行融资融券信用交易，需向具备融资融券业务资格的证券公司申请，开设 E
字头的 “ 投资者信用证券账户 ” 。
开展融券业务的证券公司必须在中登公司开设 “ 证券公司融券专用账户 ” ，存放自有证券，
供投资者进行融券交易。证券公司融券专用账户不得进行任何申报。
开展融券业务的证券公司还必须在中登公司开设 “ 证券公司信用交易担保证券账户 ” ，该
帐户与 “ 投资者信用证券账户 ” 之间是总帐与二级明细帐的关系，用于记载投资者委托证券公
司持有的担保证券的明细数据，对应明细数据由中登公司维护。证券公司信用交易担保证券
4

交易网关数据接口规范
账户不得进行任何申报。
投资者信用证券账户可申报的非交易业务包括：发行（具体参考交易所通知）、配股 /
科创板配售、配转债 <span style="color:red">和</span> <span style="color:red">4</span> <span style="color:red">种证券划转业务（余券划转、还券划转、担保品划入、担保品划</span>
<span style="color:red">出）</span> 。
融资融券信用交易业务，仅供投资者信用证券账户申报，且必须带信用标签，信用标签
使用说明如下：
信用交易
CreditTag
Side
SecurityID
担保品买入
XY
1
担保品标的
担保品卖出
2
股票、封闭式基金、 ETF 、国债、可转债
融资买入
RZ
1
融资买入标的
卖券还款
2
股票、封闭式基金、 ETF 、国债、可转债
融券卖出
RQ
2
融券卖出标的
买券还券
1
买券还券标的
平仓买入
PC
1
买券还券标的
平仓卖出
2
股票、封闭式基金、 ETF 、国债、可转债
注：融券卖出不支持市价订单。
4

> **变更标注说明**：本文档中已用 `<span style="color:...">` 标注了变更内容（红色=修改/新增，蓝色=其他说明）。


<metadata>
{
  "title": "20230928_IS122_上海证券交易所交易网关STEP接口规格说明书（竞价平台）0",
  "source_url": null,
  "raw_path": "knowledge\\raw\\sse\\测试文档\\20230928_IS122_上海证券交易所交易网关STEP接口规格说明书（竞价平台）0.57版（竞价非交易迁移互联网_技术开发稿）_20230926.pdf",
  "markdown_path": "knowledge\\articles\\sse\\markdown\\测试文档\\IS122_上海证券交易所交易网关STEP接口规格说明书（竞价平台）0.57版（竞价非交易迁移互联网_技术开发稿）_20.md",
  "file_hash": "sha256:367a2b70114d689141da9afa7dfc9042afe2a9da434a81c259a403baf0c58200",
  "file_format": "pdf",
  "page_count": 49,
  "doc_type": "interface_spec",
  "version": null,
  "previous_version": null,
  "public_date": "2021-04-15",
  "effective_date": null,
  "has_changes": true,
  "parse_status": "success",
  "parse_date": "2026-06-13T17:45:30.997060+00:00",
  "sub_category": null
}
</metadata>