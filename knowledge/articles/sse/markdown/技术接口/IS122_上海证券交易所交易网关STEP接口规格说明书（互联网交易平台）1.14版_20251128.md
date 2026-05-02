上海证券交易所
交易网关 STEP 接口规格说明书
（互联网交易平台）
V1.14
二〇二五年十一月

交易网关数据接口规范
文档版本
日期
版本
状态
说明
2021-07
0.10
开发稿
创建文档。
2021-09
0.20
开发稿
增加基金通业务接口
2022-02
0.30
开发稿
（ 1 ）更新消息头的填写说明
（ 2 ）新订单申报中申报价格修改为非必填，对基金通
报价交易，申报价格必填；基金通转入转出，申报价
格为空；
2022-02
1.00
正式稿
1. 增加询价业务类接口
2. 增加订阅机制
2022-04
1.10
开发稿
3. 转入转出不支持撤单
1. 修改消息流图：报价方撤销报价处理，删除撤单成
功执行报告；
2. 修改报价、报价状态回报、转发报价 tag 453 后接重
复组字段表述，“询价”修改为“报价”
2022-07
1.11
开发稿
3. 修改 tag 693 QuoteRespID 字段类型为 C18
4. 删除报价状态回报（ Quote Status Report ）中 tag 693
QuoteRespID
5. 报价回复新增字段： tag131 QuoteReqID ，用于匹配
成交
1. 询价申报中订单价格上下限字段，增加字段说明“预
留，暂不启用”
2. 调整询价处理消息流图：转发询价请求、转发报价
请求去掉 orderID ；报价撤销成功回报去掉
ordID=or00003 ；报价撤销成功回报的报价状态调整为
2022-08
1.12
正式稿
QuoteStatus=Cancelled
3. 转发询价请求、转发报价请求不再提供 orderID ，字
段调整为非必填
4. 询价状态回报、报价状态回报中 OrderID 调整为非
必填，补充字段说明
2025-08
1.13
正式稿
1. 要约 / 现金选择权（要约预受 / 现金选择权登记、要约
撤销 / 现金选择权注销）、开放式基金相关业务（申赎、
分红选择、份额转出）、融资融券非交易业务（余券
划转、还券划转、担保品划入、担保品划出、券源划
入、券源划出）、网络密码服务（密码激活 / 注销），
从竞价撮合平台迁移至互联网交易平台。
2. 4.4.1.1 章节中，订单类型字段改为非必填；参与方
个数取值改为 11 ，其中结算会员代码改为非必填；变
2

交易网关数据接口规范
更发起方营业部代码范围及说明、结算会员代码字段
填写说明。
3. 4.4.1.2 章节中，参与方个数变更；
4. 4.4.3.1.1 章节中，参与方个数变更，结算会员代码
改为非必填。
<span style="color:red">2025-11</span>
<span style="color:red">1.14</span>
<span style="color:red">正式稿</span>
<span style="color:red">1.</span> <span style="color:red">基于《</span> <span style="color:red">IS101</span> <span style="color:red">上海证券交易所竞价撮合平台市场参与</span>
<span style="color:red">者接口规格说明书》文档正式废止，相关内容迁移至</span>
<span style="color:red">《</span> <span style="color:red">IS124</span> <span style="color:red">上海证券交易所市场数据文件交换接口规格</span>
<span style="color:red">说明书》，更新相关引用描述。</span>
3

交易网关数据接口规范
目录
第一章前言 ...................................................................................................................................... 6
1.1 目的 ..................................................................................................................................... 6
1.2 术语和定义 ......................................................................................................................... 6
1.3 参考文档 ............................................................................................................................. 6
1.4 联系方式 ............................................................................................................................. 7
第二章系统简介 .............................................................................................................................. 8
2.1 系统接入 ............................................................................................................................. 8
2.2 业务范围 ............................................................................................................................. 8
第三章交互机制 ............................................................................................................................ 10
3.1 会话机制 ........................................................................................................................... 10
3.1.1 建立会话 ................................................................................................................10
3.1.2 关闭会话 ................................................................................................................10
3.1.3 维持会话 ................................................................................................................ 11
3.1.4 其他约定 ................................................................................................................ 11
3.2 申报与回报 ....................................................................................................................... 11
3.2.1 业务类型 ................................................................................................................12
3.2.2 消息流图 ................................................................................................................13
3.2.3 平台状态 ................................................................................................................19
3.2.4 重复订单 ................................................................................................................20
3.2.5 执行报告 ................................................................................................................21
3.3 恢复场景 ........................................................................................................................... 22
3.4 订阅机制 ........................................................................................................................... 23
第四章消息定义 ............................................................................................................................ 24
4.1 消息结构与约定 ...............................................................................................................24
4.2 数据类型 ........................................................................................................................... 24
4.2.1 STEP 格式约定 .......................................................................................................25
4.2.2 STEP 消息头 ...........................................................................................................25
4.2.3 STEP 消息尾 ...........................................................................................................26
4.2.4 STEP 消息完整性 ...................................................................................................26
4.3 会话消息 ........................................................................................................................... 26
4.3.1 登录消息（ MsgType=A ） ....................................................................................26
4.3.2 注销消息（ MsgType=5 ） .....................................................................................27
4.3.3 心跳消息（ MsgType=0 ） .....................................................................................28
4.3.4 测试请求消息（ MsgType=1 ） ............................................................................ 28
4.3.5 重发请求消息（ MsgType=2 ） ............................................................................ 28
4.3.6 会话拒绝消息（ MsgType=3 ） ............................................................................ 29
4.3.7 序号重设消息（ MsgType=4 ） ............................................................................ 29
4.4 应用消息 ........................................................................................................................... 30
4.4.1 订单业务类 ............................................................................................................30
4.4.2 询价业务类 ............................................................................................................36
4.4.3 执行报告类 ............................................................................................................48
4.4.4 网络密码服务（ Password Service ） ................................................................... 53
4.4.5 其它消息 ................................................................................................................55
4

交易网关数据接口规范
第五章
附录 .................................................................................................................................. 58
5.1 附一
计算校验和 ...........................................................................................................58
5.2 附二
PBU 及说明 .......................................................................................................... 58
5.3 附三
错误代码说明 .......................................................................................................59
5.4 附四
“用户私有信息”说明 .......................................................................................59
5

交易网关数据接口规范
第一章前言
1.1 目的
本接口规范描述了上海证券交易所（以下称本所）交易网关与市场参与者系统之间以
STEP 协议进行交易数据交换时所采用的交互机制、消息格式、消息定义和数据内容。目前，
本接口规范仅适用于本所互联网交易平台提供的各类业务。
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
ITCS
Internet Trade Communication Server
互联网交易平台通信服务器
STEP
Securities Trading Exchange Protocol
证券交易数据交换协议
1.3 参考文档
名称
<span style="color:red">《</span> <span style="color:red">IS101</span> <span style="color:red">上海证券交易所竞价撮合平台市场参与者接口规格说明书》</span>
《 IS111 上海证券交易所报盘软件错误代码表》
6

交易网关数据接口规范
1.4 联系方式
技术服务 QQ 群： 298643611
技术服务电话 : 4008888400-2 (8:00-20:00)
电子邮件：
tech_support@sse.com.cn
技术服务微信公众号： SSE-TechService ( 回复 00 进入
人工服务 )
7

交易网关数据接口规范
第二章系统简介
2.1 系统接入
为满足业务发展需求和提升交易服务水平，本所通过交易网关（ TDGW ）对接互联网交
易平台系统，提供实时交易流接口。 TDGW 对接交易系统及市场参与者系统（ OMS ）的示
意图如下：
TDGW 通过交易业务单元（ PBU ）登录并接入交易系统， PBU 的配置由用户提前在
TDGW 端完成。
TDGW 每个平台开放一个端口供 OMS 建立会话， TDGW 仅接受 OMS 为每个平台建立
一个 TCP/IP 连接，每个连接仅允许建立一个有效的会话。该会话既用于接收 OMS 的业务
申报，又向 OMS 推送交易所接收申报后产生的回报数据。
OMS 与 TDGW 间的连接为标准 TCP/IP 连接，由 OMS 负责发起。 OMS 与 TDGW 之间
传输的数据是非加密的，数据传输的安全性由部署的网络予以保证。
附录二对术语 PBU 在不同场景下的使用进行了说明。
2.2 业务范围
目前支持互联网交易平台相关业务：
8

交易网关数据接口规范
平台
业务
业务申报时间
基金通报价交易
基金通转入转出
基金通询价交易
开放式基金业务（申购、赎
回、转托管转出、分红选择）
要约预受 / 现金选择权登记
9:30-11:30
互联网交易平台
13:00-15:00
要约撤销 / 现金选择权撤销
融资融券业务（余券划转、
还券划转、担保品划转、券
源划转）
网络密码服务
9

交易网关数据接口规范
第三章交互机制
3.1 会话机制
OMS 与 TDGW 间的会话消息包括登录 Logon 、注销 Logout 和心跳 Heartbeat 等消息。
3.1.1 建立会话
OMS 负责发起到交易网关的 TCP 连接，并在连接建立后发送 Logon 消息。 OMS 连接
后的首个消息必须是 Logon 消息。如果登录成功， TDGW 返回一个 Logon 消息作为确认；
如果失败， TDGW 返回一个含失败原因的 Logout 消息，并由 OMS 关闭连接。 OMS 只应在
收到 TDGW 的登录成功确认后才能发送其他消息。
3.1.2 关闭会话
会话建立成功后，连接双方均可发送 Logout 注销消息，告知对端将关闭会话，一般地，
接收方应回复一个 Logout 消息作为回应。 Logout 的发起方在收到回应后关闭连接。如果超
过 5 秒没有收到对方回传的 Logout 消息，注销发起方也可直接关闭连接。连接双方在发送
10

交易网关数据接口规范
Logout 消息后不应再发送任何消息。
3.1.3 维持会话
在消息交换的空闲期间，连接双方通过 Heartbeat 心跳消息维持会话，即连接的任何一
方在心跳时间间隔内若没有发送任何消息，需要产生并发送一个 Heartbeat 消息。
心跳间隔通过登录过程进行协商，以登录成功后 TDGW 返回的登录确认消息中的
HeartBtInt 域为准。一般地，当 OMS 发送 Logon 消息中的 HeartBtInt 取值属于 [5,60] 时， TDGW
返回原值，否则取边界值（ 5 或 60 ）。
接收方接收到任何消息（不仅仅是心跳）可重置读心跳间隔计数。若接收方在 5 个心跳
间隔内未收到任何消息，则可以认为会话出现异常并立即关闭连接。 OMS 关闭连接后，可
重新发起会话或切换至其他 TDGW 。
3.1.4 其他约定
TDGW 在未成功登录至交易系统时， OMS 将无法成功与 TDGW 建立会话； TDGW 与
ITCS 连接断开时， TDGW 将注销与 OMS 间的会话，此时 OMS 应稍后尝试重建会话，或切
换至备用 TDGW 服务。
此外， TDGW 在以下情况下会主动断开与 OMS 间的连接：

