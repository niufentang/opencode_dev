工程技术标准
深圳证券交易所成交汇总文件接口
市场参与者技术系统变更指南
(Ver1.0 7 )
深圳证券交易所
二○二○年十 二 月

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
文档说明
修订历史
日期
版本
修订说明
2016-6-3
Ver1.00
新建
增加债券质押式三方回购交易业务成交确认、债券质押式
2018-2-12
Ver1.01
三方回购出入库业务订单响应执行报告
增加期权组合策略保证金业务订单响应执行报告、期权普
2019-1-16
Ver1.02
通与备兑仓互转业务订单响应执行报告、期权行权指令合
并申报业务订单响应执行报告
增加盘后定价交易业务订单成交执行报告
2020-3-25
Ver1.03
转融通证券出借非约定申报成交执行报告、转融通证券出
借约定申报成交确认增加字段：股份性质（ ShareProperty ）
2020-9-1
Ver1.04 修改债券质押式协议回购成交确认
债券转股回售业务订单响应执行报告增加字段：股份性质
2020-10-13 Ver1.05
（ ShareProperty ）
债券质押式协议回购业务成交确认增加字段：股份性质
2020-12-23 Ver1.06
（ UnderlyingShareProperty ）
（本文档中橙色修订部分）
2020-12-29 Ver1.07
期权集中竞价交易业务订单执行报告增加字段：第二交易
所订单编号（ SecondaryOrderID ）
I

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
目 录
一、
说明 ..................................................................................................................................................... 1
二、
成交汇总文件接口简介 ..................................................................................................................... 1
三、
成交汇总文件接收申请方式 ............................................................................................................. 1
四、
文件网关配置说明 ............................................................................................................................. 2
五、
成交汇总文件内容说明 ..................................................................................................................... 2
六、
相关事宜 ............................................................................................................................................. 5
6.1
参考文档 ........................................................................................................................................... 5
6.2
联系方式 ........................................................................................................................................... 5
七、
附 录 ................................................................................................................................................... 5
7.1
附录一：成交记录示例 ................................................................................................................... 5
7.1.1
现货集中竞价业务订单成交执行报告 ............................................................................... 5
7.1.2
质押式回购业务订单成交执行报告 ................................................................................... 6
7.1.3
债券分销业务订单成交执行报告 ....................................................................................... 7
7.1.4
期权集中竞价业务订单成交执行报告 ............................................................................... 8
7.1.5
协议交易业务订单成交执行报告 ....................................................................................... 9
7.1.6
协议交易业务双方配对成交确认 ..................................................................................... 10
7.1.7
盘后定价大宗交易业务订单成交执行报告 ..................................................................... 11
7.1.8
转融通证券出借非约定申报成交执行报告 ..................................................................... 12
7.1.9
转融通证券出借约定申报成交确认 ................................................................................. 13
7.1.10
资产管理计划份额转让业务成交申报响应 ..................................................................... 15
7.1.11
股票质押式回购业务成交申报响应 ................................................................................. 16
7.1.12
约定购回业务成交申报响应 ............................................................................................. 18
7.1.13
质押式报价回购业务成交申报响应 ................................................................................. 19
7.1.14
ETF 实时申购赎回业务订单响应执行报告 ...................................................................... 21
7.1.15
网上发行认购业务订单响应执行报告 ............................................................................. 22
7.1.16
配股认购业务订单响应执行报告 ..................................................................................... 24
7.1.17
债券转股回售业务订单响应执行报告 ............................................................................. 25
7.1.18
期权行权业务订单响应执行报告 ..................................................................................... 26
7.1.19
期权行权指令合并申报业务订单响应执行报告 ............................................................. 27
7.1.20
开放式基金申购赎回业务订单响应执行报告 ................................................................. 28
7.1.21
要约收购业务订单响应执行报告 ..................................................................................... 30
7.1.22
质押式回购质押解押业务订单响应执行报告 ................................................................. 31
7.1.23
转托管注册执行报告 ......................................................................................................... 32
7.1.24
黄金 ETF 实物申购赎回业务订单响应执行报告 ............................................................ 33
7.1.25
权证行权业务订单响应执行报告 ..................................................................................... 34
7.1.26
转处置业务订单响应执行报告 ......................................................................................... 35
7.1.27
垫券还券业务订单响应执行报告 ..................................................................................... 37
7.1.28
待清偿扣划业务订单响应执行报告 ................................................................................. 38
7.1.29
债券质押式协议回购业务成交确认 ................................................................................. 39
7.1.30
分级基金实时分拆合并业务订单响应执行报告 ............................................................. 41
7.1.31
债券质押式三方回购交易业务成交确认 ......................................................................... 42
II

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
7.1.32
债券质押式三方回购出入库业务订单响应执行报告 ..................................................... 44
7.1.33
期权组合策略保证金业务订单响应执行报告 ................................................................. 45
7.1.34
期权普通与备兑仓互转业务订单响应执行报告 ............................................................. 47
7.1.35
盘后定价交易业务订单成交执行报告 ............................................................................. 48
III

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
深圳证券交易所成交汇总文件接口
市场参与者技术系统变更指南
一、
说明
深圳证券交易所（以下简称“深交所”）新一代交易系统已经通过流接口的形式向
市场参与者提供了成交汇总数据服务，为了能够在收市后以文件形式提供成交汇总服务，
深交所新增了成交汇总文件接口。
本文档旨在阐述成交汇总文件接口的相关技术方案，供市场参与者及其 IT 提供商
进行相关技术系统改造时使用。如果方案有所变更，本文档将做相应修订。
深交所改造系统的宗旨：从技术上保障证券市场安全运行，同时，尽量降低系统改
造对市场参与者的影响。
二、
成交汇总文件接口简介
成交汇总文件提供文件形式的成交汇总服务，供基金托管行及其他有需要的市场参
与者使用。市场参与者需要申请并开通了成交汇总通信网关（以申请确认将哪些交易单
元的成交记录汇总）后才可以申请接收成交汇总文件服务。
成交汇总文件通过文件网关接收，与流接口相比除了通道、格式方面有差异外，在
记录内容和顺序上完全一致。
成交汇总文件的具体说明见《深圳证券交易所数据文件交换接口规范》。
三、
成交汇总文件接收申请方式
申请单位登录深交所会员业务系统提交申请，不能登录会员业务专区的申请单位请
向深证通提交书面申请。
申请步骤如下：
1. 新建成交汇总通信网关；
2. 开通成交汇总通信网关；
3. 文件通信网关（如没有则需申请新建）配置变更，申请开通“盘后成交汇总文
件接收”功能；
4. 交易单元有变化时，通过成交汇总通信网关配置变更，新增或删除交易单元。
上述各个步骤详细的办理流程和申请表见《深圳证券交易所新一代交易系统网关业
务办理指南》。
第 1 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
四、
文件网关配置说明
1. 添加连接人
登录 FxTerm 界面 -> 左树 “ 菜单导航 ”-> 配置菜单 -> 对端连接人配置，将深交所文件网
关号： F000000X0003 ，添加为联系人；
2. 配置传输规则
成交汇总文件下发业务，对端深交所网关号为 F000000X0003 ，传输规则名称为
szse_report_FnnnnnnFxxxx ，其中 FnnnnnnFxxxx 是用户的成交汇总网关号 。
详细的文件网关配置说明请见《深圳证券交易所新一代交易系统文件网关配置说
明》。
五、
成交汇总文件内容说明
成交汇总文件为文本文件，文件中的每条记录（一行）为一笔成交，记录内容定义
参考《深圳证券交易所 Binary 交易数据接口规范》中的二进制成交消息定义，记录的
具体格式说明参见《深圳证券交易所数据文件交换接口规范》。
市场参与者系统使用成交汇总文件时应注意：
1 、 深交所交易系统定义的每个业务平台对应一个成交汇总文件，如果该平台当天
没有回报记录，则也会下发一个空文件。
2 、 系统应能支持成交记录尾部扩展新的字段，不使用新扩展的字段时应能自动忽
略新字段而不需做技术改造。
为减少成交汇总服务的数据量，成交汇总服务下发的数据中不包括《深圳证券交易
所 Binary 交易数据接口规范》中仅用于委托确认的回报消息，具体可接收的消息类型
范围如下：
消息类型说明
消息类型
所属平台
MsgType
200115
现货集中
现货集中竞价交易业务订单成交执行报
竞价交易
告
平台
200215
综合金融
质押式回购交易业务订单成交执行报告
服务平台
200315
现货集中
债券分销业务订单成交执行报告
竞价交易
第 2 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
平台
期权集中竞价交易业务订单成交执行报
200415
衍生品集
中竞价交
告
易平台
协议交易业务订单成交执行报告
200515
协议交易业务双方配对成交确认
200503
盘后定价大宗交易业务订单成交执行报
200615
综合金融
服务平台
告
转融通证券出借业务非约定申报成交执
200715
综合金融
服务平台
行报告
转融通证券出借业务约定申报成交确认
200703
资产管理计划份额转让业务成交申报响
200804
综合金融
应
服务平台
股票质押式回购业务成交申报响应
200904
综合金融
服务平台
约定购回业务成交申报响应
201004
综合金融
服务平台
质押式报价回购业务成交申报响应
201104
综合金融
服务平台
201202
非交易处
ETF 实时申购赎回业务订单响应执行报告
理平台
201302
非交易处
网上发行认购业务订单响应执行报告
理平台
201402
非交易处
配股认购业务订单响应执行报告
理平台
201502
非交易处
债券转股回售业务订单响应执行报告
理平台
201602
非交易处
期权行权业务订单响应执行报告
理平台
期权行权指令合并申报业务订单响应执
201622
非交易处
行报告
理平台
开放式基金申购赎回业务订单响应执行
201702
非交易处
理平台
报告
201802
非交易处
要约收购业务订单响应执行报告
理平台
第 3 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
质押式回购质押解押业务订单响应执行
201902
非交易处
理平台
报告
202098
非交易处
转托管注册执行报告
理平台
黄金ETF 实物申购赎回业务订单响应执行
202202
非交易处
报告
理平台
202302
非交易处
权证行权业务订单响应执行报告
理平台
202702
非交易处
转处置业务订单响应执行报告
理平台
202802
非交易处
垫券还券业务订单响应执行报告
理平台
202902
非交易处
待清偿扣划业务订单响应执行报告
理平台
203003
固定收益
债券质押式协议回购业务成交确认
交易平台
分级基金实时分拆合并业务订单响应执
203102
非交易处
行报告
理平台
203203
综合金融
债券质押式三方回购交易申报成交确认
服务平台
债券质押式三方回购出入库订单响应执
203302
综合金融
行报告
服务平台
203422
衍生品集
期权组合策略保证金业务订单响应执行
中竞价交
报告
易平台
203502
衍生品集
期权普通与备兑仓互转业务订单响应执
中竞价交
行报告扩展字段
易平台
203715
综合金融
盘后定价交易业务订单成交执行报告
服务平台
各类成交记录的示例见附录一。
第 4 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
六、
相关事宜
6.1
参考文档
《深圳证券交易所数据文件交换接口规范》
《深圳证券交易所 Binary 交易数据接口规范）》
6.2
联系方式
技术咨询电话：（ 0755 ） 82083500
七、
附 录
7.1
附录一：成交记录示例
下面举例中的成交汇总记录中的 <T> 表示 Tab 字符（ ASCII 码为 0x09 ）， <N> 代表行
分隔符（ ASCII 码为 0x0A ）如“ 200115<T>2<T>010<N> ”。
7.1.1 现货集中竞价业务订单成交执行报告
二进制消息内容：
域名
取值
MsgType
200115
BodyLength
--
ReportIndex
2
ApplID
010
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
ExecID
1100000000004124
ExecType
F
OrdStatus
1
LastPx
171000
第 5 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
LastQty
30000
LeavesQty
90000
CumQty
30000
Side
1
AccountID
0100004698
BranchID
AA
CashMargin
1
对应到成交汇总文件中记录内容为：
200115<T>2<T>010<T>000100<T>000100<T>000001<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T>1100000000004124<T>F
<T>1<T>17.1000<T>300.00<T>900.00<T>300.00<T>1<T>0100004698<T>AA<T>1<N>
7.1.2 质押式回购业务订单成交执行报告
二进制消息内容：
域名
取值
MsgType
200215
BodyLength
--
ReportIndex
2
ApplID
020
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
131801
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
ExecID
1100000000004124
ExecType
F
OrdStatus
1
LastPx
171000
第 6 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
LastQty
30000
LeavesQty
90000
CumQty
30000
Side
1
AccountID
0100004698
BranchID
AA
MarturityDate
20160601
对应到成交汇总文件中记录内容为：
200215<T>2<T>020<T>000100<T>000100<T>131801<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T>1100000000004124<T>F
<T>1<T>17.1000<T>300.00<T>900.00<T>300.00<T>1<T>0100004698<T>AA<T>201606
01<N>
7.1.3 债券分销业务订单成交执行报告
二进制消息内容：
域名
取值
MsgType
200315
BodyLength
--
ReportIndex
2
ApplID
030
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
101651
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
ExecID
1100000000004124
ExecType
F
OrdStatus
1
第 7 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
LastPx
171000
LastQty
30000
LeavesQty
90000
CumQty
30000
Side
1
AccountID
0100004698
BranchID
AA
对应到成交汇总文件中记录内容为：
200315<T>2<T>030<T>000100<T>000100<T>101651<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T>1100000000004124<T>F
<T>1<T>17.1000<T>300.00<T>900.00<T>300.00<T>1<T>0100004698<T>AA<N>
7.1.4 期权集中竞价业务订单成交执行报告
二进制消息内容：
域名
取值
MsgType
200415
BodyLength
--
ReportIndex
2
ApplID
040
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
90000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
ExecID
1100000000004124
ExecType
F
OrdStatus
1
LastPx
171000
第 8 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
LastQty
30000
LeavesQty
90000
CumQty
30000
Side
1
AccountID
0100004698
BranchID
AA
PositionEffect
C
CoveredOrUncovered
0
ContractAccountCode
000100
SecondaryOrderID
6B4569CDNB009C03
对应到成交汇总文件中记录内容为：
200415<T>2<T>040<T>000100<T>000100<T>10000001<T>102<T>1<T>01<T>2013
0228144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T>1100000000004124<T
>F<T>1<T>17.1000<T>300.00<T>900.00<T>300.00<T>1<T>0100004698<T>AA<T> C <T
>0<T> 000100 <T> 6B4569CDNB009C03 <N>
7.1.5 协议交易业务订单成交执行报告
二进制消息内容：
域名
取值
MsgType
200515
BodyLength
--
ReportIndex
2
ApplID
051
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
第 9 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
ExecID
1100000000004124
ExecType
F
OrdStatus
1
LastPx
171000
LastQty
30000
LeavesQty
90000
CumQty
30000
Side
1
AccountID
0100004698
BranchID
AA
ConfirmID
00041246
CashMargin
1
对应到成交汇总文件中记录内容为：
200515<T>2<T>051<T>000100<T>000100<T>000001<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T>1100000000004124<T>F
<T>1<T>17.1000<T>300.00<T>900.00<T>300.00<T>1<T>0100004698<T>AA<T> 000412
46 <T>1<N>
7.1.6 协议交易业务双方配对成交确认
二进制消息内容：
域名
取值
MsgType
200503
BodyLength
--
ReportIndex
2
ApplID
053
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
第 10 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
TradeID
6B4569CDNB009C03
TradeReportID
0000004127
TradeReportType
0
TradeReportTransType
0
TradeHandlingInstr
2
LastPx
171000
LastQty
30000
TrdType
1031
TrdSubType
0
ConfirmID
11000045
ExecID
1100000000004124
Side
1
PBUID
000100
AccountID
0100004698
BranchID
AA
CounterpartyPBUID
000100
CounterpartyAccountID
0100005898
CounterpartyBranchID
BB
CashMargin
1
对应到成交汇总文件中记录内容为：
200503<T>2<T>053<T>000100<T>000100<T>000001<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>0000004127<T>0<T>0<T>2<T>17.100
0<T>300.00<T>1031<T>0<T>11000045<T>1100000000004124<T>1<T>000100<T>01000
04698<T>AA<T>000100<T>0100005898<T>BB<T>1<N>
7.1.7 盘后定价大宗交易业务订单成交执行报告
二进制消息内容：
域名
取值
MsgType
200615
BodyLength
--
ReportIndex
2
ApplID
060
第 11 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
ExecID
1100000000004124
ExecType
F
OrdStatus
1
LastPx
171000
LastQty
30000
LeavesQty
90000
CumQty
30000
Side
1
AccountID
0100004698
BranchID
AA
CashMargin
1
对应到成交汇总文件中记录内容为：
200615<T>2<T>060<T>000100<T>000100<T>000001<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T>1100000000004124<T>F
<T>1<T>17.1000<T>300.00<T>900.00<T>300.00<T>1<T>0100004698<T>AA<T>1<N>
7.1.8 转融通证券出借非约定申报成交执行报告
二进制消息内容：
域名
取值
MsgType
200715
BodyLength
--
ReportIndex
2
ApplID
070
第 12 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
ExecID
1100000000004124
ExecType
F
OrdStatus
1
LastPx
171000
LastQty
30000
LeavesQty
90000
CumQty
30000
Side
1
AccountID
0100004698
BranchID
AA
ExpirationDays
10
ExpirationType
1
MarturityDate
20160601
ShareProperty
00
对应到成交汇总文件中记录内容为：
200715<T>2<T>070<T>000100<T>000100<T>000001<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T>1100000000004124<T>F
<T>1<T>17.1000<T>300.00<T>900.00<T>300.00<T>1<T>0100004698<T>AA<T>10<T>
1<T>20160601<T>00<N>
7.1.9 转融通证券出借约定申报成交确认
二进制消息内容：
域名
取值
第 13 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
MsgType
200703
BodyLength
--
ReportIndex
2
ApplID
071
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
TradeID
6B4569CDNB009C03
TradeReportID
0000004127
TradeReportType
0
TradeReportTransType
0
TradeHandlingInstr
2
LastPx
171000
LastQty
30000
TrdType
1031
TrdSubType
0
ConfirmID
11000045
ExecID
1100000000004124
Side
1
PBUID
000100
AccountID
0100004698
BranchID
AA
CounterpartyPBUID
000100
CounterpartyAccountID
0100005898
CounterpartyBranchID
BB
ExpirationDays
10
ExpirationType
1
MarturityDate
20160601
ShareProperty
00
第 14 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
对应到成交汇总文件中记录内容为：
200703<T>2<T>071<T>000100<T>000100<T>000001<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>0000004127<T>0<T>0<T>2<T>17.100
0<T>300.00<T>1031<T>0<T>11000045<T>1100000000004124<T>1<T>000100<T>01000
04698<T>AA<T>000100<T>0100005898<T>BB<T>10<T>1<T> 20160601 <T>00<N>
7.1.10 资产管理计划份额转让业务成交申报响应
二进制消息内容：
域名
取值
MsgType
200804
BodyLength
--
ReportIndex
2
ApplID
080
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
119502
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
TradeID
6B4569CDNB009C03
TradeReportID
0000004127
TradeReportType
0
TradeReportTransType
0
TradeHandlingInstr
2
TradeReportRefID
0000004144
TrdAckStatus
0
TrdRptStatus
0
TradeReportRejectReason 0
LastPx
171000
LastQty
30000
第 15 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
TrdType
1031
TrdSubType
0
ConfirmID
11000045
ExecID
1100000000004124
Side
1
PBUID
000100
AccountID
0100004698
BranchID
AA
CounterpartyPBUID
000100
CounterpartyAccountID
0100005898
CounterpartyBranchID
BB
PriceType
3
对应到成交汇总文件中记录内容为：
200804<T>2<T>080<T>000100<T>000100<T>119502<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>0000004127<T>0<T>0<T>2<T>00000
04144<T>0<T>0<T>0<T>17.1000<T>300.00<T>1031<T>0<T>11000045<T>11000000000
04124<T>1<T>000100<T>0100004698<T>AA<T>000100<T>0100005898<T>BB<T>3<N
>
7.1.11 股票质押式回购业务成交申报响应
二进制消息内容：
域名
取值
MsgType
200904
BodyLength
--
ReportIndex
2
ApplID
090
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
第 16 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
TransactTime
20130228144215555
UserInfo
test
TradeID
6B4569CDNB009C03
TradeReportID
0000004127
TradeReportType
0
TradeReportTransType
0
TradeHandlingInstr
2
TradeReportRefID
0000004144
TrdAckStatus
0
TrdRptStatus
0
TradeReportRejectReason 0
LastPx
171000
LastQty
30000
TrdType
1031
TrdSubType
0
ConfirmID
11000045
ExecID
1100000000004124
Side
2
PBUID
000100
AccountID
0100004698
BranchID
AA
CounterpartyPBUID
000100
CounterpartyAccountID
0100005898
CounterpartyBranchID
BB
CashOrderQty
0
ShareProperty
0
MaturityDate
20160601
PledgeeType
1
OrigTradeID
6B4569CDNB009D31
OrigSubmittingPBUID
000100
OrigTradeReportID
1110004127
OrigTradeDate
20160108
对应到成交汇总文件中记录内容为：
第 17 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
200904<T>2<T>090<T>000100<T>000100<T>000001<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>0000004127<T>0<T>0<T>2<T>00000
04144<T>0<T>0<T>0<T>17.1000<T>300.00<T>1031<T>0<T>11000045<T>11000000000
04124<T>2<T>000100<T>0100004698<T>AA<T>000100<T>0100005898<T>BB<T>0.00
00<T>0<T>20160601<T>1<T>6B4569CDNB009D31<T>000100<T>1110004127<T>2016
0108<N>
7.1.12 约定购回业务成交申报响应
二进制消息内容：
域名
取值
MsgType
201004
BodyLength
--
ReportIndex
2
ApplID
100
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
TradeID
6B4569CDNB009C03
TradeReportID
0000004127
TradeReportType
0
TradeReportTransType
0
TradeHandlingInstr
2
TradeReportRefID
0000004144
TrdAckStatus
0
TrdRptStatus
0
TradeReportRejectReason 0
LastPx
171000
LastQty
30000
第 18 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
TrdType
1031
TrdSubType
0
ConfirmID
11000045
ExecID
1100000000004124
Side
1
PBUID
000100
AccountID
0100004698
BranchID
AA
CounterpartyPBUID
000100
CounterpartyAccountID
0100005898
CounterpartyBranchID
BB
CashOrderQty
0
MaturityDate
20160601
OrigTradeID
6B4569CDNB009D31
OrigSubmittingPBUID
000100
OrigTradeReportID
1110004127
OrigTradeDate
20160108
对应到成交汇总文件中记录内容为：
201004<T>2<T>100<T>000100<T>000100<T>000001<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>0000004127<T>0<T>0<T>2<T>00000
04144<T>0<T>0<T>0<T>17.1000<T>300.00<T>1031<T>0<T>11000045<T>11000000000
04124<T>1<T>000100<T>0100004698<T>AA<T>000100<T>0100005898<T>BB<T>0.00
00<T>20160601<T>6B4569CDNB009D31<T>000100<T>1110004127<T>20160108<N>
7.1.13 质押式报价回购业务成交申报响应
二进制消息内容：
域名
取值
MsgType
201104
BodyLength
--
ReportIndex
2
ApplID
110
ReportingPBUID
000100
第 19 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
SubmittingPBUID
000100
SecurityID
132001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
TradeID
6B4569CDNB009C03
TradeReportID
0000004127
TradeReportType
0
TradeReportTransType
0
TradeHandlingInstr
2
TradeReportRefID
0000004144
TrdAckStatus
0
TrdRptStatus
0
TradeReportRejectReason 0
LastPx
171000
LastQty
30000
TrdType
1031
TrdSubType
0
ConfirmID
11000045
ExecID
1100000000004124
Side
1
PBUID
000100
AccountID
0100004698
BranchID
AA
CounterpartyPBUID
000100
CounterpartyAccountID
0100005898
CounterpartyBranchID
BB
PriceType
1
ExpirationExecInst
1
ExpirationDays
10
MaturityDate
20160601
OrigTradeID
6B4569CDNB009D31
第 20 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
OrigSubmittingPBUID
000100
OrigTradeReportID
1110004127
OrigTradeDate
20160108
对应到成交汇总文件中记录内容为：
201104<T>2<T>110<T>000100<T>000100<T>132001<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>0000004127<T>0<T>0<T>2<T>00000
04144<T>0<T>0<T>0<T>17.1000<T>300.00<T>1031<T>0<T>11000045<T>11000000000
04124<T>1<T>000100<T>0100004698<T>AA<T>000100<T>0100005898<T>BB<T>1<T
>1<T>10<T>20160601<T>6B4569CDNB009D31<T>000100<T>1110004127<T>20160108
<N>
7.1.14 ETF 实时申购赎回业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
201202
BodyLength
--
ReportIndex
2
ApplID
120
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
159001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
1100000000004124
ExecType
0
OrdStatus
1
OrdRejReason
0
第 21 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
LeavesQty
90000
CumQty
30000
Side
1
OrdType
2
OrderQty
30000
Price
171000
AccountID
0100004698
BranchID
AA
OrderRestrictions
InsufficientSecurityID
NoSecurity
3
UnderlyingSecurityID
000001
UnderlyingSecurityIDSource 102
DeliveryQty
150000
SubstCash
0
UnderlyingSecurityID
000002
UnderlyingSecurityIDSource 102
DeliveryQty
70000
SubstCash
60375000
UnderlyingSecurityID
000004
UnderlyingSecurityIDSource 102
DeliveryQty
0
SubstCash
513571360
对应到成交汇总文件中记录内容为：
201202<T>2<T>120<T>000100<T>000100<T>159001<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T>
<T>1100000000004124<T>0<T>1<T>0<T>900.00<T>300.00<T>1<T>2<T>300.00<T>17.
1000<T>0100004698<T>AA<T><T><T>3<T>000001<T>102<T>1500.00<T>0.0000<T>0
00002<T>102<T>700.00<T>6037.5000<T>000004<T>102<T>0.00<T>51357.1360<N>
7.1.15 网上发行认购业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
201302
BodyLength
--
第 22 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
ReportIndex
2
ApplID
130
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
169102
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
1100000000004124
ExecType
0
OrdStatus
1
OrdRejReason
0
LeavesQty
90000
CumQty
30000
Side
1
OrdType
2
OrderQty
30000
Price
171000
AccountID
0100004698
BranchID
AA
OrderRestrictions
对应到成交汇总文件中记录内容为：
201302<T>2<T>130<T>000100<T>000100<T>169102<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T>
<T>1100000000004124<T>0<T>1<T>0<T>900.00<T>300.00<T>1<T>2<T>300.00<T>17.
1000<T>0100004698<T>AA<T><N>
第 23 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
7.1.16 配股认购业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
201402
BodyLength
--
ReportIndex
2
ApplID
140
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
380001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
1100000000004124
ExecType
0
OrdStatus
1
OrdRejReason
0
LeavesQty
90000
CumQty
30000
Side
1
OrdType
2
OrderQty
30000
Price
171000
AccountID
0100004698
BranchID
AA
OrderRestrictions
对应到成交汇总文件中记录内容为：
201402<T>2<T>140<T>000100<T>000100<T> 380001 <T>102<T>1<T>01<T>2013022
第 24 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
8144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T>
<T>1100000000004124<T>0<T>1<T>0<T>900.00<T>300.00<T>1<T>2<T>300.00<T>17.
1000<T>0100004698<T>AA<T><N>
7.1.17 债券转股回售业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
201502
BodyLength
--
ReportIndex
2
ApplID
150
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
117002
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
0301000000004124
ExecType
0
OrdStatus
0
OrdRejReason
0
LeavesQty
100000
CumQty
0
Side
1
OrdType
2
OrderQty
100000
Price
0
AccountID
0100004698
第 25 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
BranchID
AA
OrderRestrictions
ShareProperty
00
对应到成交汇总文件中记录内容为：
201502<T>2<T>150<T>000100<T>000100<T>
117002 <T>102<T>1<T>01<T>20130228144215555<T>test<T>6B4569CDNB009C03<T>A
0000001<T><T>0301000000004124<T>0<T>0<T>0<T>1000.00<T>0.00<T>1<T>2<T>10
00.00<T>0.0000<T> 0100004698<T>AA<T><T>00<N>
7.1.18 期权行权业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
201602
BodyLength
--
ReportIndex
2
ApplID
160
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
90000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
0301000000004124
ExecType
0
OrdStatus
0
OrdRejReason
0
LeavesQty
100000
第 26 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
CumQty
0
Side
1
OrdType
2
OrderQty
100000
Price
0
AccountID
0100004698
BranchID
AA
OrderRestrictions
ContractAccountCode
000100
对应到成交汇总文件中记录内容为：
201602<T>2<T>160<T>000100<T>000100<T>10000001<T>102<T>1<T>01<T>2013
0228144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T><T>030100000000412
4<T>0<T>0<T>0<T>1000.00<T>0.00<T>1<T>2<T>1000.00<T>0.0000<T>0100004698<T
>AA<T><T>000100<N>
7.1.19 期权行权指令合并申报业务订单响应执行报告
二进制消息内容:
域名
取值
MsgType
201622
BodyLength
--
ReportIndex
2
ApplID
161
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
159901
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
第 27 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
OrigClOrdID
ExecID
1100000000004124
ExecType
0
OrdStatus
0
OrdRejReason
0
LeavesQty
0
CumQty
0
Side
1
OrdType
2
OrderQty
120000
Price
0
AccountID
0100004698
BranchID
AA
OrderRestrictions
ContractAccountCode
000100
NoLegs
2
LegSecurityID
90000001
LegSecurityIDSource
102
LegOrderQty
120000
LegSecurityID
90000002
LegSecurityIDSource
102
LegOrderQty
120000
对应到成交汇总文件中记录内容为：
201602<T>2<T>161<T>000100<T>000100<T>159901<T>102<T>1<T>01<T>2013
0228144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T>
<T>1100000000004124<T>0<T>0<T>0<T>0.00<T>0.00<T>1200.00<T>1<T>2<T>1200
.00<T>0.0000<T>0100004698<T>AA<T><T>000100<T>2<T>90000001<T>102<T>120
0.00<T>90000002<T>102<T>1200.00<N>
7.1.20 开放式基金申购赎回业务订单响应执行报告
二进制消息内容：
域名
取值
第 28 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
MsgType
201702
BodyLength
--
ReportIndex
2
ApplID
170
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
150008
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
0301000000004124
ExecType
0
OrdStatus
0
OrdRejReason
0
LeavesQty
0
CumQty
0
Side
D
OrdType
2
OrderQty
0
Price
0
AccountID
0100004698
BranchID
AA
OrderRestrictions
CashOrderQty
100000000
对应到成交汇总文件中记录内容为：
201702<T>2<T>170<T>000100<T>000100<T>150008<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T><T>0301000000004124<
第 29 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
T>0<T>0<T>0<T>0.00<T>0.00<T>D<T>2<T>0.00<T>0.0000<T>0100004698<T>AA<T>
<T>10000.0000<N>
7.1.21 要约收购业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
201802
BodyLength
--
ReportIndex
2
ApplID
180
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
0301000000004124
ExecType
0
OrdStatus
0
OrdRejReason
0
LeavesQty
100000
CumQty
0
Side
1
OrdType
2
OrderQty
100000
Price
0
AccountID
0100004698
BranchID
AA
第 30 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
OrderRestrictions
Tenderer
000001
对应到成交汇总文件中记录内容为：
201802<T>2<T>180<T>000100<T>000100<T>000001<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T><T>0301000000004124<
T>0<T>0<T>0<T>1000.00<T>0.00<T>1<T>2<T>1000.00<T>0.0000<T>0100004698<T>
AA<T><T>000001<N>
7.1.22 质押式回购质押解押业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
201902
BodyLength
--
ReportIndex
2
ApplID
190
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
0301000000004124
ExecType
0
OrdStatus
0
OrdRejReason
0
LeavesQty
100000
CumQty
0
第 31 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
Side
1
OrdType
2
OrderQty
100000
Price
0
AccountID
0100004698
BranchID
AA
OrderRestrictions
对应到成交汇总文件中记录内容为：
201902<T>2<T>190<T>000100<T>000100<T>000001<T>102<T>1<T>01<T>201302281
44215555<T>test<T>6B4569CDNB009C03<T>A0000001<T><T>0301000000004124<T>
0<T>0<T>0<T>1000.00<T>0.00<T>1<T>2<T>1000.00<T>0.0000<T>0100004698<T>AA
<T><N>
7.1.23 转托管注册执行报告
二进制消息内容：
域名
字段描述
MsgType
202098
BodyLength
--
ReportIndex
2
ApplID
200
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
0301000000004124
第 32 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
ExecType
0
OrdRejReason
0
DesignationInstruction
3
DesignationTransType
1
AccountID
0100004698
BranchID
AA
OrderQty
100000
TransfereePBUID
000200
对应到成交汇总文件中记录内容为：
202098<T>2<T>200<T>000100<T>000100<T>000001<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T><T>0301000000004124<
T>0<T>0<T>3<T>1<T>0100004698<T>AA<T>1000.00<T>000200<N>
7.1.24 黄金 ETF 实物申购赎回业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
202202
BodyLength
--
ReportIndex
2
ApplID
220
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
159934
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
第 33 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
ExecID
0301000000004124
ExecType
0
OrdStatus
0
OrdRejReason
0
LeavesQty
100000
CumQty
0
Side
D
OrdType
2
OrderQty
100000
Price
0
AccountID
0100004698
BranchID
AA
OrderRestrictions
对应到成交汇总文件中记录内容为：
202202<T>2<T>220<T>000100<T>000100<T>159934<T>102<T>1<T>01<T>20130
228144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T><T>0301000000004124
<T>0<T>0<T>0<T>1000.00<T>0.00<T>D<T>2<T>1000.00<T>0.0000<T>0100004698<T
>AA<T><N>
7.1.25 权证行权业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
202302
BodyLength
--
ReportIndex
2
ApplID
230
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
038999
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
第 34 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
0301000000004124
ExecType
0
OrdStatus
0
OrdRejReason
0
LeavesQty
100000
CumQty
0
Side
1
OrdType
2
OrderQty
100000
Price
0
AccountID
0100004698
BranchID
AA
OrderRestrictions
对应到成交汇总文件中记录内容为：
202302<T>2<T>230<T>000100<T>000100<T>038999<T>102<T>1<T>01<T>20130
228144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T><T>0301000000004124
<T>0<T>0<T>0<T>1000.00<T>0.00<T>1<T>2<T>1000.00<T>0.0000<T>0100004698<T
>AA<T><N>
7.1.26 转处置业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
202702
BodyLength
--
ReportIndex
2
ApplID
270
ReportingPBUID
000100
第 35 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
SubmittingPBUID
000100
SecurityID
10000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
0301000000004124
ExecType
0
OrdStatus
0
OrdRejReason
0
LeavesQty
100000
CumQty
0
Side
1
OrdType
2
OrderQty
100000
Price
0
AccountID
0100004698
BranchID
AA
OrderRestrictions
DisposalPBU
000200
DisposalAccountID
0100004690
对应到成交汇总文件中记录内容为：
202702<T>2<T>270<T>000100<T>000100<T>10000001<T>102<T>1<T>01<T>201
30228144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T><T>03010000000041
24<T>0<T>0<T>0<T>1000.00<T>0.00<T>1<T>2<T>1000.00<T>0.0000<T>0100004698<
T>AA<T><T>000200<T> 0100004690<N>
第 36 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
7.1.27 垫券还券业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
202802
BodyLength
--
ReportIndex
2
ApplID
280
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
10000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
0301000000004124
ExecType
0
OrdStatus
0
OrdRejReason
0
LeavesQty
100000
CumQty
0
Side
1
OrdType
2
OrderQty
100000
Price
0
AccountID
0100004698
BranchID
AA
OrderRestrictions
LenderPBU
000200
LenderAccountID
0100004690
第 37 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
对应到成交汇总文件中记录内容为：
202802<T>2<T>280<T>000100<T>000100<T>10000001<T>102<T>1<T>01<T>201
30228144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T><T>03010000000041
24<T>0<T>0<T>0<T>1000.00<T>0.00<T>1<T>2<T>1000.00<T>0.0000<T>0100004698<
T>AA<T><T>000200<T> 0100004690<N>
7.1.28 待清偿扣划业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
202902
BodyLength
--
ReportIndex
2
ApplID
290
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
10000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
0301000000004124
ExecType
0
OrdStatus
0
OrdRejReason
0
LeavesQty
100000
CumQty
0
Side
1
OrdType
2
第 38 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
OrderQty
100000
Price
0
AccountID
0100004698
BranchID
AA
OrderRestrictions
DeductionPBU
000200
DeductionAccountID
0100004690
对应到成交汇总文件中记录内容为：
202902<T>2<T>290<T>000100<T>000100<T>10000001<T>102<T>1<T>01<T>201
30228144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T><T>03010000000041
24<T>0<T>0<T>0<T>1000.00<T>0.00<T>1<T>2<T>1000.00<T>0.0000<T>0100004698<
T>AA<T><T>000200<T> 0100004690<N>
7.1.29 债券质押式协议回购业务成交确认
二进制消息内容：
域名
字段描述
MsgType
203003
BodyLength
--
ReportIndex
2
ApplID
300
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
100213
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
TradeID
6B4569CDNB009C03
TradeReportID
0000004127
TradeReportType
0
TradeReportTransType
0
第 39 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
TradeHandlingInstr
2
LastPx
171000
LastQty
10000
TrdType
1031
TrdSubType
0
ConfirmID
11000045
ExecID
0201000000004124
Side
1
PBUID
000100
AccountID
0100004698
BranchID
AA
CounterpartyPBUID
000100
CounterpartyAccountID
0100005898
CounterpartyBranchID
BB
MemberID
000001
InvestorType
01
InvestorID
0000000001
InvestorName
investor_name
TraderCode
01000000
CounterpartyMemberID
000002
CounterpartyInvestorType
02
CounterpartyInvestorID
0000000002
CounterpartyInvestorName
counterparty_investor_name
CounterpartyTraderCode
02000000
TrdMatchID
0201000000000001
ExpirationDays
7
CashOrderQty
17100000
Memo
Memo
NoSecurity
1
UnderlyingSecurityID
100213
UnderlyingSecurityIDSource
102
DeliveryQty
10000000
DeliverySide
1
第 40 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
UnderlyingShareProperty
00
对应到成交汇总文件中记录内容为：
203003<T>2<T>300<T>000100<T>000100<T>100213<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>0000004127<T>0<T>0<T>2<T>17.100
0<T>100.00<T>1031<T>0<T>11000045<T>0201000000004124<T>1<T>000100<T>0100
004698<T>AA<T>000100<T>0100005898<T>BB<T>000001<T>01<T>0000000001<T>in
vestor_name<T>01000000<T>000002<T>02<T>0000000002<T>counterparty_investor_na
me<T>02000000<T>0201000000000001<T>7<T>1710.0000<T>Memo<T>1<T>100213<T
>102<T>1000.0000<T>1 <T>00 <N>
7.1.30 分级基金实时分拆合并业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
203102
BodyLength
--
ReportIndex
2
ApplID
310
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
160420
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
0301000000004124
ExecType
0
OrdStatus
0
OrdRejReason
0
第 41 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
LeavesQty
100000
CumQty
0
Side
1
OrdType
2
OrderQty
100000
Price
0
AccountID
0100004698
BranchID
AA
OrderRestrictions
InsufficientSecurityID
NoSecurity
2
UnderlyingSecurit
150303
→
yID
UnderlyingSecurit
→
102
yIDSource
→
DeliveryQty
50000
UnderlyingSecurit
150304
→
yID
UnderlyingSecurit
→
102
yIDSource
→
DeliveryQty
50000
对应到成交汇总文件中记录内容为：
203102<T>2<T>310<T>000100<T>000100<T>160420<T>102<T>1<T>01<T>20130
228144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T><T>0301000000004124
<T>0<T>0<T>0<T>1000.00<T>0.00<T>1<T>2<T>1000.00<T>0.0000<T>0100004698<T
>AA<T><T><T>2<T> 150303<T>102<T>500.00 <T> 150304<T>102<T>500.00 <N>
7.1.31 债券质押式三方回购交易业务成交确认
二进制消息内容：
域名
取值
MsgType
203203
BodyLength
--
第 42 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
ReportIndex
2
ApplID
320
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
SecurityIDSource
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
TradeID
6B4569CDNB009C03
TradeReportID
0000004129
TradeReportType
0
TradeReportTransType
0
TradeHandlingInstr
2
LastPx
51000
LastQty
0
TrdType
1041
TrdSubType
0
ConfirmID
11000045
ExecID
0201000000004124
Side
1
PBUID
000100
AccountID
0100004698
BranchID
AA
CounterpartyPBUID
000100
CounterpartyAccountID
0100005898
CounterpartyBranchID
TrdMatchID
0201000000000001
OrigTradeDate
20130228
MaturityDate
20130307
ExpirationDays
7
CashOrderQty
5000000000
第 43 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
SettlCurrAmt
5500000000
NoBaskets
2
→
BasketID
1
→
BasketID
2
NoUnderlyings
2
UnderlyingSecurity
100203
→
ID
UnderlyingSecurity
102
→
IDSource
→
DeliveryQty
20000
→
DeliverySide
1
UnderlyingSecurity
100213
→
ID
UnderlyingSecurity
102
→
IDSource
→
DeliveryQty
30000
→
DeliverySide
1
对应到成交汇总文件中记录内容为：
203203<T>2<T>320<T>000100<T>000100<T><T><T>1<T>01<T>201302281442155
55<T>test<T>6B4569CDNB009C03<T>0000004129<T>0<T>0<T>2<T>5.1000<T><T>10
41<T>0.00<T>11000045<T>0201000000004124<T>1<T>000100<T>0100004698<T>AA<
T>000100<T>0100005898<T><T>0201000000000001<T>20130228<T>20130307<T>7<T
>500000.0000<T>550000.0000<T>2<T>1<T>2<T>2<T>100203<T>102<T>200.00<T>1<
T>100213<T>102<T>300.00<T>1<N>
7.1.32 债券质押式三方回购出入库业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
203302
BodyLength
--
ReportIndex
2
ApplID
330
ReportingPBUID
000100
第 44 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
SubmittingPBUID
000100
SecurityID
100203
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
Test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
1100000000004124
ExecType
0
OrdStatus
1
OrdRejReason
0
LeavesQty
0
CumQty
30000
Side
1
OrdType
2
OrderQty
30000
Price
0
AccountID
0100004698
BranchID
AA
OrderRestrictions
对应到成交汇总文件中记录内容为：
203302<T>2<T>330<T>000100<T>000100<T>100203<T>102<T>1<T>01<T>201302
28144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T>
<T>1100000000004124<T>0<T>1<T>0<T>0.00<T>300.00<T>1<T>2<T>300.00<T>0.000
0<T>0100004698<T>AA<T><N>
7.1.33 期权组合策略保证金业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
203422
第 45 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
BodyLength
--
ReportIndex
2
ApplID
340
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
159901
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
Test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
1100000000004124
ExecType
0
OrdStatus
0
OrdRejReason
0
LeavesQty
0
CumQty
0
Side
1
OrdType
2
OrderQty
100
Price
0
AccountID
0100004698
BranchID
AA
OrderRestrictions
ContractAccountCode
000100
SecondaryOrderID
6B4569CSDB009C56
SecurityType
MLEG
SecuritySubType
CNSJC
NoLegs
2
→
LegSecurityID
90000001
→
LegSecurityIDSource 102
第 46 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
→
LegSide
1
→
LegOrderQty
100
→
LegSecurityID
90000002
→
LegSecurityIDSource 102
→
LegSide
2
→
LegOrderQty
100
对应到成交汇总文件中记录内容为：
203422<T>2<T>340<T>000100<T>000100<T>100203<T>102<T>1<T>01<T>201302
28144215555<T>Test<T>6B4569CDNB009C03<T>A0000001<T><T>1100000000004124
<T>0<T>0<T>0<T>0<T>0<T>1<T>2<T>1.00<T>0<T>0100004698<T>AA<T><T>00010
0<T>6B4569CSDB009C56<T>MLEG<T>CNSJC<T>2<T>90000001<T>102<T>1<T>1.00
<T>90000002<T>102<T>2<T>1.00<T><N>
7.1.34 期权普通与备兑仓互转业务订单响应执行报告
二进制消息内容：
域名
取值
MsgType
203502
BodyLength
--
ReportIndex
2
ApplID
350
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
90000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
ClOrdID
A0000001
OrigClOrdID
ExecID
0301000000004124
ExecType
0
第 47 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
OrdStatus
0
OrdRejReason
0
LeavesQty
100000
CumQty
0
Side
1
OrdType
2
OrderQty
100000
Price
0
AccountID
0100004698
BranchID
AA
OrderRestrictions
ContractAccountCode
000100
对应到成交汇总文件中记录内容为：
203502<T>2<T>350<T>000100<T>000100<T> 92000001 <T>102<T>1<T>01<T>20130
228144215555<T>test<T>6B4569CDNB009C03<T>A0000001<T><T>0301000000004124
<T>0<T>0<T>0<T>1000.00<T>0.00<T>1<T>2<T>1000.00<T>0.0000<T>0100004698<T
>AA<T><T>000100<N>
7.1.35 盘后定价交易业务订单成交执行报告
二进制消息内容：
域名
取值
MsgType
203715
BodyLength
--
ReportIndex
2
ApplID
370
ReportingPBUID
000100
SubmittingPBUID
000100
SecurityID
000001
SecurityIDSource
102
OwnerType
1
ClearingFirm
01
TransactTime
20130228144215555
UserInfo
test
OrderID
6B4569CDNB009C03
第 48 页 共 49 页

