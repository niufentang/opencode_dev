上海证券交易所
交易网关 STEP 接口规格说明书
（互联网交易平台 <span style="color:blue">）</span>
<span style="color:blue">（新固收</span> 技术开发稿）
2. <span style="color:blue">10</span> 版

二〇二五年 <span style="color:blue">十一</span> 月
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
（ 1 ）更新消息头的填写说明
（ 2 ）新订单申报中申报价格修改为非必填，对基金通报价交易，
2022-02
0.30
开发稿
申报价格必填；基金通转入转出，申报价格为空；
2022-02
1.00
正式稿
1. 增加询价业务类接口
2. 增加订阅机制
2022-04
1.10
开发稿
3. 转入转出不支持撤单
1. 修改消息流图：报价方撤销报价处理，删除撤单成功执行报告；
2. 修改报价、报价状态回报、转发报价 tag 453 后接重复组字段
表述， “ 询价 ” 修改为 “ 报价 ”
3. 修改 tag 693 QuoteRespID 字段类型为 C18
2022-07
1.11
开发稿
4. 删除报价状态回报（ Quote Status Report ）中 tag 693
QuoteRespID
5. 报价回复新增字段： tag131 QuoteReqID ，用于匹配成交
1. 询价申报中订单价格上下限字段，增加字段说明 “ 预留，暂不
启用 ”
2. 调整询价处理消息流图：转发询价请求、转发报价请求去掉
2022-08
1.12
正式稿
orderID ；报价撤销成功回报去掉 ordID=or00003 ；报价撤销成功
回报的报价状态调整为 QuoteStatus=Cancelled
3. 转发询价请求、转发报价请求不再提供 orderID ，字段调整为

日期
版本
状态
说明
非必填
4. 询价状态回报、报价状态回报中 OrderID 调整为非必填，补充
字段说明
1. 要约 / 现金选择权（要约预受 / 现金选择权登记、要约撤销 / 现金
选择权注销）、开放式基金相关业务（申赎、分红选择、份额转
出）、融资融券非交易业务（余券划转、还券划转、担保品划入、
担保品划出、券源划入、券源划出）、网络密码服务（密码激活 /
注销），从竞价撮合平台迁移至互联网交易平台。
2025.08
1.13
正式稿
2.4.4.1.1 章节中，订单类型字段改为非必填；参与方个数取值改
为 10 ，其中结算会员代码改为非必填；变更发起方营业部代码范
围及说明、结算会员代码字段填写说明。
3.4.4.1.2 章节中，参与方个数变更；
4.4.3.1.1 章节中，参与方个数变更，结算会员代码改为非必填。
补充了原固定收益系统迁移至互联网交易平台一债通模块相关业
务申报接口内容，包括 :
1. 业务类型章节添加了新增的业务类型
2. 询价处理消息流中添加了通过公开行情发布的场景
3. 添加了意向申报和成交申报两类消息流图
4. 4.4.1 章节新订单申报中添加相关字段适配新增业务
2023.12
2.00
开发稿
5. 4.4.2.1 询价请求中删除了询价请求编号（ QuoteReqID ）字段，
添加了询价请求类型（ QuoteRequestType ）字段； 4.4.2.7 章节中
删除了报价回复消息编号（ QuoteRespID ）
6. 4.4.2 章节中添加相关字段适配新增业务
7. 新增了 4.4.3 和 4.4.4 两类申报消息
8. 4.4.5.1 中添加相关字段适配新增业务
1. 对于成交申报，支持对质押券各自设置份额类型和限售期
2. 对于各类业务的非通用必填项添加了业务分类对照表
2024.03
2.01
开发稿
3. 调整补充约定和补充条款字段标签；调整了成交申报中的相关

日期
版本
状态
说明
字段：原 RepurchaseTerm （回购期限）调整为 ExpirationDays （期
限），原 ExecType （执行报告类型）调整为 TrdAckStatus （成交
申报响应类型），原 OrdStatus （订单状态）调整为 TrdRptStatus
（成交申报状态），原
OrdRejReason
调整为
TradeReportRejectReason ；意向申报响应原 OrdRejReason 调整为
QuoteRejectReason
4. 调整总成交金额、总到期结算金额、总回购利息字段为预留字
段，原质权人名称字段调整为逆回购方账户名称
5. 新订单申报中对于基金通业务，结算会员代码调整为非必填
1. 4.4.4 成交申报中删除 OrigTradeDate （ 1125 ）字段
2. 4.4.4 成交申报中将 LastQty （ 32 ）调整为 CashOrderQty （ 152 ）
3. 4.4.2 询价报价消息体中 SecurityID （ 48 ）调整为 C12 ， ExecID
（ 17 ）由 C10 调整为 C16 ， QuoteID （ 117 ）调整为 C18
4. 根据市场反馈， 4.4.4 成交申报中增加 TEXT （ 58 ）
2024.03
2.02
开发稿
5. 转发成交申报调整为与成交申报一致
6. PreTradeAnonymity 字段删除 “9= 不指定 ” 枚举值
7. QuoteRespType 字段将 “2=Counter ，重报 ” 枚举值改为预留
8. 报价及转发报价重复组中相关字段统一调整为 “ 报价发起方 ” ，
报价回复重复组中相关字段统一调整为 “ 报价回复方 ”
1. 添加了三方回购申报接口
2. 添加了竞买业务的申报接口（预留，暂不启用）
3. 3.2.2.2.3 询价方与报价方成交（转发请求）和 3.2.2.3 报价处理
消息流图中对待定报价和确定报价的限定范围申报添加了成交后
更新转发订单信息的说明
2024.06
2.03
开发稿
4. 3.2.1 业务类型中私募可交换债转股修改为允许撤单
5. 4.2 中增加了中文编码的说明
6. 4.4.2.1 和 4.4.2.4 中对于冰山订单数量（ DisplayQty ）字段不允
许填 0 ； 4.4.2.2 中询价拒绝码调整为非必填。

日期
版本
状态
说明
7. 4.4.2.3 转发询价请求和 4.4.2.6 转发报价中移除冰山订单数量
字段，同时对于双边报价限定范围发布的情况明确将拆分为两笔
对外发送
8. 增加了 4.4.2.8 转发报价回复消息，
9. 4.4.3.1 意向申报中， SecurityID 调整为非必填；对于协议回购
意向申报调整 ExpirationDays 为必填， SettlDate 为选填
10. 4.4.1 和 4.4.5 中银行间托管账户由 C13 调整为 C11
11. 4.4.4 成交申报中为兼容迁移前存续期合约，补回了
OrigTradeDate （ 1125 ）字段；对于协议回购批量申报， N 笔质押
券将生成 N 笔响应，并拆分为 N 笔转发成交申报给对手方逐一确
认。
12. 4.4.4.2 转发成交申报中增加到期续做类型字段， 4.4.4.3 中增
加对于协议回购批量申报逐笔响应的说明并将发起方业务单元调
整为非必填
13. 4.4.4.4 成交确认中发起方投资者账户调整为非必填，增加了期
限、结算场所、结算周期和结算方式字段，增加了对于成交报告
模式下被动成交方的字段填写说明
14. 4.4.5.1.1 执行报告中增加了结算场所、结算时间和结算方式字
段
15. 4.4.2.2 询价请求响应、 4.4.2.5 报价状态回报、 4.4.3.3 意向申报
响应、 4.4.4.3 成交申报响应、 4.4.4.4 成交确认和 4.4.5.1 执行报告
中增加 ExecMethod （ 2405 ）字段表征申报订单来源
16. 4.4.7.1 申报拒绝（ Order Reject ）新增了意向申报和成交申报
消息，并将 SecurityID 调整为非必填
17. 移除各申报重复组中的发起方交易参与人代码
1. 4.4.4.1 成交申报、 4.4.4.2 转发成交申报、 4.4.4.3 成交申报响应、
4.4.4.4 成交确认修订了 EventType （ 865 ）字段的使用方式， Rest
2024.11
2.04
开发稿
rictedMonth （ 10332 ）格式修改为 N4 ，三方回购提前终止时修改
对提前终止后的到期结算金额和回购利息使用字段的表述

日期
版本
状态
说明
2. 4.4.2.3/4.4.2.6/4.4.2.8/4.4.4.2 转发询价、转发报价、转发报价
回复、转发成交申报请求中重复组中移除发起方业务交易单元号
和发起方营业部代码字段，转发报价回复中增加 PartitionNo （ 10
197 ）和 ReportIndex （ 10179 ）、发起方投资者账户调整为非必填；
转发成交申报中增加了投资者账户；转发询价、转发报价、转发
意向申报重复组中增加了对手方机构代码字段
3. 4.4.2.5 报价状态回报中明确买卖数量在撤单时表示剩余数量
4. 4.4.3.1 意向申报中对于现券和协议回购意向申报撤单时调整 S
ecurityID （ 48 ）为必填， 4.4.3.3 意向申报响应中添加了 IOITrans
Type （ 28 ）字段
5. 4.4.4.1 成交申报中对于现券和协议回购申报撤单时调整 Securi
tyID （ 48 ）为必填
6. 4.4.4.3 成交申报响应中将发起方业务单元调整为非必填，增加
了 ShareProperty(10331) 、 RestrictedMonth(10332) 和 ContractMulti
plier(231) 字段
7. 4.4.4.4 和 4.4.5.1 在成交回报中添加了对手方的信息， 4.4.4.4
成交确认中增加了 ShareProperty(10331) 、 RestrictedMonth(10332)
和 ContractMultiplier(231) 字段， 4.4.5.1 中增加了竞买申报自动发
起场景的响应描述
8. 账户名称字段由 C120 扩为 C180 ，备注字段由 C900 调整为 C
600 ，同时增加了场务应急成交录入的场景说明
1. 4.4.4.1 成交申报、 4.4.4.2 转发成交申报、 4.4.4.3 成交申报响应、
4.4.4.4 成交确认增加债券借贷业务相关字段及填报说明（预留，
暂不启用），协议回购批量申报时要求质押券不可重复
2. 3.2.2.2 询价报价处理消息流图、 3.2.2.3 报价处理消息流图、 3.
2025.1
2.05
开发稿
2.2.4.2 意向申报撤销请求处理（转发请求）、 3.2.2.5.3.2 成交请求
模式 - 撤单处理中根据实际协议字段统一了 QuoteReqID 、 QuoteRe
spID 、 QuoteID 、 OrderID 、 TradeID 等字段的描述方式

日期
版本
状态
说明
3. 4.4.2.5 报价状态回报中增加了报价回复响应中 QuoteID 填写方
式的说明
4. 4.4.5.1 执行报告中对于 OrderID 删除了“仅订单申报成功 Exe
cType=0 时有效”字样
5. 4.4.4.4 成交确认中增加 TotalValueTraded （ 8504 ）字段
1. 3.2.1 业务类型中对于三方回购转入转出修改笔误，不允许撤
单
2. 4.4.4.1 成交申报（ Trade Capture Report, MsgType=AE) 中 Ori
gTradeDate 字段格式调整为 date
3. 4.4.2.1 询价请求（ Quote Request, MsgType=R ）、 4.4.2.4 报价
（ Quote, MsgType=S ）、 4.4.3.1 意向申报（ IOI, Indication of Int
erest, MsgType=6) 及转发请求中对于 CounterpartyParticipantCode
字段和机构代码字段允许输入特殊符号‘ - ’
2025.2
2.06
开发稿
4. 4.4.4 成交申报类中不再要求填写账户名称字段，对于成交报告
申报模式的被动成交方，订单所有者类型（ OwnerType ）填‘ 103 ’
5. 4.4.5.1 执行报告（ Execution Report, MsgType = 8 ）中对于竞
买预约自动发起时申报来源（ ExecMethod ）字段与预约时相同，
对手方选择‘匿名’且为‘净额结算’时相关字段调整为填写‘ a
nonymous ’（转发报价、转发询价请求、转发报价回复时作类似
处理）。
1. 调整成交报告附后说明中的表格列宽，三方回购到期续做时增
加‘ TotalValueTraded ’字段必填
2. 调整 3.2.2.5.1 协议配对申报模式、 3.2.2.5.2 成交报告申报模式、
2025.4
2.07
开发稿
3.2.2.5.3 成交请求申报模式中的消息流图，修订若干字段笔误并
在协议配对申报模式中增加了配对失败的场景说明
1. 调整 3.2.2.2 询价报价处理消息流图的文字描述
2025.06
2.08
开发稿
2. 明确 4.4.4.2 转发成交申报中方向（ Side ）字段的具体含义
3. 为应对三方回购换券时存在同名质押券多次质押的场景， 4.4.

日期
版本
状态
说明
4.1 成交申报明确：三方回购对于换出券需要填写冻结申请书号
4. 3.2.2.5.4 双边确认申报模式数据流示意图中调整了转发申报 Tr
adeID 的填写方式
4.4.4.1 成交申报（ Trade Capture Report, MsgType=AE) 中，对于
协议回购：
2025.10
2.09
开发稿
1. 首期或续做利率大于 5% 时，调整 memo 字段必填，填写此利
率的合理性说明
<span style="color:blue">1.</span> <span style="color:blue">3.2.2.2</span> <span style="color:blue">询价报价处理消息流图和</span> <span style="color:blue">3.2.2.3</span> <span style="color:blue">报价处理消息流图中</span>
<span style="color:blue">调整笔误，将报价回复响应中的</span> <span style="color:blue">ClOrdID</span> <span style="color:blue">调整为</span> <span style="color:blue">QuoteMsgID</span>
<span style="color:blue">2.</span> <span style="color:blue">4.4.2.2</span> <span style="color:blue">询价请求响应、</span> <span style="color:blue">4.4.2.3</span> <span style="color:blue">转发询价请求、</span> <span style="color:blue">4.4.2.5</span> <span style="color:blue">报价状态</span>
<span style="color:blue">回报、</span> <span style="color:blue">4.4.2.6</span> <span style="color:blue">转发报价、</span> <span style="color:blue">4.4.2.8</span> <span style="color:blue">转发报价回复、</span> <span style="color:blue">4.4.3.2</span> <span style="color:blue">转发意向</span>
<span style="color:blue">申报、</span> <span style="color:blue">4.4.4.2</span> <span style="color:blue">转发成交申报中重复组中增加登录或订阅交易单元</span>
<span style="color:blue">3.</span> <span style="color:blue">4.4.3</span> <span style="color:blue">意向申报类、</span> <span style="color:blue">4.4.4</span> <span style="color:blue">成交申报类中对于</span> <span style="color:blue">ContractMultiplier</span>
<span style="color:blue">为保证上下游定义统一，调整为</span> <span style="color:blue">N5(2)</span>
<span style="color:blue">4.</span> <span style="color:blue">4.4.4.3</span> <span style="color:blue">成交申报响应中对于订单拒绝码，调整为</span> <span style="color:blue">TrdAckStatus</span>
<span style="color:blue">=8</span> <span style="color:blue">时有效</span>
<span style="color:blue">2025.11</span>
<span style="color:blue">2.10</span>
<span style="color:blue">开发稿</span>
<span style="color:blue">5.</span> <span style="color:blue">4.4.1.1</span> <span style="color:blue">新订单申报中对于固收各业务添加对</span> <span style="color:blue">Text</span> <span style="color:blue">字段的选填</span>
<span style="color:blue">说明</span>
<span style="color:blue">6.</span> <span style="color:blue">4.4.2.2</span> <span style="color:blue">询价请求响应、</span> <span style="color:blue">4.4.2.5</span> <span style="color:blue">报价状态回报、</span> <span style="color:blue">4.4.4.3</span> <span style="color:blue">成交申报</span>
<span style="color:blue">响应、</span> <span style="color:blue">4.4.4.4</span> <span style="color:blue">成交确认、</span> <span style="color:blue">4.4.5.1</span> <span style="color:blue">执行报告中对于不同业务返回字</span>
<span style="color:blue">段进行了明确区分</span>
<span style="color:blue">7.</span> <span style="color:blue">4.4.2</span> <span style="color:blue">询价报价业务类、</span> <span style="color:blue">4.4.3</span> <span style="color:blue">意向申报类、</span> <span style="color:blue">4.4.4</span> <span style="color:blue">成交申报类中</span>
<span style="color:blue">调整了部分字段的前后顺序</span>
8. <span style="color:blue">针对本次固收迁移业务，取消营业部代码字段</span>

目
录
1 前言 .................................................................................................................................................1
1.1 目的 ......................................................................................................................................1
1.2 术语和定义 ......................................................................................................................... 1
1.3 参考文档 ............................................................................................................................. 1
1.4 联系方式 ............................................................................................................................. 2
2 系统简介 .........................................................................................................................................3
2.1 系统接入 ............................................................................................................................. 3
2.2 业务范围 ............................................................................................................................. 4
3 交互机制 .........................................................................................................................................5
3.1 会话机制 ............................................................................................................................. 5
3.1.1 建立会话 .................................................................................................................. 5
3.1.2 关闭会话 .................................................................................................................. 5
3.1.3 维持会话 .................................................................................................................. 6
3.1.4 其他约定 .................................................................................................................. 6
3.2 申报与回报 ......................................................................................................................... 7
3.2.1 业务类型 .................................................................................................................. 7
3.2.2 消息流图 .................................................................................................................. 9
3.2.3 平台状态 ................................................................................................................ 27
3.2.4 重复订单 ................................................................................................................ 28
3.2.5 执行报告 ................................................................................................................ 29
3.3 恢复场景 ........................................................................................................................... 30
3.4 订阅机制 ........................................................................................................................... 31
4 消息定义 .......................................................................................................................................32
4.1 消息结构与约定 ............................................................................................................... 32
4.2 数据类型 ........................................................................................................................... 32
4.2.1 STEP 格式约定 .......................................................................................................33
4.2.2 STEP 消息头 ...........................................................................................................33
4.2.3 STEP 消息尾 ...........................................................................................................33
4.2.4 STEP 消息完整性 ...................................................................................................34
4.3 会话消息 ........................................................................................................................... 35
4.3.1 登录消息（ MsgType=A ） ....................................................................................35
4.3.2 注销消息（ MsgType=5 ） .....................................................................................36
4.3.3 心跳消息（ MsgType=0 ） .....................................................................................36
4.3.4 测试请求消息（ MsgType=1 ） .............................................................................36
4.3.5 重发请求消息（ MsgType=2 ） .............................................................................37
4.3.6 会话拒绝消息（ MsgType=3 ） .............................................................................37
4.3.7 序号重设消息（ MsgType=4 ） .............................................................................37
4.4 应用消息 ........................................................................................................................... 39
4.4.1 订单业务类 ............................................................................................................ 39
4.4.2 询价报价业务类 .................................................................................................... 48
4.4.3 意向申报类 ............................................................................................................ 72
4.4.4 成交申报类 ............................................................................................................ 77

4.4.5 执行报告类 .......................................................................................................... 102
4.4.6 网络密码服务（ Password Service, MsgType = U006 ） ................................... 110
4.4.7 其它消息 .............................................................................................................. 112
附录 .................................................................................................................................................116
附录一计算校验和 .............................................................................................................. 116
附录二 PBU 及说明 ..............................................................................................................117
附录三错误代码说明 .......................................................................................................... 118
附录四“用户私有信息”说明 .......................................................................................... 119

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
1 前言
1.1 目的
本接口规范描述了上海证券交易所（以下称本所）交易网关与市场参与者系统之间以 STEP 协议进行
交易数据交换时所采用的交互机制、消息格式、消息定义和数据内容。目前，本接口规范仅适用于本所互
联网交易平台 <span style="color:blue">和新固定收益系统</span> 提供的各类业务。
文档采用的术语及消息内容与 STEP 数据接口规范具有对应关系，可互为参考。
1.2 术语和定义
名词
含义
TDGW
交易网关 TraDing GateWay
MDGW
行情网关 Market Data GateWay
OMS
用户订单管理系统 Order Management System
会员等市场参与者通过 OMS 接入 TDGW 并进行交易数据交换
PBU
市场参与者交易业务单元 Participant Business Unit
ITCS
互联网交易平台通信服务器 Internet Trade Communication Server
STEP
证券交易数据交换协议 Securities Trading Exchange Protocol
1.3 参考文档
《 IS101 上海证券交易所竞价撮合平台市场参与者接口规格说明书》
《 IS111 上海证券交易所报盘软件错误代码表》
1

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
1.4 联系方式
技术服务 QQ 群：
298643611
技术服务电话：
4008888400-2 (8:00-20:00)
电子邮件：
tech_support@sse.com.cn
技术服务微信公众号： SSE-TechService （回复 00 进入人工服务）
2

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
2 系统简介
2.1 系统接入
为满足业务发展需求和提升交易服务水平，本所通过交易网关（ TDGW ）对接互联网交易平台 <span style="color:blue">和新固</span>
<span style="color:blue">定收益</span> 系统，提供实时交易流接口。 TDGW 对接交易系统及市场参与者系统（ OMS ）的示意图如下：
TDGW 通过交易业务单元（ PBU ）登录并接入交易系统， PBU 的配置由用户提前在 TDGW 端完成。
TDGW 每个平台开放一个端口供 OMS 建立会话， TDGW 仅接受 OMS 为每个平台建立一个 TCP/IP
连接，每个连接仅允许建立一个有效的会话。该会话既用于接收 OMS 的业务申报，又向 OMS 推送交易所
接收申报后产生的回报数据。
OMS 与 TDGW 间的连接为标准 TCP/IP 连接，由 OMS 负责发起。 OMS 与 TDGW 之间传输的数据是
非加密的，数据传输的安全性由部署的网络予以保证。
附录二对术语 PBU 在不同场景下的使用进行了说明。
3

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
2.2 业务范围
<span style="color:blue">目前支持互联网交易平台相关业务：</span>
<span style="color:blue">系统</span>
业务
业务申报时间
基金通报价交易
基金通转入转出
基金通询价交易
开放式基金业务（申购、赎回、转托管转出、分红选择）
9:30-11:30
<span style="color:blue">互联网交易平台</span>
要约预受 / 现金选择权登记
13:00-15:00
要约撤销 / 现金选择权撤销
融资融券业务（余券划转、还券划转、担保品划转、券源划转）
网络密码服务
债券质押式协议回购
债券质押式三方回购
债券借贷（预留，暂不启用）
协议回购意向申报
三方回购意向申报
债券现券意向申报
确定报价
待定报价
一债通询价
9:00-11:30
现券协商成交
<span style="color:blue">新固定收益系统</span>
13:00-15:30
合并申报
场务应急成交录入
竞买（预留，暂不启用）
三方回购转入转出
双非可转债转股冻结
私募可交换债换股
债券回售（一债通）
债券回售撤销
债券转托管
4

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3 交互机制
3.1 会话机制
OMS 与 TDGW 间的会话消息包括登录 Logon 、注销 Logout 和心跳 Heartbeat 等消息。
3.1.1 建立会话
OMS 负责发起到交易网关的 TCP 连接，并在连接建立后发送 Logon 消息。 OMS 连接后的首个消息必
须是 Logon 消息。如果登录成功， TDGW 返回一个 Logon 消息作为确认；如果失败， TDGW 返回一个含
失败原因的 Logout 消息，并由 OMS 关闭连接。 OMS 只应在收到 TDGW 的登录成功确认后才能发送其他
消息。
3.1.2 关闭会话
会话建立成功后，连接双方均可发送 Logout 注销消息，告知对端将关闭会话，一般地，接收方应回复
一个 Logout 消息作为回应。 Logout 的发起方在收到回应后关闭连接。如果超过 5 秒没有收到对方回传的
Logout 消息，注销发起方也可直接关闭连接。连接双方在发送 Logout 消息后不应再发送任何消息。
5

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.1.3 维持会话
在消息交换的空闲期间，连接双方通过 Heartbeat 心跳消息维持会话，即连接的任何一方在心跳时间间
隔内若没有发送任何消息，需要产生并发送一个 Heartbeat 消息。
心跳间隔通过登录过程进行协商，以登录成功后 TDGW 返回的登录确认消息中的 HeartBtInt 域为准。
一般地，当 OMS 发送 Logon 消息中的 HeartBtInt 取值属于 [5,60] 时， TDGW 返回原值，否则取边界值（ 5
或 60 ）。
接收方接收到任何消息（不仅仅是心跳）可重置读心跳间隔计数。若接收方在 5 个心跳间隔内未收到
任何消息，则可以认为会话出现异常并立即关闭连接。 OMS 关闭连接后，可重新发起会话或切换至其他
TDGW 。
3.1.4 其他约定
TDGW 在未成功登录至交易系统时， OMS 将无法成功与 TDGW 建立会话； TDGW 与 ITCS 连接断开
时， TDGW 将注销与 OMS 间的会话，此时 OMS 应稍后尝试重建会话，或切换至备用 TDGW 服务。
此外， TDGW 在以下情况下会主动断开与 OMS 间的连接：

OMS 与 TDGW 建立 TCP 连接之后，超过 5 秒未完成登录；

OMS 在登录失败之后，未在 5 秒内关闭连接；

OMS 在发起注销后，未在 5 秒内关闭连接；

OMS 未能及时处理 TDGW 下行消息，导致 TDGW 内积压的待发送消息超过特定阈值；