OMS 与 TDGW 建立 TCP 连接之后，超过 5 秒未完成登录；

OMS 在登录失败之后，未在 5 秒内关闭连接；

OMS 在发起注销后，未在 5 秒内关闭连接；

OMS 未能及时处理 TDGW 下行消息，导致 TDGW 内积压的待发送消息超过特定
阈值；

TDGW 与 ITCS 间的连接已经断开；
3.2 申报与回报
OMS 进行的新订单申报（ New Order Single ）、询价请求（ Quote Request ）、报价（ Quote ）
时，本所交易系统会进行前置检查，若检查未通过将返回订单拒绝（ Order Reject ）、询价
请求响应（ Quote Request Ask ）和报价状态回报（ QuoteStatusReport ）消息。
11

交易网关数据接口规范
对于通过前置校验的申报，交易系统根据业务的不同，向 OMS 返回相应的执行报告
（ Execution Report ）、转发询价请求（ AllegeQuote Request ）和转发报价（ Allege Quote ）消
息。执行报告包括对申报的确认，如对新订单的确认或拒绝响应 1 、撤单响应等；如产生成
交时（包括新订单申报及询价请求），执行报告中会包含成交确认。
总体示意图如下：
3.2.1 业务类型
订单申报需要指定业务类型（ ApplID ），其产生的回报以不同的执行报告分区
（ PartitionNo ）划分为多个逻辑上相互独立的数据流。根据具体业务的不同，下表给出业务
类型、分区的对应关系，并明确业务相关属性。
业务类型
执行报告分区
业务
消息类型
支持
撤单
申报
确认
成交
确认
(MsgType)
(ApplID)
(PartitionNo)
基金通报价交易
D
600020
602-607
Y
Y
Y
基金通转入转出
D
600021
602-607
N
Y
Y
基金通询价交易
R （询价）
S （报价）
600022
602-607
Y
Y
Y
1 除前置检查未通过返回Reject 外，执行报告中也包含有因业务校验未通过产生的拒绝响应Execution Report
（ExecType=8）。
12

交易网关数据接口规范
开放式基金申购
D
600030
608-613
Y
Y
N
开放式基金赎回
D
600040
608-613
Y
Y
N
开放式基金转托管转
出
D
600050
608-613
Y
Y
N
开放式基金分红选择
D
600060
608-613
Y
Y
N
要约预受 / 现金选择
权登记
D
600070
608-613
Y
Y
N
要约撤销 / 现金选择
权撤销
D
600071
608-613
Y
Y
N
融资融券余券划转
D
600080
608-613
Y
Y
N
融资融券还券划转
D
600090
608-613
Y
Y
N
融资融券担保品划入
D
600100
608-613
Y
Y
N
融资融券担保品划出
D
600101
608-613
Y
Y
N
融资融券券源划入
D
600110
608-613
Y
Y
N
融资融券券源划出
D
600111
608-613
Y
Y
N
网络密码服务
U006
600120
N
Y
N
注：
1 、 Y 为是， N 为否。
2 、网络密码服务业务，申报响应消息不进执行报告（ Execution Report ）。
3.2.2 消息流图
3.2.2.1 新订单处理消息流图
3.2.2.1.1 新订单申报
适用于互联网交易平台。
订单（ OrdType=2 ）消息流如下：
13

交易网关数据接口规范
暂不支持市价订单。
3.2.2.1.2 新订单撤单
支持撤单的业务类型见前述章节业务类型表。
14

交易网关数据接口规范
3.2.2.2 询价处理消息流图
询价交易可以分为两个阶段：询价阶段、报价阶段。
在询价阶段，询价方申报询价请求，交易系统转发询价请求给报价方（一个或多个），
报价方可以选择进行报价也可以不进行报价。若报价方不进行报价，询价在超时后会自动失
效，整个交易过程结束。
在报价阶段，报价方对询价请求进行报价，交易系统将报价转发给询价方。若报价方想
要修改报价，需将原报价撤销后重新发起报价。询价方可以选择接受或不接受报价方的报价。
若询价方接受报价，则申报一笔报价回复，交易系统对报价及报价回复进行撮合成交并发送
成交回报执行报告，同时转发询价撤销消息告知其余报价方。若询价方不接受报价，报价在
询价失效后也自动失效。
询价未成交前，询价方可以撤销询价。报价未成交前，报价方可以撤销报价。若询价交
易超过总时长仍未成交，则需通过询价请求响应及报价状态回报将失效消息转发至相关方。
15

交易网关数据接口规范
3.2.2.2.1 询价方撤销询价请求处理
OMS1
TDGW
OMS2
询价请求
（ Quote Request,MsgType=R ）
询价方发起询价请求
QuoteReqID=qr00001
QuoteRequestTransType=New
ClOrdID=c00001
转发给报价方
询价请求响应
（ Quote Request,MsgType=R ）
转发询价请求
（ Quote Request Ack,MsgType=R ）
QuoteReqID=qr00001
QuoteRequestTransType=New
QuoteReqID=uqr00001
QuoteRequestTransType=New
QuoteRequestType=Submit
QuoteRequestStatus=Accepted
QuoteRequestType=Alleged
QuoteRequestStatus=Accepted
OrderID=or00001
报价
（ Quote,MsgType=S ）
报价方发起报价
QuoteReqID=uqr00001
QuoteMsgID=qm00001
QuoteID=q00001
QuoteType=Tradable
报价状态回报
（ Quote Status Report,,MsgType=AI ）
转发报价
（ Allege Quote,MsgType=S ）
转发给询价方
QuoteReqID=qr00001
QuoteMsgID=qm00001
QuoteID=uq00001
QuoteType=Tradable
QuoteID=q00001
QuoteType=Tradable
OrderID=or00002
询价请求
（ Quote Request,MsgType=R ）
询价方撤销询价
请求
QuoteReqID=qr00001
QuoteRequestTransType=Cancel
ClOrdID=c00002
询价请求响应
（ Quote Request,MsgType=R ）
Reject
QuoteReqID=qr00001
QuoteStatus=Rejected
QuoteRequestRejectReason=20001
询价请求响应
（ Quote Request,MsgType=R ）
转发询价请求
（ Quote Request Ack,MsgType=R ）
Accept
通知报价方询价
已被撤销
QuoteReqID=uqr00001
QuoteRequestTransType=Cancel
QuoteReqID=qr00001
QuoteType=Tradable
QuoteRequestTransType=Cancel
QuoteRequestType=Alleged
QuoteRequestStatus=Cancelled
QuoteRequestType=Submit
QuoteRequestStatus=Accepted
OrderID=or00001
16

交易网关数据接口规范
3.2.2.2.2 报价方撤销报价处理
OMS1
TDGW
OMS2
询价请求
（ Quote Request,MsgType=R ）
询价方发起询价请求
QuoteReqID=qr00001
QuoteRequestTransType=New
ClOrdID=c00001
转发询价请求
（ Quote Request Ack,MsgType=R ）
询价请求响应
（ Quote Request,MsgType=R ）
转发给报价方
QuoteReqID=uqr00001
QuoteRequestTransType=New
QuoteReqID=qr00001
QuoteRequestTransType=New
QuoteRequestType=Alleged
QuoteRequestStatus=Accepted
QuoteRequestType=Submit
QuoteRequestStatus=Accepted
OrderID=or00001
报价方发起报价
报价
（ Quote,MsgType=S ）
QuoteReqID=uqr00001
QuoteMsgID=qm00001
QuoteID=q00001
QuoteType=Tradable
报价状态回报
（ Quote Status Report,MsgType=AI ）
转发报价
（ Allege Quote,MsgType=S ）
转发给询价方
QuoteMsgID=qm00001
QuoteReqID=qr00001
QuoteID=q00001
QuoteType=Tradable
QuoteID=uq00001
QuoteType=Tradable
OrderID=or00002
报价撤销
（ Quote,MsgType=S ）
报价方发起报价撤销
QuoteReqID=uqr00001
QuoteMsgID=qm00002
QuoteID=q00001
BidSize=0
OfferSize=0
报价状态回报
（ Quote Status Report,MsgType=AI ）
Reject
QuoteMsgID=qm00002
QuoteID=q00001
QuoteRejectReason=5011
报价状态回报
（ Quote Status Report,MsgType=AI ）
Accept
转发报价
（ Allege Quote,MsgType=S ）
QuoteMsgID=qm00002
转发给询价方
QuoteReqID=qr00001
QuoteID=q00001
QuoteStatus=Cancelled
OuoteType=Tradable
QuoteID=uq00001
QuoteType=Tradable
BidSize=0
OfferSize=0
17

交易网关数据接口规范
3.2.2.2.3 询价方与报价方成交
OMS1
TDGW
OMS2
询价请求
（ Quote Request,MsgType=R ）
询价方发起询价请求
QuoteReqID=qr00001
QuoteRequestTransType=New
ClOrdID=c00001
转发询价请求
（ Quote Request Ack,MsgType=R ）
询价请求响应
（ Quote Request,MsgType=R ）
转发给报价方
QuoteReqID=uqr00001
QuoteRequestTransType=New
QuoteReqID=qr00001
QuoteRequestTransType=New
QuoteRequestType=Alleged
QuoteRequestStatus=Accepted
QuoteRequestType=Submit
QuoteRequestStatus=Accepted
OrderID=or00001
报价方发起报价
报价
（ Quote,MsgType=S ）
QuoteReqID=uqr00001
QuoteMsgID=qm00001
QuoteID=q00001
QuoteType=Tradable
报价状态回报
（ Quote Status Report,MsgType=AI ）
转发报价
（ Allege Quote,MsgType=S ）
转发给询价方
QuoteMsgID=qm00001
QuoteReqID=qr00001
QuoteID=q00001
QuoteType=Tradable
QuoteID=uq00001
QuoteType=Tradable
OrderID=or00002
报价回复
（ Quote Response,MsgType=AJ ）
询价方接受报价
QuoteRespID=qrp00001
ClOrdID=c00002
QuoteID=uq00001(点击成交)/QuoteReqID=qr00001
（匹配成交）
QuoteRespType=Hit/Lift
报价状态回报
（ Quote Status Report,MsgType=AI ）
Reject
QuoteRespID=qrp00001
QuoteID=uq00001（点击成交）/QuoteReqID=qr00001
（匹配成交）
QuoteStatus=Rejected
QuoteRejectReason=5011
报价状态回报
（ Quote Status Report,MsgType=AI ）
Accept
QuoteRespID=qrp00001
QuoteID=uq00001（点击成交）/QuoteReqID=qr00001
（匹配成交）
QuoteStatus=Accepted
QuoteMsgID=c00002
OrderID=or00003
成交报告
（ MsgType=8 ）
询价方成交
成交报告
（ MsgType=8 ）
报价方成交
OrderID=or00003
ClOrdID=c00002
OrderID=or00002
ClOrdID=qm00001
ExecID=e00001
ExecID=e00001
OrdStatus=2
OrdStatus=2
ExecType=F
ExecType=F
转发询价请求
（ Quote Request Ack,MsgType=R ）
通知其他报价方询价
已被撤销
QuoteReqID=uqr00001
QuoteRequestTransType=Cancel
QuoteRequestType=Alleged
QuoteRequestStatus=Cancelled
18