工程技术标准 深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南
ClOrdID
A0000001
ExecID
1100000000004124
ExecType
F
OrdStatus
1
LastPx
171000
LastQty
30000
LeavesQty
90000
CumQty
30000
Side
1
AccountID
0100004698
BranchID
AA
CashMargin
1
对应到成交汇总文件中记录内容为：
203715<T>2<T>370<T>000100<T>000100<T>000001<T>102<T>1<T>01<T>201302281
44215555<T>test<T>6B4569CDNB009C03<T>A0000001<T>1100000000004124<T>F<T
>1<T>17.1000<T>300.00<T>900.00<T>300.00<T>1<T>0100004698<T>AA<T>1<N>
第 49 页 共 49 页

> **变更标注说明**：本文档中已用 `<span style="color:...">` 标注了变更内容（红色=修改/新增，蓝色=其他说明）。


<metadata>
{
  "title": "20201229_深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南（Ver1",
  "source_url": null,
  "raw_path": "knowledge\\raw\\szse\\技术指南\\20201229_深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南（Ver1.07）.pdf",
  "markdown_path": "knowledge\\articles\\szse\\markdown\\技术指南\\深圳证券交易所成交汇总文件接口市场参与者技术系统变更指南（Ver1.07）.md",
  "file_hash": "sha256:b36824a7a04be379cc9466893251779ef02214225e567de57ff6c9344abf5183",
  "file_format": "pdf",
  "page_count": 53,
  "doc_type": "guide",
  "version": "1",
  "previous_version": null,
  "public_date": "2020-10-13",
  "effective_date": null,
  "has_changes": true,
  "parse_status": "success",
  "parse_date": "2026-06-13T17:45:50.706520+00:00",
  "sub_category": null
}
</metadata>