TDGW 与 ITCS 间的连接已经断开；
6

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2 申报与回报
OMS 进行的新订单申报（ New Order Single ）、询价请求（ Quote Request ）、报价（ Quote ）、意向申
报（ IOI ）和成交申报（ Trade Capture Report ）时，本所交易系统会进行前置检查，若检查未通过将返回订
单拒绝（ Order Reject ）、询价请求响应（ Quote Request Ask ）和报价状态回报（ QuoteStatusReport ）、意
向申报响应（ IOI Response ）和成交申报响应（ Trade Capture Report Response ）消息。
对于通过前置校验的申报，交易系统根据业务的不同，向 OMS 返回相应的执行报告（ Execution Report ）、
转发询价请求（ Allege Quote Request ）、转发报价（ Allege Quote ）、转发意向申报（ Allege IOI ）和转发
成交申报（ Allege Trade Capture Report ）消息。执行报告包括对申报的确认，如对新订单的确认或拒绝响
应 1 、撤单响应等；新订单申报及询价请求产生成交时，执行报告中会包含成交确认。
总体示意图如下：
3.2.1 业务类型
订单申报需要指定业务类型（ ApplID ），其产生的回报以不同的执行报告分区（ PartitionNo ）划分为
多个逻辑上相互独立的数据流。根据具体业务的不同，下表给出业务类型、分区的对应关系，并明确业务
相关属性。
业务
消息类型 (MsgType)
业务类型 (ApplID)
支持撤单
申报确认
成交确认
基金通报价交易
D
600020
Y
Y
Y
1 除前置检查未通过返回 Reject 外，执行报告中也包含有因业务校验未通过产生的拒绝响应 Execution Report （ ExecType=8 ）。
7

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
业务
消息类型 (MsgType)
业务类型 (ApplID)
支持撤单
申报确认
成交确认
基金通转入转出
D
600021
N
Y
Y
R （询价）
基金通询价交易
S （报价）
600022
Y
Y
Y
AJ （报价回复）
开放式基金申购
D
600030
Y
Y
N
开放式基金赎回
D
600040
Y
Y
N
开放式基金转托管转出
D
600050
Y
Y
N
开放式基金分红选择
D
600060
Y
Y
N
要约预受 / 现金选择权登记
D
600070
Y
Y
N
要约撤销 / 现金选择权撤销
D
600071
Y
Y
N
融资融券余券划转
D
600080
Y
Y
N
融资融券还券划转
D
600090
Y
Y
N
融资融券担保品划入
D
600100
Y
Y
N
融资融券担保品划出
D
600101
Y
Y
N
融资融券券源划入
D
600110
Y
Y
N
融资融券券源划出
D
600111
Y
Y
N
网络密码服务 2
U006
600120
N
Y
N
债券质押式协议回购
AE
600130
Y 3
Y
Y
债券质押式三方回购
AE
600140
Y 3
Y
Y
协议回购意向申报
6
600150
Y
Y
N
三方回购意向申报
6
600160
Y
Y
N
债券现券意向申报
6
600170
Y
Y
N
S （报价）
确定报价
600180
Y
Y
Y
AJ （报价回复）
R （询价）
一债通询价
S （报价）
600190
Y
Y
Y
AJ （报价回复）
R （待定报价发起）
待定报价
600200
Y
Y
Y
S （报价）
8

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
业务
消息类型 (MsgType)
业务类型 (ApplID)
支持撤单
申报确认
成交确认
AJ （报价回复）
现券协商成交
AE
600210
Y
Y
Y
合并申报
AE
600220
Y
Y
Y
双非可转债转股冻结
D
600230
Y
Y
N
私募可交换债换股
D
600240
Y
Y
N
债券回售（一债通）
D
600250
Y
Y
N
债券回售撤销
D
600251
Y
Y
N
债券转托管
D
600260
Y
Y
N
三方回购转入转出
D
600270
N
Y
Y
竞买（预留，暂不启用）
D
600290
Y 4
Y
Y
债券借贷（预留，暂不启用） AE
600300
Y 3
Y
Y
场务应急成交录入
AE
600310
N
N
Y
注：
1 、 Y 为是， N 为否。
2 、网络密码服务业务，申报响应消息不进执行报告（ Execution Report ）。
3 、协议回购、三方回购和债券借贷部分成交申报不支持撤单，包括：协议回购到期确认、债券借贷
到期结算（债券结算且场内结算）、三方回购到期购回三方回购补券申报。
4 、在应价方提交有效的应价申报前，可以撤销竞买发起申报；采用单一主体中标方式的，应价申报
不可撤销；采用多主体中标方式的，应价申报可以在应价申报时间截止前撤销。
3.2.2 消息流图
3.2.2.1 新订单处理消息流图
3.2.2.1.1 新订单申报
<span style="color:blue">适用于互联网交易平台。</span>
订单（ OrdType=2 ）消息流如下：
9

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
OMS
TDGW
限价申报（ New Order Single ）
订单拒绝（ Order Reject, OrdRejReason=xxx ）
前置校验失败
限价申报（ New Order Single ）
申报确认（ Execution Report, ExecType=8 ）
业务校验失败
限价申报（ New Order Single ）
通过业务校验，先返回申
报确认，后根据订单执行
情况返回成交回报
申报确认（ Execution Report, ExecType=0 ）
成交回报（ Execution Report, ExecType=F ）
暂不支持市价订单。
3.2.2.1.2 新订单撤单
支持撤单的业务类型见前述章节业务类型表。
OMS
TDGW
撤单申报（ Order Cancel ）
前置校验失败
订单拒绝（ Order Reject, OrdRejReason=xxx ）
撤单申报（ Order Cancel ）
撤单失败
撤单失败（ Execution Report ）
撤单申报（ Order Cancel ）
撤单成功
撤单成功（ Execution Report,ExecType=4 ）
10

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.2 询价报价处理消息流图
询价报价交易总体上可以分为两个阶段：询价阶段和报价阶段。
在询价阶段，询价方申报询价请求，交易系统转发询价请求给报价方（一个或多个），报价方可以选
择进行报价也可以不进行报价。
在报价阶段，报价方对询价请求进行报价，交易系统将报价转发给询价方。若报价方想要修改报价，
需将原报价撤销后重新发起报价。询价方可以选择接受或不接受报价方的报价。若询价方接受报价，则申
报一笔报价回复，交易系统对报价及报价回复进行撮合成交并发送成交回报执行报告 <span style="color:blue">，同时转发询价撤销</span>
<span style="color:blue">消息告知其余报价方</span> 。若询价方不接受报价，报价在询价失效后也自动失效。
询价未成交前，询价方可以撤销询价。报价未成交前，报价方可以撤销报价。对于基金通询价，若报
价方不进行报价，询价在超时后会自动失效，整个交易过程结束；若询价交易超过总时长仍未成交，则需
通过询价请求响应及报价状态回报将失效消息转发至相关方。
此消息流适用于：基金通询价、一债通询价和待定报价。
对于基金通或一债通询价，用户仅可在限定范围内发布询价信息；对于待定报价，用户可针对全市场
或在限定范围内发起报价。对于发送给全市场的消息，将通过公开行情对外发布；对于限定范围内发布的
询报价消息，则将该消息转发给对应对手方。
11

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.2.1 询价方撤销询价请求处理（转发请求）
OMS1
OMS2
TDGW
询价请求
（ Quote Request,MsgType=R ）
询价方发起询价请求
QuoteRequestTransType=New
ClOrdID=c00001
询价请求响应
（ Quote Request Ack,MsgType=R ）
转发询价请求
（ Allege Quote Request,MsgType=R ）
转发给报价方
QuoteReqID=qr00001, OrderID=qr00001
QuoteRequestTransType=New
QuoteReqID=qr00001
QuoteRequestTransType=New
QuoteRequestType=Submit
QuoteRequestStatus=Accepted
QuoteRequestType=Alleged
QuoteRequestStatus=Accepted
报价
（ Quote,MsgType=S ）
报价方发起报价
QuoteReqID=qr00001
QuoteMsgID=qm00001
报价状态回报
（ Quote Status Report,,MsgType=AI ）
转发报价
（ Allege Quote,MsgType=S ）
转发给询价方
QuoteMsgID=qm00001
QuoteID=q00001,OrderID=q00001
QuoteReqID=qr00001
QuoteID=q00001
ClOrdID=c00001
询价请求
（ Quote Request,MsgType=R ）
QuoteRequestTransType=Cancel
询价方撤销询价
请求
ClOrdID=c00002
OrigClOrdID=c00001
询价请求响应
（ Quote Request Ack,MsgType=R ）
Reject
QuoteReqID=qr00002
QuoteRequestStatus=Rejected
QuoteRequestRejectReason=20001
询价请求响应
（ Quote Request Ack,MsgType=R ）
Accept
QuoteReqID=qr00002,OrderID=qr00001
转发询价请求
（ Allege Quote Request,MsgType=R ）
通知报价方询价
已被撤销
QuoteRequestType=Submit
QuoteRequestStatus=Cancelled
QuoteReqID=qr00001
QuoteRequestTransType=Cancel
QuoteRequestType=Alleged
QuoteRequestStatus=Cancelled
OrderID=qr00001
12

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.2.2 询价报价方撤销报价处理（转发请求）
OMS1
OMS2
TDGW
询价请求
（ Quote Request,MsgType=R ）
询价方发起询价请求
QuoteRequestTransType=New
ClOrdID=c00001
转发询价请求
（ Allege Quote Request,MsgType=R ）
询价请求响应
（ Quote Request Ack,MsgType=R ）
转发给报价方
QuoteReqID=qr00001,OrderID=qr00001
QuoteRequestTransType=New
QuoteReqID=qr00001
QuoteRequestTransType=New
QuoteRequestType=Submit
QuoteRequestStatus=Accepted
QuoteRequestType=Alleged
QuoteRequestStatus=Accepted
报价方发起报价
报价
（ Quote,MsgType=S ）
QuoteReqID=qr00001
QuoteMsgID=qm00001
报价状态回报
（ Quote Status Report,MsgType=AI ）
转发报价
（ Allege Quote,MsgType=S ）
转发给询价方
QuoteReqID=qr00001
QuoteMsgID=qm00001
QuoteID=q00001,OrderID=q00001
QuoteID=q00001
ClOrdID=c00001
报价撤销
（ Quote,MsgType=S ）
报价方发起报价撤销
OrigClOrdID=qm00001
QuoteMsgID=qm00002
BidSize=0
OfferSize=0
报价状态回报
（ Quote Status Report,MsgType=AI ）
Reject
OrigClOrdID=qm00001
QuoteMsgID=qm00002
QuoteStatus=Rejected
QuoteRejectReason=5011
报价状态回报
（ Quote Status Report,MsgType=AI ）
Accept
转发报价
（ Allege Quote,MsgType=S ）
转发给询价方
QuoteMsgID=qm00002
QuoteID=q00002,OrderID=q00001
QuoteID=q00001
QuoteStatus=Cancelled
QuoteReqID=qr00001
ClOrdID=c00001
BidSize=0
OfferSize=0
13

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.2.3 询价方与报价方成交（转发请求）
询价发起方报价回复确认成交后，模式一将通知其他报价方此询价被撤销，模式二将通知其他报价方
更新报价数量。基金通询价和待定报价全部成交适用于模式一，待定报价部分成交适用于模式二。
O M S1
O M S2
TD G W
询价请求
（Q u ote R eq uest,M sg Typ e= R ）
询价方发起询价请求
QuoteRequestTransType=New
ClOrdID=c00001
转发询价请求
（A lleg e Q uo te R eq uest,M sg Typ e= R ）
询价请求响应
（Q u ote R eq uest A ck,M sg Typ e= R ）
转发给报价方
QuoteReqID=qr00001,OrderID=qr00001
QuoteReqID=qr00001
QuoteRequestTransType=New
QuoteRequestTransType=New
QuoteRequestType=Alleged
QuoteRequestStatus=Accepted
QuoteRequestType=Submit
QuoteRequestStatus=Accepted
报价
（Q u ote,M sg Typ e= S）
报价方发起报价
QuoteReqID=qr00001
QuoteMsgID=qm00001
报价回报
（Q u ote Status R ep o rt,M sg Typ e= A I）
转发报价（A lleg e Q uo te,M sg Typ e= S ）
转发给询价方
QuoteReqID=qr00001
QuoteMsgID=qm00001
QuoteID=q00001,OrderID=q00001
QuoteID=q00001
报价回复
（Q u ote R esp o nse,M sg Typ e= A J）
询价方接受报价
ClOrdID=c00002
QuoteID=q00001/ QuoteReqID=qr00001
QuoteRespType=Hit/ Lift
报价状态回报
（Q u ote Status R ep o rt,M sg Typ e= A I）
R eject
QuoteID=q00001/ QuoteReqID=qr00001
QuoteStatus=Rejected
QuoteRejectReason=5011
报价状态回报
（Q u ote Status R ep o rt,M sg Typ e= A I）
A ccep t
QuoteID=q00001/ QuoteReqID=qr00001
QuoteStatus=Accepted
QuoteMsgID=c00002
OrderID=qr00002
询价方成交
成交报告（M sg Typ e= 8）
成交报告（M sg Typ e= 8）
报价方成交
ClOrdID=c00002
ClOrdID=qm00001
ExecID=e00001
ExecID=e00001
OrdStatus=1/ 2
OrdStatus=2
ExecType=F
ExecType=F
转发询价请求
（A llg e Q u o te R eq u est,M sg Typ e= R ）
模式一：
通知其他报价方询价
已被撤销
QuoteReqID=qr00001
QuoteRequestTransType=Cancel
QuoteRequestType=Alleged
QuoteRequestStatus=Cancelled
转发询价请求
（A llg e Q u o te R eq u est,M sg Typ e= R ）
模式二：
成交后更新报价数量
QuoteReqID=qr00001
QuoteRequestTransType=New
QuoteRequestType=Alleged
QuoteRequestStatus=Accepted
14

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.2.4 询价方拒绝报价方报价（转发请求）
O M S1
O M S2
TD G W
询价请求
（Q u ote R eq uest,M sg Typ e= R ）
询价方发起询价请求
QuoteRequestTransType=New
ClOrdID=c00001
转发询价请求
（A lleg e Q uo te R eq uest,M sg Typ e= R ）
询价请求响应
（Q u ote R eq uest A ck,M sg Typ e= R ）
转发给报价方
QuoteReqID=qr00001
QuoteRequestTransType=New
QuoteReqID=qr00001
QuoteRequestTransType=New
QuoteRequestType=Submit
QuoteRequestStatus=Accepted
QuoteRequestType=Alleged
QuoteRequestStatus=Accepted
报价
（Q u ote,M sg Typ e= S）
报价方发起报价
QuoteReqID=qr00001
QuoteMsgID=qm00001
报价回报
（Q u ote Status R ep o rt,M sg Typ e= A I）
转发报价（A lleg e Q uo te,M sg Typ e= S ）
转发给询价方
QuoteMsgID=qm00001
QuoteReqID=qr00001
QuoteID=q00001
QuoteID=q00001
报价回复
（Q u ote R esp o nse,M sg Typ e= A J）
询价方拒绝报价
ClOrdID=c00002
QuoteID=q00001
QuoteRespType=Pass
报价状态回报
（Q u ote Status R ep o rt,M sg Typ e= A I）
R eject
QuoteMsgID=c00002
QuoteID=q00001
OrderID=q00002
QuoteStatus=Rejected
QuoteRejectReason=5011
报价状态回报
（Q u ote Status R ep o rt,M sg Typ e= A I）
A ccep t
转发报价回复
（A llg e Q u o te R esp o nse,M sg Typ e= A J）
通知报价方报价被拒绝
QuoteMsgID=qm00001
OrderID=q00002
QuoteID=q00001
QuoteStatus=Accepted
QuoteMsgID=c00002
QuoteID=q00001
QuoteRespType=Pass
15

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.2.5 询价报价请求处理（公开行情）
对于公开行情中询价发起方拒绝报价的场景，可参见询价方拒绝报价方报价（转发请求）章节。
OMS2
OMS1
TDGW
MDGW
询价请求（ Quote Request, MsgType=R)
场景 1 ：询价申报成功
ClOrdID=100
QuoteRequestTransType=New
询价请求响应
(Quote Request Ack, MsgType=R)
待定报价逐笔委托行情
QuoteReqID=t100,OrderID=t100
QuoteRequestStatus=Accepted
申报撤单 (Quote Request, MsgType=R)
ClOrdID=101, OrigClordID=100
QuoteRequestTransType=Cancel
申报拒绝 (Order Reject, MsgType=j)
Order Reject
场景 2A ：前置校验失败订单拒绝
撤单响应 (Quote Request Ack, MsgType=R)
场景 2B ：撤销申报成功或失败
QuoteReqID=t101
QuoteRequestStatus=Rejected
撤单响应 (Quote Request Ack, MsgType=R)
场景 2C ：撤销申报成功
QuoteReqID=t101,OrderID=t100
更新待定报价逐笔委托行情
QuoteRequestStatus=Accepted
场景 3 ：对手方报价
报价申报 (Quote, MsgType=S)
QuoteMsgID=200
QuoteReqID=t100
报价申报响应
(Quote Status Report, MsgType=AI)
QuoteID=t200,OrderID=t200
转发报价申报 (Allege Quote, MsgType=S)
QuoteMsgID=200
QuoteStatus=Accepted
QuoteID=t200
QuoteReqID=t100
ClOrdID=100
场景 3 ：对手方报价撤销
报价申报 (Quote, MsgType=S)
QuoteMsgID=201
OrigClOrdID=200
BidSize=0, OfferSize=0
报价申报响应
（ Quote Status Report, MsgType=AI)
转发报价申报 (Allege Quote, MsgType=S)
OuoteID=t201,OrderID=t200
QuoteMsgID=201,OrigClOrdID=200
QuoteID=t200
BidSize=0, OfferSize=0
QuoteStatus=Cancelled
报价回复 (Quote Response, MsgType=AJ)
场景 4 ：询价发起方接受报价
ClOrdID=102
NoQuote=1,QuoteID=t200
QuoteRespType=1/ 6
回复响应 (Quote Status Report, MsgType=AI)
QuoteMsgID=102
QuoteID=t200,OrderID=t102
QuoteStatus=Accepted
成交报告
(Execution Report, MsgType=8)
成交报告 (Execution Report, MsgType=8)
ClOrdID=102
OrdStatus=1/ 2
生成逐笔成交行情
ExecID=m100
ClOrdID=200
OrdStatus=2
ExecID=m100
16

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.3 报价处理消息流图
报价可对全市场或在限定范围内发起。面向全市场的报价，交易系统将以逐笔委托行情向市场发布报
价信息，而对于限定范围的报价，交易系统将把报价消息转发给指定对手方。
此消息流适用于确定报价。
OMS1
TDGW
MDGW
OMS2
报价申报 (Quote, MsgType=S)
QuoteMsgID=200
申报拒绝 (Order Reject, MsgType=j)
场景 1A ：报价发起前置校验失败
Order Reject
申报响应 (Quote Status Report, MsgType=AI)
QuoteID=t200,OrderID=t200
场景 1B ：报价发起业务校验成功
或失败
更新逐笔委托行情
场景 1C ：报价公开发布
QuoteMsgID=200
QuoteStatus=Accepted/ Rejected
转发报价申报 (Allege Quote, MsgType=S)
场景 1D ：报价限定范围发布
QuoteID=t200
报价申报 (Quote, MsgType=S)
QuoteMsgID=201
OrigClOrdID=200
BidSize=0, OfferSize=0
申报拒绝 (Order Reject, MsgType=j)
场景 2A ：报价撤销前置校验失败
Order Reject
报价申报响应 (Quote Status Report, MsgType=AI)
场景 2B ：报价撤销业务校验成功
或失败
QuoteID=t201,OrderID=t200
更新逐笔委托行情
场景 2C ：报价公开发布
QuoteMsgID=201
QuoteStatus=Cancelled/ Rejected
转发报价申报 (Allege Quote, MsgType=S)
场景 2D ：报价限定范围发布
QuoteID=t200
BidSize=0, OfferSize=0
报价回复 (Quote Response, MsgType=AJ)
ClOrdID=102
NoQuote=1,QuoteID=t200
申报拒绝 (Order Reject, MsgType=j)
场景 3A ：点击成交前置校验失败
Order Reject
报价回复响应
(Quote Status Report, MsgType=AI)
场景 3B ：点击成交业务校验成功
或失败
QuoteMsgID=102
QuoteID=t200,OrderID=t102
QuoteStatus=Accepted/ Rejected
成交报告 (Execution Report, MsgType=8)
成交报告 (Execution Report, MsgType=8)
场景 3C ：成交后更新行情或转发
其他参与人更新委托数量
ClOrdID=200
OrdStatus=1/ 2
ExecID=m100
ClOrdID=102
OrdStatus=2
ExecID=m100
更新逐笔成交行情
转发报价申报 (Allege Quote, MsgType=S)
QuoteID=t200
17

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.4 意向申报消息流图
意向申报可对全市场或在限定范围内发起。面向全市场的意向申报，交易系统将以逐笔委托行情向市
场发布意向申报信息，而对于限定范围的意向申报，交易系统将把意向申报请求转发给指定对手方。
此消息流支持协议回购意向申报、三方回购意向申报和债券现券意向申报。其中协议回购意向申报和
三方回购意向申报仅支持对全市场发起。
3.2.2.4.1 意向申报撤销请求处理（公开行情）
OMS
TDGW
MDGW
意向申报（ IOI, MsgType=6)
IOIID=100
IOITransType=New
申报拒绝 (Order Reject, MsgType=j)
场景 1A ：前置校验失败订单
拒绝
Order Reject
申报响应 (IOI Response, MsgType=AJ)
场景 1B ：业务校验失败订单
拒绝
IOIID=100
QuoteRespID=q100
ExecType=Rejected
申报响应 (IOI Response, MsgType=AJ)
ExecType=Accepted
意向申报公共行情
QuoteRespID=q100
场景 1C ：申报被接受
申报撤单 (IOI, MsgType=6)
IOIID=101
IOIRefID=100
IOITransType=Cancel
申报拒绝 (Order Reject, MsgType=j)
Order Reject
场景 2A ：前置校验失败订单
拒绝
申报响应 (IOI Response, MsgType=AJ)
场景 2B ：撤销意向申报失
败
IOIID=101
ExecType=Rejected
申报响应 (IOI Response, MsgType=AJ)
更新意向申报公共行情
场景 2C ：撤销意向申报成
功
IOIID=101
IOIRefID=100
QuoteRespID=q101
ExecType=Cancelled
18

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.4.2 意向申报撤销请求处理（转发请求）
特别地，对于债券现券意向申报，也支持在限定范围内发布意向报价，此时系统将把意向申报转发给
指定的对手方。
OMS1
TDGW
OSM2
意向申报（ IOI, MsgType=6)
IOIID=100
IOITransType=New
申报拒绝 (Order Reject, MsgType=j)
场景 1A ：前置校验失败订单
拒绝
Order Reject
申报响应 (IOI Response, MsgType=AJ)
场景 1B ：业务校验失败订单
拒绝
IOIID=100
QuoteRespID=q100
ExecType=Rejected
申报响应 (IOI Response, MsgType=AJ)
转发意向申报 (Allege IOI, MsgType=6)
场景 1C ：申报被接受
ExecType=Accepted
QuoteRespID=q100
QuoteRespID=q100
QuoteRespType=Alleged
IOITransType=New
申报撤单 (IOI, MsgType=6)
IOIID=101
IOIRefID=100
IOITransType=Cancel
申报拒绝 (Order Reject, MsgType=j)
Order Reject
场景 2A ：前置校验失败订单拒绝
撤单响应 (IOI Response, MsgType=AJ)
场景 2B ：撤销意向申报失
败
IOIID=101
ExecType=Rejected
撤单响应 (IOI Response, MsgType=AJ)
转发意向申报 (Allege IOI, MsgType=6)
场景 2C ：撤销意向申报成
功
QuoteRespID=q100
QuoteRespType=Alleged
IOITransType=Cancel
IOIID=101
IOIRefID=100
QuoteRespID=q101
ExecType=Cancelled
19

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.5 成交申报消息流图
3.2.2.5.1 协议配对申报模式
协议配对申报模式指交易双方各 <span style="color:blue">向互联网交易平台</span> 申报一笔订单，订单内容包括对手方信息、买卖方
向和约定号等，当双方信息匹配后成交，订单未匹配前可以撤销。
此模式适用于现券协商成交。
OMS1
TDGW
OMS2
成交申报（ AE)
TradeReportID=100
TradeReportType=Submit
TradeReportTransType=New
ConfirmID=1234
场景 1A ：申报业务校验失败
申报响应 (AR)
TrdAckStatus=Rejected
TradeReportType=Submit
TradeReportTransType=New
TradeReportID=100
TradeID=t100
TrdRptStatus=Rejected
场景 1B ：申报被接受
成交申报（ AE)
申报响应 (AR)
TrdAckStatus=Accepted
TradeReportType=Submit
TradeReportTransType=New
TradeReportID=200
TradeReportType=Submit
TradeReportTransType=New
TradeReportID=100
ConfirmID=1234
TradeID=t100
TrdRptStatus=Unmatched
申报响应（ AR)
场景 2A ：申报被接受
TrdAckStatus=Accepted
TradeReportTransType=New
TradeReportID=200
TradeID=t200
场景 2B ：业务校验或协议配对失败
申报响应（ AR)
TrdAckStatus=Rejected
TradeReportTransType=New
TradeReportID=200
TradeID=t200
成交申报（ AE)
TradeReportID=101
TradeReportRefID=100
TradeReportType=Submit
TradeReportTransType=Cancel
场景 3A ：撤单业务校验失败
申报响应 (AR)
TrdAckStatus=Rejected
TradeReportType=Submit
TradeReportTransType=Cancel
TradeReportID=101
TradeID=t100
TrdRptStatus=Rejected
场景 3B ：撤单成功
申报响应 (AR)
TrdAckStatus=Accepted
TradeReportType=Submit
TradeReportTransType=Cancel
TradeReportID=101
TradeID=t100
TrdRptStatus=Cancelled
成交回报（ AE)
场景 2C ：成交匹配成功
成交回报 (AE)
TradeReportID=100
TradeReportID=200
TradeID=t100
TradeReportTransType=Replace
TradeID=t200
TradeReportTransType=Replace
ExecID=m001
TrdAckStatus=Trade
TrdRptStatus=Matched
ExecID=m001
TrdAckStatus=Trade
TrdRptStatus=Matched
20

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.5.2 成交报告申报模式
成交报告申报模式指无需对手方手动确认、自动成交、不可撤单的各类申报。
此模式适用于协议回购到期确认、三方回购到期购回和补券申报、债券借贷到期结算（债券结算且场
内结算）、场务应急成交录入（由场务人员录入，实际交易双方均可收到成交确认）等。
OMS1
TDGW
OMS2
成交申报（ AE)
TradeReportID=100
TradeReportType=Submit
TradeReportTransType=New
申报拒绝 (j)
Order Reject
场景 1A ：前置校验失败订单拒绝
申报响应 (AR)
场景 1B ：业务校验失败申报
拒绝
TradeReportID=100
TradeID=t100
TrdAckStatus=Rejected
TradeReportTransType=New
TradeReportID=100
申报响应 (AR)
场景 1C ：申报校验通过，
成交自动达成
TradeID=t100
TrdAckStatus=Accepted
TradeReportTransType=New
成交回报 (AE)
成交回报 (AE)
TradeReportID=100
TradeReportID=UB00000001
TradeID=t100
TradeReportTransType=Replace
TradeID=t101
TradeReportTransType=New
TradeReportType=Submit
TradeReportType=Submit
ExecID=e100
ExecID=e100
21

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.5.3 成交请求申报模式
成交请求申报模式指一方发起经由交易服务转发至单个对手方，并由对手方手动确认（或拒绝）的各
类申报。
此模式适用于协议回购和三方回购的协商成交、提前终止、换券、到期续做和解除质押申报，以及债
券借贷的协商成交、到期结算、提前终止、质押券变更、到期续做、逾期结算和解除质押申报。
3.2.2.5.3.1 申报处理
OMS2
OMS1
TDGW
成交申报
（ Trade Capture Report, MsgType=AE)
TradeReportID=100
TradeReportType=Submit
TradeReportTransType=New
转发成交申报（ AE)
场景 1 ：申报被接受
TradeReportTransType=New
申报响应 (AR)
TrdAckStatus=Accepted
TradeReportType=Submit
TradeReportTransType=New
TradeID=t100
TradeReportType=Alleged
TradeReportID=100
TradeID=t100
成交申报确认或拒绝
（ Trade Capture Report, MsgType=AE)
TradeReportID=200
TradeReportType=Accpet/Decline
TradeReportTransType=Replace
ExecRefID=t100
申报响应（ AR)
TrdAckStatus=Accepted
TradeReportType=Accept/Decline
TradeReportID=200
TradeID=t200
成交确认
（ Trade Capture Report, MsgType=AE)
成交确认
（ Trade Capture Report, MsgType=AE)
场景 2A ：订单被确认
TradeReportTransType=Replace
TradeReportTransType=Replace
TradeReportID=100
TradeReportID=200
TradeID=t100
TradeReportType=Submit
TradeID=t200
TradeReportType=Submit
ExecID=e100
ExecID=e100
场景 2B ：订单被拒绝
转发成交申报（ AE)
TradeReportTransType=Cancel
TradeReportType=Decline
TradeID=t200
ExecRefID=t100
22

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.5.3.2 撤单处理
OMS1
TDGW
OMS2
成交申报（ AE)
TradeReportID=100
TradeReportType=Submit
TradeReportTransType=New
申报拒绝 (j)
Order Reject
场景 1A ：前置校验失败订单
拒绝
申报响应 (AR)
TradeReportID=100
场景 1B ：业务校验失败订单
拒绝
TradeID=t100
TradeReportType=Submit
TradeReportTransType=New
TrdAckStatus=Rejected
TrdRptStatus=Rejected
转发成交申报（ AE)
申报响应 (AR)
场景 1C ：申报被接受
TradeReportID=100
TradeReportTransType=New
TradeID=t100
TradeReportType=Alleged
TradeID=t100
TradeReportType=Submit
TradeReportTransType=New
TrdAckStatus=Accepted
TrdRptStatus=Unmatched
申报撤单 (AE)
TradeReportID=101
TradeReportType=Submit
TradeReportTransType=Cancel
TradeReportRefID=100
申报拒绝 (j)
场景 2A ：前置校验失败撤单
拒绝
Order Reject
撤单响应 (AR)
场景 2B ：业务校验失败撤单
拒绝
TradeReportID=101
TradeID=t101
TradeReportType=Submit
TradeReportTransType=Cancel
TrdAckStatus=Rejected
TrdRptStatus=Rejected
撤单响应 (AR)
转发成交申报（ AE)
TradeReportTransType=Cancel
TradeReportID=101
场景 2C ：撤销成交申报成
功
TradeID=t101
OrigTradeID=t100
TradeReportType=Alleged
TradeID=t101
TradeReportType=Submit
TradeReportTransType=Cancel
TrdAckStatus= Accepted
TrdRptStatus=Cancelled
23

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.5.4 双边确认申报模式
双边确认申报模式指中间方发起一笔包含买卖双方的订单，经交易系统转发给买卖双方分别确认后方
可成交，任何一方拒绝该订单后此申报自动撤销。此模式适用于合并申报。
24

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.5.4.1 两对手方均确认，成交达成
OMS1
( 中间方 )
TDGW
OMS2
( 对手方 1)
OMS3
( 对手方 2)
成交申报（ AE)
TradeReportID=100
TradeReportType=Submit
TradeReportTransType=New
申报拒绝 (j)
Order Reject
场景 1A ：前置校验失败订单
拒绝
申报响应 (AR)
TradeReportID=100
场景 1B ：业务校验失败订单
拒绝
TradeID=t100
TradeReportType=Submit
TradeReportTransType=New
TrdAckStatus=Rejected
转发成交申报（ AE)
申报响应 (AR)
场景 1C ：申报被接受
TradeReportID=100
TradeID=t201
TradeReportType=Alleged
TradeReportTransType=New
转发成交申报（ AE)
TradeID=t100
TradeReportType=Submit
TradeReportTransType=New
TrdAckStatus=Accepted
TradeID=t202
TradeReportType=Alleged
TradeReportTransType=New
申报撤单 (AE)
场景 2 ：撤销成交申报成功
TradeReportID=101
TradeReportType=Submit
TradeReportTransType=Cancel
TradeReportRefID=100
撤单响应 (AR)
转发成交申报（ AE)
TradeReportID=101
TradeID=t101
OrigTradeID=t201
TradeReportType=Alleged
TradeReportTransType=Cancel
TradeID=t101
TradeReportType=Submit
TradeReportTransType=Cancel
转发成交申报（ AE)
TrdAckStatus= Accepted
TrdRptStatus=Cancelled
TradeID=t101
OrigTradeID=t202
TradeReportType=Alleged
TradeReportTransType=Cancel
成交申报 (AE)
场景 3 ：买卖双方均确认，
成交达成
TradeReportID=301
ExecRefID=t201
TradeReportType=Accpet
TradeReportTransType=Replace
成交申报响应（ AR)
TradeID=t301
TradeReportID=301
TrdAckStatus=Accepted
TradeReportType=Accept
TradeReportTransType=Replace
成交申报 (AE)
TradeReportID=302
ExecRefID=t202
TradeReportType=Accpet
TradeReportTransType=Replace
成交申报响应（ AR)
TradeID=t302
TradeReportID=302
TrdAckStatus=Accepted
TradeReportType=Accept
TradeReportTransType=Replace
成交回报 (AE)
成交回报（ AE)
TradeReportID=100
TradeReportID=t301
ExecID=m001
TradeReportTransType=Replace
ExecID=m001
TradeReportTransType=Replace
TradeReportType=Submit
TradeReportType=Submit
成交回报 (AE)
TradeReportID=100
成交回报（ AE)
TradeReportID=t302
ExecID=m002
TradeReportTransType=Replace
ExecID=m002
TradeReportTransType=Replace
TradeReportType=Submit
TradeReportType=Submit
3.2.2.5.4.2 某一对手方拒绝，自动撤销
如两个对手方中任何一方拒绝该订单后此申报自动撤销。
25

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
OMS1
( 中间方 )
TDGW
OMS2
( 对手方 1)
OMS3
( 对手方 2)
成交申报（ AE)
TradeReportID=100
TradeReportType=Submit
TradeReportTransType=New
转发成交申报（ AE)
申报响应 (AR)
发起方申报被接受
TradeReportID=100
TradeID=t201
TradeReportType=Alleged
TradeReportTransType=New
转发成交申报（ AE)
TradeID=t100
TradeReportType=Submit
TradeReportTransType=New
TrdAckStatus=Accepted
TradeID=t202
TradeReportType=Alleged
TradeReportTransType=New
成交申报 (AE)
对手方发起拒绝
TradeReportID=300
ExecRefID=t201
TradeReportType=Decline
TradeReportTransType=Replace
成交申报响应（ AR)
TradeID=t300
TradeReportID=300
TrdAckStatus=Accepted
TradeReportType=Decline
TradeReportTransType=Replace
转发成交申报（ AE)
转发成交申报（ AE)
撤单信息转发给发起方和
另一对手方
TradeID=t300
OrigTradeID=t100
TradeReportType=Decline
TradeReportTransType=Cancel
TradeID=t300
OrigTradeID=t202
TradeReportType=Alleged
TradeReportTransType=Cancel
26

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.6 网络密码服务处理消息流图
OMS
TDGW
网络密码服务（ Password Service ）
前置校验失败，服务拒绝
订单拒绝（ Order Reject, OrdRejReason=xxx ）
网络密码服务（ Password Service ）
前置校验通过，业务校验
失败
申报响应（ Password Service Report,  OrdRejReason=xxx ）
网络密码服务（ Password Service ）
业务校验通过，申报成功
申报响应（ Password Service Report,  ExecType=0 ）
3.2.3 平台状态
OMS 向 TDGW 进行申报应符合交易时间表 2 要求。 TDGW 依据交易时间表对平台状态进行了划分，
示意图如下。
处于 NotOpen 、 Break 、 Close 状态时不接收申报， TDGW 返回 Order Reject （ OrdRejReason=5009 ）予
以拒绝。 PreOpen3 状态下， TDGW 提前接收 OMS 的申报，并在 Open 时向交易系统转发。 PreOpen 及 Open
状态下 TDGW 接收的申报是否被交易系统主机接受， OMS 应以申报确认为准。
在 OMS 与 TDGW 交易通道建立会话成功后， TDGW 向 OMS 发送一条平台状态 PlatformState 消息。
当平台状态发生变化时， TDGW 也向已建立会话的 OMS 发送一条平台状态消息予以通知。
2 时间表以本所交易规则为准。
3 目前，设置 PreOpen 为各交易时段 Open 前的 5 秒。以交易时段 9:15-9:25 为例， 9:14:55TDGW 转为 PreOpen ， 9:15:00 TDGW
转为 Open 状态。
27

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
交易系统依据申报中的业务 PBU + 会员内部订单编号组合的取值判断申报是否为重复订单 ; 其中，业
务 PBU 取 Parties 组件中 PartyID 字段（当 PartyRole=1 ）。
会员内部订单编号取消息类型相应字段：
申报类型
会员内部订单编号字段
New Order Single
ClOrdID
Order Cancel
ClOrdID
Quote Request
ClOrdID
Quote
QuoteMsgID
Quote Response
ClOrdID
Password Service
ClOrdID
IOI
IOIID
Trade Capture Report
TradeReportID
对于重复订单， TDGW 返回拒绝消息（ Order Reject ）。
28

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
OMS
TDGW
新申报
New Order Single
ClOrdID=10  Pbu=20001
Execution Report ,ExecType=0
申报确认
重复申报
New Order Single
ClOrdID=10  Pbu=20001
拒绝响应
Order Reject
OrdRejReason=11270
3.2.5 执行报告
每笔执行报告消息都包含 PBU 、分区（ PartitionNo ）和序号（ ReportIndex ）信息。
PBU 字段表明了该执行报告是在哪一个登录 PBU 上进行申报所产生的回报数据，一般为 OMS 所连接
的 TDGW 上正在登录的 PBU ；若 TDGW 配置了订阅，该字段取值也可能为被订阅的其他 PBU ，详见后续
订阅章节的说明。
在每个 PBU 下，执行报告根据分区（ PartitionNo ）划分为多个编号相互独立的数据流。在一个交易日
内，每个执行报告流中的 ReportIndex 由 1 开始连续递增。多个不同业务可以属于同一个分区，从而在同
一个流中按序发送。
OMS 与 TDGW 建立会话后， TDGW 会向 OMS 推送执行报告分区信息（ ExecRptInfo ）消息，其中包
含 PBU 列表和分区列表， OMS 应根据此信息维护多个逻辑上的执行报告流。
OMS 与 TDGW 建立会话后，应根据 ExecRptInfo 中的信息，向 TDGW 发送各个执行报告流的分区序
号同步（ ExecRptSync ）消息， TDGW 将返回一个分区序号同步响应消息（ ExecRptSyncRsp ）进行回应。
对于 ExecRptSync 请求校验通过的情况， TDGW 将依据其中约定的序号 BeginReportIndex 发送后续执行报
告。
OMS 若不发送序号同步消息， TDGW 将不会推动执行报告。如果 OMS 发送的序号同步消息中，
BeginReportIndex 大于实际存在的分区回报最大序号，则 TDGW 不会推送执行报告，直至实际分区回报数
确实达到 BeginReportIndex 后再开始推送。闭市后， TDGW 不再接收 OMS 申报，但可以通过序号同步消
29

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
息重新获取当日历史执行报告数据。
OMS 应对 TDGW 推送的执行报告进行数据持久化操作，且 OMS 应具备识别重复执行报告的能力，
避免重复处理。
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
在 OMS 重新与 TDGW 建立会话后，由于断连期间可能存在传输中的消息丢失， OMS 应对上下行两
个方向的消息进行恢复。建议 OMS 先对执行报告进行恢复，以尽可能更新断连前申报订单的状态。 OMS
可在恢复一段时间后，对仍然处于 “ 已报但未确认 ” 状态的订单进行重新申报。
TDGW 与 ITCS 断开
TDGW 与 ITCS 间连接断开时， TDGW 将通过 Logout （ SessionStatus=5006 ）消息注销与 OMS 间的会
话，并尝试切换备用 ITCS 。在 TDGW 未登录至交易系统期间， OMS 发起到 TDGW 的会话将无法成功。
TDGW 恢复登录，且 OMS 重建与 TDGW 间的会话后， OMS 对消息的恢复处理可与上一节描述相同。
30

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.4 订阅机制
通过在 TDGW 端进行配置， OMS 可通过与一个 TDGW 间的会话，接收到其他 TDGW 上登录的另一
PBU 所产生的执行报告数据。
TDGW 端登录的 PBU-B ，若需订阅另一 TDGW 上登录的 PBU-A 所产生的执行报告， PBU-B 与 PBU-A
需要属于同一市场参与者机构。
目前，交易系统限制每个登录 PBU 可被最多 3 个其他登录 PBU 订阅成功。为减少订阅对登录 PBU 自
身回报数据处理的影响， TDGW 将优先发送登录 PBU 自身的回报数据。
在同一市场参与者机构的范围内，订阅的配置和管理由市场参与者机构负责，市场参与者机构在充分
利用订阅形成 TDGW 互备的同时，也应做好订阅权限和数据权限的控制。
31

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4 消息定义
4.1 消息结构与约定
每一条 STEP 消息由消息头、消息体和消息尾组成，消息最大长度为 4K 字节。
4.2 数据类型
数据类型相关说明如下：
1. 字符串类型用 CX 表示， X 表示字符串最大字节数，除特别声明，字符串只包含数字、大写字母、
小写字母以及空格；字符串实际长度小于字段类型最大长度时可以不补空格；字符串统一采用 UTF-8 编码，
不可输入系统保留字符，包括 ‘\r’ ， ‘\t’ ， ‘\’’ 和 ‘&’ 。
2. 十进制整数用 NX 表示， X 表示整数最大位数（不包括正负号），除特殊说明，整数类型均有正负。
3. 浮点数用 NX （ Y ）表示， X 表示整数与小数总计位数（不包括小数点及正负号）， Y 表示小数位
数，小数位数不足时必须在后面补 0 ，除非特殊说明，浮点数类型均有正负。
4. 数值类型字段默认填 0 值，字符串类型默认填空格；针对 “ 暂不启用 ” 字段，填写默认值。
5. 针对部分字段填写固定值的场景，固定值根据实际字段类型进行填写。如字段要求 “ 固定填 1” ，若
字段类型为 N13(5) ，则实际填写 1.00000 ；若字段类型为 C1 ，则实际填写字符 ‘1’ 。
6. 为简化描述，定义部分业务类型如下：
字段名
类型
说明
price
N13(5)
价格，对于债券单位为元；对于回购或借贷，表示利率，单位为 % 。
quantity
N15(3)
数量。对于债券，单位为千元面额；对于基金或公募 REITs ，单位为份；对于
信用保护凭证，单位为 10 张。
amount
N18(5)
金额，单位为元
date
C8
当前时区日期，格式 YYYYMMDD ， YYYY 为年，取值范围 0000-9999 ， MM
为月，取值范围 01-12 ， DD 为日，取值范围 01-31
ntime
C13
当前时区时间，格式 HHMMSSsss ， HH 为小时，取值范围 00-23 ， MM 为分钟，
取值范围 00-59 ， SS 为秒，取值范围 00-59 ， sss 为毫秒，取值范围 000-999
Boolean
C1
代表该字符串内容为布尔值，有效取值是 Y 或者 N 。
32

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.2.1 STEP 格式约定
STEP 结构均采用依次排列 “ 标签 = 字段取值 <SOH>” 的方式组织，标签为数字字符，前后无空格。除非
特别声明外，字段取值均为可打印 ASCII 码字符串表示，不得采用全角字母字符；对于支持中文的字段，
采用 UTF-8 编码。 <SOH> 为字段界定符，值为不可打印 ASCII 码字符：十六进制的 0x01 。
STEP 结构中重复组部分的字段需严格遵循接口规格中定义的先后顺序；字符型字段用空格表示空值，
即采用 “ 标签 = <SOH>” 的方式表示（等号后与分隔符间有一个空格），数值型字段用 0 表示空值，即 “ 标签
=0<SOH>” （注：含小数数值型字段空值需符合格式要求，例 N13 （ 5 ）空值表示为 “ 标签 =0.00000<SOH>” ）。
4.2.2 STEP 消息头
每一个会话或应用消息都有一个消息头，该消息头指明消息类型、消息体长度、消息序号及发送时间
等信息。
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
56
TargetCompID
Y
接收方代码， OMS 发出的消息中填写 “TDGW”
C32
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
YYYYMMDD-HH:MM:SS.sss
347
MessageEncoding
N
字符编码类型，取值如下：
C16
UTF-8
4.2.3 STEP 消息尾
每一个会话或应用消息都有一个消息尾，并以此终止。消息尾可分隔多个消息，包含有 3 位数的校验
和值。
33

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
消息长度通过 BodyLength 域记录，表示 BodyLength 域值之后第一个域界定符 <SOH> （不包括）与
CheckSum 域号前的最后一个域界定符 <SOH> （包括）之间的字符个数。
校验和是把每个字符的 ASCII 码值从消息开头 ‘8=’ 中的 ‘8’ 开始相加，一直加到紧靠在 CheckSum 域号
‘10=’ 之前的域界定符，然后取按 256 取模得到的结果。计算校验和的代码段可参考附录一 “ 计算校验和 ” 。
34

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.3 会话消息
会话消息将在以下各节中予以介绍，并定义会话消息格式，会话层消息机制兼容《 LFIXT 会话协议接
口规范》。
4.3.1 登录消息（ MsgType=A ）
登录消息（ Logon ）应是 OMS 建立连接后发送的首个消息。
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
ResetSeqNumFlag
N
双方序号重置为 1 的标记（请求时必填
Boolean
Y ）
789
NextExpectedMsgSeqNum
N
接收方期望得到的下一条消息序号（请
N18
求时必填 1 ）
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
1137
DefaultApplVerID
Y
本次会话中使用的 FIX 消息的缺省版本
C8
1407
DefaultApplExtID
N
本次会话中使用的 FIX 消息的缺省扩展
N8
包
1408
DefaultCstmApplVerID
Y
本次会话中 FIX 消息的缺省自定义应
C32
用
版
本
。
填
写
格
式
为
STEP1.20_SH_n.xy 其中 n.xy 为接入
协议版本号，如接入协议版本号为 1.70
时，则填写： STEP1.20_SH_1.70 。
（ TDGW 将限制接入的协议版本。当前
最低接入协议版本要求为 0.10 版）
标准消息尾
35

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.3.2 注销消息（ MsgType=5 ）
注销消息是发起或确认会话终止的消息。连接双方在发送注销消息之后不应发送任何消息。
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
4.3.3 心跳消息（ MsgType=0 ）
心跳消息用于监控通信连接的状况。如果接收方在 5 倍心跳时间间隔内未收到任何消息的时候，可认
定会话出现异常，可以立即关闭 TCP 连接。
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
如是对测试请求消息（ 4.2.4 ）而发送的心跳消息，则需包
C32
含本域，否则不包含本域。本域的内容复制于测试请求消
息（ 4.2.4 ）的 TestReqID 内容
标准消息尾
Y
4.3.4 测试请求消息（ MsgType=1 ）
测试请求消息能强制对方发出心跳消息。测试请求消息的作用是检查对方消息序号和检查通信线路的
状况。对方用带有测试请求标识符（ TestReqID ）的心跳作应答。 TDGW 不会主动发送此消息，但会遵循
FIX 标准引擎规则而响应 OMS 发送的该请求。
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
36

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.3.5 重发请求消息（ MsgType=2 ）
TDGW 不会主动发送此消息，但会遵循 FIX 标准引擎规则而响应 OMS 发送的该请求。 TDGW 接收到
重发请求消息，通过序号重设消息（ 4.2.7 ）响应。
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
4.3.6 会话拒绝消息（ MsgType=3 ）
当接收方收到一条违反会话层规则而不能正确处理的消息时，应该发出会话拒绝消息。 TDGW 不会主
动发送此消息。
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
相关错误消息中，出现错误的 FIX 域号
N6
372
RefMsgType
N
相关错误消息的 MsgType
C16
373
SessionRejectReason
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
序号重设消息用于告知接收方下一个消息的消息序号。序号重设消息的 MsgSeqNum 按标准 FIX 协议
规定可以任意填写且接收方不会检查，建议固定填写为 1 。 TDGW 不会主动发送此消息，但会遵循 FIX 标
准引擎规则而响应 OMS 发送的重发请求消息（ 4.2.5 ）。当 TDGW 收到用户序号重设消息，则重置入向消
息序号 NxtIn = NewSeqNo 。
序号重设消息格式如下：
37

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
38

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.4 应用消息
4.4.1 订单业务类
4.4.1.1 新订单申报（ New Order Single, MsgType = D ）
标签
字段名
字段描述
必须
类型
消息头
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
订单所有者类型，取值包括：
Y
N3
1= 个人投资者
103= 机构投资者
104= 自营交易
54
Side
买卖方向，取值：
Y
C1
1 = 买（转入）
2 = 卖（转出）
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
110
MinQty
最低成交数量
N
quantity
40
OrdType
订单类型： 2= 限价（目前仅支持限价）
N
C1
59
TimeInForce
订单有效时间类型，取值范围： 0 表示当日有效
Y
C1
（ GFD ）
60
TransactTime
订单申报时间
Y
ntime
544
CashMargin
信用标签，信用交易时填写，取值： XY= 担保品
N
C2
买卖、 RZ= 融资交易、 PC= 平仓交易
1091
PreTradeAnonymity
是否匿名报价，取值：匿名 =1 ，显名 =0
N
C1
63
SettlType
结算方式： 1= 净额结算， 2=RTGS 结算
N
C1
担保券可填 1 或 2 ；非担保券只能为 2 。特别地，
39

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
对于公募可转债或公募 REITs ，只能填 1 。
198
SecondaryOrderID
第二交易所订单编号
N
C16
10238
BidTransType
竞买业务类型
N
C1
1 = 竞买预约
2 = 竞买申报
3 = 应价申报
10239
BidExecInstType
竞买成交方式
N
C1
1 = 单一主体中标
2 = 多主体单一价格中标
3 = 多主体多重价格中标
432
ExpireDate
失效日期
N
date
529
OrderRestrictions
订单限制，表示是否竞买日自动发起竞买申报
N
Boolean
Y = 是
N = 否
58
Text
用户私有信息
N
C32
453
NoPartyIDs
参与方个数，取值 =14 ，后接重复组，依次包含发
Y
N2
起方的投资者账户、业务交易单元号、三方回购
专用账户、三方回购专户对应交易单元号、交易
员一债通账户、银行间托管账号、营业部代码、
结算会员代码、投资者中国结算开放式基金账户、
投资者中国结算交易账户、销售人代码、券商网
点号码、开放式基金转托管的目标方、申报编号。
发起方投资者
448
PartyID
发起方投资者帐户
Y
C13
账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起方投资者帐
Y
N4
户。
发起方业务交
448
PartyID
发起方业务交易单元代码，填写 5 位业务交易单
Y
C8
易单元号
元号。
452
PartyRole
取 1 ，表示当前 PartyID 的取值为发起方业务交易
Y
N4
单元号。
发起方三方回
448
PartyID
填写三方回购专用账户。
N
C13
40

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
购专用账户
452
PartyRole
取 107 ，表示当前 PartyID 的取值为发起方三方回
N
N4
购专用账户
发起方三方回
448
PartyID
发起方三方回购专用账户对应交易单元号
N
C8
购专户对应交
452
PartyRole
取 106 ，表示当前 PartyID 的取值为发起方三方回
N
N4
易单元号
购专用账户对应交易单元号
发起方交易员
448
PartyID
交易员一债通账户
N
C10
一债通账户
452
PartyRole
取 101 ，表示当前 PartyID 的取值为发起方的交易
N
N4
员一债通账户
银行间托管帐
448
PartyID
银行间托管账号。债券转托管时适用。
N
C11
号
452
PartyRole
取 28 ，表示当前 PartyID 的取值为银行间托管账号
N
N4
发起方营业部
448
PartyID
发起方营业部代码
<span style="color:blue">NY</span>
C8
代码
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为发起方的营业
<span style="color:blue">NY</span>
N4
部代码。
结算会员代码
448
PartyID
结算会员代码
N
C8
452
PartyRole
取 4 ，表示当前 PartyID 的取值为结算会员代码。
N
N4
投资者中国结
448
PartyID
投资者场外开放式基金账户
N
C12
算开放式基金
452
PartyRole
取 4010 ，表示当前 PartyID 的取值为发起方的中国
N
N4
账户
结算开放式基金账户。
投资者中国结
448
PartyID
投资者中国结算交易账户
N
C17
算交易账户
452
PartyRole
取 4011 ，表示当前 PartyID 的取值为发起方中国结
N
N4
算开放式基金账户下的交易账户。
销售人代码
448
PartyID
销售人代码
N
C9
452
PartyRole
取 117 ，表示当前 PartyID 的取值为发起方的销售
N
N4
代码。
券商网点号码
448
PartyID
券商网点号码
N
C9
452
PartyRole
取 81 ，表示当前 PartyID 的取值为发起方的客户端
N
N4
编码或网点号码。
开放式基金转
448
PartyID
开放式基金转托管的目标方代理人，对方对应的
N
C3
托管的目标方
销售人代码，取值 000-999 ，不足 3 位左侧补 0 。
452
PartyRole
取 30 ，表示当前 PartyID 的取值为开放式基金转
N
N4
41

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
托管的目标方代理人。
申报编号
448
PartyID
申报编号
N
C6
452
PartyRole
取 4003 ，表示当前 PartyID 的取值为申报编号
N
N4
8532
DividendSelect
分红选项， U= 红利转投， C= 现金分红
N
C1
说明：
1 、各业务填写字段说明如下：
ApplID
业务类型
相关字段填写说明
1.Price 字段必填
2.OrderQty 申报数量单位为份；
3. 投资者中国结算开放式基金账户、投资者中国结算交易账户、销
600020
基金通报价交易
售人代码、券商网点号码 <span style="color:blue">、营业部代码</span> 为必填
4.OrdType 必填
1. 投资者中国结算开放式基金账户、投资者中国结算交易账户、销
售人代码、券商网点号码 <span style="color:blue">、营业部代码</span> 为必填
600021
基金通转入转出
2.OrderQty 申报数量单位为份
3.OrdType 必填
1. Price 固定填 1 。
2.Side 固定填 1 。
3.OrderQty 表示申购金额，单位为元，填写非 0 正整数，累加申购
600030
开放式基金申购
金额为 100 元或其整数倍。
4. SecurityID 填写正股代码（ 519XXX ）。
<span style="color:blue">5.</span> <span style="color:blue">营业部代码必填。</span>
1. Price 固定填 1 。
2.Side 固定填 2 。
3. OrderQty 表示赎回份额，单位为份，填写非 0 正整数，不支持小
600040
开放式基金赎回
数。
4. SecurityID 填写正股代码（ 519XXX ）。
<span style="color:blue">5.</span> <span style="color:blue">营业部代码必填。</span>
600050
开放式基金转托管转出
1.Price 固定填 1 。
42

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
ApplID
业务类型
相关字段填写说明
2. OrderQty 表示基金份额，单位为份，填写非 0 正整数，不支持小
数。
3.Side 固定填 2 。
4. SecurityID 填写正股代码（ 519XXX ）。
5. 开放式基金转托管的目标方 <span style="color:blue">、营业部代码</span> 字段必填。
1.Price 固定填 1 。
2.Side 固定填 1 。
3.OrderQty 固定填 1 。
600060
开放式基金分红选择
4. SecurityID 填写正股代码（ 519XXX ）。
5. DividendSelect 必填， U= 红利转投， C= 现金分红。
<span style="color:blue">6.</span> <span style="color:blue">营业部代码必填</span>
1.Price 表示收购价，单位为元，填写非 0 正数。
2.Side 固定填 2 。
要约预受 / 现金选择权登
3. OrderQty 表示收购数量，填写非 0 正整数。
600070
记
4. SecurityID 填写标的证券正股代码。
5. 申报编号字段必填，填写 6 位数字 <span style="color:blue">；营业部代码必填</span> 。
1.Price 表示收购价，单位为元，填写非 0 正数。
2.Side 固定填 1 。
要约撤销 / 现金选择权注
3. OrderQty 表示收购数量，填写非 0 正整数。
600071
销
4. SecurityID 填写标的证券正股代码。
5. 申报编号字段必填，填写 6 位数字 <span style="color:blue">；营业部代码必填</span> 。
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
3. Side 固定填 1 。买入转义为标的证券从“证券公司融券专用账户”
过户到“证券公司信用交易担保证券账户”。仅允许投资者信用账
600080
融资融券余券划转
户（ E 字头）申报。
4.OrderQty 表示划转数量 , 填写非 0 正整数，允许零散股。
<span style="color:blue">5.</span> <span style="color:blue">营业部代码必填</span>
600090
融资融券还券划转
1. SecurityID 表示转入的标的产品代码。
43

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
ApplID
业务类型
相关字段填写说明
2. Price 固定填 1 。
3.Side 固定填 2 。卖出转义为标的证券从“证券公司信用交易担保证
券账户”过户到“证券公司融券专用账户”。仅允许投资者信用账
户（ E 字头）申报。
4. OrderQty 表示划转数量 , 填写非 0 正整数，允许零散股 <span style="color:blue">；营业部</span>
<span style="color:blue">代码必填</span> 。
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
3.Side 固定填 1 。买入转义为标的证券从“投资者普通证券账户”过
户到“证券公司信用交易担保证券账户”。仅允许投资者信用账户
600100
融资融券担保品划入
（ E 字头）申报。
4. OrderQty 划转数量 , 填写非 0 正整数，允许零散股 <span style="color:blue">；营业部代码</span>
<span style="color:blue">必填</span> 。
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
3.Side 固定填 2 。卖出转义为标的证券从“证券公司信用交易担保证
券账户”过户到“投资者普通证券账户”。仅允许投资者信用账户
600101
融资融券担保品划出
（ E 字头）申报。
4. OrderQty 划转数量 , 填写非 0 正整数，允许零散股 <span style="color:blue">；营业部代码</span>
<span style="color:blue">必填</span> 。
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
3.Side 固定填 2 ，卖出转义为标的证券从“证券公司自营账户”过户
600110
融资融券券源划入
到“证券公司融券专用账户”。仅允许证券公司自营账户申报。
4. OrderQty 划转数量 , 填写非 0 正整数，允许零散股 <span style="color:blue">；营业部代码</span>
<span style="color:blue">必填</span> 。
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
600111
融资融券券源划出
3.Side 固定填 1 。买入转义为标的证券从“证券公司融券专用账户”
44

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
ApplID
业务类型
相关字段填写说明
过户到“证券公司融券自营账户”。仅允许证券公司自营账户申报。
4. OrderQty 划转数量 , 填写非 0 正整数，允许零散股 <span style="color:blue">；营业部代码</span>
<span style="color:blue">必填</span> 。
600230
双非可转债转股冻结
1. 参与方中需要填写交易员一债通账户；对转托管申报，银行间托
管账号必填；三方回购转入转出时，专用账户及其对应的交易单元
600240
私募可交换债换股
必填；
600250
债券回售（一债通）
2. Side ：对于转托管、回售、转股冻结和换股，填 2 ；对回售撤销
600251
债券回售撤销
申报填 1 。对三方回购转入填 1 ，转出填 2 。交易员仅可输入转股冻
600260
债券转托管
结，场务可进行转股解冻，转股解冻时方向（订单响应中）填 1 。
600270
三方回购转入转出
3. OrderQty 必填； Text 选填。其他非必填字段无效。
1. BidTransType 填 1 ， Price 表示底价， OrderQty 表示竞买数量。
2. 参与方中交易员一债通账户必填。
3. SettlType 、 BidExecInstType 、 PreTradeAnonymity 、 ExpireDate 、
竞买预约
OrderRestrictions 必填， ExpireDate 表示竞买申报日。
4. MinQty 如选择多主体中标时必填，否则不可填； Text 选填；其他
非必填字段无效。
1. BidTransType 填 2 ， 1.Price 表示底价， OrderQty 表示竞买数量。
600290
2. 参与方中交易员一债通账户必填。
（预留，
竞买申报
3. MinQty 如选择多主体中标时必填，否则不可填。
暂不启
4. SettlType 、 BidExecInstType 、 PreTradeAnonymity 与竞买预约申报
用）
相同，本次不可修改； Text 选填；其他非必填字段无效。
1. BidTransType 填 3 ；
2. 对于单一主体中标， OrderQty 必须与竞买预约数量相等， Price
应当大于等于底价；
应价申报
3. 参与方中交易员一债通账户必填、 PreTradeAnonymity 必填；
SecondaryOrderID 必填，表示应价对应的竞买申报编号； Text 选填；
其他非必填字段无效。
2 、 OrdType 字段：开放式基金、要约 / 现金选择权、融资融券业务申报请求暂不启用。
3 、 Text 字段对于开放式基金、融资融券、要约 / 现金选择权非交易业务仅前 12 位有效。
4 、 “ 发起方营业部代码 ” 字段： 5 位数字表示，目前使用区间为 [00000 ， 65535] ，不足 5 位的左侧补 0 。
45

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
营业部代码可于本所网站会员专区查询，若无对应营业部代码，则该字段填写空格。
5 、 “ 结算会员代码 ” 字段： B 股结算会员代码，对于 A 股投资者取值无意义，对于 B 股境外投资者 C9
类账户此记录不能为空，直接填写中登公司公布的 B 股结算会员代码，不足 5 位的左侧补 0, 。对于 B 股境
内投资者 C1 类账户无意义，前 5 位有效。对于开放式基金、要约 / 现金选择权、融资融券非交易业务无意
义。
6 、 OwnerType 字段：开放式基金、要约 / 现金选择权、融资融券非交易业务申报请求暂不启用。
7 、参与方个数应小于等于 14 ，重复组个数应与申报参与方个数相匹配并按序依次填写，非必填参与
方可跳过。若参与方重复申报，则允许覆盖并仅以最末尾上报值为准（后处理逻辑相同）。
4.4.1.2 撤单申报（ Order Cancel, MsgType = F ）
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
买卖方向，取值： 1 表示买（转入）， 2 表示卖（转出）
Y
C1
41
OrigClOrdID
原始会员内部订单编号，指被撤单订单的 ClOrdID
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
参与方个数，取值 =12 ，后接重复组，依次包含发起方的投资
者账户、业务交易单元号、三方回购专用账户、三方回购专
户对应交易单元号、交易员一债通账户、银行间托管账号、
453
NoPartyIDs
Y
N2
营业部代码、投资者中国结算开放式基金账户、投资者中国
结算交易账户、销售人代码、券商网点号码、申报编号。
448
PartyID
发起方投资者帐户
Y
C13
发起方投
资者账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起方投资者帐户。
Y
N4
发起方业
448
PartyID
发起方业务交易单元代码，填写 5 位业务交易单元号。
Y
C8
务交易单
452
PartyRole
取 1 ，表示当前 PartyID 的取值为发起方业务交易单元号。
Y
N4
元号
46

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
发起方三
448
PartyID
填写三方回购专用账户。
N
C13
方回购专
452
PartyRole
取 107 ，表示当前 PartyID 的取值为发起方三方回购专用账户
N
N4
用账户
发起方三
448
PartyID
发起方三方回购专用账户对应交易单元号
N
C8
方回购专
取 106 ，表示当前 PartyID 的取值为发起方三方回购专用账户
N
N4
户对应交
452
PartyRole
对应交易单元号
易单元号
448
PartyID
交易员一债通账户
N
C10
发起方交
易员一债
取 101 ，表示当前 PartyID 的取值为发起方的交易员一债通账
452
PartyRole
N
N4
通账户
户
银行间托管账号，填写 11 位银行间托管账号。债券转托管时
N
C11
银行间托
448
PartyID
适用。
管帐号
452
PartyRole
取 28 ，表示当前 PartyID 的取值为银行间托管账号
N
N4
448
PartyID
发起方营业部代码
<span style="color:blue">NY</span>
C8
发起方营
业部代码
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为发起方的营业部代码。
<span style="color:blue">NY</span>
N4
投资者中
448
PartyID
投资者场外开放式基金账户
N
C12
国结算开
取 4010 ，表示当前 PartyID 的取值为发起方的中国结算开放
放式基金
452
PartyRole
N
N4
式基金账户。
账户
投资者中
448
PartyID
投资者中国结算交易账户
N
C17
国结算交
取 4011 ，表示当前 PartyID 的取值为发起方中国结算开放式
452
PartyRole
N
N4
易账户
基金账户下的交易账户。
销售人代
448
PartyID
销售人代码
N
C9
码
452
PartyRole
取 117 ，表示当前 PartyID 的取值为发起方的销售代码。
N
N4
448
PartyID
券商网点号码
N
C9
券商网点
取 81 ，表示当前 PartyID 的取值为发起方的客户端编码或网
号码
452
PartyRole
N
N4
点号码。
448
PartyID
申报编号
N
C6
申报编号
452
PartyRole
取 4003 ，表示当前 PartyID 的取值为申报编号
N
N4
说明：
47

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
1 、基金通报价交易 ApplID=600020 ，基金通转入转出 ApplID=600021 时，投资者中国结算开放式基
金账户、投资者中国结算交易账户、销售人代码、券商网点号码 <span style="color:blue">、营业部代码</span> 为必填。
2 、撤单申报中， APPIID 、发起方投资者账户、发起方业务交易单元号、发起方三方回购专用账户、
发起方三方回购专户对应交易单元号、发起方交易员一债通账户、银行间托管帐号、投资者中国结算开放
式基金账户、投资者中国结算交易账户、销售人代码、券商网点、 SecurityID 、 Side 取值应与原申报相同，
OrigClOrdID 的取值应与待撤原订单的 ClOrdID 相同 <span style="color:blue">，</span> <span style="color:blue">Text</span> <span style="color:blue">字段选填</span> 。对于开放式基金、要约 / 现金选择权、
融资融券非交易业务，仅要求 ApplID 、发起方业务交易单元号、 SecurityID 取值应与待撤原订单相同，
OrigClOrdID 的取值应与待撤原订单的 ClOrdID 相同； Text 字段仅前 12 位有效。
3 、要约 / 现金选择权业务撤单申报时，申报编号字段必填，且需与原订单保持一致。
4 、发起方投资者账户、发起方营业部代码、 OwnerType 、 Side 字段对于开放式基金、要约 / 现金选择
权、融资融券非交易业务暂不启用。
<span style="color:blue">5</span> <span style="color:blue">、发起方营业部代码对开放式基金、要约</span> <span style="color:blue">/</span> <span style="color:blue">现金选择权、融资融券非交易业务、双非可转债转股冻结、</span>
<span style="color:blue">私募可交换债换股、债券回售（一债通）、债券回售撤销、债券转托管、三方回购转入转出和竞买业务暂</span>
<span style="color:blue">不启用，其他业务必填。</span>
4.4.2 询价报价业务类
4.4.2.1 询价请求（ Quote Request, MsgType=R ）
标签
字段名
字段描述
必须
类型
消息头
MsgType=R
1180
ApplID
业务类型
Y
C6
11
ClOrdID
会员内部编号
Y
C10
原始会员内部订单编号，指被撤单订单的
41
OrigClOrdID
N
C10
ClOrdID
报价类别
537
QuoteType
N
N4
1=Tradeable ，表示可交易的报价
订单所有者类型
1= 个人投资者
522
OwnerType
Y
N3
103= 机构投资者
104= 自营交易
48

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
60
TransactTime
订单申报时间
N
ntime
48
SecurityID
证券代码
Y
C12
买卖方向，取值有：
0 = 双边报价
54
Side
Y
C1
1 = 买
2 = 卖
订单数量
38
OrderQty
N
quantity
特别地， Side 为 0 时表示买入数量
订单价格
N
price
44
Price
特别地， Side 为 0 时表示买入价格
640
Price2
Side 为 0 时表示卖出价格
N
price
32
LastQty
Side 为 0 时表示卖出数量
N
quantity
1138
DisplayQty
冰山订单数量
N
quantity
价格下限
2551
StartPriceRange
N
price
预留字段，暂不启用
价格上限
2552
EndPriceRange
N
price
预留字段，暂不启用
询价请求事务类型
0-New ，新订单
10200
QuoteRequestTransType
Y
C1
1-Cancel ，撤销
1091
PreTradeAnonymity
是否匿名报价，取值：匿名 =1 ，显名 =0
N
C1
8418
FullAmountTrade
是否全额成交： 1= 是， 2= 否
N
C1
结算方式： 1= 净额结算， 2=RTGS 结算
担保券可填 1 或 2 ；非担保券只能为 2 。特别
63
SettlType
N
C1
地，对于公募可转债或公募 REITs ，只能填 1 。
结算场所： 1= 中国结算， 2= 中央结算
双边托管券，可填 1 或 2 ，单边托管券只能填
207
SecurityExchange
N
C1
其实际托管方。预留字段，暂不启用。
结算周期：
10216
SettlPeriod
N
C1
0 = T+0
49

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
1 = T+1
2 = T+2
3 = T+3
预留字段，暂不启用
126
ExpireTime
询价请求失效时间，预留字段，暂不启用
N
ntime
10300
NoCounterpartyParticipant
询价接收方参与人个数
Y
N10
→
10301
CounterpartyParticipantCode
询价接收方参与人代码，支持特殊符号‘ - ’
N
C12
参与方个数，取值 =8 ，后接重复组，依次包含
询价发起方的投资者账户、业务交易单元代
码、营业部代码、交易员一债通账户、投资者
453
NoPartyIDs
Y
N2
中国结算开放式基金账户、投资者中国结算交
易账户、销售人代码、券商网点号码。
发起方
448
PartyID
询价发起方投资者帐户
Y
C13
投资者
取 5 ，表示当前 PartyID 的取值为发起方投资
452
PartyRole
Y
N4
账户
者帐户
发起方
询价发起方业务交易单元代码，填写 5 位业务
448
PartyID
Y
C8
交易单元号。
业务交
易单元
取 1 ，表示当前 PartyID 的取值为发起方业务
452
PartyRole
Y
N4
号
交易单元号。
发起方
448
PartyID
询价发起方营业部代码
<span style="color:blue">NY</span>
C8
营业部
取 4001 ，表示当前 PartyID 的取值为询价发起
452
PartyRole
<span style="color:blue">NY</span>
N4
代码
方的营业部代码。
发起方
448
PartyID
交易员一债通账户
N
C10
交易员
取 101 ，表示当前 PartyID 的取值为发起方的
452
PartyRole
一债通
N
N4
交易员一债通账户
账户
投资者
448
PartyID
投资者场外开放式基金账户
N
C12
中国结
取 4010 ，表示当前 PartyID 的取值为发起方的
N
N4
算开放
452
PartyRole
场外开放式基金账户。
式基金
50

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
账户
投资者
448
PartyID
投资者中国结算交易账户
N
C17
中国结
取 4011 ，表示当前 PartyID 的取值为发起方的
N
N4
算交易
452
PartyRole
场外交易账户。
账户
448
PartyID
销售人代码
N
C9
销售人
取 117 ，表示当前 PartyID 的取值为发起方的
N
N4
代码
452
PartyRole
销售代码。
448
PartyID
券商网点号码
N
C9
券商网
取 81 ，表示当前 PartyID 的取值为发起方的客
N
N4
点号码
452
PartyRole
户端编码或网点号码。
说明：
1 、对于询价请求订单申报， TransactTime 选填，其他非必填字段要求如下 <span style="color:blue">，未提及的非必填字段均无</span>
<span style="color:blue">效</span> ：
业务类型（ ApplID ）
申报填写说明
撤单填写说明
基
金
通
询
价
1. Side 仅可填 1 或 2 ， OrderQty 表示对应方向数量
OrigClOrdID
（ 600022 ）
必填
2. 投资者中国结算开放式基金账户、投资者中国结算交易账户、销售
人代码、券商网点号码、营业部代码为必填
3. “ 询价接收方参与人个数 ” 字段可填 [0,50] ，填 0 时， “ 询价接收方参与
人代码 ” 字段必须为空，表示向市场该产品对应全部做市商发起询价
待定报价（ 600200 ）
1. SettlType 、 FullAmountTrade 、 PreTradeAnonymity 必填
OrigClOrdID 、
发起方交易员
2. NoCounterpartyParticipant 必填，可填 [0,5] ， 0 表示发送给全市场；如
信息必填
指定范围发送， CounterpartyParticipantCode 必填
3. DisplayQty 选填，需要为最小变动单位的正整数倍； DisplayQty 和
FullAmountTrade=1 不可同时申报。如指定范围发送，不支持冰山订单。
4. 支持双边报价：如 Side 填 0 ，则 OrderQty 、 Price 、 LastQty 、 Price2
均需填写；否则仅填写对应方向的价格和数量即可
5. 发起方交易员信息必填
一
债
通
询
价
1. Side 仅可填 1 或 2
（ 600190 ）
2. OrderQty 、 PreTradeAnonymity 、 SettlType 必填
51

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
业务类型（ ApplID ）
申报填写说明
撤单填写说明
3. NoCounterpartyParticipant 必填，可填 [0,5] ，填 0 时表示发给潜在投
资者；大于 0 时， CounterpartyParticipantCode 必填
4. 发起方交易员信息必填
2 、对于待定报价双边报价，如在限定范围内发布，将拆分为两笔子订单转发给对手方；如全市场发
布，则拆分为两笔子订单通过逐笔行情对外发布。
4.4.2.2 询价请求响应（ Quote Request Ack, MsgType=R ）
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
业务类型
Y
C6
询价请求编号，交易所唯一化处理后的询价请
131
QuoteReqID
Y
C18
求 ID
11
ClOrdID
会员内部编号
Y
C10
原始会员内部订单编号，指被撤单订单的
41
OrigClOrdID
N
C10
ClOrdID
申报来源
0 = 网页端申报
2405
ExecMethod
N
C1
1 = 接口端（ TDGW ）申报
报价类别
537
QuoteType
N
N4
1=Tradeable ，表示可交易的报价
订单所有者类型
1= 个人投资者
522
OwnerType
Y
N3
103= 机构投资者
104= 自营交易
60
TransactTime
<span style="color:blue">回报订单申报</span> 时间
N
ntime
48
SecurityID
证券代码
Y
C12
54
Side
买卖方向，取值有：
Y
C1
52

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
0 = 双边
1= 买
2= 卖
订单数量，撤单时表示剩余数量
Side 为 0 时表示买入数量，双边撤单时表示买
38
OrderQty
N
quantity
入剩余数量
Side 为 0 时表示卖出数量，双边撤单时表示卖
N
quantity
32
LastQty
出剩余数量
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
QuoteRequestStatus=0 时为交易所订单编号，
37
OrderID
N
C16
QuoteRequestStatus=4 时为被撤询价单交易所
订单编号
17
ExecID
订单执行编号
N
C16
询价请求事务类型
0-New ，新订单
10200
QuoteRequestTransType
Y
C1
1-Cancel ，撤销
询价请求类型
101=Submit ，提交
303
QuoteRequestType
Y
C3
102=Alleged ，转发
询价请求状态
0=Accepted ，已接受
4=Cancelled ，已撤销
10222
QuoteRequestStatus
Y
C1
5=Rejected ，已拒绝
7=Expired ，已超时
658
QuoteRequestRejectReason
订单拒绝码
N
C5
10237
QuoteRequestRejectText
订单拒绝原因说明
N
C32
126
ExpireTime
询价请求失效时间，预留字段，暂不启用
N
ntime
10300
NoCounterpartyParticipant
询价接收方参与人个数
Y
N10
53

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
→
10301 CounterpartyParticipantCode
询价接收方参与人代码，支持特殊符号‘ - ’
N
C12
参与方个数，取值 = <span style="color:blue">9</span> ，后接重复组，依次包含
询价发起方的 <span style="color:blue">登录或订阅交易单元、</span> 投资者账
户、业务交易单元代码、营业部代码、交易员
453
NoPartyIDs
Y
N2
一债通账户、投资者中国结算开放式基金账户、
投资者中国结算交易账户、销售人代码、券商
网点号码。
<span style="color:blue">发起方</span>
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">发起方登录或订阅交易单元（除基金通外必填）</span> <span style="color:blue">N</span>
<span style="color:blue">C8</span>
<span style="color:blue">交易单</span>
<span style="color:blue">取</span> <span style="color:blue">17</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为登录或订阅</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">N</span>
<span style="color:blue">N4</span>
<span style="color:blue">元</span>
<span style="color:blue">交易单元。</span>
发起方
448
PartyID
询价发起方投资者帐户
Y
C13
投资者
取 5 ，表示当前 PartyID 的取值为发起方投资者
452
PartyRole
Y
N4
账户
帐户
发起方
询价发起方业务交易单元代码，填写 5 位业务
448
PartyID
Y
C8
交易单元号。
业务交
易单元
取 1 ，表示当前 PartyID 的取值为发起方业务交
452
PartyRole
Y
N4
号
易单元号。
发起方
448
PartyID
询价发起方营业部代码
<span style="color:blue">NY</span>
C8
营业部
取 4001 ，表示当前 PartyID 的取值为询价发起
452
PartyRole
<span style="color:blue">NY</span>
N4
代码
方的营业部代码。
发起方
448
PartyID
交易员一债通账户
N
C10
交易员
取 101 ，表示当前 PartyID 的取值为发起方的交
452
PartyRole
N
N4
一债通
易员一债通账户
账户
投资者
448
PartyID
投资者场外开放式基金账户
N
C12
中国结
算开放
取 4010 ，表示当前 PartyID 的取值为发起方的
452
PartyRole
N
N4
式基金
场外开放式基金账户。
账户
投资者 448
PartyID
投资者中国结算交易账户
N
C17
54

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
中国结
取 4011 ，表示当前 PartyID 的取值为发起方的
算交易
452
PartyRole
N
N4
场外交易账户。
账户
448
PartyID
销售人代码
N
C9
销售人
取 117 ，表示当前 PartyID 的取值为发起方的销
代码
452
PartyRole
N
N4
售代码。
448
PartyID
券商网点号码
N
C9
券商网
取 81 ，表示当前 PartyID 的取值为发起方的客
点号码
452
PartyRole
N
N4
户端编码或网点号码。
说明：
<span style="color:blue">1.</span> <span style="color:blue">对于以下业务，发起方交易单元、发起方交易员一债通账户、</span> <span style="color:blue">TransactTime</span> <span style="color:blue">、</span> <span style="color:blue">ExecMethod</span> <span style="color:blue">有效；</span> <span style="color:blue">申</span>
<span style="color:blue">报或撤单成功时，</span> <span style="color:blue">OrderID</span> <span style="color:blue">有效；订单被拒绝时，</span> <span style="color:blue">QuoteRequestRejectReason</span> <span style="color:blue">有效。其他非必填字段要求如下，</span>
<span style="color:blue">未提及的非必填字段均无效：</span>
<span style="color:blue">业务类型</span>
<span style="color:blue">申报填写说明</span>
<span style="color:blue">撤单</span>
<span style="color:blue">（</span> <span style="color:blue">ApplID</span> <span style="color:blue">）</span>
<span style="color:blue">待定报价</span>
<span style="color:blue">NoCounterpartyParticipant/CounterpartyParticipantCode</span> <span style="color:blue">、</span>
<span style="color:blue">1.</span> <span style="color:blue">撤单成功时</span> <span style="color:blue">OrderQty</span> <span style="color:blue">或</span> <span style="color:blue">LastQty</span>
<span style="color:blue">（</span> <span style="color:blue">600200</span> <span style="color:blue">）</span>
<span style="color:blue">表示剩余数量，否则无效。</span>
<span style="color:blue">OrderQty</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">2.</span> <span style="color:blue">OrigClOrdID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">一债通询价</span>
<span style="color:blue">NoCounterpartyParticipant/CounterpartyParticipantCode</span> <span style="color:blue">、</span>
<span style="color:blue">1.</span> <span style="color:blue">撤单成功时</span> <span style="color:blue">OrderQty</span> <span style="color:blue">表示剩余</span>
<span style="color:blue">（</span> <span style="color:blue">600190</span> <span style="color:blue">）</span>
<span style="color:blue">数量，否则无效。</span>
<span style="color:blue">OrderQty</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">2.</span> <span style="color:blue">OrigClOrdID</span> <span style="color:blue">同申报信息</span>
2. 对于双边报价撤单，如双边订单中有一笔撤销成功，一笔因已成交或其他原因撤销失败，返回撤销
成功（已撤销）；如两笔均因已成交或其他原因撤销失败，返回撤销失败（已拒绝）。
4.4.2.3 转发询价请求（ Allege Quote Request, MsgType=R ）
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
业务类型
Y
C6
55

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
询价请求编号，交易所进行唯一化处理后的询价请求
131
QuoteReqID
Y
C18
ID
报价类别
537
QuoteType
N
N4
1=Tradeable ，表示可交易的报价
订单所有者类型
1= 个人投资者
522
OwnerType
N
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
C12
买卖方向，表示询价发起方的方向，取值有：
1 = 买
54
Side
Y
C1
2 = 卖
44
Price
订单价格
N
price
38
OrderQty
订单数量 <span style="color:blue">，撤单时表示剩余数量</span>
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
询价请求事务类型
0-New ，新订单
10200
QuoteRequestTransType
Y
C1
1-Cancel ，撤销
询价请求类型
101=Submit ，提交
303
QuoteRequestType
Y
C3
102=Alleged ，转发
询价请求状态
0=Accepted ，已接受
4=Cancelled ，已撤销
10222
QuoteRequestStatus
Y
C1
5=Rejected ，已拒绝
7=Expired ，已超时
56

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
8=Filled ，已成交
8418
FullAmountTrade
是否全额成交： 1= 是， 2= 否。
N
C1
63
SettlType
结算方式： 1= 净额结算， 2=RTGS 结算
N
C1
结算场所： 1= 中国结算， 2= 中央结算
207
SecurityExchange
N
C1
预留字段，暂不启用
结算周期：
0 = T+0
1 = T+1
10216
SettlPeriod
N
C1
2 = T+2
3 = T+3
预留字段，暂不启用
126
ExpireTime
询价请求失效时间，预留字段，暂不启用
N
ntime
参与方个数，取值 = <span style="color:blue">8</span> ，后接重复组，依次包含 <span style="color:blue">登录或</span>
<span style="color:blue">订阅交易单元、</span> 询价发起方的投资者账户、交易员一
债通账户、对手方交易参与人机构代码、发起方投资
453
NoPartyIDs
Y
N2
者中国结算开放式基金账户、投资者中国结算交易账
户、销售人代码、券商网点号码。
<span style="color:blue">登录或订阅交易单元（指转发消息的接收方，除基金</span>
<span style="color:blue">登录或订</span>
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">N</span>
<span style="color:blue">C8</span>
<span style="color:blue">通外必填）。</span>
<span style="color:blue">阅交易单</span>
<span style="color:blue">取</span> <span style="color:blue">17</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为登录或订阅交易单</span>
<span style="color:blue">元</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">N</span>
<span style="color:blue">N4</span>
<span style="color:blue">元。</span>
发起方投
448
PartyID
询价发起方投资者帐户
N
C13
资者账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起方投资者帐户
N
N4
448
PartyID
交易员一债通账户
N
C10
发起方交
易员一债
取 101 ，表示当前 PartyID 的取值为发起方的交易员
452
PartyRole
N
N4
通账户
一债通账户
对手方
448
PartyID
对手方交易参与人机构代码，支持特殊符号‘ - ’
N
C12
机构代
取 37 ，表示当前 PartyID 的取值为对手方的交易参
452
PartyRole
N
N4
码
与人代码
投资者中 448
PartyID
投资者场外开放式基金账户
N
C12
57

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
国结算开
取 4010 ，表示当前 PartyID 的取值为发起方的场外开
放式基金
452
PartyRole
N
N4
放式基金账户。
账户
投资者中
448
PartyID
投资者中国结算交易账户
N
C17
国结算交
取 4011 ，表示当前 PartyID 的取值为发起方的场外交
452
PartyRole
N
N4
易账户
易账户。
448
PartyID
销售人代码
N
C9
销售人代
取 117 ，表示当前 PartyID 的取值为发起方的销售代
码
452
PartyRole
N
N4
码。
448
PartyID
券商网点号码
N
C9
券商网点
取 81 ，表示当前 PartyID 的取值为发起方的客户端编
号码
452
PartyRole
N
N4
码或网点号码。
说明：
<span style="color:blue">1</span> <span style="color:blue">、</span> 基金通询价交易（ 600022 ）时，投资者中国结算开放式基金账户、投资者中国结算交易账户、销
售人代码、券商网点号码为必填。
<span style="color:blue">2</span> <span style="color:blue">、一债通询价（</span> <span style="color:blue">600190</span> <span style="color:blue">）、待定报价（</span> <span style="color:blue">600200</span> <span style="color:blue">）时，发起方交易员一债通账户、对手方机构代码必</span>
<span style="color:blue">填。如询价方选择‘匿名’且为‘净额结算’时，发起方交易员一债通账户、发起方投资者账户（如有）</span>
<span style="color:blue">填‘</span> <span style="color:blue">anonymous</span> <span style="color:blue">’。</span>
<span style="color:blue">3</span> <span style="color:blue">、转发信息字段与被转发字段相同，对于业务无效字段，不进行转发。</span>
4.4.2.4 报价（ Quote, MsgType=S ）
标签
字段名
字段描述
必须
类型
消息头
MsgType=S
1180
ApplID
业务类型
Y
C6
<span style="color:blue">报价类别</span>
<span style="color:blue">537</span>
<span style="color:blue">QuoteType</span>
<span style="color:blue">N</span>
<span style="color:blue">N4</span>
<span style="color:blue">1=Tradeable</span> <span style="color:blue">，表示可交易的报价</span>
<span style="color:blue">当报价是对询价请求的响应时，填写转发询价请求的</span>
<span style="color:blue">131</span>
<span style="color:blue">QuoteReqID</span>
<span style="color:blue">N</span>
<span style="color:blue">C18</span>
<span style="color:blue">QuoteReqID</span> <span style="color:blue">或公开报价行情中的</span> <span style="color:blue">QuoteID</span>
1166
QuoteMsgID
客户报价消息编号，类似 CIOrderID 会员内部编号
Y
C10
41
OrigClOrdID
被撤订单的 QuoteMsgID
N
C10
订单所有者类型
522
OwnerType
Y
N3
1= 个人投资者
58

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
C12
132
BidPx
买报价 BidSize>0 时必须填写（表示报价发起方买）
N
price
133
OfferPx
卖报价 OfferSize>0 时必须填写（表示报价发起方卖） N
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
1138
DisplayQty
冰山订单数量
N
quantity
是否匿名
0= 显名
1091
PreTradeAnonymity
N
C1
1= 匿名
8418
FullAmountTrade
是否全额成交： 1= 是， 2= 否。
N
C1
结算方式： 1= 净额结算， 2=RTGS 结算。
担保券可填 1 或 2 ；非担保券只能为 2 。特别地，对于
63
SettlType
N
C1
公募可转债或公募 REITs ，只能填 1 。
结算场所： 1= 中国结算， 2= 中央结算
双边托管券，可填 1 或 2 ，单边托管券只能填其实际
207
SecurityExchange
N
C1
托管方。目前仅可填 1 。
预留字段，暂不启用。
结算周期：
0 = T+0
1 = T+1
10216
SettlPeriod
N
C1
2 = T+2
3 = T+3
预留字段，暂不启用
<span style="color:blue">62</span>
<span style="color:blue">ValidUntilTime</span>
<span style="color:blue">报价有效时间，预留字段，暂不启用</span>
<span style="color:blue">N</span>
<span style="color:blue">ntime</span>
报价接收方参与人个数
10300
NoCounterpartyParticipant
N
N10
撤单时不适用。
103
→
CounterpartyParticipantCode
报价接收方参与人代码，支持特殊符号 ’-’
N
C12
01
59

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
参与方个数，取值 =8 ，后接重复组，依次包含报价发
起方的投资者账户、业务交易单元代码、营业部代码、
交易员一债通账户、投资者中国结算开放式基金账户、
453
NoPartyIDs
Y
N2
投资者中国结算交易账户、销售人代码、券商网点号
码。
发起方投
448
PartyID
报价发起方投资者帐户
Y
C13
资者账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起方投资者帐户
Y
N4
报价发起方业务交易单元代码，填写 5 位业务交易单
448
PartyID
发起方业
Y
C8
元号。
务交易单
取 1 ，表示当前 PartyID 的取值为发起方业务交易单元
452
PartyRole
元号
Y
N4
号。
448
PartyID
报价发起方营业部代码
<span style="color:blue">NY</span>
C8
发起方营
取 4001 ，表示当前 PartyID 的取值为报价发起方的营
452
PartyRole
业部代码
<span style="color:blue">NY</span>
N4
业部代码。
448
PartyID
报价发起方交易员一债通账户
N
C10
发起方交
易员一债
取 101 ，表示当前 PartyID 的取值为发起方的交易员一
452
PartyRole
N
N4
通账户
债通账户
投资者中
448
PartyID
投资者场外开放式基金账户
N
C12
国结算开
取 4010 ，表示当前 PartyID 的取值为发起方的场外开
放式基金
452
PartyRole
N
N4
放式基金账户。
账户
投资者中
448
PartyID
投资者中国结算交易账户
N
C17
国结算交
取 4011 ，表示当前 PartyID 的取值为发起方的场外交
452
PartyRole
N
N4
易账户
易账户。
销售人代
448
PartyID
销售人代码
N
C9
码
452
PartyRole
取 117 ，表示当前 PartyID 的取值为发起方的销售代码。 N
N4
448
PartyID
券商网点号码
N
C9
券商网点
取 81 ，表示当前 PartyID 的取值为发起方的客户端编
号码
452
PartyRole
N
N4
码或网点号码。
说明：
60

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
1 、基金通询价交易（ ApplID=600022 ）时，投资者中国结算开放式基金账户、投资者中国结算交易账
户、销售人代码、券商网点号码 <span style="color:blue">、营业部代码</span> 为必填。
2 、报价消息体中支持以下报价方式，其中确定报价支持双边报价（双边报价撤销时需要同时撤销，
也即 BidSize 和 OfferSize 均填 0 ），其他业务仅支持单边报价。
报价方式
BidSize （ 134 ）
OfferSize （ 135 ）
买报价
>0
=0
卖报价
=0
>0
双边报价
>0
>0
撤销报价
=0
=0
3 、对于确定报价、一债通询价和待定报价，发起方交易员 <span style="color:blue">一债通账户</span> 必填， TransactTime 选填，其
他非必填字段要求如下 <span style="color:blue">，未提及的非必填字段对该业务无效</span> ：
业务类型（ ApplID ）
申报填写说明
撤单填写说明
确定报价（ 600180 ） 1. SettlType 、 FullAmountTrade 、 PreTradeAnonymity 必填
1. BidSize 和
2. NoCounterpartyParticipant 必填，可填 [0,5] ， 0 表示发送给全市场；
OfferSize 参照说
如指定范围发送， CounterpartyParticipantCode 必填
明 2 填写
3. DisplayQty 选填，需要为最小变动单位的正整数倍； DisplayQty
2. OrigClOrdID
有效
和 FullAmountTrade=1 不可同时申报。如指定范围发送，不支持冰
山订单
4. 支持双边报价： BidPx/BidSize 和 OfferPx/OfferSize 需要至少填
写一对
一
债
通
询
价
1. QuoteReqID 必填
（ 600190 ）
2. BidPx/BidSize 和 OfferPx/OfferSize 需要填写其中一对，例如询
价请求中 Side 为买，此处应当填 OfferPx 和 OfferSize
待定报价（ 600200 ） 1. QuoteReqID 必填
2. BidSize 或 OfferSize 中的任一个必填，如如询价请求中 Side 为
买，此处应当填 OfferSize
4 、对于确定报价或待定报价，如在限定范围内发布，将拆分为两笔子订单转发给对手方；如全市场
发布，则拆分为两笔子订单通过逐笔行情对外发布。
61

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.4.2.5 报价状态回报（ Quote Status Report, MsgType=AI ）
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
执行报告编号，从 1 开始连续递增编号
Y
N16
1180
ApplID
业务类型
Y
C6
1166
QuoteMsgID
客户报价消息编号，类似 CIOrderID 会员内部编号
Y
C10
41
OrigClOrdID
被撤单订单的 QuoteMsgID
N
C10
申报来源
0 = 网页端申报
2405
ExecMethod
N
C1
1 = 接口端（ TDGW ）申报
117
QuoteID
报价请求编号
Y
C18
当报价是对询价请求的响应时，填写转发询价请求
131
QuoteReqID
N
C18
的 QuoteReqID 或公开报价行情中的 QuoteID
报价类别
537
QuoteType
N
N4
1=Tradeable ，表示可交易的报价
订单所有者类型
1= 个人投资者
522
OwnerType
Y
N3
103= 机构投资者
104= 自营交易
报价状态
0=Accepted ，接受
4=Cancelled ，已撤销
297
QuoteStatus
N
C1
5=Rejected ，拒绝
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
C12
132
BidPx
买报价
N
price
62

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
133
OfferPx
卖报价
N
price
134
BidSize
买数量，撤单时表示买入剩余数量
N
quantity
135
OfferSize
卖数量，撤单时表示卖出剩余数量
N
quantity
交易所订单编号
QuoteStatus=0 时为交易所订单编号， QuoteStatus=4
37
OrderID
N
C16
时为被撤报价单交易所订单编号
17
ExecID
执行编号
N
C16
62
ValidUntilTime
报价失效时间，预留字段，暂不启用
N
ntime
参与方个数，取值 = <span style="color:blue">9</span> ，后接重复组，依次包含报价
发起方的 <span style="color:blue">登录或订阅交易单元、</span> 投资者账户 <span style="color:blue">、</span> 业务
交易单元代码、营业部代码、交易员一债通账户、
453
NoPartyIDs
Y
N2
投资者中国结算开放式基金账户、投资者中国结算
交易账户、销售人代码、券商网点号码。
<span style="color:blue">发起方</span>
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">发起方登录或订阅交易单元（除基金通外必填）。</span>
<span style="color:blue">N</span>
<span style="color:blue">C8</span>
<span style="color:blue">交易单</span>
<span style="color:blue">取</span> <span style="color:blue">17</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为登录或订阅交易</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">N</span>
<span style="color:blue">N4</span>
<span style="color:blue">元</span>
<span style="color:blue">单元。</span>
发起方
448
PartyID
报价发起方投资者帐户
Y
C13
投资者
取 5 ，表示当前 PartyID 的取值为发起方投资者帐
452
PartyRole
Y
N4
账户
户
发起方
报价发起方业务交易单元代码，填写 5 位业务交易
448
PartyID
Y
C8
单元号。
业务交
易单元
取 1 ，表示当前 PartyID 的取值为发起方业务交易
452
PartyRole
Y
N4
号
单元号。
发起方
448
PartyID
交易员一债通账户
N
C10
交易员
取 101 ，表示当前 PartyID 的取值为发起方的交易
452
PartyRole
N
N4
一债通
员一债通账户
账户
发起方
448
PartyID
报价发起方营业部代码
<span style="color:blue">NY</span>
C8
营业部
取 4001 ，表示当前 PartyID 的取值为报价发起方的
452
PartyRole
<span style="color:blue">NY</span>
N4
代码
营业部代码。
63

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
投资者
448
PartyID
投资者场外开放式基金账户
N
C12
中国结
算开放
取 4010 ，表示当前 PartyID 的取值为发起方的场外
452
PartyRole
N
N4
式基金
开放式基金账户。
账户
投资者
448
PartyID
投资者中国结算交易账户
N
C17
中国结
取 4011 ，表示当前 PartyID 的取值为发起方的场外
算交易
452
PartyRole
N
N4
交易账户。
账户
448
PartyID
销售人代码
N
C9
销售人
取 117 ，表示当前 PartyID 的取值为发起方的销售代
代码
452
PartyRole
N
N4
码。
448
PartyID
券商网点号码
N
C9
券商网
取 81 ，表示当前 PartyID 的取值为发起方的客户端
点号码
452
PartyRole
N
N4
编码或网点号码。
说明：
<span style="color:blue">1</span> <span style="color:blue">、</span> 对于基金通询价， SecurityID （ 48 ）左数前六位有效， ExecID （ 17 ）左数前 10 位有效，且均不补空格。
<span style="color:blue">2</span> <span style="color:blue">、对于以下业务，响应中的</span> <span style="color:blue">QuoteID</span> <span style="color:blue">字段，如申报为报价，填写交易所唯一化处理后的报价请求</span> <span style="color:blue">ID</span> <span style="color:blue">；如</span>
<span style="color:blue">申报为报价回复，且回复中填写了</span> <span style="color:blue">QuoteID</span> <span style="color:blue">，则响应中与申报时填写字段相同。发起方交易单元、发起方</span>
<span style="color:blue">交易员一债通账户、</span> <span style="color:blue">TransactTime</span> <span style="color:blue">、</span> <span style="color:blue">QuoteStatus</span> <span style="color:blue">、</span> <span style="color:blue">ExecMethod</span> <span style="color:blue">有效；</span> <span style="color:blue">申报或撤单成功时，</span> <span style="color:blue">OrderID</span> <span style="color:blue">有效；订</span>
<span style="color:blue">单被拒绝时，</span> <span style="color:blue">QuoteRequestRejectReason</span> <span style="color:blue">有效。其他非必填字段要求如下，未提及的非必填字段对该业务无</span>
<span style="color:blue">效：</span>
<span style="color:blue">业务类型</span>
<span style="color:blue">报价回报填写说明</span>
<span style="color:blue">报价回复回报填写说明</span>
<span style="color:blue">报价撤单填写说明</span>
<span style="color:blue">（</span> <span style="color:blue">ApplID</span> <span style="color:blue">）</span>
<span style="color:blue">确定报价</span>
<span style="color:blue">BidSize</span> <span style="color:blue">或</span> <span style="color:blue">OfferSize</span> <span style="color:blue">同</span>
<span style="color:blue">BidPx</span> <span style="color:blue">、</span> <span style="color:blue">BidSize</span> <span style="color:blue">、</span> <span style="color:blue">OfferPx</span> <span style="color:blue">、</span> <span style="color:blue">OfferSize</span>
<span style="color:blue">1.</span> <span style="color:blue">OrigClOrdID</span> <span style="color:blue">有效；</span>
<span style="color:blue">（</span> <span style="color:blue">600180</span> <span style="color:blue">）</span>
<span style="color:blue">同申报信息</span>
<span style="color:blue">OrderQty</span>
<span style="color:blue">2.</span> <span style="color:blue">撤单成功时</span> <span style="color:blue">BidSize</span> <span style="color:blue">、</span>
<span style="color:blue">一债通询价</span>
<span style="color:blue">OfferSize</span> <span style="color:blue">有效表示剩余</span>
<span style="color:blue">/</span>
<span style="color:blue">QuoteReqID</span> <span style="color:blue">、</span> <span style="color:blue">BidPx</span> <span style="color:blue">、</span> <span style="color:blue">BidSize</span> <span style="color:blue">、</span>
<span style="color:blue">OfferPx</span> <span style="color:blue">、</span> <span style="color:blue">OfferSize</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">（</span> <span style="color:blue">600190</span> <span style="color:blue">）</span>
<span style="color:blue">数量，否则无效。</span>
<span style="color:blue">待定报价</span>
<span style="color:blue">/</span>
<span style="color:blue">QuoteReqID</span> <span style="color:blue">、</span> <span style="color:blue">BidSize</span> <span style="color:blue">、</span> <span style="color:blue">OfferSize</span> <span style="color:blue">同</span>
<span style="color:blue">（</span> <span style="color:blue">600200</span> <span style="color:blue">）</span>
<span style="color:blue">申报信息</span>
64

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.4.2.6 转发报价（ Allege Quote, MsgType=S ）
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
执行报告编号，从 1 开始连续递增编号
Y
N16
1180
ApplID
业务类型
Y
C6
报价类别
537
QuoteType
N
N4
1=Tradeable ，表示可交易的报价
当报价是对询价请求的响应时，填写询价请求的
131
QuoteReqID
N
C18
QuoteReqID 或公开报价行情中的 OrderID
QuoteReqID 对应的会员内部编号，不适用于基金通
11
ClOrdID
N
C10
询价
117
QuoteID
报价请求编号，交易所唯一化处理后的报价请求 ID
Y
C18
订单所有者类型
1= 个人投资者
522
OwnerType
N
N3
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
C12
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
C16
8418
FullAmountTrade
是否全额成交： 1= 是， 2= 否。
N
C1
63
SettlType
结算方式： 1= 净额结算， 2=RTGS 结算
N
C1
结算场所： 1= 中国结算， 2= 中央结算
207
SecurityExchange
N
C1
预留字段，暂不启用。
10216
SettlPeriod
结算周期：
N
C1
65

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
0 = T+0
1 = T+1
2 = T+2
3 = T+3
预留字段，暂不启用。
62
ValidUntilTime
报价失效时间，预留字段，暂不启用
N
ntime
参与方个数，取值 = <span style="color:blue">8</span> ，后接重复组，依次包含 <span style="color:blue">登录</span>
<span style="color:blue">或订阅交易单元、</span> 报价发起方的投资者账户、交易
员一债通账户、对手方交易参与人机构代码、发起
453
NoPartyIDs
Y
N2
方的投资者中国结算开放式基金账户、投资者中国
结算交易账户、销售人代码、券商网点号码。
<span style="color:blue">登录或订阅交易单元（指转发消息的接收方，除基</span>
<span style="color:blue">登录或订</span>
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">N</span>
<span style="color:blue">C8</span>
<span style="color:blue">金通外必填）</span>
<span style="color:blue">阅交易单</span>
<span style="color:blue">取</span> <span style="color:blue">17</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为登录或订阅交易</span>
<span style="color:blue">元</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">N</span>
<span style="color:blue">N4</span>
<span style="color:blue">单元。</span>
发起方投
448
PartyID
报价发起方投资者帐户
N
C13
资者账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起方投资者帐户
N
N4
448
PartyID
报价发起方交易员一债通账户
N
C10
发起方交
易员一债
取 101 ，表示当前 PartyID 的取值为发起方的交易员
452
PartyRole
N
N4
通账户
一债通账户
对手方
448
PartyID
对手方交易参与人机构代码，支持特殊符号‘ - ’
N
C12
机构代
取 37 ，表示当前 PartyID 的取值为对手方的交易参
452
PartyRole
N
N4
码
与人代码
投资者中
448
PartyID
投资者场外开放式基金账户
N
C12
国结算开
取 4010 ，表示当前 PartyID 的取值为发起方的场外
放式基金
452
PartyRole
N
N4
开放式基金账户。
账户
投资者中
448
PartyID
投资者中国结算交易账户
N
C17
国结算交
取 4011 ，表示当前 PartyID 的取值为发起方的场外
452
PartyRole
N
N4
易账户
交易账户。
66

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
448
PartyID
销售人代码
N
C9
销售人代
取 117 ，表示当前 PartyID 的取值为发起方的销售代
码
452
PartyRole
N
N4
码。
448
PartyID
券商网点号码
N
C9
券商网点
取 81 ，表示当前 PartyID 的取值为发起方的客户端
号码
452
PartyRole
N
N4
编码或网点号码。
<span style="color:blue">说明：</span>
<span style="color:blue">1</span> <span style="color:blue">、确定报价（</span> <span style="color:blue">600180</span> <span style="color:blue">）、一债通询价（</span> <span style="color:blue">600190</span> <span style="color:blue">）、待定报价（</span> <span style="color:blue">600200</span> <span style="color:blue">）时，发起方交易员一债通账</span>
<span style="color:blue">户、对手方机构代码必填。如询价方或报价方选择‘匿名’且为‘净额结算’时，发起方交易员一债通账</span>
<span style="color:blue">户、发起方投资者账户（如有）填‘</span> <span style="color:blue">anonymous</span> <span style="color:blue">’。</span>
2 、 <span style="color:blue">转发信息字段与被转发字段相同，对于业务无效字段，不进行转发。</span>
4.4.2.7 报价回复（ Quote Response, MsgType=AJ ）
标签
字段名
字段描述
必须
类型
消息头
MsgType=AJ
1180
ApplID
业务类型
Y
C6
11
ClOrdID
会员内部编号
Y
C10
报价类别
537
QuoteType
N
N4
1=Tradeable ，表示可交易的报价
订单所有者类型
1= 个人投资者
522
OwnerType
Y
N3
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
C12
报价回复类型
1=Hit/Lift ，接受
694
QuoteRespType
N
C1
2=Counter ，重报（枚举值预留，暂不启用）
6=Pass ，拒绝
54
Side
买卖方向，取值有： 1 表示买， 2 表示卖
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
N
quantity
67

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
报价回复成交类型，取值：
Y=Negotiated Trade ，表示点击成交报价交易
40
OrdType
Y
C1
2=Limit ，表示匹配成交报价交易
10199
NoQuote
报价消息个数
Y
报价请求编号，交易所唯一化处理后的报价请求
->
117
QuoteID
N
C18
ID
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
报价有效时间，预留字段，暂不启用
N
ntime
参与方个数，取值 =8 ，后接重复组，依次包含报
价回复发起方的投资者账户、业务交易单元、营
业部代码、交易员一债通账户、投资者中国结算
453
NoPartyIDs
Y
N2
开放式基金账户、投资者中国结算交易账户、销
售人代码、券商网点号码。
448
PartyID
报价回复方投资者帐户
Y
C13
发起方投
取 5 ，表示当前 PartyID 的取值为发起方投资者帐
452
PartyRole
资者账户
Y
N4
户
报价回复方业务交易单元代码，填写 5 位业务交
448
PartyID
发起方业
Y
C8
易单元号。
务交易单
取 1 ，表示当前 PartyID 的取值为发起方业务交易
452
PartyRole
元号
Y
N4
单元号。
448
PartyID
报价回复方营业部代码
<span style="color:blue">NY</span>
C8
发起方营
取 4001 ，表示当前 PartyID 的取值为询价发起方
452
PartyRole
业部代码
<span style="color:blue">NY</span>
N4
的营业部代码。
448
PartyID
报价回复方交易员一债通账户
N
C10
发起方交
易员一债
取 101 ，表示当前 PartyID 的取值为发起方的交易
452
PartyRole
N
N4
通账户
员一债通账户
投资者中
448
PartyID
投资者场外开放式基金账户
N
C12
国结算开
452
PartyRole
取 4010 ，表示当前 PartyID 的取值为发起方的场
N
N4
68

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
放式基金
外开放式基金账户。
账户
投资者中
448
PartyID
投资者中国结算交易账户
N
C17
国结算交
取 4011 ，表示当前 PartyID 的取值为发起方的场
452
PartyRole
N
N4
易账户
外交易账户。
448
PartyID
销售人代码
N
C9
销售人代
取 117 ，表示当前 PartyID 的取值为发起方的销售
码
452
PartyRole
N
N4
代码。
448
PartyID
券商网点号码
N
C9
券商网点
取 81 ，表示当前 PartyID 的取值为发起方的客户
号码
452
PartyRole
N
N4
端编码或网点号码。
说明：
1 、对于基金通询价交易（ 600022 ），投资者中国结算开放式基金账户、投资者中国结算交易账户、
销售人代码、券商网点号码 <span style="color:blue">、营业部代码</span> 为必填；点击成交时报价请求编号（ QuoteID ）必填，匹配成交
时询价请求编号（ QuoteReqID ）必填；报价回复类型（ QuoteRespType ）仅可填 1 ，如未接受，超时自动失
效。
2 、对于确定报价、一债通询价和待定报价，报价回复方交易员信息必填， NoQuote 填 1 ， QuoteID 必
填， TransactTime 选填，其他非必填字段要求如下 <span style="color:blue">，未提及的非必填字段对该业务无效</span> ：
业务类型（ ApplID ）
填写说明
确定报价（ 600180 ）
OrderQty 必填； OrdType 填 ‘Y’
一债通询价（ 600190 ）
QuoteRespType 必填，仅可填 1 或 6 ，不支持填 2 ； OrdType 填 ‘Y’
待定报价（ 600200 ）
QuoteRespType 必填，仅可填 1 或 6 ，不支持填 2 ； OrdType 填 ‘Y’
4.4.2.8 转发报价回复（ Allege Quote Response, MsgType=AJ ）
标签
字段名
字段描述
必须
类型
消息头
MsgType=AJ
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
1166
QuoteMsgID
客户报价消息编号
Y
C10
69

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
报价类别
537
QuoteType
N
N4
1=Tradeable ，表示可交易的报价
订单所有者类型
1= 个人投资者
522
OwnerType
Y
N3
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
C12
报价回复类型
694
QuoteRespType
N
C1
6=Pass ，拒绝
54
Side
买卖方向，取值有： 1 表示买， 2 表示卖
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
N
quantity
报价回复成交类型，取值：
Y=Negotiated Trade ，表示点击成交报价交易
40
OrdType
Y
C1
2=Limit ，表示匹配成交报价交易
10199
NoQuote
报价消息个数
Y
->
117
QuoteID
报价请求编号，交易所唯一化处理后的报价请求 ID
N
C18
->
10225 QuotePrice 报价价格
N
price
->
10226 QuoteQty
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
报价有效时间，预留字段，暂不启用
N
ntime
参与方个数，取值 =7 ，后接重复组，依次包含登录
或订阅交易单元、报价回复方的投资者账户、交易
员一债通账户、投资者中国结算开放式基金账户、
453
NoPartyIDs
Y
N2
投资者中国结算交易账户、销售人代码、券商网点
号码。
登录或
登录或订阅交易单元（指转发消息的接收方 , 除基
448
PartyID
N
C8
金通外必填）
订阅交
易单元
452
PartyRole
取 17 ，表示当前 PartyID 的取值为登录或订阅交易
N
N4
70

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
单元。
发起方
448
PartyID
报价回复方投资者帐户
N
C13
投资者
取 5 ，表示当前 PartyID 的取值为发起方投资者帐
452
PartyRole
N
N4
账户
户
发起方
448
PartyID
报价回复方交易员一债通账户
N
C10
交易员
取 101 ，表示当前 PartyID 的取值为发起方的交易
452
PartyRole
N
N4
一债通
员一债通账户
账户
投资者
448
PartyID
投资者场外开放式基金账户
N
C12
中国结
算开放
取 4010 ，表示当前 PartyID 的取值为发起方的场外
452
PartyRole
N
N4
式基金
开放式基金账户。
账户
投资者
448
PartyID
投资者中国结算交易账户
N
C17
中国结
取 4011 ，表示当前 PartyID 的取值为发起方的场外
算交易
452
PartyRole
N
N4
交易账户。
账户
448
PartyID
销售人代码
N
C9
销售人
取 117 ，表示当前 PartyID 的取值为发起方的销售
代码
452
PartyRole
N
N4
代码。
448
PartyID
券商网点号码
N
C9
券商网
取 81 ，表示当前 PartyID 的取值为发起方的客户端
点号码
452
PartyRole
N
N4
编码或网点号码。
说明：
1 、一债通询价（ 600190 ）、待定报价（ 600200 ）时，发起方交易员一债通账户必填。如询价方或报
价方选择‘匿名’且为‘净额结算’时，发起方交易员一债通账户、发起方投资者账户（如有）填‘ anonymous ’。
2 、 <span style="color:blue">转发信息字段与被转发字段相同，对于业务无效字段，不进行转发。</span>
71

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.4.3 意向申报类
4.4.3.1 意向申报（ IOI, Indication of Interest, MsgType=6)
标签
字段名
字段描述
必填
类型
35
消息头
MsgType=6
1180
ApplID
业务类型
Y
C6
23
IOIID
会员内部编号
Y
C10
订单所有者类型
1= 个人投资者
522
OwnerType
Y
N3
103= 机构投资者
104= 自营交易
意向申报事务类型
N=New ，新申报
28
IOITransType
Y
C1
C=Cancel ，撤销申报
26
IOIRefID
原意向申报 IOIID
N
C10
54
Side
方向： 1= 买或正回购， 2= 卖或逆回购
Y
C1
48
SecurityID
证券代码
N
C12
44
Price
意向价格或回购利率
N
price
38
OrderQty
证券数量
N
quantity
8911
ExpirationDays
期限（天），可填 [1,365]
N
N4
64
SettlDate
首次结算日
N
date
231
ContractMultiplier
折算比例（ % ）
N
N <span style="color:blue">6</span> 5(2)
8504
TotalValueTraded
成交金额
N
amount
发布范围
10300
NoCounterpartyParticipant
N
N10
撤单时不适用。
→ 10301
CounterpartyParticipantCode 交易参与人机构代码，支持特殊符号‘ - ’
N
C12
60
TransactTime
业务发生时间
Y
ntime
左起顺序代表第 1 号至第 N 号篮子。例如指定 1 ，
10194
BasketID
N
C16
2 ， 5 号篮子，填 “1100100000000000”
453
NoPartyIDs
发起方重复组，依次包含发起方的交易员一债通
Y
N2
72

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
账户、投资者帐户、业务交易单元 <span style="color:blue">、营业部代码</span> 。
取值为 <span style="color:blue">4</span> 3
448
PartyID
发起方交易员一债通账户
Y
C10
取 101 ，表示当前 PartyID 的取值为发起方的交易
→
452
PartyRole
Y
N4
员一债通账户
448
PartyID
发起方投资者帐户
N
C13
取 5 ，表示当前 PartyID 的取值为发起方投资者帐
→
452
PartyRole
N
N4
户
448
PartyID
发起方业务交易单元代码
Y
C8
取 1 ，表示当前 PartyID 的取值为发起方业务交易
→
452
PartyRole
Y
N4
单元号。
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">发起方营业部代码</span>
<span style="color:blue">Y</span>
<span style="color:blue">C8</span>
<span style="color:blue">取</span> <span style="color:blue">4001</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为发起方的营</span>
<span style="color:blue">→</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">Y</span>
<span style="color:blue">N4</span>
<span style="color:blue">业部代码。</span>
<span style="color:blue">说明：</span>
非必填字段填写说明 <span style="color:blue">，未提及的非必填字段对该业务无效</span> ：
业务类型（ ApplID ）
申报
撤单
1. SecurityID 、 ExpirationDays 必填， SecurityID 表示质押券代码
2. Price 、 OrderQty 、 ContractMultiplier 、 TotalValueTraded 、 SettlDate
IOIRefID 、
协议回购意向申报
选填
SecurityID
（ 600150 ）
3. TotalValueTraded 计算方式为：债券成交金额 = 质押券数量 *10*
必填
单张质押券面值 * 折算比例 /100 ；基金成交金额 = 质押券数量 * 竞
价前收盘价 * 折算比例 /100 ，四舍五入
1. ExpirationDays 、 BasketID 必填
三方回购意向申报
2. 发起方投资者账户必填，若为正回购方，填三方回购专用帐
IOIRefID 必
户，若为逆回购方，则填写其对应普通账户
填
（ 600160 ）
3. Price 、 TotalValueTraded 选填
1. SecurityID 、 Price 必填
IOIRefID 、
债券现券意向申报
2. OrderQty 选填
SecurityID 、
（ 600170 ）
发起方投资
3. NoCounterpartyParticipant 必填，可填 [0,5] ，填 0 时表示发送
73

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
者账户必填
给全市场，否则 CounterpartyParticipantCode 必填
4. 发起方投资者账户必填
4.4.3.2 转发意向申报（ Allege IOI, MsgType=6)
标签
字段名
字段描述
必填
类型
35
消息头
MsgType=6
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
意向申报类型
694
QuoteRespType
Y
C1
1=Alleged ，转发意向申报
28
IOITransType
意向申报事务类型
Y
C1
693
QuoteRespID
交易所订单编号
Y
C16
54
Side
方向，表示申报发起方的方向
<span style="color:blue">N</span> Y
C1
48
SecurityID
证券代码
Y
C12
44
Price
意向价格
N
price
38
OrderQty
意向数量
N
quantity
60
TransactTime
业务发生时间
Y
ntime
发起方重复组，取值 =3 ，依次包含登录或订阅交易单元、
发起方的交易员一债通账户、对手方交易参与人机构代
453
NoPartyIDs
Y
N2
码。
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">登录或订阅交易单元（指转发消息的接收方）。</span>
<span style="color:blue">Y</span>
<span style="color:blue">C8</span>
<span style="color:blue">→</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">取</span> <span style="color:blue">17</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为登录或订阅交易单元。</span>
<span style="color:blue">Y</span>
<span style="color:blue">N4</span>
448
PartyID
发起方交易员一债通账户
Y
C10
取 101 ，表示当前 PartyID 的取值为发起方的交易员一债
→
452
PartyRole
Y
N4
通账户
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">对手方交易参与人机构代码，支持特殊符号‘</span> <span style="color:blue">-</span> <span style="color:blue">’</span>
<span style="color:blue">Y</span>
<span style="color:blue">C12</span>
<span style="color:blue">→</span>
<span style="color:blue">取</span> <span style="color:blue">37</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为对手方的交易参与人</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">Y</span>
<span style="color:blue">N4</span>
<span style="color:blue">代码</span>
<span style="color:blue">说明：</span>
<span style="color:blue">1</span> <span style="color:blue">、转发信息字段与被转发字段相同，对于业务无效字段，不进行转发。</span>
74

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.4.3.3 意向申报响应（ IOI Response, MsgType=AJ ）
标签
字段名
字段描述
必须
类型
消息头
MsgType = AJ
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
<span style="color:blue">意向申报事务类型</span>
<span style="color:blue">N=New</span> <span style="color:blue">，新申报</span>
<span style="color:blue">28</span>
<span style="color:blue">IOITransType</span>
<span style="color:blue">Y</span>
<span style="color:blue">C1</span>
<span style="color:blue">C=Cancel</span> <span style="color:blue">，撤销申报</span>
<span style="color:blue">订单所有者类型，取值包括：</span>
<span style="color:blue">1=</span> <span style="color:blue">个人投资者</span>
<span style="color:blue">522</span>
<span style="color:blue">OwnerType</span>
<span style="color:blue">Y</span>
<span style="color:blue">N3</span>
<span style="color:blue">103=</span> <span style="color:blue">机构投资者</span>
<span style="color:blue">104=</span> <span style="color:blue">自营交易</span>
<span style="color:blue">60</span>
<span style="color:blue">TransactTime</span>
<span style="color:blue">回报时间</span>
<span style="color:blue">Y</span>
<span style="color:blue">ntime</span>
<span style="color:blue">48</span>
<span style="color:blue">SecurityID</span>
<span style="color:blue">证券代码</span>
<span style="color:blue">N</span>
<span style="color:blue">C12</span>
意向申报类型
694
QuoteRespType
Y
C1
2=Replace ，意向申报响应
执行报告类型，取值有：
0=Accepted ，订单申报成功
150
ExecType
Y
C1
4=Cancelled ，订单撤销成功
8=Rejected ，订单申报拒绝
23
IOIID
会员内部订单编号
Y
C10
申报来源
0 = 网页端申报
2405
ExecMethod
Y
C1
1 = 接口端（ TDGW ）申报
54
Side
买卖方向
Y
C1
44
Price
申报价
N
price
26
IOIRefID
原始会员内部订单编号， ExecType=4 时有效
N
C10
300
QuoteRejectReason
订单拒绝码， ExecType=8 时有效
N
C5
75

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
693
QuoteRespID
交易所订单编号
Y
C16
参与方个数，取值 = <span style="color:blue">5</span> 4 ，后接重复组，依次包含登录
或订阅交易单元、发起方业务交易单元、交易员一
453
NoPartyIDs
Y
N2
债通账户、投资者账户 <span style="color:blue">、发起方营业部代码</span> 。
448
PartyID
发起方登录或订阅交易单元。
Y
C8
取 17 ，表示当前 PartyID 的取值为登录或订阅交易
→
452
PartyRole
Y
N4
单元。
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">发起方投资者帐户，协议回购意向申报时不适用</span>
<span style="color:blue">N</span>
<span style="color:blue">C13</span>
<span style="color:blue">→</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">取</span> <span style="color:blue">5</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为发起方投资者帐户。</span>
<span style="color:blue">N</span>
<span style="color:blue">N4</span>
448
PartyID
发起方业务交易单元。
Y
C8
取 1 ，表示当前 PartyID 的取值为发起方业务交易单
→
452
PartyRole
Y
N4
元。
448
PartyID
发起方交易员一债通账户
Y
C10
取 101 ，表示当前 PartyID 的取值为发起方的交易员
→
452
PartyRole
Y
N4
一债通账户
<span style="color:blue">说明：</span>
<span style="color:blue">非必填字段填写说明，</span> <span style="color:blue">QuoteRejectReason</span> <span style="color:blue">当订单申报拒绝时有效，未提及的非必填字段对该业务无效：</span>
<span style="color:blue">业务类型（</span> <span style="color:blue">ApplID</span> <span style="color:blue">）</span>
<span style="color:blue">申报</span>
<span style="color:blue">撤单</span>
<span style="color:blue">协议回购意向申报</span>
<span style="color:blue">IOIRefID</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">同申报</span>
<span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">Price</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">信息</span>
<span style="color:blue">（</span> <span style="color:blue">600150</span> <span style="color:blue">）</span>
<span style="color:blue">三方回购意向申报</span>
<span style="color:blue">发起方投资者账户、</span> <span style="color:blue">Price</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">IOIRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">（</span> <span style="color:blue">600160</span> <span style="color:blue">）</span>
<span style="color:blue">债券现券意向申报</span>
<span style="color:blue">IOIRefID</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、发起</span>
<span style="color:blue">（</span> <span style="color:blue">600170</span> <span style="color:blue">）</span>
<span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">Price</span> <span style="color:blue">、发起方投资者账户同申报信息</span>
<span style="color:blue">方投资者账户同申报信息</span>
76

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.4.4 成交申报类
4.4.4.1 成交申报（ Trade Capture Report, MsgType=AE)
必
标签
字段名
字段描述
类型
填
35
消息头
MsgType=AE
1180
ApplID
业务类型
Y
C6
828
TrdType
业务子类型，见附表
N
C3
<span style="color:blue">571</span>
<span style="color:blue">TradeReportID</span>
<span style="color:blue">会员内部编号</span>
<span style="color:blue">Y</span>
<span style="color:blue">C10</span>
成交申报类型
0=Submit ，提交成交申报
856
TradeReportType
Y
C1
2=Accept ，确认成交申报
3=Decline ，拒绝成交申报
成交申报事务类别
0=New ，新申报
487
TradeReportTransType
Y
C1
1=Cancel ，撤销申报
2=Replace ，响应
订单所有者类型
1= 个人投资者
522
OwnerType
Y
N3
103= 机构投资者
104= 自营交易
原始交易会员内部编号，表示被撤消订单的会员内
572
TradeReportRefID
N
C10
部编号
买卖方向： 1= 买， 2= 卖
对于回购： 1= 正回购， 2= 逆回购
54
Side
Y
C1
对于借贷： F= 出借， G= 借入
对于合并申报且 TradeReportType 为 0 时：填 0
申报价格（元）或回购利率（ % ）或借贷费率（ % ）
44
Price
N
price
合并申报时代表买入价格
640
Price2
申报价格 2
N
price
77

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
合并申报时代表卖出价格（元）
455
SecurityAltID
辅助证券代码
N
C12
<span style="color:blue">60</span>
<span style="color:blue">TransactTime</span>
<span style="color:blue">业务发生时间</span>
<span style="color:blue">Y</span>
<span style="color:blue">ntime</span>
<span style="color:blue">8504</span>
<span style="color:blue">TotalValueTraded</span>
<span style="color:blue">总成交金额</span>
<span style="color:blue">N</span>
<span style="color:blue">amount</span>
8903
DeliveryQty
证券交付数量
N
quantity
8911
ExpirationDays
期限（天），可填 [1,365]
N
N4
64
SettlDate
首次结算日
N
date
541
MaturityDate
到期日
N
date
193
SettlDate2
到期结算日
N
date
915
AgreementDate
协议日期
N
date
8847
UAInterestAccrualDays
实际占款天数，可填 [1,365]
N
N3
累计利息总额，代表总回购利息或债券借贷标的券
TotalAccruedInterestA
540
N
amount
应计利息总额
mt
10330
TotalSettlCurrAmt
总到期结算金额
N
amount
580
NoDates
违约宽限期（天）， [0,365] 。
N
N3
订单限制
对于协议回购表示 “ 是否同意在违约情形下由质权
方对该违约交易项下的质押券直接以拍卖、变卖等
方式进行处置 ” ；对于三方回购表示 “ 违约后担保品
529
OrderRestrictions
N
Boolean
是否由质权人处置 ” 。
Y = 是
N = 否
结算场所： 1= 中国结算， 2= 中央结算
双边托管券，可填 1 或 2 ，单边托管券只能填其实
207
SecurityExchange
N
C1
际托管方。
预留字段，暂不启用。
结算周期：
0 = T+0
10216
SettlPeriod
N
C1
1 = T+1
2 = T+2
78

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3 = T+3
预留字段，暂不启用
结算方式： 1= 净额结算， 2=RTGS 结算。
担保券可填 1 或 2 ；非担保券只能为 2 。特别地，
63
SettlType
N
C1
对于公募可转债或公募 REITs ，只能填 1 。
146
NoRelatedSym
合约结算个数
N
N1
合约相关编号
1= 代表当前合约，债券借贷代表当前合约或到期续
→
655
ContraLegRefID
N
C1
做时的原合约
2= 代表新合约，债券借贷代表到期续做时的新合约
结算形式
0 = 现金，债券借贷代表现金结算
→
668
DeliveryForm
N
C3
2 = 实物，债券借贷代表债券结算
101 = 其他，债券借贷代表部分现金结算
资金结算方式
1 = 场内结算
→
172
SettlDeliveryType
N
C1
2 = 场外结算
→
510
NoDistribInsts
交收账户重复组个数
N
N1
F= 出借方
→
→
624
LegSide
N
C1
G= 借入方
→
→
498
CashDistribAgentName
资金交收机构名称，债券借贷代表资金开户行
N
C75
→
→
499
CashDistribAgentCode
资金交收机构代码，债券借贷代表支付系统行号
N
C18
CashDistribAgentAcctN
→
→
500
资金账户
N
C22
umber
CashDistribAgentAcctN
→
→
502
资金账户名称
N
C87
ame
左起顺序代表第 1 号至第 N 号篮子。例如指定 1 ， 2 ，
10194
BasketID
N
C16
5 号篮子，填 “1100100000000000”
711
NoUnderlyings
证券个数
N
N2
→
865
EventType
操作标识
N
C2
79

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
21= 换入 / 补入券
22= 换出券
→
48
SecurityID
证券代码
N
C12
→
38
OrderQty
证券数量
N
quantity
份额类型
0 = 限售
→
10331
ShareProperty
N
C1
1 = 非限售
→
10332
RestrictedMonth
限售期（月），指初始登记限售期
N
N4
→
231
ContractMultiplier
折算比例（ % ）
N
N <span style="color:blue">6</span> 5(2)
→
152
CashOrderQty
质押券面值总额
N
amount
→
381
GrossTradeAmt
成交金额
N
amount
→
159
AccruedInterestAmt
回购利息
N
amount
→
119
SettlCurrAmt
到期结算金额
N
amount
→
880
TrdMatchID
辅助交易编号
N
C18
192
OrderQty2
本期回购结算利息
N
amount
到期续做类型
N = 非第三方续做（原对手方）
829
TrdSubType
N
C1
Y = 第三方续做（新对手方）
1125
OrigTradeDate
原成交日期， YYYYMMDD
N
date
当 TradeReportType 为 0 时，如为非首期合约，表
示原合约成交编号；
19
ExecRefID
N
C16
当 TradeReportType 为 2 或 3 时，表示待确认（拒
绝）的申报的交易所订单编号。
10248
MemoEx
扩展备注，支持中文
N
C96
58
Text
用户私有信息
N
C32
发起方重复组，依次包含发起方交易员一债通账
户、业务单元、 <span style="color:blue">营业部代码、</span> 投资者账户、对手方
453
NoPartyIDs
Y
N2
交易员一债通账户 1 、对手方交易员一债通账户 2 。
取值为 5
→
448
PartyID
发起方交易员一债通账户
Y
C10
80

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
取 101 ，表示当前 PartyID 的取值为发起方的交易
452
PartyRole
Y
N4
员一债通账户
448
PartyID
发起方业务交易单元代码
Y
C8
→
取 1 ，表示当前 PartyID 的取值为发起方业务交易
452
PartyRole
Y
N4
单元号。
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">发起方营业部代码</span>
<span style="color:blue">Y</span>
<span style="color:blue">C8</span>
<span style="color:blue">取</span> <span style="color:blue">4001</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为发起方的营业</span>
<span style="color:blue">→</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">Y</span>
<span style="color:blue">N4</span>
<span style="color:blue">部代码。</span>
发起方投资者帐户， TradeReportType 为 0 或 2 时
448
PartyID
N
C13
必填。
→
取 5 ，表示当前 PartyID 的取值为发起方投资者帐
452
PartyRole
N
N4
户
对手方交易员一债通账户 1 ，当合并申报时表示买
448
PartyID
Y
C10
方交易员一债通账户
→
取 102 ，表示当前 PartyID 的取值为对手方的交易
452
PartyRole
Y
N4
员一债通账户
对手方交易员一债通账户 2 ，仅合并申报发起时有
448
PartyID
N
C10
效表示卖方交易员。其他申报无意义。
→
452
PartyRole
取 57 ，表示当前的 PartyID 的取值为合并申报卖方
N
N4
约定号， TradeReportType=0 时可以填写，用于对
手方定位订单信息。仅可填大小写英文字母或数
664
ConfirmID
N
C12
字。
10198
Memo
可填写补充约定或备注，支持中文
N
C600
说明：
1 、业务申报填写说明 <span style="color:blue">，未提及的非必填字段对该业务无效</span>
ApplID
TrdType
描述
填写说明
81

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
ApplID
TrdType
描述
填写说明
131
协商成交
1. Price 必填，表示回购利率； ExpirationDays 必填，表示回购期限；
SettlDate 必填，填当前交易日
2. MaturityDate 、 SettlDate2 和 UAInterestAccrualDays 必填，其中回
购到期日 = 当前交易日 + 回购期限；到期结算日 = 首次结算日 + 实际占
款天数
3. NoDates 、 OrderRestrictions 必填
4. NoUnderlyings 必填，可填 [1,10] ， SecurityID/OrderQty 填写对应
质押券代码和数量；如质押券为公募 REITs ，需要填写
ShareProperty ，如为公募 REITs 限售份额，需填写 RestrictedMonth ，
指初始登记或扩募登记时中国结算提供的“挂牌年份”字段。批量
申报时 N 支质押券将收到 N 笔响应，允许部分成功， N 笔申报将分
别转发至对手方逐一确认，确认后将生成 N 笔成交，确认一笔，成
交一笔。批量申报时各支质押券不可重复。
5. ContractMultiplier （折算比例）、 CashOrderQty （面值总额）、
GrossTradeAmt （成交金额）、 AccruedInterestAmt （回购利息）和
SettlCurrAmt （到期结算金额）必填，均为正数，保留两位小数，四
舍五入，其中：
协议回购
（ 600130 ）
债券面值总额 = 质押券数量 ×10× 单张质押券面值
基金或 REITs 面值总额 = 质押券数量 * 前收盘价
成交金额 = 面值总额 × 折算比例 /100
回购利息 = 成交金额 × 回购利率 /100× 实际占款天数 /365
到期结算金额 = 成交金额 + 回购利息
6. Text 、 ConfirmID 、 Memo 选填；特别地，当利率大于 5% 时， Memo
必填，填写此利率的合理性说明。
1. NoUnderlyings 填 1 ， SecurityID/OrderQty 填写对应质押券代码和
数量
132
到期确认
2. OrigTradeDate 、 ExecRefID 必填
3. Text 、 Memo 选填
1. Price 必填，表示新回购利率； ExpirationDays 必填，表示新回购
期限； SettlDate 必填，填当前交易日
2. MaturityDate 、 SettlDate2 和 UAInterestAccrualDays 必填，其中新
回购到期日 = 当前交易日 + 新回购期限；新到期结算日 = 首次结算日 +
新实际占款天数
3. NoDates 、 OrderRestrictions 、 OrderQty2 （精确到小数点后两位）、
TrdSubType 必填
133
到期续做 *
4. NoUnderlyings 填 1 ， SecurityID/OrderQty 表示对应质押券代码和
数量；如质押券为公募 REITs ， ShareProperty 必填，限售份额不可
续做； <span style="color:blue">，为公募</span> <span style="color:blue">REITs</span> <span style="color:blue">限售份额，</span> <span style="color:blue">RestrictedMonth</span>
5. ContractMultiplier 、 CashOrderQty 、 GrossTradeAmt 、
AccruedInterestAmt 和 SettlCurrAmt 必填，表示新合约相关参数，计
算方式同协商成交申报
6. OrigTradeDate 、 ExecRefID 必填， Text 、 ConfirmID 、 Memo 选填；
特别地，当利率大于 5% 时， Memo 必填，填写此利率的合理性说明。
82

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
ApplID
TrdType
描述
填写说明
1. Price 必填，表示实际回购利率， ExpirationDays 、
UAInterestAccrualDays 、 AccruedInterestAmt 和 SettlCurrAmt 必填，
表示提前终止后的相应值
134
提前终止
2. NoUnderlyings 填 1 ， SecurityID/OrderQty 表示对应质押券代码和
数量
3. OrigTradeDate 、 ExecRefID 必填， Text 、 ConfirmID 、 Memo 选填
1. NoUnderlyings 填 2 ， EventType 必填
2. EventType 为 21 时， SecurityID/OrderQty 填换入券代码和数量，
如换入券为公募 REITs ，需要填写 ShareProperty （仅可填 1 ），
135
换券申报
ContractMultiplier （折算比例）、 CashOrderQty （面值总额）、
GrossTradeAmt （成交金额）必填，换入券的成交金额应当与换出券
相等； EventType 为 22 时， SecurityID 必填，表示被换出券。
3. OrigTradeDate 、 ExecRefID 必填， Text 、 ConfirmID 、 Memo 选填
1. NoUnderlyings 填 1 ， SecurityID/OrderQty 表示对应质押券代码和
数量
136
解除质押
2. OrigTradeDate 、 ExecRefID 必填， Text 、 ConfirmID 、 Memo 选填
不适用
到期续做
前期合约
137
了结
138
到期续做
合约新开
不适用
141
协商成交
三方回购
（ 600140 ）
1. Price 必填，表示回购利率； ExpirationDays 必填，表示回购期限；
SettlDate 必填，填当前交易日
<span style="color:blue">2.</span> TotalValueTraded 、 MaturityDate 、 SettlDate2 和
UAInterestAccrualDays 必填，其中回购到期日 = 当前交易日 + 回购期
限；到期结算日 = 首次结算日 + 实际占款天数
3. OrderRestrictions 、 BasketID 必填
4. NoUnderlyings 选填，可填 [1,3] ， SecurityID/OrderQty 填写对应质
押券代码和数量，质押券应当属于已选择的篮子
5. TotalAccruedInterestAmt （回购利息）和 TotalSettlCurrAmt （到期
结算金额）必填，均为正数，保留两位小数，四舍五入，其中：
回购利息 = 成交金额 × 回购利率 /100× 实际占款天数 /365
到期结算金额 = 成交金额 + 回购利息
6. 发起方投资者账户必填，填三方回购专用账户；对手方接受时填
写普通账户
7. Text 、 ConfirmID 、 Memo 选填
142
到期购回
1. OrigTradeDate 、 ExecRefID 必填
2. Text 选填
83

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
ApplID
TrdType
描述
填写说明
1. Price 必填，表示新回购利率； ExpirationDays 必填，表示新回购
期限； SettlDate 必填，填当前交易日
2. TotalValueTraded 、 MaturityDate 、 SettlDate2 和
UAInterestAccrualDays 必填，其中新回购到期日 = 当前交易日 + 新回
购期限；新到期结算日 = 首次结算日 + 新实际占款天数
143
到期续做
3. BasketID 、 OrigTradeDate 、 ExecRefID 、 OrderRestrictions 必填，
TotalAccruedInterestAmt （回购利息）和 TotalSettlCurrAmt （到期结
算金额）必填，表示新合约相关参数，计算方式同协商成交申报
4. 发起方投资者账户必填，填三方回购专用账户，对手方接受时填
写普通账户
5. Text 、 ConfirmID 、 Memo 选填
1. Price 必填，表示实际回购利率
144
提前终止
2. ExpirationDays 、 UAInterestAccrualDays 、 TotalAccruedInterestAmt
和 TotalSettlCurrAmt 必填，表示提前终止后的相应值
3. OrigTradeDate 、 ExecRefID 必填， Text 、 ConfirmID 、 Memo 选填
1. NoUnderlyings 填 1 或 2 ，填 1 时表示仅换出； EventType 必填，
145
换券申报
SecurityID/OrderQty 填对应换入或换出券代码和数量；换入券和换
出券应当属于同一个篮子； EventType=22 时 TrdMatchID 必填，表
示质押券的冻结申请书号
2. OrigTradeDate 、 ExecRefID 必填， Text 、 ConfirmID 选填
146
解除质押
1. OrigTradeDate 、 ExecRefID 必填
2. Text 、 ConfirmID 、 Memo 选填
1. NoUnderlyings 填 1 ， SecurityID/OrderQty 填对应补入券代码和数
量
147
补券申报
2. OrigTradeDate 、 ExecRefID 必填， Text 选填
1.Price 必填，表示申报价格； SettlType 、 ConfirmID 必填
2.NoUnderlyings 填 1 ， SecurityID/OrderQty 填写交易券代码和数量
成交
现券协商成
交（ 600210 ）
不适用
现券协商
3.Text 、 Memo 选填
1. Price 、 Price2 必填，分别表示买入价格和卖出价格
合并申报 *
（ 600220 ）
不适用
合并申报
2. SettlType 必填， Side 填 0
3. NoUnderlyings 填 1 ， SecurityID/OrderQty 填写交易券代码和数量
4. 对手方交易员一债通账户 2 和投资者账户必填， Text 选填
1. Price 必填，表示借贷费率
2. ExpirationDays 、 SettlDate 、 SettlDate2 必填，其中 ExpirationDays
表示借贷期限， SettlDate 填当前交易日，到期结算日 = 首次结算日 +
债券借贷
（ 600300 ）
301
协商成交
借贷期限
3. NoRelatedSym 、 NoDistribInsts 填 1 ，发起方资金账户、资金账户
名称必填，资金开户行和支付系统行号选填
4. SecurityAltID/DeliveryQty 必填，表示标的券代码 / 数量
5. NoUnderlyings 选填，可填 [1,20] ， SecurityID/OrderQty 填写对应
质押券代码和数量
84

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
ApplID
TrdType
描述
填写说明
6. TotalAccruedInterestAmt 必填，表示标的券应计利息总额
7. AgreementDate 必填，表示标的券下一付息日； SettlDeliveryType
必填，表示到期费用结算方式； TotalValueTraded 必填，表示借贷费
用金额
8. MemoEx 选填，填写争议解决方式； Memo 选填，可填入补充约
定内容
302
到期结算
1. SettlDeliveryType 必填
2. DeliveryForm 必填，表示到期结算方式
3. ExecRefID 必填
4. SettlDeliveryType 必填， SettlDeliveryType=2 时，资金账户、资
金账户名称、资金开户行、支付系统行号必填
5. TotalSettlCurrAmt 选填，当 DeliveryForm =2 或 101 时必填，表示
现金结算金额
6. DeliveryQty 选填，当 DeliveryForm = <span style="color:blue">1</span> <span style="color:blue">或</span> 101 时必填，表示归还
标的券数量
303
到期续做
1. ExecRefID 必填
2. Price 必填，表示新借贷费率
3. ExpirationDays 、 SettlDate 、 SettlDate2 必填，其中 ExpirationDays
表示新借贷期限， SettlDate 填当前交易日，新到期结算日 = 当前交
易日 + 新借贷期限
4. 投资者账户、资金账户、资金账户名称必填
5. NoRelatedSym 填 2 ， ContraLegRefID 分别填 1 和 2 ， NoDistribInsts
填 1
6. 发起方资金账户、资金账户名称、资金开户行和支付系统行号选
填， SettlDeliveryType 为 2 时，发起方资金账户、资金账户名称、
资金开户行和支付系统行号必填
7. SecurityAltID/DeliveryQty 填写新合约标的券代码、数量
8. NoUnderlyings 选填，可填 [1,20] ， SecurityID/OrderQty 填写变更
的质押券代码和数量， EventType 填写变更类型， EventType=22 时
TrdMatchID 必填，表示质押券的冻结申请书号
9. TotalAccruedInterestAmt 必填，表示新应计利息总额；
AgreementDate 必填，表示新合约下一付息日； SettlDeliveryType 必
填，表示到期费用结算方式； TotalValueTraded 必填，表示新借贷费
用
10. MemoEx 选填，填写新争议解决方式； Memo 选填，可填入新
补充约定内容
1. SettlDeliveryType 必填
2. DeliveryForm 必填，表示到期结算方式
3. ExecRefID 必填
4. SettlDeliveryType 必填， SettlDeliveryType=2 时，资金账户、资
金账户名称、资金开户行、支付系统行号必填
304
提前终止
5. TotalSettlCurrAmt 选填，当 DeliveryForm =2 或 101 时必填，表示
现金结算金额
6. DeliveryQty 选填，当 DeliveryForm = <span style="color:blue">1</span> <span style="color:blue">或</span> 101 时必填，表示归还
标的券数量
85

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
ApplID
TrdType
描述
填写说明
7. UAInterestAccrualDays 必填，表示实际借贷期限， MaturityDate
必填，表示提前终止日
8. TotalValueTraded 必填，表示实际借贷费用金额
1. NoUnderlyings 选填，可填 [1,20] ， SecurityID/OrderQty 填写对应
质押券代码和数量， EventType 填写变更类型， EventType=22 时
305
质押券变
更申报
TrdMatchID 必填，表示质押券的冻结申请书号
2. ExecRefID 必填
306
解除质押
ExecRefID 必填
1. SettlDeliveryType 必填
2. DeliveryForm 必填，表示逾期结算方式
3. ExecRefID 必填
4. SettlDeliveryType 必填， SettlDeliveryType=2 时，资金账户、资
金账户名称、资金开户行、支付系统行号必填
307
逾期结算
5. TotalSettlCurrAmt 选填，当 DeliveryForm =2 或 101 时必填，表示
现金结算金额
6. DeliveryQty 选填，当 DeliveryForm =101 时必填，表示归还标的
券数量
7. UAInterestAccrualDays 必填，表示实际借贷期限， MaturityDate
必填，表示实际结算日
8. TotalValueTraded 必填，表示实际借贷费用金额
场务应急成
不适用
不适用
不适用，交易员无需申报订单，如交易员已绑定，绑定的交易单元
可收到成交确认
交录入
（ 600310 ）
注 1 ：对于协议回购到期续做（ TrdType: 133 ），如对手方确认后将生成两笔成交，一笔为到期续做前期合
约了结（ 137 ），另一笔为到期续做合约新开（ 138 ）。
注 2 ：对于合并申报，将拆分为两笔申报转发给两个对手方。对手双方均确认后也将生成两笔成交（对于
中间方来说），一笔为中间方与买方的成交，另一笔为中间方与卖方的成交。
注 3 ：对于债券借贷到期续做（ TrdType: 303 ） <span style="color:blue">或三方回购到期续做（</span> <span style="color:blue">TrdType: 143</span> <span style="color:blue">）</span> ，仅生成一笔成交，
该笔成交包含原合约到期结算及新开合约信息。
2 、业务撤单或确认或拒绝填写说明 <span style="color:blue">，未提及的非必填字段对该业务无效</span>
ApplID
TrdType
描述
撤单
对手方确认
对手方拒绝
ExecRefID 、 NoUnderlyings 、 Sec
ExecRefID 、
131
协商成交
TradeReportRefI
urityID 、投资者账户必填， Text
D 必填， Text 选
NoUnderlyin
协议回购
133
到期续做
选填
填。对于协议回
gs 、 SecurityI
（ 600130 ）
购、合并申报和
D 必填， Eve
134
提前终止
ExecRefID 、 NoUnderlyings 、 Sec
现券协商成交， N
ntType 换券
urityID 、投资者账户必填， Event
135
换券申报
86

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
oUnderlyings 、 Se
时必填， Text
Type 换券时必填， Text 选填
136
解除质押
选填
curityID 必填， E
ventType 换券时
141
协商成交
ExecRefID 、投资者账户必填， T
必填，内容与申
ext 选填
143
到期续做
三方回购
ExecRefID 必
报时一致；协议
144
提前终止
（ 600140 ）
填， Text 选填
ExecRefID 、投资者账户必填， T
回购批量申报撤
ext 选填
145
换券申报
单时，允许仅针
146
解除质押
对一笔或几笔质
ExecRefID 、
押券部分撤单。
ExecRefID 、 NoUnderlyings 、 Sec
NoUnderlyin
合并申报
不适用
合并申报
urityID 、投资者账户必填， Text
gs 、 SecurityI
（ 600220 ）
选填
D 必填， Text
选填
现券协商成交
不适用
协商成交
不适用
不适用
（ 600210 ）
301
协商成交
债券借贷
TradeReportRefI
ExecRefID 必
（ 600300 ）
D 必填
填
303
到期续做
ExecRefID 、对手方一债通账户、
投资者账户、交易单元必填；
协商成交时， NoRelatedSym 、 No
DistribInsts 填 1 ，资金账户、资金
账户名称必填，资金开户行、支
付系统行号选填；
到期续做时， NoRelatedSym 填 2 ，
ContraLegRefID 分别填 1 和 2 ，
NoDistribInsts 填 1 ，若 ContraLeg
RefID 填 1 ， SettlDeliveryType
填 2 时，则发起方资金账户、资
金账户名称、资金开户行和支付
系统行号必填，若 ContraLegRefI
D 填 2 时，则资金账户、资金账
户名称必填，资金开户行、支付
系统行号选填；
304
提前终止
302
到期结算
ExecRefID 必填； SettlDeliveryTy
pe=2 时对手方资金账户、资金账
户名称、资金开户行、支付系统
行号必填
307
逾期结算
306
解除质押
ExecRefID 必填
305
质押券变更
申报
87

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.4.4.2 转发成交申报（ Allege Trade Capture Report, MsgType=AE)
必
标签
字段名
字段描述
类型
填
35
消息头
MsgType=AE
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
<span style="color:blue">828</span>
<span style="color:blue">TrdType</span>
<span style="color:blue">业务子类型</span>
<span style="color:blue">N</span>
<span style="color:blue">C3</span>
1003
TradeID
交易所订单编号
Y
C16
成交申报类型
1=Alleged ，转发成交申报
856
TradeReportType
Y
C1
3=Decline ，拒绝成交申报
成交申报事务类别
0=New ，新申报
487
TradeReportTransType
Y
C1
1=Cancel ，撤销申报
被撤消订单的交易所订单编号，撤销申报
1126
OrigTradeID
N
C16
必填
表示被转发方也即本申报发起方的方向。
买卖方向： 1= 买， 2= 卖
54
Side
Y
C1
若为回购，则： 1= 正回购， 2= 逆回购
若为借贷，则： F= 出借， G= 借入
44
Price
申报价格或回购利率
N
price
455
SecurityAltID
辅助证券代码
N
C12
<span style="color:blue">60</span>
<span style="color:blue">TransactTime</span>
<span style="color:blue">订单接收时间</span>
<span style="color:blue">Y</span>
<span style="color:blue">ntime</span>
<span style="color:blue">8504</span>
<span style="color:blue">TotalValueTraded</span>
<span style="color:blue">总成交金额</span>
<span style="color:blue">N</span>
<span style="color:blue">amount</span>
8903
DeliveryQty
证券交付数量
N
quantity
8911
ExpirationDays
期限（天）
N
N4
64
SettlDate
首次结算日
N
date
541
MaturityDate
到期日
N
date
193
SettlDate2
到期结算日
N
date
88

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
915
AgreementDate
协议日期
N
date
8847
UAInterestAccrualDays
实际占款天数
N
N3
累计利息总额，代表总回购利息或债券借
TotalAccruedInterestAm
540
N
amount
贷标的券应计利息总额
t
10330
TotalSettlCurrAmt
总到期结算金额
N
amount
580
NoDates
违约宽限期（天）
N
N3
订单限制
对于协议回购表示 “ 是否同意在违约情形
下由质权方对该违约交易项下的质押券直
接以拍卖、变卖等方式进行处置 ” ；；对于
529
OrderRestrictions
N
Boolean
三方回购表示 “ 违约后担保品是否由质权
人处置 ” 。
Y= 是；
N= 否
结算场所： 1= 中国结算， 2= 中央结算
双边托管券，可填 1 或 2 ，单边托管券只能
207
SecurityExchange
N
C1
填其实际托管方。预留字段，暂不启用。
结算周期：
0 = T+0
1 = T+1
10216
SettlPeriod
N
C1
2 = T+2
3 = T+3
预留字段，暂不启用
63
SettlType
结算方式： 1= 净额结算， 2=RTGS 结算
N
C1
146
NoRelatedSym
合约结算个数
N
N1
合约相关编号
1= 代表当前合约，债券借贷代表当前合约
或到期续做时的原合约
→
655
ContraLegRefID
N
C1
2= 代表新合约，债券借贷代表续做时的新
合约
89

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
结算形式
0 = 现金，债券借贷代表现金结算
→
668
DeliveryForm
N
C3
2 = 实物，债券借贷代表债券结算
101 = 其他，债券借贷代表部分现金结算
资金结算方式
1 = 场内结算
→
172
SettlDeliveryType
N
C1
2 = 场外结算
→
510
NoDistribInsts
交收账户重复组个数
N
N1
F= 出借方
→
→
624
LegSide
N
C1
G= 借入方
→
→
498
CashDistribAgentName
资金交收机构名称
N
C75
→
→
499
CashDistribAgentCode
资金交收机构代码
N
C18
CashDistribAgentAcctN
→
→
500
资金账户
N
C22
umber
CashDistribAgentAcctN
→
→
502
资金账户名称
N
C87
ame
左起顺序代表第 1 号至第 N 号篮子。例如指
10194
BasketID
N
C16
定 1 ， 2 ， 5 号篮子，填 “1100100000000000”
711
NoUnderlyings
证券个数
N
N2
操作标识
21= 换入 / 补入券
→
865
EventType
N
C2
22= 换出券
→
48
SecurityID
质押券代码
N
C12
→
38
OrderQty
质押券数量
N
quantity
份额类型
0= 限售；
→
10331
ShareProperty
N
C1
1= 非限售
→
10332
RestrictedMonth
限售期（月）
N
N4
→
231
ContractMultiplier
折算比例（ % ）
N
N <span style="color:blue">6</span> 5(2)
→
152
CashOrderQty
质押券面值总额
N
amount
90

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
→
381
GrossTradeAmt
成交金额
N
amount
→
159
AccruedInterestAmt
回购利息
N
amount
→
119
SettlCurrAmt
到期结算金额
N
amount
→
880
TrdMatchID
辅助交易编号
N
C18
192
OrderQty2
本期回购结算利息
N
amount
到期续做类型
N = 非第三方续做
829
TrdSubType
N
C1
Y = 第三方续做
1125
OrigTradeDate
原成交日期
N
date
TradeReportType 为 1 时，对非首期合约表
示原成交编号；为 3 时表示被拒绝订单的
19
ExecRefID
N
C16
交易所订单编号。
10248
MemoEx
扩展备注，支持中文
N
C96
发起方重复组，依次包含登录或订阅交易
单元、发起方的交易员一债通账户、投资
者账户、投资者账户名称，对手方交易参
453
NoPartyIDs
Y
N2
与人代码以及对手方交易员信息。取值为
6 。
<span style="color:blue">登录或订阅交易单元（指转发消息的接收</span>
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">Y</span>
<span style="color:blue">C8</span>
<span style="color:blue">方）。</span>
<span style="color:blue">→</span>
<span style="color:blue">取</span> <span style="color:blue">17</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为登录或</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">Y</span>
<span style="color:blue">N4</span>
<span style="color:blue">订阅交易单元。</span>
448
PartyID
发起方交易员一债通账户
Y
C10
取 101 ，表示当前 PartyID 的取值为发起方
→
452
PartyRole
Y
N4
的交易员一债通账户
448
PartyID
发起方投资者帐户
N
C13
→
取 5 ，表示当前 PartyID 的取值为发起方投
452
PartyRole
N
N4
资者帐户
448
PartyID
发起方投资者账户名称。
N
C180
→
452
PartyRole
取 38 ，表示当前 PartyID 的取值为发起方
N
N4
91

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
投资者账户名称
448
PartyID
对手方参与人机构代码，支持特殊符号‘ - ’ Y
C12
→
取 37 ，表示当前 PartyID 的取值为对手方
452
PartyRole
Y
N4
的交易参与人代码
448
PartyID
对手方交易员一债通账户
Y
C10
→
取 102 ，表示当前 PartyID 的取值为对手方
452
PartyRole
Y
N4
的交易员一债通账户
664
ConfirmID
约定号，仅可填大小写英文字母或数字
N
C12
10198
Memo
可填写补充约定或备注，支持中文
N
C600
<span style="color:blue">说明：</span>
<span style="color:blue">1.</span> <span style="color:blue">对于协议回购批量申报</span> <span style="color:blue">N</span> <span style="color:blue">笔质押券校验通过后，将生成</span> <span style="color:blue">N</span> <span style="color:blue">笔转发成交申报给对手方，每笔仅有一笔</span>
<span style="color:blue">质押券。</span>
<span style="color:blue">2.</span> <span style="color:blue">对于</span> <span style="color:blue">OrigTradeID</span> <span style="color:blue">，撤单时必填，表示被撤消订单的交易所订单编号；对于</span> <span style="color:blue">ExecRefID</span> <span style="color:blue">，</span>
<span style="color:blue">TradeReportType</span> <span style="color:blue">为</span> <span style="color:blue">1</span> <span style="color:blue">时，对非首期合约表示原成交编号；为</span> <span style="color:blue">3</span> <span style="color:blue">时表示被拒绝订单的交易所订单编号；其他</span>
<span style="color:blue">场景无效。证券帐户名称（与投资者账户一一对应，如对应账户未查询到名称，则无此字段）有效。其他</span>
<span style="color:blue">转发信息字段与被转发字段相同，对于业务无效字段，不进行转发。</span>
4.4.4.3 成交申报响应（ Trade Capture Report Response, MsgType=AR ）
标签
字段名
字段描述
必须
类型
消息头
MsgType = AR
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
828
TrdType
业务子类型
N
C3
856
TradeReportType
成交申报类型
Y
C1
487
TradeReportTransType
成交申报事务类别
Y
C1
成交申报响应类型，取值有：
0=Accepted ，订单申报成功
8912
TrdAckStatus
Y
C1
8=Rejected ，订单申报拒绝
571
TradeReportID
会员内部订单编号
Y
C10
申报来源
2405
ExecMethod
Y
C1
0 = 网页端申报
92

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
1 = 接口端（ TDGW ）申报
1003
TradeID
交易所订单编号
Y
C16
1126
OrigTradeID
被撤订单交易所订单编号
N
C16
522
OwnerType
订单所有者类型
Y
N3
买卖方向，取值：
1= 买（正回购） /2= 卖（逆回购）
54
Side
Y
C1
F= 出借 /G= 借入
对于合并申报中间方发起时，取值为 0
44
Price
申报价格
N
price
455
SecurityAltID
辅助证券代码
N
C12
8903
DeliveryQty
证券交付数量
N
quantity
左起顺序代表第 1 号至第 N 号篮子。例如指定 1 ，
10194
BasketID
N
C16
2 ， 5 号篮子，填 “1100100000000000”
711
NoUnderlyings
证券个数
N
N2
操作标识
21= 换入 / 补入券
→
865
EventType
N
C2
22= 换出券
→
48
SecurityID
证券代码
N
C12
→
38
OrderQty
申报数量
N
quantity
份额类型
0 = 限售
→
10331
ShareProperty
N
C1
1 = 非限售
→
10332
RestrictedMonth
限售期（月）
N
N4
→
231
ContractMultiplier
折算比例（ % ）
N
N5(2)
→
381
GrossTradeAmt
成交金额
N
amount
→
880
TrdMatchID
辅助交易编号
N
C18
成交申报状态，取值有：
0=Unmatched ，已挂单未成交
939
TrdRptStatus
Y
C1
4=Cancelled ，已撤销
8=Rejected ，已拒绝
93

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
572
TradeReportRefID
原始会员内部订单编号，撤单时有效
N
C10
751
TradeReportRejectReason
订单拒绝码， TrdAckStatus <span style="color:blue">TrdRptStatus</span> =8 时有效
N
N5
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
参与方个数，取值 =4 <span style="color:blue">5</span> ，后接重复组，依次包含
登录或订阅交易单元、发起方业务交易单元、交
453
NoPartyIDs
Y
N2
易员一债通账户、投资者账户 <span style="color:blue">、营业部代码</span> 。
448
PartyID
发起方登录或订阅交易单元。
Y
C8
取 17 ，表示当前 PartyID 的取值为登录或订阅交
→
452
PartyRole
Y
N4
易单元。
448
PartyID
发起方业务交易单元。
N
C8
取 1 ，表示当前 PartyID 的取值为发起方业务交
→
452
PartyRole
N
N4
易单元。
448
PartyID
发起方交易员一债通账户
Y
C10
取 101 ，表示当前 PartyID 的取值为发起方的交
→
452
PartyRole
Y
N4
易员一债通账户
448
PartyID
发起方投资者帐户
N
C13
取 5 ，表示当前 PartyID 的取值为发起方投资者
→
452
PartyRole
N
N4
帐户。
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">发起方营业部代码</span>
<span style="color:blue">Y</span>
<span style="color:blue">C8</span>
<span style="color:blue">取</span> <span style="color:blue">4001</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为发起方的营</span>
<span style="color:blue">→</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">Y</span>
<span style="color:blue">N4</span>
<span style="color:blue">业部代码。</span>
<span style="color:blue">说明：</span>
<span style="color:blue">1</span> <span style="color:blue">、对于协议回购协商成交批量申报，</span> <span style="color:blue">N</span> <span style="color:blue">笔质押券将收到</span> <span style="color:blue">N</span> <span style="color:blue">笔响应，每笔响应仅有一只质押券，可能</span>
<span style="color:blue">出现部分成功的场景；撤单时，允许对批量申报的多笔质押券中仅对某一只或某几只进行撤单，每只质押</span>
<span style="color:blue">券，将收到一个撤单响应，也可能出现部分成功的场景。</span>
<span style="color:blue">2</span> <span style="color:blue">、各业务响应字段说明如下，发起方业务交易单元、发起方投资者账户、</span> <span style="color:blue">Text</span> <span style="color:blue">字段与原始申报相同，</span>
<span style="color:blue">其他未提及的非必填字段均无效</span> <span style="color:blue">:</span>
<span style="color:blue">(1)</span> <span style="color:blue">业务发起</span>
<span style="color:blue">ApplID</span>
<span style="color:blue">TrdType</span>
<span style="color:blue">描述</span>
<span style="color:blue">填写说明</span>
<span style="color:blue">协议回购</span>
<span style="color:blue">（</span> <span style="color:blue">600130</span> <span style="color:blue">）</span>
<span style="color:blue">131</span>
<span style="color:blue">协商成交</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">填</span> <span style="color:blue">1</span> <span style="color:blue">，</span> <span style="color:blue">Price</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">、</span> <span style="color:blue">ShareProperty</span> <span style="color:blue">、</span>
<span style="color:blue">RestrictedMonth</span> <span style="color:blue">、</span> <span style="color:blue">ContractMultiplier</span> <span style="color:blue">、</span> <span style="color:blue">GrossTradeAmt</span> <span style="color:blue">同申报信息</span>
94

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:blue">ApplID</span>
<span style="color:blue">TrdType</span>
<span style="color:blue">描述</span>
<span style="color:blue">填写说明</span>
<span style="color:blue">132</span>
<span style="color:blue">到期确认</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">133</span>
<span style="color:blue">到期续做</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">Price</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">、</span> <span style="color:blue">ShareProperty</span> <span style="color:blue">、</span>
<span style="color:blue">RestrictedMonth</span> <span style="color:blue">、</span> <span style="color:blue">ContractMultiplier</span> <span style="color:blue">、</span> <span style="color:blue">GrossTradeAmt</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">134</span>
<span style="color:blue">提前终止</span>
<span style="color:blue">NoUnderlying</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">、</span> <span style="color:blue">Price</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">135</span>
<span style="color:blue">换券申报</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">EventType</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">、</span> <span style="color:blue">ShareProperty</span> <span style="color:blue">、</span>
<span style="color:blue">ContractMultiplier</span> <span style="color:blue">、</span> <span style="color:blue">GrossTradeAmt</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">136</span>
<span style="color:blue">解除质押</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">141</span>
<span style="color:blue">协商成交</span>
<span style="color:blue">Price</span> <span style="color:blue">、</span> <span style="color:blue">BasketID</span> <span style="color:blue">、</span> <span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">同申报信</span>
<span style="color:blue">息</span>
<span style="color:blue">142</span>
<span style="color:blue">到期购回</span>
<span style="color:blue">/</span>
<span style="color:blue">143</span>
<span style="color:blue">到期续做</span>
<span style="color:blue">Price</span> <span style="color:blue">、</span> <span style="color:blue">BasketID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">144</span>
<span style="color:blue">提前终止</span>
<span style="color:blue">Price</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">三方回购</span>
<span style="color:blue">（</span> <span style="color:blue">600140</span> <span style="color:blue">）</span>
<span style="color:blue">145</span>
<span style="color:blue">换券申报</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">EventType</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">、</span> <span style="color:blue">TrdMatchID</span> <span style="color:blue">同</span>
<span style="color:blue">申报信息</span>
<span style="color:blue">146</span>
<span style="color:blue">解除质押</span>
<span style="color:blue">/</span>
<span style="color:blue">147</span>
<span style="color:blue">补券申报</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">EventType</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">成交</span>
<span style="color:blue">Price</span> <span style="color:blue">、</span> <span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">现券协商成</span>
<span style="color:blue">交（</span> <span style="color:blue">600210</span> <span style="color:blue">）</span>
<span style="color:blue">不适用</span>
<span style="color:blue">现券协商</span>
<span style="color:blue">合并申报</span>
<span style="color:blue">（</span> <span style="color:blue">600220</span> <span style="color:blue">）</span>
<span style="color:blue">不适用</span>
<span style="color:blue">合并申报</span>
<span style="color:blue">Price</span> <span style="color:blue">、</span> <span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">301</span>
<span style="color:blue">协商成交</span>
<span style="color:blue">1.</span> <span style="color:blue">Price</span> <span style="color:blue">、</span> <span style="color:blue">SecurityAltID</span> <span style="color:blue">、</span> <span style="color:blue">DeliveryQty</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">2.</span> <span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">302</span>
<span style="color:blue">到期结算</span>
<span style="color:blue">DeliveryForm</span> <span style="color:blue">、</span> <span style="color:blue">SettlDeliveryType</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">303</span>
<span style="color:blue">到期续做</span>
<span style="color:blue">1.</span> <span style="color:blue">Price</span> <span style="color:blue">、</span> <span style="color:blue">SecurityAltID</span> <span style="color:blue">、</span> <span style="color:blue">DeliveryQty</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">2.</span> <span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">、</span> <span style="color:blue">EventType</span> <span style="color:blue">、</span> <span style="color:blue">TrdMatchID</span>
<span style="color:blue">同申报信息</span>
<span style="color:blue">304</span>
<span style="color:blue">提前终止</span>
<span style="color:blue">DeliveryForm</span> <span style="color:blue">、</span> <span style="color:blue">SettlDeliveryType</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">债券借贷</span>
<span style="color:blue">（</span> <span style="color:blue">600300</span> <span style="color:blue">）</span>
<span style="color:blue">质押券变</span>
<span style="color:blue">305</span>
<span style="color:blue">更申报</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">、</span> <span style="color:blue">EventType</span> <span style="color:blue">、</span> <span style="color:blue">TrdMatchID</span> <span style="color:blue">同</span>
<span style="color:blue">申报信息</span>
<span style="color:blue">306</span>
<span style="color:blue">解除质押</span>
<span style="color:blue">/</span>
<span style="color:blue">307</span>
<span style="color:blue">逾期结算</span>
<span style="color:blue">DeliveryForm</span> <span style="color:blue">、</span> <span style="color:blue">SettlDeliveryType</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">（</span> <span style="color:blue">2</span> <span style="color:blue">）业务撤单、确认或拒绝</span> <span style="color:blue">:</span>
<span style="color:blue">ApplID</span>
<span style="color:blue">TrdType</span>
<span style="color:blue">描述</span>
<span style="color:blue">撤单</span>
<span style="color:blue">对手方确认</span> <span style="color:blue">/</span> <span style="color:blue">拒绝</span>
95

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:blue">131</span>
<span style="color:blue">协商成交</span>
<span style="color:blue">133</span>
<span style="color:blue">到期续做</span>
<span style="color:blue">协议回购</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">Even</span>
<span style="color:blue">134</span>
<span style="color:blue">提前终止</span>
<span style="color:blue">tType</span> <span style="color:blue">同申报信息（指换入券）</span>
<span style="color:blue">（</span> <span style="color:blue">600130</span> <span style="color:blue">）</span>
<span style="color:blue">135</span>
<span style="color:blue">换券申报</span>
<span style="color:blue">136</span>
<span style="color:blue">解除质押</span>
<span style="color:blue">OrigTradeID</span> <span style="color:blue">、</span> <span style="color:blue">TradeReport</span>
<span style="color:blue">RefID</span> <span style="color:blue">有效。对于协议回</span>
<span style="color:blue">141</span>
<span style="color:blue">协商成交</span>
<span style="color:blue">购、合并申报和现券协商成</span>
<span style="color:blue">143</span>
<span style="color:blue">到期续做</span>
<span style="color:blue">三方回购</span>
<span style="color:blue">交，</span> <span style="color:blue">NoUnderlyings</span> <span style="color:blue">填</span> <span style="color:blue">1</span> <span style="color:blue">，</span> <span style="color:blue">S</span>
<span style="color:blue">144</span>
<span style="color:blue">提前终止</span>
<span style="color:blue">/</span>
<span style="color:blue">（</span> <span style="color:blue">600140</span> <span style="color:blue">）</span>
<span style="color:blue">ecurityID</span> <span style="color:blue">、</span> <span style="color:blue">EventType</span> <span style="color:blue">同申</span>
<span style="color:blue">145</span>
<span style="color:blue">换券申报</span>
<span style="color:blue">报信息（指换入券）。</span>
<span style="color:blue">146</span>
<span style="color:blue">解除质押</span>
<span style="color:blue">合并申报</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">同申报</span>
<span style="color:blue">不适用</span>
<span style="color:blue">合并申报</span>
<span style="color:blue">信息</span>
<span style="color:blue">（</span> <span style="color:blue">600220</span> <span style="color:blue">）</span>
<span style="color:blue">现券协商成交</span>
<span style="color:blue">不适用</span>
<span style="color:blue">协商成交</span>
<span style="color:blue">不适用</span>
<span style="color:blue">（</span> <span style="color:blue">600210</span> <span style="color:blue">）</span>
<span style="color:blue">301</span>
<span style="color:blue">协商成交</span>
<span style="color:blue">303</span>
<span style="color:blue">到期续做</span>
<span style="color:blue">302</span>
<span style="color:blue">到期结算</span>
<span style="color:blue">债券借贷</span>
<span style="color:blue">304</span>
<span style="color:blue">提前终止</span>
<span style="color:blue">TradeReportRefID</span> <span style="color:blue">有效</span>
<span style="color:blue">/</span>
<span style="color:blue">（</span> <span style="color:blue">600300</span> <span style="color:blue">）</span>
<span style="color:blue">307</span>
<span style="color:blue">逾期结算</span>
<span style="color:blue">306</span>
<span style="color:blue">解除质押</span>
<span style="color:blue">305</span>
<span style="color:blue">质押券变更申报</span>
<span style="color:blue">（</span> <span style="color:blue">3</span> <span style="color:blue">）业务发起、撤单、确认或拒绝失败，</span> <span style="color:blue">TradeReportRejectReason</span> <span style="color:blue">、</span> <span style="color:blue">Text</span> <span style="color:blue">有效，撤单时</span> <span style="color:blue">TradeReportRefID</span>
<span style="color:blue">有效</span> <span style="color:blue">:</span>
<span style="color:blue">ApplID</span>
<span style="color:blue">描述</span>
<span style="color:blue">TrdType</span> <span style="color:blue">、</span> <span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">有效；换券时，仅返</span>
<span style="color:blue">协议回购（</span> <span style="color:blue">600130</span> <span style="color:blue">）</span>
<span style="color:blue">回换入券</span>
<span style="color:blue">三方回购（</span> <span style="color:blue">600140</span> <span style="color:blue">）</span>
<span style="color:blue">TrdType</span> <span style="color:blue">有效</span>
<span style="color:blue">合并申报（</span> <span style="color:blue">600220</span> <span style="color:blue">）</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">有效</span>
<span style="color:blue">现券协商成交（</span> <span style="color:blue">600210</span> <span style="color:blue">）</span>
<span style="color:blue">债券借贷（</span> <span style="color:blue">600300</span> <span style="color:blue">）</span>
<span style="color:blue">TrdType</span> <span style="color:blue">有效</span>
96

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.4.4.4 成交确认（ Trade Capture Report, MsgType=AE ）
标签
字段名
字段描述
必须
类型
消息头
MsgType = AE
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
828
TrdType
业务子类型
N
C3
571
TradeReportID
会员内部订单编号
Y
C10
申报来源
0 = 网页端申报
2405
ExecMethod
Y
C1
1 = 接口端（ TDGW ）申报
1003
TradeID
交易所订单编号
Y
C16
成交申报类型
856
TradeReportType
Y
C1
0=Submit ，提交成交申报
成交申报事务类别
0=New ，新申报
487
TradeReportTransType
Y
C1
2=Replace ，响应
订单所有者类型，取值包括：
1= 个人投资者
522
OwnerType
Y
N3
103= 机构投资者
104= 自营交易
执行报告类型，取值有：
8912
TrdAckStatus
Y
C1
F=Trade ，成交
当前申报的状态，取值有：
939
TrdRptStatus
Y
C1
2=Matched ，已成交
54
Side
买卖方向
Y
C1
31
LastPx
成交价格
N
price
17
ExecID
成交编号
Y
C16
455
SecurityAltID
辅助证券代码
N
C12
97

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:blue">60</span>
<span style="color:blue">TransactTime</span>
<span style="color:blue">成交时间</span>
<span style="color:blue">Y</span>
<span style="color:blue">ntime</span>
<span style="color:blue">8504</span>
<span style="color:blue">TotalValueTraded</span>
<span style="color:blue">总成交金额</span>
<span style="color:blue">N</span>
<span style="color:blue">amount</span>
8903
DeliveryQty
证券交付数量
N
quantity
<span style="color:blue">8911</span>
<span style="color:blue">ExpirationDays</span>
<span style="color:blue">期限（天）</span>
<span style="color:blue">N</span>
<span style="color:blue">N4</span>
<span style="color:blue">结算场所：</span> <span style="color:blue">1=</span> <span style="color:blue">中国结算，</span> <span style="color:blue">2=</span> <span style="color:blue">中央结算</span>
<span style="color:blue">双边托管券，可填</span> <span style="color:blue">1</span> <span style="color:blue">或</span> <span style="color:blue">2</span> <span style="color:blue">，单边托管券只能</span>
<span style="color:blue">207</span>
<span style="color:blue">SecurityExchange</span>
<span style="color:blue">N</span>
<span style="color:blue">C1</span>
<span style="color:blue">填其实际托管方。预留字段，暂不启用。</span>
<span style="color:blue">结算周期：</span>
<span style="color:blue">0 = T+0</span>
<span style="color:blue">1 = T+1</span>
<span style="color:blue">10216</span>
<span style="color:blue">SettlPeriod</span>
<span style="color:blue">N</span>
<span style="color:blue">C1</span>
<span style="color:blue">2 = T+2</span>
<span style="color:blue">3 = T+3</span>
<span style="color:blue">预留字段，暂不启用</span>
<span style="color:blue">结算方式：</span>
<span style="color:blue">1 =</span> <span style="color:blue">净额结算</span>
<span style="color:blue">63</span>
<span style="color:blue">SettlType</span>
<span style="color:blue">N</span>
<span style="color:blue">C1</span>
<span style="color:blue">2 = RTGS</span> <span style="color:blue">结算</span>
146
NoRelatedSym
合约结算个数
N
N1
合约相关编号
1= 代表当前合约，债券借贷代表当前合约
或到期续做时的原合约
→
655
ContraLegRefID
N
C1
2= 代表新合约，债券借贷代表续做时的新
合约
结算形式
0 = 现金，债券借贷代表现金结算
→
668
DeliveryForm
N
C3
2 = 实物，债券借贷代表债券结算
101 = 其他，债券借贷代表部分现金结算
资金结算方式
1 = 场内结算
→
172
SettlDeliveryType
N
C1
2 = 场外结算
→
510
NoDistribInsts
交收账户重复组个数
N
N1
98

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
F= 出借方
→
→
624
LegSide
N
C1
G= 借入方
→
→
498
CashDistribAgentName
资金交收机构名称
N
C75
→
→
499
CashDistribAgentCode
资金交收机构代码
N
C18
CashDistribAgentAcct
→
→
500
资金账户
N
C22
Number
CashDistribAgentAcct
→
→
502
资金账户名称
N
C87
Name
左起顺序代表第 1 号至第 N 号篮子。例如指
10194
BasketID
N
C16
定 1 ， 2 ， 5 号篮子，填 “1100100000000000”
711
NoUnderlyings
证券个数
N
N2
操作标识
21= 换入 / 补入券
→
865
EventType
N
C2
22= 换出券
→
48
SecurityID
证券代码
N
C12
→
32
LastQty
成交数量
N
quantity
份额类型
0 = 限售
→
10331
ShareProperty
N
C1
1 = 非限售
→
10332
RestrictedMonth
限售期（月），指初始登记限售期
N
N4
→
231
ContractMultiplier
折算比例（ % ）
N
N5(2)
→
381
GrossTradeAmt
成交金额
N
amount
→
880
TrdMatchID
辅助交易编号
N
C18
<span style="color:blue">8500</span>
<span style="color:blue">OrderEntryTime</span>
<span style="color:blue">订单接收时间</span>
<span style="color:blue">N</span>
<span style="color:blue">ntime</span>
<span style="color:blue">1125</span>
<span style="color:blue">OrigTradeDate</span>
<span style="color:blue">原成交日期</span>
<span style="color:blue">N</span>
<span style="color:blue">date</span>
<span style="color:blue">19</span>
<span style="color:blue">ExecRefID</span>
<span style="color:blue">原成交编号</span>
<span style="color:blue">N</span>
<span style="color:blue">C16</span>
<span style="color:blue">58</span>
<span style="color:blue">Text</span>
<span style="color:blue">用户私有信息</span>
<span style="color:blue">N</span>
<span style="color:blue">C32</span>
<span style="color:blue">参与方个数，取值</span> <span style="color:blue">=87</span> <span style="color:blue">，后接重复组，依次</span>
<span style="color:blue">包含发起方投资者账户、登录或订阅交易</span>
<span style="color:blue">453</span>
<span style="color:blue">NoPartyIDs</span>
<span style="color:blue">Y</span>
<span style="color:blue">N2</span>
<span style="color:blue">单元、业务交易单元、交易员一债通账户、、</span>
99

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:blue">对手方交易员一债通账户、投资者账户、</span>
<span style="color:blue">账户名称。</span>
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">发起方登录或订阅交易单元。</span>
<span style="color:blue">Y</span>
<span style="color:blue">C8</span>
<span style="color:blue">取</span> <span style="color:blue">17</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为登录或订</span>
<span style="color:blue">→</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">Y</span>
<span style="color:blue">N4</span>
<span style="color:blue">阅交易单元。</span>
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">发起方交易员一债通账户</span>
<span style="color:blue">Y</span>
<span style="color:blue">C10</span>
<span style="color:blue">取</span> <span style="color:blue">101</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为发起方</span>
<span style="color:blue">→</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">Y</span>
<span style="color:blue">N4</span>
<span style="color:blue">的交易员一债通账户</span>
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">发起方业务交易单元。</span>
<span style="color:blue">Y</span>
<span style="color:blue">C8</span>
<span style="color:blue">取</span> <span style="color:blue">1</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为发起方业</span>
<span style="color:blue">→</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">Y</span>
<span style="color:blue">N4</span>
<span style="color:blue">务交易单元。</span>
<span style="color:blue">448</span>
<span style="color:blue">PartyID</span>
<span style="color:blue">发起方投资者帐户</span>
<span style="color:blue">Y</span>
<span style="color:blue">C13</span>
<span style="color:blue">取</span> <span style="color:blue">5</span> <span style="color:blue">，表示当前</span> <span style="color:blue">PartyID</span> <span style="color:blue">的取值为发起方投</span>
<span style="color:blue">→</span>
<span style="color:blue">452</span>
<span style="color:blue">PartyRole</span>
<span style="color:blue">Y</span>
<span style="color:blue">N4</span>
<span style="color:blue">资者帐户。</span>
448
PartyID
对手方交易员一债通账户。
Y
C10
→
取 102 ，表示当前的 PartyID 的取值为对手
452
PartyRole
Y
N4
方交易员一债通账户
448
PartyID
对手方投资者帐户
Y
C13
→
取 39 ，表示当前 PartyID 的取值为对手方投
452
PartyRole
Y
N4
资者帐户
448
PartyID
证券帐户名称，支持中文。
N
C180
→
取 36 ，表示当前 PartyID 的取值为对手方投
452
PartyRole
N
N4
资者帐户名称
<span style="color:blue">说明：</span>
<span style="color:blue">1</span> <span style="color:blue">、对于成交报告申报模式的被动成交方或协议回购到期续做中的前期合约了结，也将收到成交确认。</span>
<span style="color:blue">其中：申报来源（</span> <span style="color:blue">ExecMethod</span> <span style="color:blue">）填</span> <span style="color:blue">0</span> <span style="color:blue">，订单所有者类型（</span> <span style="color:blue">OwnerType</span> <span style="color:blue">）填‘</span> <span style="color:blue">103</span> <span style="color:blue">’；会员内部订单编号</span>
<span style="color:blue">（</span> <span style="color:blue">TradeReportID</span> <span style="color:blue">）按照网页端申报自动生成；登录或订阅交易单元、业务交易单元同首期申报数据，如首</span>
<span style="color:blue">期本方通过网页端申报，则此成交实时仍仅供网页端查看。</span>
<span style="color:blue">2</span> <span style="color:blue">、各业务响应字段说明如下，证券帐户名称（如对应账户未查询到名称，则无此字段）、</span> <span style="color:blue">OrderEntryTime</span>
<span style="color:blue">有效，</span> <span style="color:blue">Text</span> <span style="color:blue">字段与原始申报相同，</span> <span style="color:blue">LastPx</span> <span style="color:blue">与申报中的</span> <span style="color:blue">Price/Price2</span> <span style="color:blue">（如有）相同，</span> <span style="color:blue">LastQty</span> <span style="color:blue">与申报中的</span> <span style="color:blue">OrderQty</span>
<span style="color:blue">（如有）相同，其他未提及的非必填字段均无效</span> <span style="color:blue">:</span>
<span style="color:blue">ApplID</span>
<span style="color:blue">TrdType</span>
<span style="color:blue">描述</span>
<span style="color:blue">填写说明</span>
100

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:blue">ApplID</span>
<span style="color:blue">TrdType</span>
<span style="color:blue">描述</span>
<span style="color:blue">填写说明</span>
<span style="color:blue">131</span>
<span style="color:blue">协商成交</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">填</span> <span style="color:blue">1</span> <span style="color:blue">，</span> <span style="color:blue">LastPx</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">、</span> <span style="color:blue">ShareProperty</span> <span style="color:blue">、</span>
<span style="color:blue">RestrictedMonth</span> <span style="color:blue">、</span> <span style="color:blue">ContractMultiplier</span> <span style="color:blue">、</span> <span style="color:blue">GrossTradeAmt</span> <span style="color:blue">、</span> <span style="color:blue">ExpirationDays</span>
<span style="color:blue">同申报信息</span>
<span style="color:blue">132</span>
<span style="color:blue">到期确认</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">、</span> <span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span> <span style="color:blue">ExecRefID</span>
<span style="color:blue">同申报信息</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">LastPx</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">、</span> <span style="color:blue">ShareProperty</span> <span style="color:blue">、</span>
<span style="color:blue">133</span>
<span style="color:blue">到期续做</span>
<span style="color:blue">RestrictedMonth</span> <span style="color:blue">、</span> <span style="color:blue">ContractMultiplier</span> <span style="color:blue">、</span> <span style="color:blue">GrossTradeAmt</span> <span style="color:blue">、</span> <span style="color:blue">ExpirationDays</span> <span style="color:blue">、</span>
<span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span> <span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">协议回购</span>
<span style="color:blue">（</span> <span style="color:blue">600130</span> <span style="color:blue">）</span>
<span style="color:blue">134</span>
<span style="color:blue">提前终止</span>
<span style="color:blue">NoUnderlying</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">、</span> <span style="color:blue">LastPx</span> <span style="color:blue">、</span> <span style="color:blue">ExpirationDays</span> <span style="color:blue">、</span>
<span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span> <span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">填</span> <span style="color:blue">1</span> <span style="color:blue">，</span> <span style="color:blue">EventType</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">、</span> <span style="color:blue">ShareProperty</span> <span style="color:blue">、</span>
<span style="color:blue">135</span>
<span style="color:blue">换券申报</span>
<span style="color:blue">ContractMultiplier</span> <span style="color:blue">、</span> <span style="color:blue">GrossTradeAmt</span> <span style="color:blue">表示换入券信息，</span> <span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span>
<span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">136</span>
<span style="color:blue">解除质押</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">、</span> <span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span> <span style="color:blue">ExecRefID</span>
<span style="color:blue">同申报信息</span>
<span style="color:blue">141</span>
<span style="color:blue">协商成交</span>
<span style="color:blue">LastPx</span> <span style="color:blue">、</span> <span style="color:blue">TotalValueTraded</span> <span style="color:blue">、</span> <span style="color:blue">BasketID</span> <span style="color:blue">、</span> <span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span>
<span style="color:blue">LastQty</span> <span style="color:blue">、</span> <span style="color:blue">ExpirationDays</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">142</span>
<span style="color:blue">到期购回</span>
<span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span> <span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">143</span>
<span style="color:blue">到期续做</span>
<span style="color:blue">LastPx</span> <span style="color:blue">、</span> <span style="color:blue">TotalValueTraded</span> <span style="color:blue">、</span> <span style="color:blue">BasketID</span> <span style="color:blue">、</span> <span style="color:blue">ExpirationDays</span> <span style="color:blue">、</span> <span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span>
<span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">144</span>
<span style="color:blue">提前终止</span>
<span style="color:blue">LastPx</span> <span style="color:blue">、</span> <span style="color:blue">ExpirationDays</span> <span style="color:blue">、</span> <span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span> <span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">三方回购</span>
<span style="color:blue">（</span> <span style="color:blue">600140</span> <span style="color:blue">）</span>
<span style="color:blue">145</span>
<span style="color:blue">换券申报</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">EventType</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">、</span> <span style="color:blue">TrdMatchID</span> <span style="color:blue">、</span>
<span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span> <span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">146</span>
<span style="color:blue">解除质押</span>
<span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span> <span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">147</span>
<span style="color:blue">补券申报</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">EventType</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">、</span> <span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span>
<span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">成交</span>
<span style="color:blue">现券协商成</span>
<span style="color:blue">交（</span> <span style="color:blue">600210</span> <span style="color:blue">）</span>
<span style="color:blue">不适用</span>
<span style="color:blue">现券协商</span>
<span style="color:blue">LastPx</span> <span style="color:blue">、</span> <span style="color:blue">SettlType</span> <span style="color:blue">、</span> <span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">同申报信</span>
<span style="color:blue">息，</span> <span style="color:blue">TotalValueTraded</span> <span style="color:blue">按照价格数量进行计算</span>
<span style="color:blue">合并申报</span> <span style="color:blue">*</span>
<span style="color:blue">（</span> <span style="color:blue">600220</span> <span style="color:blue">）</span>
<span style="color:blue">不适用</span>
<span style="color:blue">合并申报</span>
<span style="color:blue">LastPx</span> <span style="color:blue">、</span> <span style="color:blue">SettlType</span> <span style="color:blue">、</span> <span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">同申报信息，</span>
<span style="color:blue">TotalValueTraded</span> <span style="color:blue">按照价格数量进行计算</span>
<span style="color:blue">301</span>
<span style="color:blue">协商成交</span>
<span style="color:blue">1.</span> <span style="color:blue">LastPx</span> <span style="color:blue">、</span> <span style="color:blue">TotalValueTraded</span> <span style="color:blue">、</span> <span style="color:blue">SecurityAltID</span> <span style="color:blue">、</span> <span style="color:blue">DeliveryQty</span> <span style="color:blue">、</span>
<span style="color:blue">ExpirationDays</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">2.</span> <span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">、</span> <span style="color:blue">NoDistribInsts</span> <span style="color:blue">、</span>
<span style="color:blue">CashDistribAgentAcctNumber</span> <span style="color:blue">、</span> <span style="color:blue">CashDistribAgentAcctName</span> <span style="color:blue">、</span>
<span style="color:blue">CashDistribAgentName</span> <span style="color:blue">、</span> <span style="color:blue">CashDistribAgentCode</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">债券借贷</span>
<span style="color:blue">（</span> <span style="color:blue">600300</span> <span style="color:blue">）</span>
<span style="color:blue">302</span>
<span style="color:blue">到期结算</span>
<span style="color:blue">DeliveryForm</span> <span style="color:blue">、</span> <span style="color:blue">SettlDeliveryType</span> <span style="color:blue">、</span> <span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span> <span style="color:blue">ExecRefID</span> <span style="color:blue">同申</span>
<span style="color:blue">报信息</span>
<span style="color:blue">303</span>
<span style="color:blue">到期续做</span>
<span style="color:blue">1.</span> <span style="color:blue">LastPx</span> <span style="color:blue">、</span> <span style="color:blue">TotalValueTraded</span> <span style="color:blue">、</span> <span style="color:blue">SecurityAltID</span> <span style="color:blue">、</span> <span style="color:blue">DeliveryQty</span> <span style="color:blue">、</span>
<span style="color:blue">ExpirationDays</span> <span style="color:blue">、</span> <span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span> <span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">2.</span> <span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">、</span> <span style="color:blue">EventType</span> <span style="color:blue">、</span> <span style="color:blue">TrdMatchID</span> <span style="color:blue">、</span>
101

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:blue">ApplID</span>
<span style="color:blue">TrdType</span>
<span style="color:blue">描述</span>
<span style="color:blue">填写说明</span>
<span style="color:blue">NoRelatedSym</span> <span style="color:blue">、</span> <span style="color:blue">NoDistribInsts</span> <span style="color:blue">、</span> <span style="color:blue">CashDistribAgentAcctNumber</span> <span style="color:blue">、</span>
<span style="color:blue">CashDistribAgentAcctName</span> <span style="color:blue">、</span> <span style="color:blue">CashDistribAgentName</span> <span style="color:blue">、</span>
<span style="color:blue">CashDistribAgentCode</span> <span style="color:blue">、</span> <span style="color:blue">ContraLegRefID</span> <span style="color:blue">、</span> <span style="color:blue">SettlDeliveryType</span> <span style="color:blue">同申报</span>
<span style="color:blue">信息</span>
<span style="color:blue">304</span>
<span style="color:blue">提前终止</span>
<span style="color:blue">DeliveryForm</span> <span style="color:blue">、</span> <span style="color:blue">SettlDeliveryType</span> <span style="color:blue">、</span> <span style="color:blue">TotalValueTraded</span> <span style="color:blue">、</span> <span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span>
<span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">质押券变</span>
<span style="color:blue">NoUnderlyings</span> <span style="color:blue">、</span> <span style="color:blue">SecurityID</span> <span style="color:blue">、</span> <span style="color:blue">LastQty</span> <span style="color:blue">、</span> <span style="color:blue">EventType</span> <span style="color:blue">、</span> <span style="color:blue">TrdMatchID</span> <span style="color:blue">、</span>
<span style="color:blue">305</span>
<span style="color:blue">更申报</span>
<span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span> <span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">306</span>
<span style="color:blue">解除质押</span>
<span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span> <span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
<span style="color:blue">307</span>
<span style="color:blue">逾期结算</span>
<span style="color:blue">DeliveryForm</span> <span style="color:blue">、</span> <span style="color:blue">SettlDeliveryType</span> <span style="color:blue">、</span> <span style="color:blue">TotalValueTraded</span> <span style="color:blue">、</span> <span style="color:blue">OrigTradeDate</span> <span style="color:blue">、</span>
<span style="color:blue">ExecRefID</span> <span style="color:blue">同申报信息</span>
4.4.5 执行报告类
4.4.5.1 执行报告（ Execution Report, MsgType = 8 ）
4.4.5.1.1 申报响应、成交回报及撤单成功响应
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
执行报告类型，取值有：
0=Accepted ，订单申报成功
4=Cancelled ，订单撤销成功
150
ExecType
Y
C1
8=Rejected ，订单申报拒绝
F=Trade ，成交回报
会员内部订单编号，针对询价交易申报，询价方取
11
ClOrdID
Y
C10
ClOrdID ，报价方取 QuoteMsgID
申报来源（仅对固收迁移业务有效）
0 = 网页端申报
2405
ExecMethod
N
C1
1 = 接口端（ TDGW ）申报
48
SecurityID
证券代码
Y
C12
102

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
买卖方向，取值： 1 表示买（转入）， 2 表示卖（转出）
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
N
quantity
151
LeavesQty
剩余数量
N
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
订单有效时间类型， ExecType=0/4/8 时有效
N
C1
当前申报的状态，取值有：
0=Unmatched ，已挂单未成交
1=Partially Matched ，部分成交
39
OrdStatus
Y
C1
2=Matched ，已成交
4=Cancelled ，已撤消
8=Rejected ，已拒绝
结算场所： 1= 中国结算， 2= 中央结算
SecurityExchang
双边托管券，可填 1 或 2 ，单边托管券只能填其实际托
207
N
C1
e
管方。预留字段，暂不启用。
结算周期：
0 = T+0
10216
SettlPeriod
1 = T+1
N
C1
2 = T+2
3 = T+3
103

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
预留字段，暂不启用
63
SettlType
结算方式： 1= 净额结算， 2=RTGS 结算
N
C1
信用标签，信用交易时填写，取值： XY= 担保品买卖、
N
C2
544
CashMargin
RZ= 融资交易、 PC= 平仓交易
41
OrigClOrdID
原始会员内部订单编号， ExecType=4 时有效
N
C10
103
OrdRejReason
订单拒绝码， OrdStatus=8 时有效
N
N5
17
ExecID
成交编号， ExecType=F 且 OrdStatus=1&2 时有效
N
C16
37
OrderID
交易所订单编号 , 取值为数字
Y
C16
1080
RefOrderID
被撤订单交易所订单编号， ExecType=4 时有效
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
用户私有信息 <span style="color:blue">，如申报中填写，原样返回</span>
N
C32
参与方个数，取值 =16 ，后接重复组，依次包含发起方
投资者账户、登录或订阅交易单元、发起方业务交易
单元、发起方交易员一债通账户、银行间托管帐号、
发起方营业部代码、结算会员代码、投资者中国结算
453
NoPartyIDs
Y
N2
开放式基金账户、投资者中国结算交易账户、销售人
代码、券商网点号码、开放式基金转托管的目标方、
申报编号和对手方的一债通账户、投资者账户和投资
者账户名称。
发起方
448
PartyID
发起方投资者帐户
Y
C13
投资者
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起方投资者帐户。
Y
N4
账户
登录或
448
PartyID
登录或订阅交易单元。
Y
C8
订阅交
取 17 ，表示当前 PartyID 的取值为登录或订阅交易单
452
PartyRole
Y
N4
易单元
元。
发起方
448
PartyID
发起方业务交易单元。
Y
C8
业务交
452
PartyRole
取 1 ，表示当前 PartyID 的取值为发起方业务交易单元。
Y
N4
易单元
发起方
448
PartyID
交易员一债通账户
N
C10
104

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
交易员
取 101 ，表示当前 PartyID 的取值为发起方的交易员一
一债通
452
PartyRole
N
N4
债通账户
账户
银行间
448
PartyID
银行间托管账号。债券转托管时适用。
N
C11
托管帐
452
PartyRole
取 28 ，表示当前 PartyID 的取值为银行间托管账号
N
N4
号
发起方
448
PartyID
发起方营业部代码
<span style="color:blue">NY</span>
C8
营业部
取 4001 ，表示当前 PartyID 的取值为发起方的营业部
452
PartyRole
<span style="color:blue">NY</span>
N4
代码
代码。
结算会
448
PartyID
结算会员代码
N
C8
员代码
452
PartyRole
取 4 ，表示当前 PartyID 的取值为结算会员代码。
N
N4
投资者
448
PartyID
投资者场外开放式基金账户
N
C12
中国结
算开放
取 4010 ，表示当前 PartyID 的取值为发起方的场外开
452
PartyRole
N
N4
式基金
放式基金账户。
账户
投资者
448
PartyID
投资者中国结算交易账户
N
C17
中国结
取 4011 ，表示当前 PartyID 的取值为发起方的场外交易
算交易
452
PartyRole
N
N4
账户。
账户
销售人
448
PartyID
销售人代码
N
C9
代码
452
PartyRole
取 117 ，表示当前 PartyID 的取值为发起方的销售代码。
N
N4
448
PartyID
券商网点号码
N
C9
券商网
取 81 ，表示当前 PartyID 的取值为发起方的客户端编
点号码
452
PartyRole
N
N4
码或网点号码。
开放式基金转托管的目标方代理人，对方对应的销售
开放式
448
PartyID
N
C3
基金转
人代码，取值 000-999 ，不足 3 位左侧补 0 。
托管的
取 30 ，表示当前 PartyID 的取值为开放式基金转托管
452
PartyRole
N
N4
目标方
的目标方代理人。
申报编
448
PartyID
申报代码
N
C6
105

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
号
452
PartyRole
取 4003 ，表示当前 PartyID 的取值为申报代码
N
N4
对手方
448
PartyID
对手方交易员一债通账户
N
C10
一债通
取 102 ，表示当前的 PartyID 的取值为对手方交易员一
452
PartyRole
N
N4
账户
债通账户
对手方
448
PartyID
对手方投资者帐户或三方回购专户
N
C13
投资者
452
PartyRole
取 39 ，表示当前 PartyID 的取值为对手方投资者帐户
N
N4
帐户
对手方
448
PartyID
对手方帐户名称，支持中文。
N
C180
证券帐
取 36 ，表示当前 PartyID 的取值为对手方投资者帐户
452
PartyRole
N
N4
户名称
名称
分红选择，仅用于开放式基金红选择， U= 红利转投，
8532
DividendSelect
N
C1
C= 现金分红
说明：
1 、 ExecType 和 OrdStatus 组合取值：
申报成功响应：
ExecType=0, OrdStatus=0
申报拒绝响应：
ExecType=8, OrdStatus =8
撤单成功响应：
ExecType=4, OrdStatus =4
成交回报：
ExecType=F, OrdStatus =1/2/8
其中， ExecType=F,OrdStatus=8 时表示订单申报进入订单簿后因某种程序原因无法被撮合成交。
2 、对于开放式基金、要约 / 现金选择权、融资融券非交易业务， OwnerType 字段暂不启用。
3 、对于价格、数量字段说明如下：
报告类型
字段
开放式基金非交易
融资融券非交易
要约 / 现金选择权非交易
Price 申报价格
申报信息
申报成功
OrderQty 申报数量
申报信息
响应
LeavesQt 剩余数量
无意义
CxlQty 撤单数量
无意义
Price 申报价格
申报信息
申报失败
OrderQty 申报数量
申报信息
响应
LeavesQt 剩余数量
无意义
CxlQty 撤单数量
无意义
106

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
Price 申报价格
被撤原申报
撤单成功
OrderQty 申报数量
被撤原申报
响应
LeavesQt 剩余数量
无意义
CxlQty 撤单数量
无意义
<span style="color:blue">4</span> <span style="color:blue">、对于下列业务，除协议必填字段外，申报来源字段有效，发起方交易员一债通账户、</span> <span style="color:blue">Text</span> <span style="color:blue">字段同</span>
<span style="color:blue">申报信息，其他非必填字段说明如下，未提及的非必填字段对该业务无效：</span>
<span style="color:blue">ApplID</span>
<span style="color:blue">业务类型</span>
<span style="color:blue">申报成功</span>
<span style="color:blue">申报失败</span>
<span style="color:blue">撤单成功</span>
<span style="color:blue">成交</span>
<span style="color:blue">1.</span> <span style="color:blue">对转托管，银行</span>
<span style="color:blue">600230</span>
<span style="color:blue">双非可转债转股</span>
<span style="color:blue">间托管账号同申报</span>
<span style="color:blue">600240</span>
<span style="color:blue">私募可交换债换股</span>
<span style="color:blue">信息；</span>
<span style="color:blue">600250</span>
<span style="color:blue">债券回售（一债通）</span>
<span style="color:blue">2.</span> <span style="color:blue">对三方回购转入</span>
<span style="color:blue">600251</span>
<span style="color:blue">债券回售撤销</span>
<span style="color:red">1.</span> <span style="color:blue">对转股</span> <span style="color:blue">/</span> <span style="color:blue">换股和</span>
<span style="color:blue">1.</span> <span style="color:blue">对转托管，银</span>
<span style="color:blue">转出时，专用账户</span>
<span style="color:blue">行间托管账号</span>
<span style="color:blue">回售申报，</span> <span style="color:blue">Price</span> <span style="color:blue">有</span>
<span style="color:blue">同申报信息；</span>
<span style="color:blue">同申报信息；</span>
<span style="color:blue">效：代表转股价格</span> <span style="color:blue">/</span>
<span style="color:blue">3.</span> <span style="color:blue">OrdRejReason</span> <span style="color:blue">、</span>
<span style="color:blue">/</span>
<span style="color:blue">换股价格</span> <span style="color:blue">/</span> <span style="color:blue">回售价</span>
<span style="color:blue">2.</span> <span style="color:blue">对三方回购</span>
<span style="color:blue">TimeInForce</span> <span style="color:blue">有效；</span>
<span style="color:blue">格；</span>
<span style="color:blue">转入转出时，专</span>
<span style="color:blue">4.</span> <span style="color:blue">撤单失败时，</span>
<span style="color:blue">600260</span>
<span style="color:blue">债券转托管</span>
<span style="color:blue">用账户同申报</span>
<span style="color:red">2.</span> <span style="color:blue">对三方回购转</span>
<span style="color:blue">OrigClOrdID</span> <span style="color:blue">同申</span>
<span style="color:blue">入转出时，专用账</span>
<span style="color:blue">信息；</span>
<span style="color:blue">报信息；申报失败</span>
<span style="color:blue">户信息同申报信</span>
<span style="color:blue">3.</span> <span style="color:blue">OrderQty</span>
<span style="color:blue">表</span>
<span style="color:blue">时，</span> <span style="color:blue">OrderQty</span> <span style="color:blue">同申</span>
<span style="color:blue">息；</span>
<span style="color:blue">示被撤订单数</span>
<span style="color:blue">报数量。</span>
<span style="color:blue">量</span>
<span style="color:blue">；</span>
<span style="color:blue">3.</span> <span style="color:blue">对转托管，银行</span>
<span style="color:blue">1.</span> <span style="color:blue">LastQty</span> <span style="color:blue">（成交数</span>
<span style="color:blue">间托管账号有效；</span>
<span style="color:blue">OrigClOrdID</span> <span style="color:blue">、</span>
<span style="color:blue">量）为转入或转出数</span>
<span style="color:blue">4.</span> <span style="color:blue">OrderQty</span> <span style="color:blue">必填，</span>
<span style="color:blue">RefOrderID</span>
<span style="color:blue">、</span>
<span style="color:blue">量</span>
<span style="color:blue">，</span>
<span style="color:blue">ExecID</span>
<span style="color:blue">、</span>
<span style="color:blue">同申报数量；</span>
<span style="color:blue">TimeInForce</span> <span style="color:blue">必</span>
<span style="color:blue">OrderEntryTime</span>
<span style="color:blue">有</span>
<span style="color:blue">填。</span>
<span style="color:blue">TimeInForce</span> <span style="color:blue">有效。</span>
<span style="color:blue">600270</span>
<span style="color:blue">三方回购转入转出</span>
<span style="color:blue">/</span>
<span style="color:blue">效；</span>
<span style="color:blue">2.</span> <span style="color:blue">对三方回购转入</span>
<span style="color:blue">转出时，对手方投资</span>
<span style="color:blue">者帐户；</span>
<span style="color:blue">1.</span> <span style="color:blue">Price</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span> <span style="color:blue">、</span>
<span style="color:blue">1.</span> <span style="color:blue">OrderQt</span>
<span style="color:blue">、</span>
<span style="color:blue">1.</span> <span style="color:blue">OrderQty</span>
<span style="color:blue">、</span>
<span style="color:blue">竞买预约</span>
<span style="color:blue">1.</span> <span style="color:blue">Price</span>
<span style="color:blue">、</span>
<span style="color:blue">600290</span>
<span style="color:blue">OrderQty</span>
<span style="color:blue">、</span>
<span style="color:blue">SettlType</span> <span style="color:blue">同申报数</span>
<span style="color:blue">CxlQty</span> <span style="color:blue">有效</span>
<span style="color:blue">LeavesQty</span> <span style="color:blue">、</span> <span style="color:blue">LastPx</span> <span style="color:blue">、</span>
<span style="color:blue">（预留）</span>
<span style="color:blue">据；</span>
<span style="color:blue">LastQty</span>
<span style="color:blue">、</span>
<span style="color:blue">竞买申报</span> <span style="color:blue">*</span>
<span style="color:blue">SettlType</span> <span style="color:blue">同申报数</span>
<span style="color:blue">2.</span> <span style="color:blue">OrigClOrdID</span>
107

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:blue">ApplID</span>
<span style="color:blue">业务类型</span>
<span style="color:blue">申报成功</span>
<span style="color:blue">申报失败</span>
<span style="color:blue">撤单成功</span>
<span style="color:blue">成交</span>
<span style="color:blue">据</span>
<span style="color:blue">2.</span> <span style="color:blue">OrdRejReason</span> <span style="color:blue">、</span>
<span style="color:blue">、</span> <span style="color:blue">RefOrderID</span> <span style="color:blue">、</span>
<span style="color:blue">TotalValueTraded</span>
<span style="color:blue">、</span>
<span style="color:blue">2.</span> <span style="color:blue">TimeInForce</span> <span style="color:blue">必</span>
<span style="color:blue">TimeInForce</span> <span style="color:blue">必填。</span>
<span style="color:blue">TimeInForce</span> <span style="color:blue">必</span>
<span style="color:blue">SettlType</span> <span style="color:blue">、</span> <span style="color:blue">ExecID</span> <span style="color:blue">、</span>
<span style="color:blue">填</span>
<span style="color:blue">填。</span>
<span style="color:blue">OrderEntryTime</span>
<span style="color:blue">有</span>
<span style="color:blue">效；</span>
<span style="color:blue">1.</span> <span style="color:blue">OrderQty</span> <span style="color:blue">、</span> <span style="color:blue">Price</span>
<span style="color:blue">1.</span> <span style="color:blue">Price</span> <span style="color:blue">、</span> <span style="color:blue">OrderQty</span>
<span style="color:blue">必填</span>
<span style="color:blue">同申报数据；</span>
<span style="color:blue">2.</span> <span style="color:blue">对手方一债通账</span>
<span style="color:blue">应价申报</span>
<span style="color:blue">号</span> <span style="color:blue">/</span> <span style="color:blue">投资者帐户</span> <span style="color:blue">/</span> <span style="color:blue">证券</span>
<span style="color:blue">2.</span> <span style="color:blue">TimeInForce</span> <span style="color:blue">必</span>
<span style="color:blue">2.</span> <span style="color:blue">OrdRejReason</span> <span style="color:blue">、</span>
<span style="color:blue">填</span>
<span style="color:blue">帐户名称有效</span> <span style="color:blue">*</span> <span style="color:blue">。</span>
<span style="color:blue">TimeInForce</span> <span style="color:blue">必填。</span>
<span style="color:blue">600180</span>
<span style="color:blue">确定报价</span>
<span style="color:blue">/</span>
<span style="color:blue">/</span>
<span style="color:blue">/</span>
<span style="color:blue">600190</span>
<span style="color:blue">一债通询价</span>
<span style="color:blue">600200</span>
<span style="color:blue">待定报价</span>
<span style="color:blue">*</span> <span style="color:blue">如竞买预约时勾选了自动发起，且未再手动发起竞买预约，系统将在相应时点自动发起竞买申报。</span>
<span style="color:blue">此时竞买预约发起方将收到竞买申报执行报告。此时会员内部订单编号（</span> <span style="color:blue">TradeReportID</span> <span style="color:blue">）由系统自动</span>
<span style="color:blue">生成；申报来源（</span> <span style="color:blue">ExecMethod</span> <span style="color:blue">）、订单所有者类型（</span> <span style="color:blue">OwnerType</span> <span style="color:blue">）、登录或订阅交易单元、业务交易</span>
<span style="color:blue">单元同预约数据。如预约时通过网页端申报，登录或订阅单元将填写交易员绑定的交易单元；如交易</span>
<span style="color:blue">员未绑定，则此执行报告仅供网页端查看。</span>
<span style="color:blue">*</span> <span style="color:blue">对于一债通各类现券非匹配成交（点击成交、询价成交和竞买成交等），将在成交回报中返回对手</span>
<span style="color:blue">方的一债通账户、证券账户和账户名称信息。如结算方式为净额结算且任意一方选择‘匿名’，则此</span>
<span style="color:blue">字段将填写‘</span> <span style="color:blue">anonymous</span> <span style="color:blue">’；如结算方式为净额结算且双方均显名或者结算方式‘</span> <span style="color:blue">RTGS</span> <span style="color:blue">’，则将发送</span>
<span style="color:blue">实际的交易信息；但如账户名称无法自动加载，将无此字段。</span>
4.4.5.1.2 撤单失败执行报告
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
108

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
参与方个数，取值 =8 ，后接重复组，依次包含登录或订阅
交易单元、发起方业务交易单元、营业部代码、交易员一债
453
NoPartyIDs
Y
N2
通账户、投资者中国结算开放式基金账户、投资者中国结算
交易账户、销售人代码、券商网点号码。
登录或
448
PartyID
登录或订阅交易单元。
Y
C8
订阅交
452
PartyRole
取 17 ，表示当前 PartyID 的取值为登录或订阅交易单元。
Y
N4
易单元
发起方
448
PartyID
发起方业务交易单元。
Y
C8
业务交
452
PartyRole
取 1 ，表示当前 PartyID 的取值为发起方业务交易单元。
Y
N4
易单元
发起方
448
PartyID
发起方营业部代码
N
C8
营业部
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为发起方的营业部代码。
N
N4
代码
发起方
448
PartyID
交易员一债通账户
N
C10
交易员
取 101 ，表示当前 PartyID 的取值为发起方的交易员一债通
一债通
452
PartyRole
N
N4
账户
账户
投资者
448
PartyID
投资者场外开放式基金账户
N
C12
中国结
算开放
取 4010 ，表示当前 PartyID 的取值为发起方的场外开放式基
452
PartyRole
N
N4
式基金
金账户。
账户
投资者
448
PartyID
投资者中国结算交易账户
N
C17
中国结
算交易
452
PartyRole
取 4011 ，表示当前 PartyID 的取值为发起方的场外交易账户。
N
N4
账户
销售人
448
PartyID
销售人代码
N
C9
109

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
代码
452
PartyRole
取 117 ，表示当前 PartyID 的取值为发起方的销售代码。
N
N4
448
PartyID
券商网点号码
N
C9
券商网
取 81 ，表示当前 PartyID 的取值为发起方的客户端编码或网
点号码
452
PartyRole
N
N4
点号码。
说明：
1. 发起方营业部代码字段对于开放式基金、要约 / 现金选择权、融资融券非交易 <span style="color:blue">及固收迁移</span> 业务暂不启
用。
4.4.6 网络密码服务（ Password Service, MsgType = U006 ）
4.4.6.1.1 网络密码服务申报
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
Y
N3
522
OwnerType
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
8539
ValidationCode
投资者在上交所网站注册时所获得的激活码
N
C8
58
Text
用户私有信息
N
C32
参与方个数，取值 =3 ，后接重复组，依次包含发起方的
Y
N2
453
NoPartyIDs
投资者账户、发起方业务交易单元号、营业部代码。
发起方投
448
PartyID
发起方投资者帐户
Y
C13
资者账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起方投资者帐户。
Y
N4
发起方业
448
PartyID
发起方业务交易单元代码，填写 5 位业务交易单元号。
Y
C8
务交易单
452
PartyRole
取 1 ，表示当前 PartyID 的取值为发起方业务交易单元号。 Y
N4
110

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
元号
448
PartyID
发起方营业部代码
Y
C8
发起方营
取 4001 ，表示当前 PartyID 的取值为发起方的营业部代
Y
N4
业部代码
452
PartyRole
码。
说明
1 、各业务填写字段说明如下：
应用标识 ApplID
业务类型
相关字段填写说明
1 、 SecurityID ， A 股申报填写 799988 ， B 股申报填写 939988
600120
网络密码服务
2 、 OwnerType 暂不启用
4.4.6.1.2 密码服务申报响应
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
OrdRejReason
拒绝码，仅当申报成功时响应返回 “0”
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
ValidationCode
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
参与方个数，取值 =3 ，后接重复组，依次包含发起方投资者账
453
NoPartyIDs
Y
N2
户、发起方业务交易单元、发起方营业部代码。
发起方
448
PartyID
发起方投资者帐户
Y
C13
投资者
取 5 ，表示当前 PartyID 的取值为发起方投资者帐
452
PartyRole
Y
N4
账户
户。
111

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
发起方
448
PartyID
发起方业务交易单元。
Y
C8
业务交
取 1 ，表示当前 PartyID 的取值为发起方业务交易
452
PartyRole
Y
N4
易单元
单元。
发起方
448
PartyID
发起方营业部代码
Y
C8
营业部
取 4001 ，表示当前 PartyID 的取值为发起方的营
452
PartyRole
Y
N4
代码
业部代码。
注：
1 、 OwnerType 暂不启用。
4.4.7 其它消息
4.4.7.1 申报拒绝（ Order Reject ）
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
N
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
参与方个数，取值 =1 ，后接重复组，依次包含发起方
453
NoPartyIDs
Y
N2
业务交易单元。
发起方申报交易单元代码，填写 5 位
448
PartyID
Y
C8
发起方
发起方业务交易单元。
业务交
取 1 ，表示当前 PartyID 的取值为发
452
PartyRole
Y
N4
易单元
起方业务交易单元。
说明：
1 、消息类型与业务层 ID 对应表：
消息类型
被拒绝消息对应的业务层 ID
112

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
意向申报（ Indication of Interest ）
IOIID
成交申报（ Trade Capture Report ）
TradeReportID
网络密码服务（ Password Service ）
ClOrdID
2 、对于成交申报类和意向申报类消息， SecurityID 非必填；对于其他消息， SecurityID 必填。
4.4.7.2 平台状态（ PlatformState ）
标签
字段名
字段描述
必须
类型
消息头
MsgType = U109
平台标识：
10180
PlatformID
Y
C1
6= 互联网交易平台 <span style="color:blue">/</span> <span style="color:blue">新固定收益系统</span>
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
4.4.7.3 执行报告分区信息（ ExecRptInfo ）
标签
字段名
字段描述
必须
类型
消息头
MsgType = U108
平台标识：
10180
PlatformID
Y
C1
6 = 互联网交易平台 <span style="color:blue">/</span> <span style="color:blue">新固定收益系统</span>
8561
NoGateWayPBUs
登录或订阅 PBU 数量
Y
N4
→
8560
GateWayPBU
登录或订阅 PBU
Y
C8
10196
NoPartitions
平台内分区数量
Y
N4
113

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
→
10197
PartitionNo
平台内分区号
Y
N4
执行报告分区信息提供 PBU 和分区列表，供 OMS 对执行报告流进行初始化和维护。其中 PBU 可能
为 OMS 所连接 TDGW 上的登录 PBU ，也可能为该 TDGW 上订阅的其他 PBU （仅包含订阅成功的 PBU ），
TDGW 在该循环体中首先给出登录 PBU ，后给出订阅的其他 PBU （如有）。
4.4.7.4 分区序号同步（ ExecRptSync ）
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
→
8560
GateWayPBU
登录或订阅 PBU
Y
C8
→
10197
PartitionNo
平台内分区号
Y
N4
→
8562
BeginReportIndex
分区执行报告起始序号
Y
N16
序号同步请求中 BeginReportIndex 取值应大于 0 。 OMS 应避免频繁发送 “ 分区序号同步 ” 请求，禁止定
时或不必要的反复同步行为。
4.4.7.5 分区序号同步响应（ ExecRptSyncRsp ）
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
→
8560
GateWayPBU
登录或订阅 PBU
Y
C8
→
10197
PartitionNo
平台内分区号
Y
N4
→
8562
BeginReportIndex
分区执行报告起始序号
Y
N16
→
8563
EndReportIndex
分区执行报告最大序号
Y
N16
→
103
OrdRejReason
分区序号同步拒绝码
Y
N5
→
58
Text
描述
Y
C64
分区序号同步响应中 RejReason 为 0 时表示成功，其他取值表示错误（如 PBU 或 PartitionNo 取值不
正确）。
4.4.7.6 分区执行报告结束（ ExecRptEndOfStream ）
标签
字段名
字段描述
必须
类型
114

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
分区执行报告最大序号，本消息编入该分区执行报告编号
8563
EndReportIndex
Y
N16
序列。
TDGW 在闭市后向 OMS 自动发送一次，表示该执行报告流推送结束，后续该执行报告流上的序号将
不再增加，最大序号为 EndReportIndex 。
115

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
附录
附录一计算校验和
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
116

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
附录二 PBU 及说明
涉及 PBU 时有几种含义：
1 、配置于 TDGW 上用于登录至交易系统后台的登录单位，称为登录交易单元；
2 、在消息报文中，表明该消息所进行的业务归属单元，称为业务交易单元，接口文档中用 BizPbu 指
代；
3 、在消息报文中，表明与另一登录 PBU 间的订阅关系，称为订阅交易单元。
目前，业务交易单元必须与登录交易单元属于同一市场参与者机构，否则交易系统将拒绝相应的业务
申报请求。订阅 PBU 必须与登录 PBU 属于同一市场参与者机构，否则将订阅失败，在执行报告分区信息
ExecRptInfo 消息中将不会包含订阅失败的交易单元。
117

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
附录三错误代码说明
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
注：本表仅提供交易网关错误码，系统后台错误码参照互联网交易平台 <span style="color:blue">/</span> <span style="color:blue">新固定收益系统</span> 错误码信息文
件。
118

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
附录四“用户私有信息”说明
对于应用消息中的 Text 字段（用户私有信息），有如下规则：
TDGW 返回给 OMS 的下行消息中 Text ，取该条下行消息所对应的上行消息（由 OMS 发送给 TDGW ）
中的 Text 字段值。
119

> **变更标注说明**：本文档中已用 `<span style="color:...">` 标注了变更内容（红色=修改/新增，蓝色=其他说明）。


<metadata>
{
  "title": "20260113_IS122_上海证券交易所交易网关STEP接口规格说明书（互联网交易平台）2",
  "source_url": null,
  "raw_path": "knowledge\\raw\\sse\\测试文档\\20260113_IS122_上海证券交易所交易网关STEP接口规格说明书（互联网交易平台）2.10版_20260113（新固收技术开发稿）.pdf",
  "markdown_path": "knowledge\\articles\\sse\\markdown\\测试文档\\IS122_上海证券交易所交易网关STEP接口规格说明书（互联网交易平台）2.10版_20260113（新固收技术开发稿.md",
  "file_hash": "sha256:695a395f71d0c78ffff197d44f8199bd20353dfd13bc2260be8878c95885dcf8",
  "file_format": "pdf",
  "page_count": 129,
  "doc_type": "interface_spec",
  "version": null,
  "previous_version": null,
  "public_date": null,
  "effective_date": null,
  "has_changes": true,
  "parse_status": "success",
  "parse_date": "2026-05-02T01:48:22.757218+00:00",
  "sub_category": null
}
</metadata>