交易网关数据接口规范
3.2.2.3 网络密码服务处理消息流图
3.2.3 平台状态
OMS 向 TDGW 进行申报应符合交易时间表 2 要求。 TDGW 依据交易时间表对平台状态
进行了划分，示意图如下。
处于 NotOpen 、 Break 、 Close 状态时不接收申报， TDGW 返回 Order Reject
（ OrdRejReason=5009 ）予以拒绝。 PreOpen 3 状态下， TDGW 提前接收 OMS 的申报，并在
2 时间表以本所交易规则为准。
3 目前，设置 PreOpen 为各交易时段 Open 前的 5 秒。以交易时段 9:15-9:25 为例， 9:14:55TDGW 转为 PreOpen ， 9:15:00 TDGW
转为 Open 状态。
19

交易网关数据接口规范
Open 时向交易系统转发。 PreOpen 及 Open 状态下 TDGW 接收的申报是否被交易系统主机
接受， OMS 应以申报确认为准。
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
3.2.4 重复订单
交易系统依据申报中的业务 PBU + 会员内部订单编号组合的取值判断申报是否为重复
订单 ; 其中，业务 PBU 取 Parties 组件中 PartyID 字段（当 PartyRole=1 ）。
会员内部订单编号取消息类型相应字段：
申报类型
会员内部订单编号字段
New Order Single
ClOrdID
Order Cancel
ClOrdID
QuoteRequest
ClOrdID
Quote
QuoteMsgID
Quote Response
ClOrdID
Password Service
ClOrdID
对于重复订单， TDGW 返回拒绝消息（ Order Reject ）。
20

交易网关数据接口规范
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
为 OMS 所连接的 TDGW 上正在登录的 PBU ；若 TDGW 配置了订阅，该字段取值也可能为
被订阅的其他 PBU ，详见后续订阅章节的说明。
在每个 PBU 下，执行报告根据分区（ PartitionNo ）划分为多个编号相互独立的数据流。
在一个交易日内，每个执行报告流中的 ReportIndex 由 1 开始连续递增。多个不同业务可以
属于同一个分区，从而在同一个流中按序发送。
OMS 与 TDGW 建立会话后， TDGW 会向 OMS 推送执行报告分区信息（ ExecRptInfo ）
消息，其中包含 PBU 列表和分区列表， OMS 应根据此信息维护多个逻辑上的执行报告流。
OMS 与 TDGW 建立会话后，应根据 ExecRptInfo 中的信息，向 TDGW 发送各个执行报
告流的分区序号同步（ ExecRptSync ）消息， TDGW 将返回一个分区序号同步响应消息
（ ExecRptSyncRsp ）进行回应。对于 ExecRptSync 请求校验通过的情况， TDGW 将依据其
中约定的序号 BeginReportIndex 发送后续执行报告。
OMS 若不发送序号同步消息， TDGW 将不会推动执行报告。如果 OMS 发送的序号同
21

交易网关数据接口规范
步消息中， BeginReportIndex 大于实际存在的分区回报最大序号，则 TDGW 不会推送执行
报告，直至实际分区回报数确实达到 BeginReportIndex 后再开始推送。闭市后， TDGW 不
再接收 OMS 申报，但可以通过序号同步消息重新获取当日历史执行报告数据。
OMS 应对 TDGW 推送的执行报告进行数据持久化操作，且 OMS 应具备识别重复执行报告
的能力，避免重复处理。
OMS
TDGW
Logon
登录
Logon
PlatformState
平台状态
ExecRptInfo
执行报告信息
Pbu=20001, SetID=1
ExecRptSync
序号同步请求
20001, 1, BeginReportIndex=1
20001, <span style="color:red">2</span> , BeginReportIndex=100
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
在 OMS 重新与 TDGW 建立会话后，由于断连期间可能存在传输中的消息丢失， OMS
应对上下行两个方向的消息进行恢复。建议 OMS 先对执行报告进行恢复，以尽可能更新断
连前申报订单的状态。 OMS 可在恢复一段时间后，对仍然处于“已报但未确认”状态的订
单进行重新申报。
22

交易网关数据接口规范
TDGW 与 ITCS 断开
TDGW 与 ITCS 间连接断开时， TDGW 将通过 Logout （ SessionStatus=5006 ）消息注销
与 OMS 间的会话，并尝试切换备用 ITCS 。在 TDGW 未登录至交易系统期间， OMS 发起到
TDGW 的会话将无法成功。 TDGW 恢复登录，且 OMS 重建与 TDGW 间的会话后， OMS
对消息的恢复处理可与上一节描述相同。
3.4 订阅机制
通过在 TDGW 端进行配置， OMS 可通过与一个 TDGW 间的会话，接收到其他 TDGW
上登录的另一 PBU 所产生的执行报告数据。
TDGW 端登录的 PBU-B ，若需订阅另一 TDGW 上登录的 PBU-A 所产生的执行报告，
PBU-B 与 PBU-A 需要属于同一市场参与者机构。
目前，交易系统限制每个登录 PBU 可被最多 3 个其他登录 PBU 订阅成功。为减少订阅
对登录 PBU 自身回报数据处理的影响， TDGW 将优先发送登录 PBU 自身的回报数据。
在同一市场参与者机构的范围内，订阅的配置和管理由市场参与者机构负责，市场参与
者机构在充分利用订阅形成 TDGW 互备的同时，也应做好订阅权限和数据权限的控制。
23

交易网关数据接口规范
第四章消息定义
4.1 消息结构与约定
每一条 STEP 消息由消息头、消息体和消息尾组成，消息最大长度为 4K 字节。
4.2 数据类型
数据类型相关说明如下：
1. 字符串类型用 CX 表示， X 表示字符串最大字节数，除特别声明，字符串只包含数
字、大写字母、小写字母以及空格；字符串实际长度小于字段类型最大长度时可以不补空格；
字符串统一采用 ASCII 编码。
2. 十进制整数用 NX 表示， X 表示整数最大位数（不包括正负号），除特殊说明，整
数类型均有正负。
3. 浮点数用 NX （ Y ）表示， X 表示整数与小数总计位数（不包括小数点及正负号），
Y 表示小数位数，小数位数不足时必须在后面补 0 ，除非特殊说明，浮点数类型均有正负。
4. 数值类型字段默认填 0 值，字符串类型默认填空格；针对“暂不启用”字段，填写
默认值。
5. 针对部分字段填写固定值的场景，固定值根据实际字段类型进行填写。如字段要求
“固定填 1 ”，若字段类型为 N13(5) ，则实际填写 1.00000 ；若字段类型为 C1 ，则实际填写
字符‘ 1 ’。
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
YYYY 为年，取值范围 0000-9999 ，
date
C8
MM 为月，取值范围 01-12 ， DD 为日，
取值范围 01-31
ntime
C13
当前时区时间，格式 HHMMSSsss ，
HH 为小时，取值范围 00-23 ， MM 为
24

交易网关数据接口规范
分钟，取值范围 00-59 ， SS 为秒，取
值范围 00-59 ， sss 为毫秒，取值范围
000-999
Boolean
C1
代表该字符串内容为布尔值，有效取
值是 Y 或者 N 。
4.2.1 STEP 格式约定
STEP 结构均采用依次排列“标签 = 字段取值 <SOH> ”的方式组织，标签为数字字符，
前后无空格，除非特别声明外，字段取值均为可打印 ASCII 码字符串表示，不得采用全角
字母字符， <SOH> 为字段界定符，值为不可打印 ASCII 码字符：十六进制的 0x01 。
STEP 结构中重复组部分的字段需严格遵循接口规格中定义的先后顺序；字符型字段用
空格表示空值，即采用“标签 = <SOH> ”的方式表示（等号后与分隔符间有一个空格），数
值型字段用 0 表示空值，即“标签 =0<SOH> ”（注：含小数数值型字段空值需符合格式要
求，例 N13 （ 5 ）空值表示为“标签 =0.00000<SOH> ”）。
4.2.2 STEP 消息头
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
接收方代码， OMS 发出的消息
56
TargetCompID
Y
C32
中填写“ TDGW ”
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
52
SendingTime
Y
发送时间，格式：
C21
25

交易网关数据接口规范
YYYYMMDD-HH:MM:SS.sss
MessageEncodin
347
N
字符编码类型
C16
g
4.2.3 STEP 消息尾
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
4.2.4 STEP 消息完整性
STEP 消息完整性通过两个方法保证：消息体长度及校验和的验证。
消息长度通过 BodyLength 域记录，表示 BodyLength 域值之后第一个域界定符 <SOH>
（不包括）与 CheckSum 域号前的最后一个域界定符 <SOH> （包括）之间的字符个数。
校验和是把每个字符的 ASCII 码值从消息开头‘ 8= ’中的‘ 8 ’开始相加，一直加到紧
靠在 CheckSum 域号‘ 10= ’之前的域界定符，然后取按 256 取模得到的结果。计算校验和
的代码段可参考附录一“计算校验和”。
4.3 会话消息
会话消息将在以下各节中予以介绍，并定义会话消息格式，会话层消息机制兼容《 LFIXT
会话协议接口规范》。
4.3.1 登录消息（ MsgType=A ）
登录消息（ Logon ）应是 OMS 建立连接后发送的首个消息。
登录请求消息格式如下：
Tag
域名
必须
说明
类型
26

交易网关数据接口规范
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
双方序号重置为 1 的标记（请
ResetSeqNumFla
141
N
Boolean
求时必填 Y ）
g
接收方期望得到的下一条消
NextExpectedMs
789
N
N18
息序号（请求时必填 1 ）
gSeqNum
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
DefaultApplVerI
1137
Y
C8
缺省版本
D
本次会话中使用的 FIX 消息的
DefaultApplExtI
1407
N
N8
缺省扩展包
D
本次会话中 FIX 消息的缺省
自定义应用版本。填写格式为
STEP1.20_SH_n.xy 其中 n.xy
为接入协议版本号，如接入协
DefaultCstmAppl
议版本号为 1.70 时，则填写：
1408
Y
C32
VerID
STEP1.20_SH_1.70 。（ TDGW
将限制接入的协议版本。当前
最低接入协议版本要求为 0.10
版）
标准消息尾
4.3.2 注销消息（ MsgType=5 ）
注销消息是发起或确认会话终止的消息。连接双方在发送注销消息之后不应发送任何消
息。
注销消息格式如下：
Tag
域名
必须
说明
类型
27

交易网关数据接口规范
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
4.3.3 心跳消息（ MsgType=0 ）
心跳消息用于监控通信连接的状况。如果接收方在 5 倍心跳时间间隔内未收到任何消息
的时候，可认定会话出现异常，可以立即关闭 TCP 连接。
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
4.3.4 测试请求消息（ MsgType=1 ）
测试请求消息能强制对方发出心跳消息。测试请求消息的作用是检查对方消息序号和检
查通信线路的状况。对方用带有测试请求标识符（ TestReqID ）的心跳作应答。 TDGW 不会
主动发送此消息，但会遵循 FIX 标准引擎规则而响应 OMS 发送的该请求。
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
4.3.5 重发请求消息（ MsgType=2 ）
TDGW 不会主动发送此消息，但会遵循 FIX 标准引擎规则而响应 OMS 发送的该请求。
TDGW 接收到重发请求消息，通过序号重设消息（ 4.2.7 ）响应。
重发请求消息格式如下：
28

交易网关数据接口规范
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
4.3.6 会话拒绝消息（ MsgType=3 ）
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
关联消息的序号，即被拒绝消息的序号
N18
371
RefTagID
N
相关错误消息中，出现错误的 FIX 域
号
N6
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
4.3.7 序号重设消息（ MsgType=4 ）
序号重设消息用于告知接收方下一个消息的消息序号。序号重设消息的 MsgSeqNum 按
标准 FIX 协议规定可以任意填写且接收方不会检查，建议固定填写为 1 。 TDGW 不会主动
发送此消息，但会遵循 FIX 标准引擎规则而响应 OMS 发送的重发请求消息（ 4.2.5 ）。当
TDGW 收到用户序号重设消息，则重置入向消息序号 NxtIn = NewSeqNo 。
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
36
NewSeqNo
Y
新消息序号
N18
标准消息尾
Y
29

交易网关数据接口规范
4.4 应用消息
4.4.1 订单业务类
4.4.1.1 新订单申报 New Order Single
标签
字段名
字段描述
必须
类型
消
息
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
订单所有者类型，取值包括：
1= 个人投资者
522
OwnerType
Y
N3
103= 机构投资者
104= 自营交易
54
Side
买卖方向，取值： 1 表示买（转入）， 2
表示卖（转出）
Y
C1
44
Price
申报价格
N
price
38
OrderQty
申报数量
Y
quantity
40
OrdType
订单类型： 2= 限价（目前仅支持限价）
N
C1
59
TimeInForce
订单有效时间类型，取值范围： 0 表示当
日有效（ GFD ）
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
信用标签，信用交易时填写，取值： XY=
担保品买卖、 RZ= 融资交易、 PC= 平仓交
易
58
Text
用户私有信息
N
C32
453
NoPartyIDs
Y
N2
参与方个数，取值 =10 ，后接重复组，依
次包含发起方的投资者账户、业务交易
单元号、营业部代码、结算会员代码、
投资者中国结算开放式基金账户、投资
者中国结算交易账户、销售人代码、券
商网点号码、开放式基金转托管的目标
方、申报编号。
448
PartyID
发起方投资者帐户
Y
C13
发
起
方
投
资
者
取 5 ，表示当前 PartyID 的取值
为发起方投资者帐户。
Y
N4
452
PartyRo
le
30

交易网关数据接口规范
账户
448
PartyID
发起方业务交易单元代码，填
写 5 位业务交易单元号。
Y
C8
取 1 ，表示当前 PartyID 的取值
为发起方业务交易单元号。
Y
N4
452
PartyRo
le
发
起
方
业
务
交
易
单
元号
448
PartyID
发起方营业部代码
Y
C8
取 4001 ，表示当前 PartyID 的
取值为发起方的营业部代码。
Y
N4
452
PartyRo
le
发
起
方
营
业
部
代码
448
PartyID
结算会员代码
N
C8
结
算
会
员
代码
取 4 ，表示当前 PartyID 的取值
为结算会员代码。
N
N4
452
PartyRo
le
448
PartyID
投资者场外开放式基金账户
N
C12
N
N4
452
PartyRo
le
取 4010 ，表示当前 PartyID 的取
值为发起方的中国结算开放
式基金账户。
投
资
者
中
国
结
算
开
放
式
基
金
账户
448
PartyID
投资者中国结算交易账户
N
C17
N
N4
452
PartyRo
le
取 4011 ，表示当前 PartyID 的取
值为发起方中国结算开放式
基金账户下的交易账户。
投
资
者
中
国
结
算
交
易
账
户
448
PartyID
销售人代码
N
C9
销
售
人
代
码
取 117 ，表示当前 PartyID 的取
值为发起方的销售代码。
N
N4
452
PartyRo
le
448
PartyID
券商网点号码
N
C9
N
N4
券
商
网
点
号码
452
PartyRo
le
取 81 ，表示当前 PartyID 的取值
为发起方的客户端编码或网
点号码。
448
PartyID
N
C3
开放式基金转托管的目标方
代理人，对方对应的销售人代
码，取值 000-999 ，不足 3 位
左侧补 0 。
N
N4
开
放
式
基
金
转
托
管
的
目
标方
452
PartyRo
le
取 30 ，表示当前 PartyID 的
取值为开放式基金转托管的
目标方代理人。
448
PartyID
申报编号
N
C6
申
报
编号
取 4003 ，表示当前 PartyID 的取
值为申报编号
N
N4
452
PartyRo
le
8532
DividendSelect
分红选项， U= 红利转投， C= 现金分红
N
C1
31

交易网关数据接口规范
说明：
1.
适用于互联网交易平台业务
2.
各业务填写字段说明如下：
业务类型 ApplID
业务类型
相关字段填写说明
基金通报价交易
1.Price 字段必填
2.OrderQty 申报数量单位为份；
600020
3. 投资者中国结算开放式基金账户、投资者中国结
算交易账户、销售人代码、券商网点号码为必填
4.OrdType 必填
基金通转入转出
1. 投资者中国结算开放式基金账户、投资者中国结算
交易账户、销售人代码、券商网点号码为必填
600021
2.OrderQty 申报数量单位为份
3.OrdType 必填
开放式基金申购
1. Price 固定填 1 。
2.Side 固定填 1 。
600030
3.OrderQty 表示申购金额，单位为元，填写非 0 正整
数，累加申购金额为 100 元或其整数倍。
4. SecurityID 填写正股代码（ 519XXX ）。
开放式基金赎回
1. Price 固定填 1 。
2.Side 固定填 2 。
600040
3. OrderQty 表示赎回份额，单位为份，填写非 0 正
整数，不支持小数。
4. SecurityID 填写正股代码（ 519XXX ）。
1.Price 固定填 1 。
开放式基金转托管转
出
2. OrderQty 表示基金份额，单位为份，填写非 0 正
整数，不支持小数。
600050
3.Side 固定填 2 。
4. SecurityID 填写正股代码（ 519XXX ）。
5. 开放式基金转托管的目标方字段必填。
开放式基金分红选择
1.Price 固定填 1 。
2.Side 固定填 1 。
3.OrderQty 固定填 1 。
600060
4. SecurityID 填写正股代码（ 519XXX ）。
5. DividendSelect 必填， U= 红利转投， C= 现金分红。
600070
要约预受 / 现金选择权
1.Price 表示收购价，单位为元，填写非 0 正数。
32

交易网关数据接口规范
登记
2.Side 固定填 2 。
3. OrderQty 表示收购数量，填写非 0 正整数。
4. SecurityID 填写标的证券正股代码。
5. 申报编号字段必填，填写 6 位数字。
1.Price 表示收购价，单位为元，填写非 0 正数。
要约撤销 / 现金选择权
注销
2.Side 固定填 1 。
3. OrderQty 表示收购数量，填写非 0 正整数。
600071
4. SecurityID 填写标的证券正股代码。
5. 申报编号字段必填，填写 6 位数字。
融资融券余券划转
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
600080
3. Side 固定填 1 。买入转义为标的证券从“证券公司
融券专用账户”过户到“证券公司信用交易担保证券
账户”。仅允许投资者信用账户（ E 字头）申报。
4.OrderQty 表示 划转数量,填写非0 正整数，允许零
散股。
融资融券还券划转
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
600090
3.Side 固定填 2 。卖出转义为标的证券从“证券公司
信用交易担保证券账户”过户到“证券公司融券专用
账户”。仅允许投资者信用账户（ E 字头）申报。
4. OrderQty 表示 划转数量, 填写非0 正整数，允许
零散股。
融资融券担保品划入
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
600100
3.Side 固定填 1 。买入转义为标的证券从“投资者普
通证券账户”过户到“证券公司信用交易担保证券账
户”。仅允许投资者信用账户（ E 字头）申报。
4. OrderQty 划转数量, 填写非0 正整数，允许零散
股。
融资融券担保品划出
1. SecurityID 表示转入的标的产品代码。
600101
2. Price 固定填 1 。
33

交易网关数据接口规范
3.Side 固定填 2 。卖出转义为标的证券从“证券公司
信用交易担保证券账户”过户到“投资者普通证券账
户”。仅允许投资者信用账户（ E 字头）申报。
4. OrderQty 划转数量, 填写非0 正整数，允许零散
股。
融资融券券源划入
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
600110
3.Side 固定填 2 ，卖出转义为标的证券从“证券公司
自营账户”过户到“证券公司融券专用账户”。仅允
许证券公司自营账户申报。
4. OrderQty 划转数量, 填写非0 正整数，允许零散
股。
融资融券券源划出
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
600111
3.Side 固定填 1 。买入转义为标的证券从“证券公司
融券专用账户”过户到“证券公司融券自营账户”。
仅允许证券公司自营账户申报。
4. OrderQty 划转数量, 填写非0 正整数，允许零散
股。
3.
OrdType 字段：开放式基金、要约 / 现金选择权、融资融券业务申报请求暂不
启用。
4.
Text 字段对于开放式基金、融资融券、要约 / 现金选择权非交易业务仅前 12 位
有效。
5.
“发起方营业部代码”字段： 5 位数字表示，目前使用区间为 [00000 ， 65535] ，
不足 5 位的左侧补 0 。营业部代码可于本所网站会员专区查询，若无对应营业部代码，
则该字段填写空格。
6.
“结算会员代码”字段： B 股结算会员代码，对于 A 股投资者取值无意义，
对于 B 股境外投资者 C9 类账户此记录不能为空，直接填写中登公司公布的 B 股结算会
员代码，不足 5 位的左侧补 0, 。对于 B 股境内投资者 C1 类账户无意义，前 5 位有效。
对于开放式基金、要约 / 现金选择权、融资融券非交易业务无意义。
7.
OwnerType 字段：开放式基金、要约 / 现金选择权、融资融券非交易业务申报
请求暂不启用。
34

交易网关数据接口规范
8.
参与方个数应小于等于 10 ，重复组个数应于申报参与方个数相匹配并按序依
次填写，非必填参与方可跳过。若参与方重复申报，则允许覆盖并仅以最末尾上报值为
准（后处理逻辑相同）。
4.4.1.2 撤单申报 Order Cancel
标签
字段名
字段描述
必须
类型
消息头
MsgType = F
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
买卖方向，取值： 1 表示买（转入）， 2 表示
卖（转出）
Y
C1
41
OrigClOrdID
原始会员内部订单编号，指被撤单订单的
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
用户私有信息
N
C32
453
NoPartyIDs
Y
N2
参与方个数，取值 =8 ，后接重复组，依次包含
发起方的投资者账户、业务交易单元号、营业
部代码、投资者中国结算开放式基金账户、投
资者中国结算交易账户、销售人代码、券商网
点号码、申报编号。
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
取 5 ，表示当前 PartyID 的取值
为发起方投资者帐户。
Y
N4
448
PartyID
发起方业务交易单元代码，填
写 5 位业务交易单元号。
Y
C8
发起方
业务交
易单元
号
452
PartyRole
取 1 ，表示当前 PartyID 的取值
为发起方业务交易单元号。
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
取 4001 ，表示当前 PartyID 的
取值为发起方的营业部代码。
Y
N4
448
PartyID
投资者场外开放式基金账户
N
C12
452
PartyRole
N
N4
取 4010 ，表示当前 PartyID 的取
值为发起方的中国结算开放
式基金账户。
投资者
中国结
算开放
式基金
账户
448
PartyID
投资者中国结算交易账户
N
C17
452
PartyRole
N
N4
投资者
中国结
算交易
账户
取 4011 ，表示当前 PartyID 的取
值为发起方中国结算开放式
基金账户下的交易账户。
销售人
448
PartyID
销售人代码
N
C9
35

交易网关数据接口规范
代码
452
PartyRole
取 117 ，表示当前 PartyID 的取
值为发起方的销售代码。
N
N4
448
PartyID
券商网点号码
N
C9
券商网
点号码
452
PartyRole
N
N4
取 81 ，表示当前 PartyID 的取值
为发起方的客户端编码或网
点号码。
448
PartyID
申报编号
N
C6
申报编
号
452
PartyRole
取 4003 ，表示当前 PartyID 的取
值为申报编号
N
N4
说明：
1.
基金通报价交易 ApplID=600020 ，基金通转入转出 ApplID=600021 时，投资者
中国结算开放式基金账户、投资者中国结算交易账户、销售人代码、券商网点号码为必
填。
2.
撤单申报中， APPIID 、发起方投资者账户、发起方业务交易单元号、投资者
中国结算开放式基金账户、投资者中国结算交易账户、销售人代码、券商网点、 SecurityID 、
Side 取值应与原申报相同， OrigClOrdID 的取值应与待撤原订单的 ClOrdID 相同。对于
开放式基金、要约 / 现金选择权、融资融券非交易业务，仅要求 ApplID 、发起方业务交
易单元号、 SecurityID 取值应与待撤原订单相同， OrigClOrdID 的取值应与待撤原订单
的 ClOrdID 相同； Text 字段仅前 12 位有效。
3.
要约 / 现金选择权业务撤单申报时，申报编号字段必填，且需与原订单保持一
致。
4.
发起方投资者账户、发起方营业部代码、 OwnerType 、 Side 字段对于开放式基
金、要约 / 现金选择权、融资融券非交易业务暂不启用。
4.4.2 询价业务类
4.4.2.1 询价请求（ Quote Request ）
标签
字段名
字段描述
必须
类型
消息头
MsgType=R
1180
ApplID
业务类型： 600022= 基金通询价交易
Y
C6
Y
C18
131
QuoteReqID
询价请求编号 , 主动撤单时填与被撤委
托的 QuoteReqID 一致
11
ClOrdID
会员内部编号
Y
C10
537
QuoteType
报价类别
N
N4
1=Tradeable ，表示可交易的报价
订单所有者类型
Y
1= 个人投资者
522
OwnerType
N3
103= 机构投资者
104= 自营交易
60
TransactTime
订单申报时间
N
ntime
36

交易网关数据接口规范
48
SecurityID
证券代码
Y
C6
54
Side
买卖方向，取值有： 1 表示买， 2 表示卖
Y
C1
38
OrderQty
订单数量
Y
quantity
N
price
2551
StartPriceRange
价格下限
预留，暂不启用
N
price
2552
EndPriceRange
价格上限
预留，暂不启用
询价请求事务类型
Y
0-New ，新订单
C1
10200
QuoteRequestTransT
ype
1-Cancel ，撤销
126
ExpireTime
询价请求失效时间，预留
N
ntime
10300
NoCounterpar
tyParticipant
询价接收方参与人个数
Y
N10
N
询价接收方参与人代码
→
10301
C8
Counterparty
ParticipantCo
de
Y
453
NoPartyIDs
N2
参与方个数，取值 =7 ，后接重复组，依
次包含询价发起方的投资者账户、询价
发起方业务交易单元代码、询价发起方
营业部代码、投资者中国结算开放式基
金账户、投资者中国结算交易账户、销
售人代码、券商网点号码。
448
PartyID
询价发起方投资者帐户
Y
C13
发起方
投资者
账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起方
投资者帐户
Y
N4
448
PartyID
询价发起方业务交易单元代码，填写 5
位业务交易单元号。
Y
C8
发起方
业务交
易单元
号
452
PartyRole
取 1 ，表示当前 PartyID 的取值为发起方
业务交易单元号。
Y
N4
448
PartyID
询价发起方营业部代码
Y
C8
发起方
营业部
代码
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为询
价发起方的营业部代码。
Y
N4
448
PartyID
投资者场外开放式基金账户
N
C12
452
PartyRole
取 4010 ，表示当前 PartyID 的取值为发起
方的场外开放式基金账户。
N
N4
投资者
中国结
算开放
式基金
账户
448
PartyID
投资者中国结算交易账户
N
C17
452
PartyRole
取 4011 ，表示当前 PartyID 的取值为发起
方的场外交易账户。
N
N4
投资者
中国结
算交易
账户
448
PartyID
销售人代码
N
C9
销售人
代码
452
PartyRole
取 117 ，表示当前 PartyID 的取值为发起方
的销售代码。
N
N4
37

交易网关数据接口规范
448
PartyID
券商网点号码
N
C9
券商网
点号码
452
PartyRole
取 81 ，表示当前 PartyID 的取值为发起方
的客户端编码或网点号码。
N
N4
说明：
1.
基金通询价交易 ApplID=600022 时，投资者中国结算开放式基金账户、投资
者中国结算交易账户、销售人代码、券商网点号码为必填。
2.
“询价接收方参与人个数”字段为 0 时，“询价接收方参与人代码”字段必须
为空，表示向市场该产品对应全部做市商发起询价。
3.
询价请求（ Quote Request ）中询价请求编号 QuoteReqID 前 10 位有效。
4.4.2.2 询价请求响应（ Quote Request Ack ）
标签
字段名
字段描述
必须
类型
消息头
MsgType=R
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
业务类型： 600022= 基金通询价交易
Y
C6
131
QuoteReqID
询价请求编号，同询价请求中
Y
C18
QuoteReqID
11
ClOrdID
会员内部编号
Y
C10
537
QuoteType
报价类别
N
N4
1=Tradeable ，表示可交易的报价
订单所有者类型
Y
1= 个人投资者
522
OwnerType
N3
103= 机构投资者
104= 自营交易
60
TransactTime
订单申报时间
N
ntime
48
SecurityID
证券代码
Y
C6
54
Side
买卖方向，取值有： 1 表示买， 2 表示卖
Y
C1
38
OrderQty
订单数量
Y
quantity
2551
StartPriceRange
价格下限
N
price
2552
EndPriceRange
价格上限
N
price
交易所订单编号
N
37
OrderID
C16
QuoteRequestStatus=0 时为交易所订单编
号， QuoteRequestStatus=4 时为被撤询价
单交易所订单编号
17
ExecID
订单执行编号
N
C16
Y
C1
10200
QuoteRequestTransT
ype
询价请求事务类型
0-New ，新订单
1-Cancel ，撤销
Y
C3
303
QuoteRequestType
询价请求类型
101=Submit ，提交
38

交易网关数据接口规范
102=Alleged ，转发
Y
10222
QuoteRequestStatus
C1
询价请求状态
0=Accepted ，已接受
4=Cancelled ，已撤销
5=Rejected ，已拒绝
7=Expired ，已超时
658
QuoteRequestRejectR
eason
订单拒绝码
Y
C5
10237
QuoteRequestRejectT
ext
订单拒绝原因说明
N
C32
126
ExpireTime
询价请求失效时间，预留
N
ntime
10300
NoCounterpar
tyParticipant
询价接收方参与人个数
Y
N10
N
询价接收方参与人代码
→
10301
C8
Counterparty
ParticipantCo
de
Y
453
NoPartyIDs
N2
参与方个数，取值 =7 ，后接重复组，依
次包含询价发起方的投资者账户、询价
发起方业务交易单元代码、询价发起方
营业部代码、投资者中国结算开放式基
金账户、投资者中国结算交易账户、销
售人代码、券商网点号码。
448
PartyID
询价发起方投资者帐户
Y
C13
发起方
投资者
账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起方
投资者帐户
Y
N4
448
PartyID
询价发起方业务交易单元代码，填写 5
位业务交易单元号。
Y
C8
发起方
业务交
易单元
号
452
PartyRole
取 1 ，表示当前 PartyID 的取值为发起方
业务交易单元号。
Y
N4
448
PartyID
询价发起方营业部代码
Y
C8
发起方
营业部
代码
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为询
价发起方的营业部代码。
Y
N4
448
PartyID
投资者场外开放式基金账户
N
C12
452
PartyRole
取 4010 ，表示当前 PartyID 的取值为发起
方的场外开放式基金账户。
N
N4
投资者
中国结
算开放
式基金
账户
448
PartyID
投资者中国结算交易账户
N
C17
452
PartyRole
取 4011 ，表示当前 PartyID 的取值为发起
方的场外交易账户。
N
N4
投资者
中国结
算交易
账户
448
PartyID
销售人代码
N
C9
销售人
代码
452
PartyRole
取 117 ，表示当前 PartyID 的取值为发起方
的销售代码。
N
N4
券商网 448
PartyID
券商网点号码
N
C9
39

交易网关数据接口规范
点号码
452
PartyRole
取 81 ，表示当前 PartyID 的取值为发起方
的客户端编码或网点号码。
N
N4
4.4.2.3 转发询价请求（ Allege Quote Request ）
标签
字段名
字段描述
必须
类型
消息头
MsgType=R
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
业务类型： 600022= 基金通询价交易
Y
C6
Y
C18
131
QuoteReqID
询价请求编号，交易所进行唯一化处理
后的询价请求 ID
537
QuoteType
报价类别
N
N4
1=Tradeable ，表示可交易的报价
订单所有者类型
N
1= 个人投资者
522
OwnerType
N3
103= 机构投资者
104= 自营交易
60
TransactTime
订单申报时间
N
ntime
48
SecurityID
证券代码
Y
C6
54
Side
买卖方向，取值有： 1 表示买， 2 表示卖
Y
C1
38
OrderQty
订单数量
Y
quantity
2551
StartPriceRange
价格下限
N
price
2552
EndPriceRange
价格上限
N
price
37
OrderID
交易所订单编号
N
C16
17
ExecID
订单执行编号
N
C16
Y
C1
10200
QuoteRequestTransT
ype
询价请求事务类型
0-New ，新订单
1-Cancel ，撤销
询价请求类型
Y
101=Submit ，提交
303
QuoteRequestType
C3
102=Alleged ，转发
询价请求状态
Y
0=Accepted ，已接受
4=Cancelled ，已撤销
10222
QuoteRequestStatus
C1
5=Rejected ，已拒绝
7=Expired ，已超时
8=Filled ，已成交
126
ExpireTime
询价请求失效时间，预留
N
ntime
Y
453
NoPartyIDs
N2
参与方个数，取值 =7 ，后接重复组，依
次包含询价发起方的投资者账户、询价
发起方业务交易单元代码、询价发起方
40

交易网关数据接口规范
营业部代码、投资者中国结算开放式基
金账户、投资者中国结算交易账户、销
售人代码、券商网点号码。
448
PartyID
询价发起方投资者帐户
N
C13
发起方
投资者
账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起方
投资者帐户
N
N4
448
PartyID
询价发起方业务交易单元代码，填写 5
位业务交易单元号。
N
C8
发起方
业务交
易单元
号
452
PartyRole
取 1 ，表示当前 PartyID 的取值为发起方
业务交易单元号。
N
N4
448
PartyID
询价发起方营业部代码
N
C8
发起方
营业部
代码
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为询
价发起方的营业部代码。
N
N4
448
PartyID
投资者场外开放式基金账户
N
C12
452
PartyRole
取 4010 ，表示当前 PartyID 的取值为发起
方的场外开放式基金账户。
N
N4
投资者
中国结
算开放
式基金
账户
448
PartyID
投资者中国结算交易账户
N
C17
452
PartyRole
取 4011 ，表示当前 PartyID 的取值为发起
方的场外交易账户。
N
N4
投资者
中国结
算交易
账户
448
PartyID
销售人代码
N
C9
销售人
代码
452
PartyRole
取 117 ，表示当前 PartyID 的取值为发起方
的销售代码。
N
N4
448
PartyID
券商网点号码
N
C9
券商网
点号码
452
PartyRole
取 81 ，表示当前 PartyID 的取值为发起方
的客户端编码或网点号码。
N
N4
说明：
1. 基金通询价交易 ApplID=600022 时，投资者中国结算开放式基金账户、投资者中国
结算交易账户、销售人代码、券商网点号码为必填。
4.4.2.4 报价（ Quote ）
标签
字段名
字段描述
必须
类型
消息头
MsgType=S
1180
ApplID
业务类型： 600022= 基金通询价交易
Y
C6
Y
C10
1166
QuoteMsgID
客户报价消息编号，类似 CIOrderID 会员
内部编号
Y
C18
117
QuoteID
报价请求编号，主动撤单时填与被撤委
托的 QuoteID 一致
41

交易网关数据接口规范
537
QuoteType
报价类别
N
N4
1=Tradeable ，表示可交易的报价
Y
522
OwnerType
N3
订单所有者类型
1= 个人投资者
103= 机构投资者
104= 自营交易
60
TransactTime
订单申报时间
N
ntime
N
C18
131
QuoteReqID
当报价是对询价请求的响应时，填写转
发询价请求的 QuoteReqID
48
SecurityID
证券代码
Y
C6
132
BidPx
买报价 BidSize>0 时必须填写
N
price
133
OfferPx
卖报价 OfferSize>0 时必须填写
N
price
134
BidSize
买数量
N
quantity
135
OfferSize
卖数量
N
quantity
62
ValidUntilTime
报价有效时间，预留
N
ntime
是否匿名
N
0= 显名
1091
PreTradeAnonymity
C1
1= 匿名
9= 不指定
Y
453
NoPartyIDs
N2
参与方个数，取值 =7 ，后接重复组，依
次包含报价发起方的投资者账户、报价
发起方业务交易单元代码、报价发起方
营业部代码、投资者中国结算开放式基
金账户、投资者中国结算交易账户、销
售人代码、券商网点号码。
448
PartyID
报价发起方投资者帐户
Y
C13
发起方
投资者
账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起方
投资者帐户
Y
N4
448
PartyID
报价发起方业务交易单元代码，填写 5
位业务交易单元号。
Y
C8
发起方
业务交
易单元
号
452
PartyRole
取 1 ，表示当前 PartyID 的取值为发起方
业务交易单元号。
Y
N4
448
PartyID
询价发起方营业部代码
Y
C8
发起方
营业部
代码
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为报价
发起方的营业部代码。
Y
N4
448
PartyID
投资者场外开放式基金账户
N
C12
452
PartyRole
取 4010 ，表示当前 PartyID 的取值为发起
方的场外开放式基金账户。
N
N4
投资者
中国结
算开放
式基金
账户
448
PartyID
投资者中国结算交易账户
N
C17
452
PartyRole
取 4011 ，表示当前 PartyID 的取值为发起
方的场外交易账户。
N
N4
投资者
中国结
算交易
账户
42

交易网关数据接口规范
448
PartyID
销售人代码
N
C9
销售人
代码
452
PartyRole
取 117 ，表示当前 PartyID 的取值为发起方
的销售代码。
N
N4
448
PartyID
券商网点号码
N
C9
券商网
点号码
452
PartyRole
取 81 ，表示当前 PartyID 的取值为发起方
的客户端编码或网点号码。
N
N4
说明：
1.
报价（ Quote ）中报价请求编号 QuoteID 前 10 位有效。
2.
基金通询价交易 ApplID=600022 时，投资者中国结算开放式基金账户、投资
者中国结算交易账户、销售人代码、券商网点号码为必填。
3.
报价消息支持以下报价方式
报价方式
BidSize （ 134 ）
OfferSize （ 135 ）
买报价
>0
=0
卖报价
=0
>0
撤销报价
=0
=0
4.4.2.5 报价状态回报（ Quote Status Report ）
标签
字段名
字段描述
必须
类型
消息头
MsgType=AI
10197
PartitionNo
平台内分区号
Y
N4
10179
ReportIndex
执行报告编号，从 1 开始连续递增编
号
Y
N16
1180
ApplID
业务类型： 600022= 基金通询价交易
Y
C6
Y
C10
1166
QuoteMsgID
客户报价消息编号，类似 CIOrderID
会员内部编号
Y
C18
117
QuoteID
报价请求编号，主动撤单时填与被撤
委托的 QuoteID 一致
N
C18
131
QuoteReqID
当报价是对询价请求的响应时，填写
转发询价请求的 QuoteReqID
N
N4
537
QuoteType
报价类别
1=Tradeable ，表示可交易的报价
订单所有者类型
Y
1= 个人投资者
522
OwnerType
N3
103= 机构投资者
104= 自营交易
报价状态
N
0=Accepted ，接受
297
QuoteStatus
C1
4=Cancelled ，已撤销
5=Rejected ，拒绝
43

交易网关数据接口规范
7=Expired ，已超时
300
QuoteRejectReason
报价拒绝原因代码
N
C5
10236
QuoteRejectText
报价拒绝原因说明
N
C32
60
TransactTime
报价接收时间
N
ntime
48
SecurityID
证券代码
Y
C6
132
BidPx
买报价
N
price
133
OfferPx
卖报价
N
price
134
BidSize
买数量
N
quantity
135
OfferSize
卖数量
N
quantity
N
37
OrderID
C16
交易所订单编号
QuoteStatus=0 时为交易所订单编号，
QuoteStatus=4 时为被撤报价单交易所
订单编号
17
ExecID
执行编号
N
C10
62
ValidUntilTime
报价失效时间，预留
N
ntime
Y
453
NoPartyIDs
N2
参与方个数，取值 =7 ，后接重复组，
依次包含报价发起方的投资者账户、
报价发起方业务交易单元代码、报价
发起方营业部代码、投资者中国结算
开放式基金账户、投资者中国结算交
易账户、销售人代码、券商网点号码。
448
PartyID
报价发起方投资者帐户
Y
C13
发起方
投资者
账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起
方投资者帐户
Y
N4
448
PartyID
报价发起方业务交易单元代码，填写
5 位业务交易单元号。
Y
C8
发起方
业务交
易单元
号
452
PartyRole
取 1 ，表示当前 PartyID 的取值为发起
方业务交易单元号。
Y
N4
448
PartyID
报价发起方营业部代码
Y
C8
发起方
营业部
代码
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为
报价发起方的营业部代码。
Y
N4
448
PartyID
投资者场外开放式基金账户
N
C12
452
PartyRole
取 4010 ，表示当前 PartyID 的取值为发
起方的场外开放式基金账户。
N
N4
投资者
中国结
算开放
式基金
账户
448
PartyID
投资者中国结算交易账户
N
C17
452
PartyRole
取 4011 ，表示当前 PartyID 的取值为发
起方的场外交易账户。
N
N4
投资者
中国结
算交易
账户
448
PartyID
销售人代码
N
C9
销售人
代码
452
PartyRole
取 117 ，表示当前 PartyID 的取值为发
起方的销售代码。
N
N4
44

交易网关数据接口规范
448
PartyID
券商网点号码
N
C9
券商网
点号码
452
PartyRole
取 81 ，表示当前 PartyID 的取值为发起
方的客户端编码或网点号码。
N
N4
4.4.2.6 转发报价（ Allege Quote ）
标签
字段名
字段描述
必须
类型
消息头
MsgType=S
10197
PartitionNo
平台内分区号
Y
N4
10179
ReportIndex
执行报告编号，从 1 开始连续递增编
号
Y
N16
1180
ApplID
业务类型： 600022= 基金通询价交易
Y
C6
N
C18
131
QuoteReqID
当报价是对询价请求的响应时，填写
询价请求的 QuoteReqID
Y
C18
117
QuoteID
报价请求编号，交易所唯一化处理后
的报价请求 ID
N
N4
537
QuoteType
报价类别
1=Tradeable ，表示可交易的报价
Y
522
OwnerType
N3
订单所有者类型
1= 个人投资者
103= 机构投资者
104= 自营交易
60
TransactTime
报价接收时间
N
ntime
48
SecurityID
证券代码
Y
C6
132
BidPx
买报价 BidSize>0 时必须填写
N
price
133
OfferPx
卖报价 OfferSize>0 时必须填写
N
price
134
BidSize
买数量
N
quantity
135
OfferSize
卖数量
N
quantity
37
OrderID
交易所订单编号
N
C16
17
ExecID
执行编号
N
C10
62
ValidUntilTime
报价失效时间，预留
N
ntime
Y
453
NoPartyIDs
N2
参与方个数，取值 =7 ，后接重复组，
依次包含报价发起方的投资者账户、
报价发起方业务交易单元代码、报价
发起方营业部代码、投资者中国结算
开放式基金账户、投资者中国结算交
易账户、销售人代码、券商网点号码。
448
PartyID
报价发起方投资者帐户
Y
C13
发起方
投资者
账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起
方投资者帐户
Y
N4
发起方
业务交 448
PartyID
报价发起方业务交易单元代码，填写
5 位业务交易单元号。
Y
C8
45

交易网关数据接口规范
易单元
号
452
PartyRole
取 1 ，表示当前 PartyID 的取值为发起
方业务交易单元号。
Y
N4
448
PartyID
报价发起方营业部代码
Y
C8
发起方
营业部
代码
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为
询价发起方的营业部代码。
Y
N4
448
PartyID
投资者场外开放式基金账户
N
C12
452
PartyRole
取 4010 ，表示当前 PartyID 的取值为发
起方的场外开放式基金账户。
N
N4
投资者
中国结
算开放
式基金
账户
448
PartyID
投资者中国结算交易账户
N
C17
452
PartyRole
取 4011 ，表示当前 PartyID 的取值为发
起方的场外交易账户。
N
N4
投资者
中国结
算交易
账户
448
PartyID
销售人代码
N
C9
销售人
代码
452
PartyRole
取 117 ，表示当前 PartyID 的取值为发
起方的销售代码。
N
N4
448
PartyID
券商网点号码
N
C9
券商网
点号码
452
PartyRole
取 81 ，表示当前 PartyID 的取值为发起
方的客户端编码或网点号码。
N
N4
4.4.2.7 报价回复（ Quote Response ）
标签
字段名
字段描述
必须
类型
消息头
MsgType=AJ
1180
ApplID
业务类型： 600022= 基金通询价交易
Y
C6
693
QuoteRespID
报价回复消息编号
Y
C18
11
ClOrdID
会员内部编号
Y
C10
537
QuoteType
报价类别
N
N4
1=Tradeable ，表示可交易的报价
Y
522
OwnerType
N3
订单所有者类型
1= 个人投资者
103= 机构投资者
104= 自营交易
60
TransactTime
报价发起时间
N
ntime
48
SecurityID
证券代码
Y
C6
报价回复类型
N
1=Hit/Lift ，接受
694
QuoteRespType
C1
2=Counter ，重报
6-Pass ，拒绝
Y
C1
54
Side
买卖方向，取值有： 1 表示买， 2 表示
卖
46

交易网关数据接口规范
44
Price
申报价格
N
price
38
OrderQty
申报数量
N
quantity
Y
40
OrdType
C1
报价回复成交类型，取值：
Y=Negotiated Trade ，表示点击成交报
价交易
2=Limit ，表示匹配成交报价交易
10199
NoQuote
报价消息个数
Y
N
C10
->
117
QuoteID
报价请求编号，交易所唯一化处理后
的报价请求 ID
->
10225
QuotePrice
报价价格
N
price
->
10226
QuoteQty
报价数量
N
quantity
131
QuoteReqID
询价请求编号
N
C18
62
ValidUntilTime
报价有效时间，预留
N
ntime
Y
453
NoPartyIDs
N2
参与方个数，取值 =7 ，后接重复组，
依次包含询价发起方的投资者账户、
询价发起方业务交易单元代码、询价
发起方营业部代码、投资者中国结算
开放式基金账户、投资者中国结算交
易账户、销售人代码、券商网点号码。
448
PartyID
询价发起方投资者帐户
Y
C13
发起方
投资者
账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起
方投资者帐户
Y
N4
448
PartyID
询价发起方业务交易单元代码，填写
5 位业务交易单元号。
Y
C8
发起方
业务交
易单元
号
452
PartyRole
取 1 ，表示当前 PartyID 的取值为发起
方业务交易单元号。
Y
N4
448
PartyID
询价发起方营业部代码
Y
C8
发起方
营业部
代码
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为
询价发起方的营业部代码。
Y
N4
448
PartyID
投资者场外开放式基金账户
N
C12
452
PartyRole
取 4010 ，表示当前 PartyID 的取值为发
起方的场外开放式基金账户。
N
N4
投资者
中国结
算开放
式基金
账户
448
PartyID
投资者中国结算交易账户
N
C17
452
PartyRole
取 4011 ，表示当前 PartyID 的取值为发
起方的场外交易账户。
N
N4
投资者
中国结
算交易
账户
448
PartyID
销售人代码
N
C9
销售人
代码
452
PartyRole
取 117 ，表示当前 PartyID 的取值为发
起方的销售代码。
N
N4
448
PartyID
券商网点号码
N
C9
券商网
点号码
452
PartyRole
取 81 ，表示当前 PartyID 的取值为发起
方的客户端编码或网点号码。
N
N4
47

交易网关数据接口规范
说明：
1.
基金通询价交易 ApplID=600022 时，投资者中国结算开放式基金账户、投资
者中国结算交易账户、销售人代码、券商网点号码为必填。
2.
报价回复（ Quote Response ）中报价回复消息编号 QuoteRespID 前 10 位有效。
3.
报价回复时，报价请求编号、报价价格、报价数量填写说明：
点击成交报价回复
匹配成交报价回复
申报价格
空
必填
询价请求编号
空
是
空
报价请求编号
必填，交易所唯一化处理
后的报价请求 ID
报价价格
必填
空
报价数量
必填
空
4.4.3 执行报告类
4.4.3.1 执行报告 Execution Report
4.4.3.1.1 申报响应、成交回报及撤单成功响应
标签
字段名
字段描述
必须
类型
消息头
MsgType = 8
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
150
ExecType
Y
C1
执行报告类型，取值有：
0= 订单申报成功
4= 订单撤销成功
8= 订单申报拒绝
F= 成交回报
11
ClOrdID
会员内部订单编号，针对询价交易申报，
询价方取 ClOrdID ，报价方取 QuoteMsgID
Y
C10
48
SecurityID
证券代码
Y
C12
订单所有者类型，取值包括：
1= 个人投资者
522
OwnerType
Y
N3
103= 机构投资者
104= 自营交易
54
Side
买卖方向，取值：1表示买（转入），2表
Y
C1
48

交易网关数据接口规范
示卖（转出）
8500
OrderEntryTi
me
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
TotalValueTra
ded
成交金额， ExecType=F 时有效
N
amount
84
CxlQty
撤单数量， ExecType=4 时有效
N
quantity
40
OrdType
订单类型， ExecType=0/4/8 时有效
N
C1
59
TimeInForce
订单有效时间类型， ExecType=0/4/8 时有
效
N
C1
当前申报的状态，取值有：
0= 已挂单未成交
1= 部分成交
39
OrdStatus
Y
C1
2= 已成交
4= 已撤消
8= 已拒绝
544
CashMargin
N
C2
信用标签，信用交易时填写，取值： XY=
担保品买卖、 RZ= 融资交易、 PC= 平仓交
易
41
OrigClOrdID
原始会员内部订单编号， ExecType=4 时有
效
N
C10
103
OrdRejReaso
n
订单拒绝码， OrdStatus=8 时有效
N
N5
17
ExecID
成交编号， ExecType=F 且 OrdStatus=1&2
时有效
N
C16
37
OrderID
交易所订单编号 , 取值为数字，仅订单申
报成功 ExecType=0 时有效
Y
C16
1080
RefOrderID
被撤订单交易所订单编号， ExecType=4 时
有效
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
用户私有信息
N
C32
453
NoPartyIDs
Y
N2
参与方个数，取值 =11 ，后接重复组，依
次包含发起方投资者账户、登录或订阅交
易单元、发起方业务交易单元、发起方营
业部代码、结算会员代码、投资者中国结
算开放式基金账户、投资者中国结算交易
账户、销售人代码、券商网点号码、开放
式基金转托管的目标方、申报编号。
49

交易网关数据接口规范
448
PartyID
发起方投资者帐户
Y
C13
452
PartyRole
Y
N4
发起方
投资者
账户
取 5 ，表示当前 PartyID
的取值为发起方投资
者帐户。
448
PartyID
登录或订阅交易单元。
Y
C8
452
PartyRole
Y
N4
登录或
订阅交
易单元
取 17 ，表示当前 PartyID
的取值为登录或订阅
交易单元。
448
PartyID
发起方业务交易单元。
Y
C8
452
PartyRole
Y
N4
发起方
业务交
易单元
取 1 ，表示当前 PartyID
的取值为发起方业务
交易单元。
448
PartyID
发起方营业部代码
Y
C8
452
PartyRole
Y
N4
发起方
营业部
代码
取 4001 ，表示当前
PartyID 的取值为发起
方的营业部代码。
448
PartyID
结算会员代码
N
C8
结算会
员代码
452
PartyRole
N
N4
取 4 ，表示当前 PartyID
的取值为结算会员代
码。
448
PartyID
投资者场外开放式基
金账户
N
C12
取 4010 ，表示当前
452
PartyRole
N
N4
投资者
中国结
算开放
式基金
账户
PartyID 的取值为发起
方的场外开放式基金
账户。
448
PartyID
投资者中国结算交易
账户
N
C17
452
PartyRole
N
N4
投资者
中国结
算交易
账户
取 4011 ，表示当前
PartyID 的取值为发起
方的场外交易账户。
448
PartyID
销售人代码
N
C9
销售人
代码
452
PartyRole
N
N4
取 117 ，表示当前
PartyID 的取值为发起
方的销售代码。
448
PartyID
券商网点号码
N
C9
券商网
点号码
452
PartyRole
N
N4
取 81 ，表示当前 PartyID
的取值为发起方的客
户端编码或网点号码。
开放式基金转托管的
目标方代理人，对方对
应的销售人代码，取值
448
PartyID
N
C3
开放式
基金转
托管的
目标方
000-999 ，不足 3 位左
侧补 0 。
50

交易网关数据接口规范
取 30 ，表示当前
452
PartyRole
N
N4
PartyID 的取值为开放
式基金转托管的目标
方代理人。
448
PartyID
申报代码
N
C6
申报编
号
452
PartyRole
N
N4
取 4003 ，表示当前
PartyID 的取值为申报
代码
分红选择，仅用于开放式基金红选择， U=
红利转投， C= 现金分红
N
C1
8532
DividendSele
ct
说明：
1.
ExecType 和 OrdStatus 组合取值：
申报成功响应：
ExecType=0, OrdStatus=0
申报拒绝响应：
ExecType=8, OrdStatus =8
撤单成功响应：
ExecType=4, OrdStatus =4
成交回报：
ExecType=F, OrdStatus =1/2/8
其中， ExecType=F,OrdStatus=8 时表示订单申报进入订单簿后因某种程序原因无法
被撮合成交。
2.
对于开放式基金、要约 / 现金选择权、融资融券非交易业务， OwnerType 字段
暂不启用。
3.
对于价格、数量字段说明如下：
MsgType = 8
字段
开放式基金非交
易
融资融券非交易
要约 / 现金选择权
非交易
Price 申报价格
申报信息
OrderQty
申报数量
申报信息
申报成功
响应
LeavesQt
剩余数量
无意义
CxlQty
撤单数量
无意义
Price 申报价格
申报信息
OrderQty
申报数量
申报信息
申报失败
响应
LeavesQt
剩余数量
无意义
CxlQty
撤单数量
无意义
Price 申报价格
被撤原申报
撤单成功
响应
OrderQty
申报数量
被撤原申报
LeavesQt
无意义
51

交易网关数据接口规范
剩余数量
CxlQty
撤单数量
无意义
4.4.3.1.2 撤单失败执行报告
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
103
OrdRejReason
撤单订单拒绝码
Y
N5
58
Text
用户私有信息
N
C32
453
NoPartyIDs
Y
N2
参与方个数，取值 =7 ，后接重复组，依
次包含登录或订阅交易单元、发起方业
务交易单元、发起方营业部代码、投资
者中国结算开放式基金账户、投资者中
国结算交易账户、销售人代码、券商网
点号码。
448
PartyID
登录或订阅交易单元。
Y
C8
452
PartyRole
Y
N4
登录或
订阅交
易单元
取 17 ，表示当前 PartyID
的取值为登录或订阅
交易单元。
448
PartyID
发起方业务交易单元。
Y
C8
452
PartyRole
Y
N4
发起方
业务交
易单元
取 1 ，表示当前 PartyID
的取值为发起方业务
交易单元。
448
PartyID
发起方营业部代码
Y
C8
取 4001 ，表示当前
452
PartyRole
Y
N4
发起方
营业部
代码
PartyID 的取值为发起
方的营业部代码。
448
PartyID
投资者场外开放式基
金账户
N
C12
投资者
中国结
算开放
452
PartyRole
取 4010 ，表示当前
N
N4
52

交易网关数据接口规范
式基金
账户
PartyID 的取值为发起
方的场外开放式基金
账户。
448
PartyID
投资者中国结算交易
账户
N
C17
452
PartyRole
N
N4
投资者
中国结
算交易
账户
取 4011 ，表示当前
PartyID 的取值为发起
方的场外交易账户。
448
PartyID
销售人代码
N
C9
销售人
代码
452
PartyRole
N
N4
取 117 ，表示当前
PartyID 的取值为发起
方的销售代码。
448
PartyID
券商网点号码
N
C9
券商网
点号码
452
PartyRole
N
N4
取 81 ，表示当前 PartyID
的取值为发起方的客
户端编码或网点号码。
1. 发起方营业部代码字段对于开放式基金、要约 / 现金选择权、融资融券非交易业务暂不启用。
4.4.4 网络密码服务（ Password Service ）
4.4.4.1.1 网络密码服务申报
标签
字段名
字段描述
必须
类型
消息头
MsgType = U006
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
订单所有者类型，取值包括：
1= 个人投资者
522
OwnerType
Y
N3
103= 机构投资者
104= 自营交易
60
TransactTime
订单申报时间
Y
ntime
54
Side
1= 激活， 2= 挂失或重置
Y
C1
投资者在上交所网站注册时所获得的激
活码
N
C8
8539
ValidationCo
de
58
Text
用户私有信息
N
C32
453
NoPartyIDs
Y
N2
参与方个数，取值 =3 ，后接重复组，依
次包含发起方的投资者账户、发起方业
务交易单元号、营业部代码。
53

交易网关数据接口规范
448
PartyID
发起方投资者帐户
Y
C13
发起方
投资者
账户
取 5 ，表示当前 PartyID 的取值
为发起方投资者帐户。
Y
N4
452
PartyRo
le
448
PartyID
发起方业务交易单元代码，填
写 5 位业务交易单元号。
Y
C8
发起方
业务交
易单元
号
取 1 ，表示当前 PartyID 的取值
为发起方业务交易单元号。
Y
N4
452
PartyRo
le
448
PartyID
发起方营业部代码
Y
C8
发起方
营业部
代码
取 4001 ，表示当前 PartyID 的
取值为发起方的营业部代码。
Y
N4
452
PartyRo
le
说明
1 、各业务填写字段说明如下：
业务类型 ApplID
业务类型
相关字段填写说明
600120
网络密码服务
1 、 SecurityID ， A 股申报填写 799988 ， B 股申报填写
9399882 、 OwnerType 暂不启用
4.4.4.1.2 密码服务申报响应
标签
字段名
字段描述
必须
类型
消息头
MsgType = U008
1180
ApplID
业务类型：
Y
C6
11
ClOrdID
会员内部订单编号
Y
C10
48
SecurityID
申报代码
Y
C12
522
OwnerType
订单所有者类型
Y
N3
103
OrdRejReaso
n
拒绝码，仅当申报成功时响应返回“ 0 ”
N
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
8539
ValidationCo
de
校验号码
Y
C8
58
Text
用户私有信息
N
C32
54
Side
操作指令
Y
C1
453
NoPartyIDs
Y
N2
参与方个数，取值 =3 ，后接重复组，依次
包含发起方投资者账户、发起方业务交易
单元、发起方营业部代码。
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
取 5 ，表示当前 PartyID
的取值为发起方投资
Y
N4
54

交易网关数据接口规范
者帐户。
448
PartyID
发起方业务交易单元。
Y
C8
452
PartyRole
Y
N4
发起方
业务交
易单元
取 1 ，表示当前 PartyID
的取值为发起方业务
交易单元。
448
PartyID
发起方营业部代码
Y
C8
452
PartyRole
Y
N4
发起方
营业部
代码
取 4001 ，表示当前
PartyID 的取值为发起
方的营业部代码。
1.OwnerType 暂不启用
4.4.5 其它消息
4.4.5.1 申报拒绝 Order Reject
标签
字段名
字段描述
必须
类型
消息头
MsgType =j
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
用户私有信息
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
发起方申报交易单元代码，填写
5 位发起方业务交易单元。
Y
C8
发起方
业务交
易单元
452
PartyRole
取 1 ，表示当前 PartyID 的取值
为发起方业务交易单元。
Y
N4
说明：
1.
消息类型与业务层 ID 对应表：
消息类型
被拒绝消息对应的业务层 ID
新订单（ New Order Single ）
ClOrdID
撤单申报（ Order Cancel ）
ClOrdID
询价请求（ Quote Request ）
ClOrdID
报价（ Quote ）
QuoteMsgID
报价回复（ Quote Response ）
ClOrdID
网络密码服务（ Password Service ）
ClOrdID
55

交易网关数据接口规范
4.4.5.2 平台状态 PlatformState
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
6= 互联网交易平台
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
4.4.5.3 执行报告分区信息 ExecRptInfo
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
6 = 互联网交易平台
Y
C1
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
执行报告分区信息提供 PBU 和分区列表，供 OMS 对执行报告流进行初始化和维护。
其中 PBU 可能为 OMS 所连接 TDGW 上的登录 PBU ，也可能为该 TDGW 上订阅的其他 PBU
（仅包含订阅成功的 PBU ）， TDGW 在该循环体中首先给出登录 PBU ，后给出订阅的其他
PBU （如有）。
4.4.5.4 分区序号同步 ExecRptSync
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
56

交易网关数据接口规范
序号同步请求中 BeginReportIndex 取值应大于 0 。 OMS 应避免频繁发送“分区序号同步”
请求，禁止定时或不必要的反复同步行为。
4.4.5.5 分区序号同步响应 ExecRptSyncRsp
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
分区序号同步响应中 RejReason 为 0 时表示成功，其他取值表示错误（如 PBU 或
PartitionNo 取值不正确）。
4.4.5.6 分区执行报告结束 ExecRptEndOfStream
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
Y
N16
分区执行报告最大序号，本消
息编入该分区执行报告编号序
列。
TDGW 在闭市后向 OMS 自动发送一次，表示该执行报告流推送结束，后续该执行报告
流上的序号将不再增加，最大序号为 EndReportIndex 。
57

交易网关数据接口规范
第五章
附录
5.1 附一
计算校验和
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
5.2 附二
PBU 及说明
涉及 PBU 时有几种含义：
1. 配置于 TDGW 上用于登录至交易系统后台的登录单位，称为登录交易单元；
2. 在消息报文中，表明该消息所进行的业务归属单元，称为业务交易单元，接口文档中
用 BizPbu 指代；
3. 在消息报文中，表明与另一登录 PBU 间的订阅关系，称为订阅交易单元。
目前，业务交易单元必须与登录交易单元属于同一市场参与者机构，否则交易系统将拒
绝相应的业务申报请求。订阅 PBU 必须与登录 PBU 属于同一市场参与者机构，否则将订阅
失败，在执行报告分区信息 ExecRptInfo 消息中将不会包含订阅失败的交易单元。
58

交易网关数据接口规范
5.3 附三
错误代码说明
状态码 / 错误码
说明
Text （如有）
0
正常退出
Normal Logout
4012
SecurityID 错误或者业务类型 BizID 错
误
5000
上行消息超过 4K
Message Exceed Max
Length
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
PartitionNo
错误
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
注：本表仅提供交易网关错误码，系统后台错误码参照每日发送的互联网交易平台错误码信
息文件。
5.4 附四
“用户私有信息”说明
对于应用消息中的 Text 字段（用户私有信息），有如下规则：
1. TDGW 返回给 OMS 的下行消息中 Text ，取该条下行消息所对应的上行消息（由 OMS
发送给 TDGW ）中的 Text 字段值。
59

交易网关数据接口规范
60

> **变更标注说明**：本文档中已用 `<span style="color:...">` 标注了变更内容（红色=修改/新增，蓝色=其他说明）。


<metadata>
{
  "title": "20251128_IS122_上海证券交易所交易网关STEP接口规格说明书（互联网交易平台）1",
  "source_url": null,
  "raw_path": "knowledge\\raw\\sse\\技术接口\\20251128_IS122_上海证券交易所交易网关STEP接口规格说明书（互联网交易平台）1.14版_20251128.pdf",
  "markdown_path": "knowledge\\articles\\sse\\markdown\\技术接口\\IS122_上海证券交易所交易网关STEP接口规格说明书（互联网交易平台）1.14版_20251128.md",
  "file_hash": "sha256:d909786811e3dad5b24594e3913dc475e2d8b06e43e601834f6b8d26a089068c",
  "file_format": "pdf",
  "page_count": 60,
  "doc_type": "interface_spec",
  "version": null,
  "previous_version": null,
  "public_date": null,
  "effective_date": null,
  "has_changes": true,
  "parse_status": "success",
  "parse_date": "2026-05-02T01:47:07.076537+00:00",
  "sub_category": null
}
</metadata>