上海证券交易所技术文档
IS120 上海证券交易所行情网关
STEP 数据接口规范
0.61 版
上海证券交易所
二〇二六年六月

修订记录
修订日期
版本号
修订内容
<span style="color:blue">2026-05-11</span>
<span style="color:blue">0.61</span>
<span style="color:blue">1</span> <span style="color:blue">、原</span> <span style="color:blue">2.1</span> <span style="color:blue">会话机制交互图拆分为业务消息和重传消息。</span>
<span style="color:blue">2</span> <span style="color:blue">、原应用信息章节抽取逐笔行情和快照行情通用规则组成</span>
<span style="color:blue">2.5.1</span> <span style="color:blue">应用信息通用约定章节。</span>
<span style="color:blue">3</span> <span style="color:blue">、添加了固收迁移互联网平台后新增行情信息（含债券非</span> <span style="color:blue">匹配</span>
<span style="color:blue">成交</span> <span style="color:blue">快照行情及各类逐笔行情等）。</span>
<span style="color:blue">4</span> <span style="color:blue">、移除原固收文件行情接口包括：</span> <span style="color:blue">se015cjhqYYYMMDD001.txt</span>
<span style="color:blue">（固收成交行情文件）、</span> <span style="color:blue">se015cjmxYYYMMDD001.txt</span> <span style="color:blue">（固收成交</span>
<span style="color:blue">明细文件）、</span> <span style="color:blue">se015qdbjYYYMMDD001.txt</span> <span style="color:blue">（固收确定报价文件）</span>
<span style="color:blue">和</span> <span style="color:blue">se015zqxxYYYMMDD001.txt</span> <span style="color:blue">（固收证券信息文件）（本文档</span>
<span style="color:blue">无调整）。</span>
5 、 <span style="color:blue">[新增] 新增接收</span> <span style="color:blue">products_yyyymmdd.xml</span> <span style="color:blue">（证券产品基础信息文件）、</span>
<span style="color:blue">bondmbrs_yyyymmdd.xml</span> <span style="color:blue">（债券交易参与人信息文件）和</span>
<span style="color:blue">bondtrdrs_yyyymmdd.xml</span> <span style="color:blue">（债券交易员信息文件）（本文档无调</span>
<span style="color:blue">整）。</span>
2026-03-20
0.60
配合 txt 版 ETF 定义文件下线，删除相关描述。
2025-10-17
0.59
支持 ETF 公告文件 xml 版，调整 2.4.2.2 集中竞价类行情快照扩
展字段章节 IOPV 行情与 ETF 公告文件关联关系描述。
2025-08-01
0.58
在市场状态消息（ MsgType=h ）、行情快照消息（ MsgType=W ）
中增加独立 IOPV 行情描述。

2023-08-14
0.57
1 、明确 PreCloseIOPV （基金 T-1 日收盘时刻 IOPV ）、 IOPV （基
金 IOPV ）字段适用范围以及和 ETF 公告文件的关联关系。
2 、增加基金通行情接收相关描述。（本文档无调整）
2022-04-13
0.56
增加期权基础信息第二版文件接收相关描述。（本文档无调整）
2022-03-21
0.55
增加 B 转 H 行情文件接收相关描述。（本文档无调整）
2022-01-17
0.54
调整市场状态消息中股票、基金、指数及债券分销（ SecurityType
= 01 ）和债券市场行情（ SecurityType = 12 ）描述
2022-01-11
0.53
1 、调整行情接口中债券指数、债券和回购的数量单位；
2 、 调整 STEP 行情接口中“成交金额”字段长度，与 BINARY
接口保持一致；
3 、 移除市场行情状态（ SecurityType = 01 ）中债券质押回购行情
结束标志信息
2021-08-06
0.52
调整行情接口中债券相关的行情数据说明
2021-03-24
0.51
调整股票（含指数）全市场行情状态中债券质押回购行情结束标
志的相关描述
2021-03-05
0.50
调整债券产品为单独证券类型
2021-01-19
0.42
行情快照消息增加公募 REITs 相关描述
2020-05-20
0.41
变更市场状态消息、行情快照消息的消息头中 SendingTime 为交
易所时间
2019-12-05
0.40
原内容移入第二章，增加章节描述通过行情网关接收的文件及外
部转发数据

2019-01-25
0.32
1 、增加盘后固定价格交易的行情接口说明，调整国债预发行接
口字段取值
2 、调整盘后固定价格行情的产品状态取值
2019-01-10
0.31
增加债券回购延长对市场状态消息字段的说明
2018-07-11
0.30
1 、根据反馈意见调整部分说明、调整价格精度、增加成交笔数
及期权虚拟匹配数量
2 、 TradingPhaseCode 闭市集合竞价相关调整
2018-03-25
0.20
据原有文件接口进行字段及内容调整
2018-03-09
0.10
文档创建

目
录
1
引言....................................................................................................................................................1
1.1
名词释义 .....................................................................................................................................1
2
STEP 实时行情.....................................................................................................................................2
2.1
会话机制 .....................................................................................................................................2
2.1.1
消息序号.................................................................................................................................3
2.1.2
会话安全.................................................................................................................................3
2.1.3
建立行情会话.......................................................................................................................... 4
2.1.4
行情数据发布.......................................................................................................................... 4
2.1.5
关闭行情会话.......................................................................................................................... 4
2.1.6
心跳........................................................................................................................................4
2.1.7
行情网关主动关闭行情会话的情况............................................................................................ 5
2.2
协议介绍 .....................................................................................................................................5
2.2.1
字段说明.................................................................................................................................5
2.2.2
STEP 消息头............................................................................................................................6
2.2.3
STEP 消息尾............................................................................................................................7
2.2.4
STEP 消息完整性..................................................................................................................... 7
2.3
会话消息 .....................................................................................................................................8
2.3.1
登录消息（MsgType=A）........................................................................................................ 8
2.3.2
注销消息（MsgType=5）.........................................................................................................9

2.3.3
心跳消息（MsgType=0）.......................................................................................................10
2.3.4
测试请求消息（MsgType=1）................................................................................................10
2.3.5
重发请求消息（MsgType=2）................................................................................................11
2.3.6
会话拒绝消息（MsgType=3）................................................................................................11
2.3.7
序号重设消息（MsgType=4）................................................................................................12
2.4
公共消息 ................................................................................................................................... 12
2.4.1
频道心跳（MsgType=UA001）.............................................................................................. 12
2.4.2
重传消息（MsgType=UA002）.............................................................................................. 13
2.5
应用消息 ................................................................................................................................... 15
2.5.1
应用消息通用约定..................................................................................................................15
2.5.2
市场状态消息（MsgType=h）................................................................................................16
2.5.3
行情快照消息（MsgType=W）...............................................................................................20
2.5.4
逐笔行情消息（MsgType=UB001）........................................................................................28
3
文件接收........................................................................................................................................... 34
4
转发行情........................................................................................................................................... 35
5
后记..................................................................................................................................................36
附录一
计算校验和.................................................................................................................................. 37

技术文档
1
引言
上海证券交易所行情网关数据接口规范包括 BINARY 与 STEP 两卷，本卷主要介绍 STEP
数据接口规范（第二章），并对行情网关可接收文件（第三章）和转发行情（第四章）进行一定
的说明，请市场参与者结合《上海证券交易所行情网关技术指引及接口开发指南》一并使用。
文档采用的术语及消息内容与 STEP 数据接口规范具有对应关系，可以互为参考。
1.1
名词释义
名词
含义
Market Data GateWay
MDGW
行情网关
Vendor Supplied System
VSS
用户行情系统
Securities Trading Exchange Protocol
STEP
证券交易数据交换协议
Financical Information Exchange
FIX
金融信息交换协议
- 1 -

技术文档
2
STEP 实时行情
本章描述市场参与者与信息服务商等用户行情系统，通过 STEP 协议接入上海证券交易所行
情网关 MDGW 进行行情数据传输的机制和相关数据交换格式。
2.1
会话机制
用户行情系统（ VSS ）通过 TCP 方式接收行情网关（ MDGW ）发布的流式行情，会话机制
遵循《轻量级 STEP 会话层接口规范》。
交互示意图如下：
V SS
M D G W
建立TC P连接
TC P 连接
连接接受
登录消息(M sgType= A )
登录请求
登录失败(M sgType= 5)
登录处理
登录成功(M sgType= A )
心跳消息(M sgType= 0)
发送心跳
心跳消息(M sgType= 0)
心跳响应
频道心跳（M sgType= U A 001）
频道心跳接收
市场状态消息（M sgType= h）
市场状态接收
业务消息
行情快照消息（M sgType= W ）
行情快照接收
逐笔行情消息（M sgType= U B001）
逐笔行情接收
注销消息(M sgType= 5)
发送注销请求
注销处理
注销消息(M sgType= 5)
STEP 协议交互图 <span style="color:blue">（业务消息）</span>
- 2 -

技术文档
V SS
M D G W
建立TC P连接
TC P 连接
连接接受
登录消息(M sgType= A )
登录请求
登录处理
登录失败(M sgType= 5)
登录成功(M sgType= A )
心跳消息(M sgType= 0)
发送心跳
心跳消息(M sgType= 0)
心跳响应
重传消息(M sgType= U A 002)
发送重传请求
重传处理
逐笔行情消息(M sgType= U B001)
重传消息(M sgType= U A 002)
注销消息(M sgType= 5)
发送注销请求
注销处理
注销消息(M sgType= 5)
<span style="color:blue">STEP</span> <span style="color:blue">协议交互图（重传消息）</span>
2.1.1
消息序号
会话双方收发的每条消息都被分配有一个消息序号 MsgSeqNum 来唯一标识。参与通信的每
一端都需要维护一对序号（ NxtIn, NxtOut ）， NxtIn 表示下一个期望的入向消息序号， NxtOut 表
示下一个出向消息序号。消息序号一般在每次会话过程中从 1 开始，在整个会话过程中连续递
增，直到该会话过程全部结束。
2.1.2
会话安全
MDGW 与 VSS 之间传输的数据是非加密的，数据传输安全由接入用户网络保证。
- 3 -

技术文档
2.1.3
建立行情会话
每个行情会话都是完全独立的，同一 VSS 在一个交易日内的多次登录被视为不同的行情会
话。
建立行情会话包含两个步骤：建立 TCP 连接、登录。具体步骤如下：
1 、 TCP 连接
VSS 与 MDGW 建立 TCP 通讯连接，其中 MDGW 是服务端， VSS 负责发起连接。
2 、登录
VSS 发送的第一个消息必须是登录消息。如果 VSS 登录成功，则 MDGW 发送一个登录消
息作为应答。如果 VSS 登录失败， MDGW 则在发送一个含失败说明的注销消息后由 VSS 主动
关闭连接。 VSS 必须在收到 MDGW 的登录消息之后才允许发送其他消息。
2.1.4
行情数据发布
在完成建立行情会话之后， MDGW 将向 VSS 发送行情数据消息。行情数据消息格式将在 “ 应
用消息 ” 中详细叙述。 MDGW 目前发布的行情 <span style="color:blue">快照消息不支持重传，逐笔行情消息支持重传</span> 。
2.1.5
关闭行情会话
行情会话的正常关闭是通过连接双方互相发送注销消息完成的。 MDGW 和 VSS 均可以主
动发送注销消息，接收方需要回传注销消息作为应答。如果超过预定时间（一般为 5 秒）没有
收到对方回传的注销消息，任何一方均有权主动关闭连接。
2.1.6
心跳
连接双方在数据发送的空闲期间应主动发送心跳消息，通过心跳消息可以监控行情会话的
状态。心跳最小间隔由登录消息中的 HeartBtInt 域确定。
- 4 -

技术文档
连接双方在发送任何消息后，应立即重新设置心跳间隔计时器。如果 VSS 超过 2 个 HeartBtInt
指定周期没有收到 MDGW 发送的任何消息，则行情会话被视为可能存在异常， VSS 需要重新
建立行情会话。
2.1.7
行情网关主动关闭行情会话的情况
在以下几种场景（包括但不限于）下， MDGW 会主动关闭行情会话：
1 、 VSS 与 MDGW 建立 TCP 连接之后，超过预定时间（一般为 5 秒）未发送消息完成登录；
2 、 VSS 在登录失败之后，长时间不关闭 TCP 连接；
3 、 VSS 在注销之后，长时间不关闭 TCP 连接；
4 、 MDGW 与交易所行情主机连接异常；
5 、 VSS 如未及时处理 MDGW 发送的数据，导致 MDGW 内积压的待发送消息超过特定阈
值。
2.2
协议介绍
每条 STEP 消息由消息头、消息体和消息尾组成，消息最大长度为 8K 字节。
2.2.1
字段说明
字段类型说明如下：
类型
说明
CX
代表该字段内容为文本， CX 代表该字符串的最大长度，其中
X 为大于零的数字，例如 C 5 代表最大长度为 5 的文本；当最
大长度大于实际长度时可以不补空格。字符串使用 GBK 编码。
- 5 -

技术文档
NX
NX(Y)
代表该字段内容为数值， NX 代表该字符串为整数， X 为该整
数的最大长度； NX(Y) 代表该字符串为浮点数， X 代表该字符
串的最大长度， Y 代表小数位数， X 包括一位小数点，此时整
数部分最多不超过 X-Y-1 位，小数部分最多不超过 Y 位。
Boolean
C1 ，代表该字符串内容为布尔值，有效取值是 Y 或者 N ； ‘Y’
表示 Yes/True ， ‘N’ 表示 No/False
注 1 ：字段类型中如有 * 注释则为固定长度，否则为最大长度。
注 2 ：除非特别说明，消息格式不指定字段在 STEP 消息中的前后位置。
2.2.2
STEP 消息头
每一个会话或应用消息都有一个消息头，该消息头指明消息类型、消息体长度、消息序号、
发送方、接收方和发送时间等信息。
消息头格式如下：
Tag
域名
必需
说明
类型
8
BeginString
Y
起始串，固定为 FIXT.1.1( 消息的第一个域 )
C16
9
BodyLength
Y
消息体长度 ( 消息的第二个域 )
N9
35
MsgType
Y
消息类型 ( 消息的第三个域 )
C16
49
SenderCompID
Y
发送方代码
C32
56
TargetCompID
Y
接收方代码
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
- 6 -

技术文档
97
PossResend
N
应用层可能重发标志
Boolean
52
SendingTime
Y
发送时间，格式： YYYYMMDD-HH:mm:SS.sss
*C21
347
MessageEncoding
N
字符编码类型方式，固定为 GBK
C16
说明：
1.
当消息为市场状态消息或行情快照消息 <span style="color:blue">或逐笔行情消息</span> 时， SendingTime 为交易所时间。
2.2.3
STEP 消息尾
每一个会话或应用消息有一个消息尾，并以此终止。消息尾可用于分隔多个消息，包含有 3
位数的校验和值。
消息尾格式如下：
Tag
域名
必需
说明
类型
10
CheckSum
Y
校验和，消息的最末域
*C3
2.2.4
STEP 消息完整性
STEP 消息完整性通过两个方法保证：消息体长度和校验和的验证。
消息长度是以 BodyLength 域来表示，可以通过清点消息之中跟在 BodyLength 域之后、直
至并包括直接先于 CheckSum 域号（ ‘10=’ ）出现的那个域界定符 <SOH> 之间的字符来验证。
校验和是把每个字符的二进制值从消息开头 ‘8=’ 中的 ‘8’ 开始相加，一直加到紧靠在校验和
域 ‘10=’ 之前的域界定符，然后取按 256 取模得到的结果。
校验和域位于消息的最末一个。计算校验和的代码段可参考附录一 “ 计算校验和 ” 。
- 7 -

技术文档
2.3
会话消息
会话消息将在以下各节中予以介绍，并定义会话消息格式。
连接双方均可生成会话消息。
2.3.1
登录消息（ MsgType=A ）
登录消息应是在行情会话开始时 VSS 发送的第一个消息。 MDGW 只作为登录的接受方，
不会作为登录的发起方。
HeartBtInt 域用来指定心跳消息的发送时间间隔，必须设置为大于 0 的整数。 VSS 需要在登
录消息中填入预期的心跳时间间隔， MDGW 在回传登录消息时返回的 HeartBtInt 域作为协商后
的心跳时间间隔。
登录请求消息格式如下：
Tag
域名
必
说明
类型
需
标准消息头
Y
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
双方序号重置为 1 的标记（请求时必填 Y ）
Boolean
N18
789
NextExpectedMsgSeqNum
N
接收方期望得到的下一条消息序号（请求时必填
1 ）
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
- 8 -

技术文档
C8
1137
DefaultApplVerID
Y
本次会话中使用的 FIX 消息的缺省版本。对于
本文涉及的行情发布而言，固定填为 9
N8
1407
DefaultApplExtID
N
本次会话中使用的 FIX 消息 [ 在 Tag1137 基础
上 ] 的缺省扩展包。对于本文涉及的行情发布而
言，固定填为 124
C32
1408
DefaultCstmApplVerID
N
本次会话中， FIX 消息的缺省自定义应用版本。
本标签是对 tag 1137 + tag 1407 的进一步约束。
填写协议版本，如 STEP1.20_SH_0.30
标准消息尾
Y
2.3.2
注销消息（ MsgType=5 ）
注销消息是发起或确认行情会话终止的消息。未经注销消息交换而断开连接，一律视为非正
常的断开。
连接双方在发送注销消息之后不应发送任何消息。
注销消息格式如下：
Tag
域名
必需
说明
类型
标准消息头
Y
MsgType = 5
N4
1409
SessionStatus
N
Logout 时的会话状态
0
正常注销
【 1– 999 】一般情况注销，重连可以恢复
【 1000 – 9999 】严重情况注销，建议切换服务器
- 9 -

技术文档
58
Text
N
文本
C1024
标准消息尾
Y
2.3.3
心跳消息（ MsgType=0 ）
心跳消息用于监控通信连接的状况。
当连接的任何一方在心跳时间间隔（由 HeartBtInt 域指定）时间内没有接收或发送任何数据
的时候，需要产生一个心跳消息并发送出去。如果接收方在 2 倍心跳时间间隔内都没有收到任
何消息的时候，那么可认为行情会话出现异常，可以立即关闭 TCP 连接。
心跳消息格式如下：
Tag
域名
必需
说明
类型
标准消息头
Y
MsgType = 0
C32
112
TestReqID
N
如是对 TestRequest 响应而发送的心跳消
息，则应包含本域。本域的内容直接来自
于触发本心跳消息的 TestRequest 消息的内
容
标准消息尾
Y
2.3.4
测试请求消息（ MsgType=1 ）
测试请求消息能强制对方发出心跳消息。测试请求消息的作用是检查对方消息序号和检查通
信线路的状况。对方用带有测试请求标识符（ TestReqID ）的心跳作应答。 MDGW 不会主动发送
此消息，但会遵循 FIX 标准引擎规则而响应 VSS 的测试请求消息。
测试请求消息格式如下：
- 10 -

技术文档
Tag
域名
必需
说明
类型
标准消息头
Y
MsgType =1
112
TestReqID
N
测试请求标识符
C32
标准消息尾
Y
2.3.5
重发请求消息（ MsgType=2 ）
MDGW 不会主动发出会话层的重传请求，只为兼容 FIX 标准引擎提供对该请求的响应。
MDGW 接收到重发请求消息，只会通过序号重设消息（ 4.7 ）响应。
重发请求消息格式如下：
Tag
域名
必需
说明
类型
标准消息头
Y
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
Y
2.3.6
会话拒绝消息（ MsgType=3 ）
当接收方收到一条消息，由于违反了会话层规则而不能适当地处理该消息时，应该发出会话
拒绝消息。 MDGW 不会主动发出会话拒绝消息。
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
- 11 -

技术文档
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
2.3.7
序号重设消息（ MsgType=4 ）
序号重设消息用于告知接收方下一个消息的消息序号。序号重设消息的 MsgSeqNum 按标准
FIX 协议规定可以任意填写且接收方不会检查，建议固定填写为 1 。 MDGW 不会主动发出序号
重设消息，只为兼容 FIX 标准引擎。当 MDGW 收到用户的重传请求时，以序号重设消息予以
响应。当 MDGW 收到用户序号重设消息，则重置入向消息序号 NxtIn = NewSeqNo 。
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
<span style="color:blue">2.4</span>
<span style="color:blue">公共消息</span>
<span style="color:blue">2.4.1</span>
<span style="color:blue">频道心跳（</span> <span style="color:blue">MsgType=UA001</span> <span style="color:blue">）</span>
<span style="color:blue">逐笔行情支持在数据发送的空闲期间每</span> <span style="color:blue">3</span> <span style="color:blue">秒发送一次心跳，如数据一直处于发送忙状态，</span>
- 12 -

技术文档
<span style="color:blue">则可能出现频道心跳超过</span> <span style="color:blue">3s</span> <span style="color:blue">。</span>
<span style="color:blue">Tag</span>
<span style="color:blue">域名</span>
<span style="color:blue">必须</span>
<span style="color:blue">说明</span>
<span style="color:blue">类型</span>
<span style="color:blue">标准消息头</span>
<span style="color:blue">Y</span>
<span style="color:blue">MsgType=UA001</span>
<span style="color:blue">证券类型</span>
<span style="color:blue">167</span>
<span style="color:blue">SecurityType</span>
<span style="color:blue">Y</span>
<span style="color:blue">*C2</span>
<span style="color:blue">13</span> <span style="color:blue">债券（非匹配成交）</span>
<span style="color:blue">频道号</span>
<span style="color:blue">10201</span>
<span style="color:blue">ChannelNO</span>
<span style="color:blue">Y</span>
<span style="color:blue">N4</span>
<span style="color:blue">100 =</span> <span style="color:blue">非匹配成交逐笔行情</span>
<span style="color:blue">该频道已发布的最大消息记</span>
<span style="color:blue">1350</span>
<span style="color:blue">ApplLastSeqNum</span>
<span style="color:blue">Y</span>
<span style="color:blue">N18</span>
<span style="color:blue">录号</span>
<span style="color:blue">频道结束标志</span>
<span style="color:blue">Y=</span> <span style="color:blue">行情更新已结束</span>
<span style="color:blue">10205</span>
<span style="color:blue">EndOfChannel</span>
<span style="color:blue">N</span>
<span style="color:blue">Boolean</span>
<span style="color:blue">N=</span> <span style="color:blue">行情更新未结束</span>
<span style="color:blue">标准消息尾</span>
<span style="color:blue">Y</span>
<span style="color:blue">2.4.2</span>
<span style="color:blue">重传消息（</span> <span style="color:blue">MsgType=UA002</span> <span style="color:blue">）</span>
<span style="color:blue">重传消息用于请求可重传频道下的行情数据。</span>
<span style="color:blue">针对可重传的应用类消息(各类逐笔行情消息)，若应用类消息缺失，用户可向上发送重传消</span>
<span style="color:blue">息，代表重传请求。上游以“请求-应答”的方式处理重传请求，根据重传消息中指定的起始、</span>
<span style="color:blue">结束序号返回需要重传的数据，并在重传完成后返回一个重传消息，告知重传完成；若重传失</span>
<span style="color:blue">败，则返回一个重传消息，告知重传失败。上游系统仅支持一个缺口消息正在重传，当上游收</span>
<span style="color:blue">到多个重传请求时，其他请求消息会返回重传失败。</span>
- 13 -

技术文档
<span style="color:blue">对于逐笔行情数据可通过频道代码和消息记录号判断是否有消息丢失，当收到的消息记录</span>
<span style="color:blue">号<=本频道已经收到的最大消息记录号时，说明已经收到过该消息，此时应忽略该消息。当收</span>
<span style="color:blue">到的消息记录号>已经收到的最大消息记录号+1（如已收的最大消息记录号=100，新的消息记录</span>
<span style="color:blue">号=102）说明发生了消息丢失，此时应通过发送重传请求恢复丢失的数据。</span>
<span style="color:blue">Tag</span>
<span style="color:blue">域名</span>
<span style="color:blue">必须</span>
<span style="color:blue">说明</span>
<span style="color:blue">类型</span>
<span style="color:blue">标准消息头</span>
<span style="color:blue">Y</span>
<span style="color:blue">MsgType=UA002</span>
<span style="color:blue">频道号</span>
<span style="color:blue">10201</span>
<span style="color:blue">ChannelNO</span>
<span style="color:blue">Y</span>
<span style="color:blue">N4</span>
<span style="color:blue">100 =</span> <span style="color:blue">非匹配成交逐笔行情</span>
<span style="color:blue">重传类别</span>
<span style="color:blue">10077</span>
<span style="color:blue">ResendType</span>
<span style="color:blue">Y</span>
<span style="color:blue">N2</span>
<span style="color:blue">1 =</span> <span style="color:blue">逐笔行情</span>
<span style="color:blue">重传起始消息记录号</span>
<span style="color:blue">1182</span>
<span style="color:blue">ApplBegSeqNum</span>
<span style="color:blue">Y</span>
<span style="color:blue">N18</span>
<span style="color:blue">取值大于</span> <span style="color:blue">0</span>
<span style="color:blue">重传结束消息记录号</span>
<span style="color:blue">请求时取值大于</span> <span style="color:blue">ApplBegSeqNum</span> <span style="color:blue">或取值</span> <span style="color:blue">0</span> <span style="color:blue">，</span>
<span style="color:blue">当取值为</span> <span style="color:blue">0</span> <span style="color:blue">时，交易所会将此字段设置为该</span>
<span style="color:blue">1183</span>
<span style="color:blue">ApplEndSeqNum</span>
<span style="color:blue">Y</span>
<span style="color:blue">N18</span>
<span style="color:blue">频道已发布的最大消息记录号；应答时取值</span>
<span style="color:blue">为实际传输的最大消息记录号。</span>
<span style="color:blue">仅在重传应答消息中有效，取值如下：</span>
<span style="color:blue">1 =</span> <span style="color:blue">全部完成</span>
<span style="color:blue">10076</span>
<span style="color:blue">ResendStatus</span>
<span style="color:blue">N</span>
<span style="color:blue">N2</span>
<span style="color:blue">2 =</span> <span style="color:blue">部分完成（有部分请求的数据未返回）</span>
<span style="color:blue">3 =</span> <span style="color:blue">无权限</span>
- 14 -

技术文档
<span style="color:blue">4 =</span> <span style="color:blue">数据不可用</span>
<span style="color:blue">5 =</span> <span style="color:blue">数据正在重传中</span>
<span style="color:blue">99 =</span> <span style="color:blue">其他</span>
<span style="color:blue">仅在重传应答消息中有效。</span>
<span style="color:blue">C32</span>
<span style="color:blue">58</span>
<span style="color:blue">RejectText</span>
<span style="color:blue">N</span>
<span style="color:blue">填写重传拒绝的原因（如有）。</span>
<span style="color:blue">标准消息尾</span>
<span style="color:blue">注：</span>
<span style="color:blue">1</span> <span style="color:blue">、</span> <span style="color:blue">VSS</span> <span style="color:blue">应主动缓存逐笔消息，避免频繁发送重传请求，禁止定时或不必要的反复进行重传数据行为。</span>
<span style="color:blue">2</span> <span style="color:blue">、建议每次请求回补的数据不大于</span> <span style="color:blue">200</span> <span style="color:blue">条。</span>
<span style="color:blue">3</span> <span style="color:blue">、当收到</span> <span style="color:blue">ResendStatus=2</span> <span style="color:blue">的重传应答时，建议对于未传输数据重新发起重传请求。</span>
2.5
应用消息
<span style="color:blue">2.5.1</span>
<span style="color:blue">应用消息通用约定</span>
<span style="color:blue">1.</span>
<span style="color:blue">字段无意义或无该字段行情数据时，字符填空格，数值填</span> <span style="color:blue">0</span> <span style="color:blue">；数值字段取值超过约定格式最大值时，</span>
<span style="color:blue">取最大值，如</span> <span style="color:blue">N10</span> <span style="color:blue">取</span> <span style="color:blue">9999999999</span> <span style="color:blue">；</span>
<span style="color:blue">2.</span>
<span style="color:blue">行情类别</span> <span style="color:blue">(MDStreamID)</span> <span style="color:blue">及其扩展字段如下：</span>
<span style="color:blue">SecurityType</span>
<span style="color:blue">MDStreamID</span>
<span style="color:blue">说明</span>
<span style="color:blue">MD001</span>
<span style="color:blue">指数类产品</span>
<span style="color:blue">MD002</span>
<span style="color:blue">股票（</span> <span style="color:blue">A</span> <span style="color:blue">、</span> <span style="color:blue">B</span> <span style="color:blue">股）类产品</span>
<span style="color:blue">01</span>
<span style="color:blue">MD003</span>
<span style="color:blue">债券分销类产品</span>
<span style="color:blue">MD004</span>
<span style="color:blue">基金类产品（含公募</span> <span style="color:blue">REITs</span> <span style="color:blue">）</span>
<span style="color:blue">02</span>
<span style="color:blue">MD301</span>
<span style="color:blue">期权类产品</span>
<span style="color:blue">MD101</span>
<span style="color:blue">国债预发行产品</span>
<span style="color:blue">03</span>
<span style="color:blue">MD102</span>
<span style="color:blue">盘后固定价格</span>
- 15 -

技术文档
<span style="color:blue">12</span>
<span style="color:blue">MD201</span>
<span style="color:blue">债券匹配成交快照行情</span> <span style="color:blue">1</span>
<span style="color:blue">MD210</span>
<span style="color:blue">债券非匹配成交快照行情</span> <span style="color:blue">2</span>
<span style="color:blue">MD211</span>
<span style="color:blue">确定报价逐笔委托行情</span>
<span style="color:blue">MD212</span>
<span style="color:blue">待定报价逐笔委托行情</span>
<span style="color:blue">MD213</span>
<span style="color:blue">现券意向申报逐笔委托行情</span>
<span style="color:blue">13</span>
<span style="color:blue">MD214</span>
<span style="color:blue">协议回购意向申报逐笔委托行情</span>
<span style="color:blue">MD215</span>
<span style="color:blue">三方回购意向申报逐笔委托行情</span>
<span style="color:blue">MD216</span>
<span style="color:blue">竞买逐笔委托行情</span>
<span style="color:blue">MD217</span>
<span style="color:blue">债券非匹配成交逐笔成交行情</span>
<span style="color:blue">14</span>
<span style="color:blue">MDE01</span>
<span style="color:blue">IOPV</span>
<span style="color:blue">3.</span>
<span style="color:blue">对数量单位说明如下：</span>
<span style="color:blue">a)</span>
<span style="color:blue">产品价格、金额单位，除</span> <span style="color:blue">B</span> <span style="color:blue">股为美元外，其他为人民币元。特别地，对于协议回购或三方回购，</span>
<span style="color:blue">产品价格字段表示回购利率，单位为</span> <span style="color:blue">%</span> <span style="color:blue">。对于</span> <span style="color:blue">SecurityType</span> <span style="color:blue">为</span> <span style="color:blue">13</span> <span style="color:blue">的各类行情，其价格表示净价</span>
<span style="color:blue">还是全价则以证券产品基础信息文件（</span> <span style="color:blue">products_yyyymmdd.xml</span> <span style="color:blue">）中该产品的计价方式为准。</span>
<span style="color:blue">b)</span>
<span style="color:blue">指数的成交数量</span> <span style="color:blue">(TradeVolume)</span> <span style="color:blue">为参与计算相应指数的交易数量，股票指数交易数量单位是</span> <span style="color:blue">100</span>
<span style="color:blue">股，基金指数的交易数量单位是</span> <span style="color:blue">100</span> <span style="color:blue">份，债券指数的交易数量单位是千元面额；指数成交金额</span>
<span style="color:blue">(TotalValueTraded)</span> <span style="color:blue">为参与计算相应指数的成交金额；</span>
<span style="color:blue">c)</span>
<span style="color:blue">各类产品数量与成交数量单位，股票为股，基金、公募</span> <span style="color:blue">REITs</span> <span style="color:blue">为份，债券与回购为千元面额，期</span>
<span style="color:blue">权合约的数量单位为张；</span>
d)
<span style="color:blue">对于债券分销，成交金额为每笔成交的</span> <span style="color:blue">“</span> <span style="color:blue">价格</span> <span style="color:blue">*</span> <span style="color:blue">数量</span> <span style="color:blue">*10”</span> <span style="color:blue">的总和；对于债券现券，成交金额为每笔</span>
<span style="color:blue">成交的</span> <span style="color:blue">“</span> <span style="color:blue">价格</span> <span style="color:blue">*</span> <span style="color:blue">数量</span> <span style="color:blue">*10”</span> <span style="color:blue">的总和；对于通用质押式回购，成交金额为</span> <span style="color:blue">100*</span> <span style="color:blue">成交数量</span> <span style="color:blue">*10</span> <span style="color:blue">。</span>
2.5.2
市场状态消息（ MsgType=h ）
市场状态消息用于交易所发布市场状态和产品数量等信息，会周期性发布以及在市场状态变
化时发布。
市场状态消息的格式如下：
<span style="color:blue">1</span> <span style="color:blue">包含债券现券匹配成交及质押式回购类产品。</span>
<span style="color:blue">2</span> <span style="color:blue">包含债券现券非匹配成交、协议回购、三方回购产品。</span>
- 16 -

技术文档
Tag
域名
必需
说明
类型
标准消息头
Y
MsgType=h
*C2
167
SecurityType
Y
证券类型
01 股票、基金、指数及债券分销
02 衍生品
03 综合业务
12 债券 <span style="color:blue">（匹配成交）</span>
<span style="color:blue">13</span> <span style="color:blue">债券（非匹配成交）</span>
14 外部源行情
*N1
339
TradSesMode
Y
交易盘交易模式
1 = 系统测试
2 = 模拟交易
3 = 产品（正常交易）
*C8
336
TradingSessionID
Y
全市场行情状态：
该字段为 8 位字符串，左起每位
表示特定的含义，无定义则填空
格。
393
TotNoRelatedSym
Y
最大产品数目（包括指数）
N8
标准消息尾
Y
说明：
1. 衍生品指期权业务；
- 17 -

技术文档
2. 综合业务指国债预发行、盘后固定价格交易业务；
3. 全市场行情状态 (TradingSessionID) 为 8 位字符串，左起每位表示特定的含义，无定义则填空格。该字
段具体含义在不同证券类型时说明如下：
SecurityType = 01 3
第 1 位
‘S’ 表示全市场启动期间（开市前），
‘T’ 表示全市场处于交易期间（含中间休市）
‘E’ 表示全市场处于闭市期间
第 2 位
‘1’ 表示开盘集合竞价结束标志，未结束取 ‘0’
第 3 位
‘1’ 表示全市场行情结束标志，未结束取 ‘0’
第 4 位
‘1’ 表示上海市场行情结束标志，未结束取 ‘0’
SecurityType = 02
第 1 位
‘S’ 表示期权市场启动期间（开市前）
‘T’ 表示期权市场处于交易期间（含中间休市）
‘E’ 表示期权市场处于闭市期间
第 2 位
‘1’ 表示期权市场开盘集合竞价结束标志，未结束取 ‘0’
第 3 位
‘1’ 表示期权市场行情闭市标志，未闭市取 ‘0’
SecurityType = 03
第 1 位
‘S’ 表示综合业务市场启动期间（开市前）
‘T’ 表示综合业务市场处于交易期间（含中间休市）
‘E’ 表示综合业务市场处于闭市期间
第 2 位
‘1’ 表示综合业务市场开盘集合竞价结束标志，未结束取 ‘0’
3 SecurityType = 01 时，上海市场包括股票、基金、债券分销。全市场包括上海市场及指数。
- 18 -

技术文档
第 3 位
‘1’ 表示综合业务市场收盘集合竞价结束标志，未结束取 ‘0’
第 4 位
‘1’ 表示国债预发行市场行情闭市标志，未闭市取 ‘0’
第 5 位
‘1’ 表示盘后固定价格交易行情闭市标志，未闭市取 ‘0’
SecurityType = 12 4
第 1 位
‘S’ 表示债券市场启动期间（开市前）
‘T’ 表示债券市场处于交易期间（含中间休市）
‘E’ 表示债券市场处于闭市期间
第 2 位
‘1’ 表示债券市场开盘集合竞价结束标志，未结束取 ‘0’
第 3 位
‘1’ 表示债券市场行情结束标志，未结束取 ‘0’
第 4 位
‘1’ 表示债券现券（可转债及新标准券）行情结束标志，未结束取 ‘0’
第 5 位
‘1’ 表示债券质押回购、债券现券（除可转债及新标准券）行情结束标志，未结束
取 ‘0’ 。
<span style="color:blue">SecurityType = 13</span> <span style="color:blue">5</span>
<span style="color:blue">第</span> <span style="color:blue">1</span> <span style="color:blue">位</span>
<span style="color:blue">‘S’</span> <span style="color:blue">表示债券市场启动期间（开市前）</span>
<span style="color:blue">‘T’</span> <span style="color:blue">表示债券市场处于交易期间（含中间休市）</span>
<span style="color:blue">‘E’</span> <span style="color:blue">表示债券市场处于闭市期间</span>
<span style="color:blue">第</span> <span style="color:blue">2</span> <span style="color:blue">位</span>
<span style="color:blue">无意义</span>
<span style="color:blue">第</span> <span style="color:blue">3</span> <span style="color:blue">位</span>
<span style="color:blue">‘1’</span> <span style="color:blue">表示债券市场行情结束标志，未结束取</span> <span style="color:blue">‘0’</span>
4 SecurityType = 12 时，债券市场 <span style="color:blue">（匹配成交）</span> 包含债券现券及质押式回购。
<span style="color:blue">5</span> <span style="color:blue">SecurityType = 13</span> <span style="color:blue">时，债券市场（非匹配成交）包含债券现券、协议回购、三方回购等。</span>
- 19 -

技术文档
<span style="color:blue">第</span> <span style="color:blue">4</span> <span style="color:blue">位</span>
<span style="color:blue">‘1’</span> <span style="color:blue">表示债券现券（可转债）行情结束标志，未结束取</span> <span style="color:blue">‘0’</span>
<span style="color:blue">第</span> <span style="color:blue">5</span> <span style="color:blue">位</span>
<span style="color:blue">‘1’</span> <span style="color:blue">表示协议回购、三方回购、债券现券（除可转债）等行情结束标志，未结束取</span> <span style="color:blue">‘0’</span> <span style="color:blue">。</span>
SecurityType = 14
第 1 位 - 第 8
全空格
位
2.5.3
行情快照消息（ MsgType=W ）
行情快照消息用于发布证券产品行情 , 交易所会周期性发布全量快照消息以及在行情变化
时发送增量快照消息。多条快照消息之间无数据依赖性， VSS 无需区分全量 / 增量消息，可直接
替换当前数据。
消息格式如下：
Tag
域名
必须
说明
类型
标准消息头
Y
MsgType=W
- 20 -

技术文档
*C2
167
SecurityType
Y
证券类型
01 股票、基金、指数及债券
分销
02 衍生品
03 综合业务
12 债券 <span style="color:blue">（匹配成交）</span>
<span style="color:blue">13</span> <span style="color:blue">债券（非匹配成交）</span>
14 外部源行情
*N1
339
TradSesMode
Y
交易盘交易模式
1 = 系统测试
2 = 模拟交易
3 = 产品（正常交易）
75
TradeDate
Y
交易日期 YYYYMMDD
*N8
779
LastUpdateTime
N
最新更新时间 HHMMSSsss
*N9
1500
MDStreamID
Y
行情类别
*C5
48
SecurityID
Y
产品代码
C8
55
Symbol
N
产品简称
C8
140
PrevClosePx
N
昨收盘
N14(5)
387
TotalVolumeTraded
N
成交数量
N16
8503
NumTrades
N
成交笔数
N16
8504
TotalValueTraded
N
成交金额
N17(2)
- 21 -

技术文档
268
NoMDEntries
Y
行情条目个数
N5
C2

269
MDEntryType
Y
行情条目类别
0 ＝买入价（ 270 ， 271 ， 290 ）
1 ＝卖出价（ 270 ， 271 ， 290 ）
2 ＝成交价（ 270 ）
3 ＝指数 (270)
4 ＝今开盘价（ 270 ）
5 ＝今收盘价（ 270 ）
6 ＝今结算价（ 270 ）
7 ＝当日最高成交价（ 270 ）
8 ＝当日最低成交价（ 270 ）
<span style="color:blue">9=</span> <span style="color:blue">当日成交均价（</span> <span style="color:blue">270</span> <span style="color:blue">）</span>
v ＝ IOPV （ 270 ）
w= 前一日 IOPV （ 270 ）
x ＝动态参考价格及虚拟匹
配数量（ 270 、 271 ）
z1= 昨日结算价（ 270 ）
z2= 总持仓量（ 271 ）
<span style="color:blue">z3=</span> <span style="color:blue">昨日成交均价（</span> <span style="color:blue">270</span> <span style="color:blue">）</span>

270
MDEntryPx
N
价格
N14(5)

271
MDEntrySize
N
数量
N12
- 22 -

技术文档

290
MDEntryPositi
N
档位
N2
onNo
8538
TradingPhaseCode
N
产品状态
*C8
标准消息尾
Y
说明：
<span style="color:blue">字段无意义或无该字段行情数据时，字符填空格，数值填</span> <span style="color:blue">0</span> <span style="color:blue">；数值字段取值超过约定格式最大值时，取最</span>
<span style="color:blue">大值，如</span> <span style="color:blue">N10</span> <span style="color:blue">取</span> <span style="color:blue">9999999999</span> <span style="color:blue">；</span>
<span style="color:blue">行情类别</span> <span style="color:blue">(MDStreamID)</span> <span style="color:blue">及其扩展字段如下：</span>
<span style="color:blue">SecurityType</span>
<span style="color:blue">MDStreamID</span>
<span style="color:blue">说明</span>
<span style="color:blue">MD001</span>
<span style="color:blue">指数类产品</span>
<span style="color:blue">MD002</span>
<span style="color:blue">股票（</span> <span style="color:blue">A</span> <span style="color:blue">、</span> <span style="color:blue">B</span> <span style="color:blue">股）类产品</span>
<span style="color:blue">01</span>
<span style="color:blue">MD003</span>
<span style="color:blue">债券分销类产品</span>
<span style="color:blue">MD004</span>
<span style="color:blue">基金类产品（含公募</span> <span style="color:blue">REITs</span> <span style="color:blue">）</span>
<span style="color:blue">02</span>
<span style="color:blue">MD301</span>
<span style="color:blue">期权类产品</span>
<span style="color:blue">MD101</span>
<span style="color:blue">国债预发行产品</span>
<span style="color:blue">03</span>
<span style="color:blue">MD102</span>
<span style="color:blue">盘后固定价格</span>
<span style="color:blue">12</span>
<span style="color:blue">MD201</span>
<span style="color:blue">债券类产品</span> <span style="color:blue"></span>
<span style="color:blue">14</span>
<span style="color:blue">MDE01</span>
<span style="color:blue">IOPV</span>
1.
当 SecurityType =14 且 MDStreamID= MDE01 时， PrevClosePx 昨收盘、 TotalVolumeTraded 成交数量、
NumTrades 成交笔数、 TotalValueTraded 成交金额字段取值为 0 ， TradingPhaseCode 产品状态取值为空。
<span style="color:blue">对数量单位说明如下：</span>
<span style="color:blue">产品价格、金额单位，除</span> <span style="color:blue">B</span> <span style="color:blue">股为美元外，其他为人民币元；</span>
<span style="color:blue">指数的成交数量</span> <span style="color:blue">(TradeVolume)</span> <span style="color:blue">为参与计算相应指数的交易数量，股票指数交易数量单位是</span> <span style="color:blue">100</span> <span style="color:blue">股，基</span>
<span style="color:blue">金指数的交易数量单位是</span> <span style="color:blue">100</span> <span style="color:blue">份，债券指数的交易数量单位是千元面额；指数成交金额</span>
<span style="color:blue">(TotalValueTraded)</span> <span style="color:blue">为参与计算相应指数的成交金额；</span>
<span style="color:blue">各类产品数量与成交数量单位，股票为股，基金、公募</span> <span style="color:blue">REITs</span> <span style="color:blue">为份，债券与回购为千元面额，期权合</span>
<span style="color:blue">约的数量单位为张；</span>
- 23 -

技术文档
<span style="color:blue">对于债券分销，成交金额为每笔成交的</span> <span style="color:blue">“</span> <span style="color:blue">价格</span> <span style="color:blue">*</span> <span style="color:blue">数量</span> <span style="color:blue">*10”</span> <span style="color:blue">的总和；对于债券现券，成交金额为每笔成交</span>
<span style="color:blue">的</span> <span style="color:blue">“</span> <span style="color:blue">价格</span> <span style="color:blue">*</span> <span style="color:blue">数量</span> <span style="color:blue">*10”</span> <span style="color:blue">的总和；对于质押式回购，成交金额为</span> <span style="color:blue">100*</span> <span style="color:blue">成交数量</span> <span style="color:blue">*10</span> <span style="color:blue">。</span>
2.
实时阶段及标志 (TradingPhaseCode) 为 8 位字符串，左起每位表示特定的含义，无定义则填空格。该
字段具体含义在不同行情类别时说明如下：
SecurityType = 01, MDStreamID= MD001
全为空格（预留）
SecurityType = 01, MDStreamID= MD002 ， MD003 ， MD004
第 1 位
‘S’ 表示启动（开市前）时段
‘C’ 表示开盘集合竞价时段
‘T’ 表示连续交易时段
‘E’ 表示闭市时段
‘P’ 表示产品停牌
‘M’ 表示可恢复交易的熔断时段（盘中集合竞价）
‘N’ 表示不可恢复交易的熔断时段（暂停交易至闭市）
‘U’ 表示收盘集合竞价时段
第 2 位
‘0’ 表示此产品不可正常交易
‘1’ 表示此产品可正常交易
在产品进入开盘集合竞价、连续交易、收盘集合竞价、熔断（盘中集合竞价）
状态时值为 ‘1’ ，在产品进入停牌、熔断（暂停交易至闭市）状态时值为 ‘0’ ，且
闭市后保持该产品闭市前的是否可正常交易状态。
第 3 位
‘0’ 表示未上市
‘1’ 表示已上市
- 24 -

技术文档
第 4 位
‘0’ 表示此产品在当前时段不接受进行新订单申报
‘1’ 表示此产品在当前时段可接受进行新订单申报
仅在交易时段有效，在非交易时段无效
SecurityType = 02, MDStreamID= MD301
第 1 位
‘S’ 表示启动（开市前）时段
‘C’ 表示集合竞价时段
‘T’ 表示连续交易时段
‘B’ 表示休市时段
‘E’ 表示闭市时段
‘V’ 表示波动性中断
‘P’ 表示临时停牌
‘U’ 表示收盘集合竞价
‘M’ 表示可恢复交易的熔断（盘中集合竞价）
‘N’ 表示不可恢复交易的熔断（暂停交易至闭市）
第 2 位
‘0’ 表示未连续停牌
‘1’ 表示连续停牌
（预留，暂填空格）
- 25 -

技术文档
第 3 位
‘0’ 表示不限制开仓
‘1’ 表示限制备兑开仓
‘2’ 表示限制卖出开仓
‘3’ 表示限制卖出开仓、备兑开仓
‘4’ 表示限制买入开仓
‘5’ 表示限制买入开仓、备兑开仓
‘6’ 表示限制买入开仓、卖出开仓
‘7’ 表示限制买入开仓、卖出开仓、备兑开仓
第 4 位
‘0’ 表示此产品在当前时段不接受进行新订单申报
‘1’ 表示此产品在当前时段可接受进行新订单申报
仅在交易时段有效，在非交易时段无效
SecurityType = 03, MDStreamID= MD101
第 1 位
‘S’ 表示启动（开市前）时段
‘C’ 表示集合竞价时段
‘T’ 表示连续交易时段
‘E’ 表示闭市时段
‘P’ 表示停牌
SecurityType = 03, MDStreamID= MD102
- 26 -

技术文档
第 1 位
‘I’ 表示启动（开市前）时段
‘A’ 表示集中撮合时段
‘H’ 表示连续交易时段
‘D’ 表示闭市时段
‘F’ 表示停牌
SecurityType = 12, MDStreamID= MD201
第 1 位
‘S’ 表示启动（开市前）时段
‘C’ 表示开盘集合竞价时段
‘T’ 表示连续交易时段
‘E’ 表示闭市时段
‘P’ 表示产品停牌
第 2 位
‘0’ 表示此产品不可正常交易
‘1’ 表示此产品可正常交易
在产品进入开盘集合竞价、连续交易状态时值为 ‘1’ ，在产品进入停牌状态时值
为 ‘0’ ，且闭市后保持该产品闭市前的是否可正常交易状态。
第 3 位
‘0’ 表示未上市
‘1’ 表示已上市
第 4 位
‘0’ 表示此产品在当前时段不接受进行新订单申报
‘1’ 表示此产品在当前时段可接受进行新订单申报
仅在交易时段有效，在非交易时段无效。
<span style="color:blue">SecurityType = 13, MDStreamID= MD210</span>
- 27 -

技术文档
<span style="color:blue">第</span> <span style="color:blue">1</span> <span style="color:blue">位</span>
<span style="color:blue">无意义</span>
<span style="color:blue">第</span> <span style="color:blue">2</span> <span style="color:blue">位</span>
<span style="color:blue">‘0’</span> <span style="color:blue">表示当前处于停牌状态</span>
<span style="color:blue">‘1’</span> <span style="color:blue">表示当前未处于停牌状态</span>
SecurityType = 14, MDStreamID= MDE01
第 1 位 - 第 8 位
全空格
3.
对行情条目循环体说明如下：
a)
行情条目类别为 0 或 1 时，表示该条目为买卖盘档位，此时 MDEntryPx 、 MDEntrySize 、
MDEntryPositionNo 分别表示买卖价格、数量和档位序号， MDEntryPositionNo 从 0 开始计数；
b)
行情条目类别为 w 时， MDEntryPx 表示基金 T-1 日收盘时刻 IOPV 6 ，此条目仅当 MDStreamID=
MD004 时有意义，当 MDStreamID= MDE01 时无意义；行情条目类别为 v 时， MDEntryPx 表示
基金 IOPV 7 ，此条目仅当 MDStreamID=MD004 或 MDE01 时有意义；
c)
行情条目类别为 x 时 , MDEntryPx 表示动态参考价格、 MDEntrySize 表示虚拟匹配数量，仅当
MDStreamID=MD301 时有意义；
<span style="color:blue">d)</span>
行情条目类别为 z2 时， MDEntrySize 表示期权合约总持仓量，单位是 ( 张 ) ，仅当
MDStreamID=MD301 时有意义；
e)
<span style="color:blue">行情条目类别为</span> <span style="color:blue">9</span> <span style="color:blue">时，</span> <span style="color:blue">MDEntryPx</span> <span style="color:blue">表示债券非匹配成交的当日成交均价；行情条目类别为</span> <span style="color:blue">z3</span> <span style="color:blue">时，</span>
<span style="color:blue">MDEntryPx</span> <span style="color:blue">表示债券非匹配成交的昨日成交均价；</span>
f)
其他行情条目类别，将仅通过 MDEntryPx 表示相应值，其他字段无意义；
g)
在集合竞价时段内，当前买入价和当前卖出价中同时为虚拟开盘参考价格，即根据集合竞价算法
计算得出的虚拟撮合价格。同时申买量一和申卖量一为行情发布时刻的虚拟匹配量。申买量二为
行情发布时刻的买方虚拟未匹配量。申卖量二为行情发布时刻的卖方虚拟未匹配量；
h)
对期权产品（ MDStreamID=MD301 ），今日结算价通过期权收盘价格文件（ clpr03MMDD.txt ）揭
示。
<span style="color:blue">i)</span>
对盘后固定价格行情（ MDStreamID=MD102 ） , 仅今日收盘价、买一数量、卖一数量有意义。其
中，买一数量表示当前未成交的买入申报总股数，卖一数量表示当前未成交的卖出申报总股数；
6 仅对 ETF 产品，此字段有效。该字段取 0 时，无意义。该字段不作除权除息等调整。
7 仅对 ETF 产品，此字段有效。该字段取 0 时，无意义。当 ETF 公告文件 Publish 字段（是否需要发布 IOPV ）取值为 1 时，
此字段为对应产品的 IOPV 值；当 ETF 公告文件 Publish 字段取值为 0 时，此字段固定取 0 ，无意义；
- 28 -

技术文档
<span style="color:blue">j)</span>
<span style="color:blue">对债券非匹配成交快照行情（</span> <span style="color:blue">MDStreamID=MD210</span> <span style="color:blue">）</span> <span style="color:blue">,</span> <span style="color:blue">仅前收盘价、最新成交价、今开盘价、今</span>
<span style="color:blue">收盘价、当日最高成交价、当日最低成交价、当日成交均价和昨日成交均价有意义，除前收盘价</span>
<span style="color:blue">外均仅计入债券非匹配成交（含点击成交、询价成交、竞买成交和协商成交）的交易；前收盘价</span>
<span style="color:blue">对于双边挂牌产品填写其匹配成交收盘价，单边挂牌产品填写其非匹配成交参考价。</span>
<span style="color:blue">对于公募可转债和公募</span> <span style="color:blue">REITs</span> <span style="color:blue">，无当日成交均价、昨日成交均价和今收盘价信息，其今收盘价参</span>
<span style="color:blue">考对应匹配成交行情或盘后文件。</span>
<span style="color:blue">2.5.4</span>
<span style="color:blue">逐笔行情消息（</span> <span style="color:blue">MsgType=UB001</span> <span style="color:blue">）</span>
<span style="color:blue">逐笔行情包括逐笔委托行情和逐笔成交行情，两者按照发生的顺序在一个数据流中发送。</span>
<span style="color:blue">同一个频道内的逐笔委托和逐笔成交消息的消息记录号（</span> <span style="color:blue">ApplSeqNum</span> <span style="color:blue">）统一连续编号，</span> <span style="color:blue">VSS</span> <span style="color:blue">需</span>
<span style="color:blue">通过逐笔序号的连续性判断是否丢包，并通过</span> <span style="color:blue">TCP</span> <span style="color:blue">连接向上发起重传请求。</span>
<span style="color:blue">Tag</span>
<span style="color:blue">域名</span>
<span style="color:blue">必须</span>
<span style="color:blue">说明</span>
<span style="color:blue">类型</span>
<span style="color:blue">标准消息头</span>
<span style="color:blue">Y</span>
<span style="color:blue">MsgType=UB001</span>
<span style="color:blue">证券类型</span>
<span style="color:blue">167</span>
<span style="color:blue">SecurityType</span>
<span style="color:blue">Y</span>
<span style="color:blue">*C2</span>
<span style="color:blue">13</span> <span style="color:blue">债券（非匹配成交）</span>
<span style="color:blue">10201</span>
<span style="color:blue">ChannelNO</span>
<span style="color:blue">Y</span>
<span style="color:blue">频道号</span>
<span style="color:blue">N4</span>
<span style="color:blue">1181</span>
<span style="color:blue">ApplSeqNum</span>
<span style="color:blue">Y</span>
<span style="color:blue">消息记录号，从</span> <span style="color:blue">1</span> <span style="color:blue">开始计数</span>
<span style="color:blue">N18</span>
<span style="color:blue">1500</span>
<span style="color:blue">MDStreamID</span>
<span style="color:blue">Y</span>
<span style="color:blue">行情类别</span>
<span style="color:blue">*C5</span>
<span style="color:blue">48</span>
<span style="color:blue">SecurityID</span>
<span style="color:blue">Y</span>
<span style="color:blue">产品代码</span>
<span style="color:blue">C8</span>
<span style="color:blue">60</span>
<span style="color:blue">TransactTime</span>
<span style="color:blue">Y</span>
<span style="color:blue">委托或成交的行情生成时间：</span> <span style="color:blue">HHMMSSsss</span>
<span style="color:blue">*N9</span>
- 29 -

技术文档
<span style="color:blue">类型：</span>
<span style="color:blue">对于逐笔委托：</span>
<span style="color:blue">0 =</span> <span style="color:blue">[新增] 新增委托订单</span>
<span style="color:blue">150</span>
<span style="color:blue">ExecType</span>
<span style="color:blue">Y</span>
<span style="color:blue">*C1</span>
<span style="color:blue">4 =</span> <span style="color:blue">[删除] 删除委托订单</span>
<span style="color:blue">对于逐笔成交：</span>
<span style="color:blue">F =</span> <span style="color:blue">成交</span>
<span style="color:blue">[新增] 新增委托时表示委托价格，如意向申报时未</span>
<span style="color:blue">填写价格或删除委托时，则为</span> <span style="color:blue">0</span> <span style="color:blue">；</span>
<span style="color:blue">44</span>
<span style="color:blue">Price</span>
<span style="color:blue">Y</span>
<span style="color:blue">N14(5)</span>
<span style="color:blue">逐笔成交时表示成交价格</span>
<span style="color:blue">[新增] 新增委托时表示委托数量，如意向申报时未</span>
<span style="color:blue">填写数量或删除委托时，则为</span> <span style="color:blue">0</span> <span style="color:blue">；</span>
<span style="color:blue">38</span>
<span style="color:blue">OrderQty</span>
<span style="color:blue">Y</span>
<span style="color:blue">N16(3)</span>
<span style="color:blue">逐笔成交时表示成交数量</span>
<span style="color:blue">ExtendFields</span>
<span style="color:blue">Y</span>
<span style="color:blue">扩展字段</span>
<span style="color:blue">标准消息尾</span>
<span style="color:blue">Y</span>
<span style="color:blue">2.5.4.1</span>
<span style="color:blue">逐笔委托行情扩展字段</span>
<span style="color:blue">Tag</span>
<span style="color:blue">域名</span>
<span style="color:blue">必须</span>
<span style="color:blue">说明</span>
<span style="color:blue">类型</span>
<span style="color:blue">*C1</span>
<span style="color:blue">买卖方向</span>
<span style="color:blue">1 =</span> <span style="color:blue">买</span>
<span style="color:blue">54</span>
<span style="color:blue">Side</span>
<span style="color:blue">Y</span>
<span style="color:blue">2 =</span> <span style="color:blue">卖</span>
<span style="color:blue">117</span>
<span style="color:blue">QuoteID</span>
<span style="color:blue">Y</span>
<span style="color:blue">订单编号，删除委托时表示被删除委托的订单编号</span>
<span style="color:blue">C18</span>
- 30 -

技术文档
<span style="color:blue">报价方交易参与人机构代码</span>
<span style="color:blue">10211</span>
<span style="color:blue">MemberID</span>
<span style="color:blue">Y</span>
<span style="color:blue">C12</span>
<span style="color:blue">如发起方选择匿名，填空</span>
<span style="color:blue">报价交易员一债通账户</span>
<span style="color:blue">10215</span>
<span style="color:blue">TraderCode</span>
<span style="color:blue">Y</span>
<span style="color:blue">C12</span>
<span style="color:blue">如发起方选择匿名，填空</span>
<span style="color:blue">是否全额成交</span>
<span style="color:blue">1 =</span> <span style="color:blue">是</span>
<span style="color:blue">8418</span>
<span style="color:blue">FullAmountTrade</span>
<span style="color:blue">N</span>
<span style="color:blue">*N1</span>
<span style="color:blue">2 =</span> <span style="color:blue">否</span>
<span style="color:blue">结算方式</span>
<span style="color:blue">63</span>
<span style="color:blue">SettlType</span>
<span style="color:blue">N</span>
<span style="color:blue">*N1</span>
<span style="color:blue">1 =</span> <span style="color:blue">净额结算</span>
<span style="color:blue">2 =</span>
<span style="color:blue">RTGS</span>
<span style="color:blue">231</span>
<span style="color:blue">ContractMultiplier</span>
<span style="color:blue">N</span>
<span style="color:blue">折算比例（</span> <span style="color:blue">%</span> <span style="color:blue">），如发起方未填写此字段，填</span> <span style="color:blue">0</span>
<span style="color:blue">N6(2)</span>
<span style="color:blue">8911</span>
<span style="color:blue">ExpirationDays</span>
<span style="color:blue">N</span>
<span style="color:blue">期限（天），如发起方未填写此字段，填</span> <span style="color:blue">0</span>
<span style="color:blue">N3</span>
<span style="color:blue">8504</span>
<span style="color:blue">TotalValueTraded</span>
<span style="color:blue">N</span>
<span style="color:blue">成交金额，如发起方未填写此字段，填</span> <span style="color:blue">0</span>
<span style="color:blue">N17(2)</span>
<span style="color:blue">篮子信息</span>
<span style="color:blue">左起顺序代表第</span> <span style="color:blue">1</span> <span style="color:blue">号至第</span> <span style="color:blue">N</span> <span style="color:blue">号篮子。例如指定</span> <span style="color:blue">1</span> <span style="color:blue">，</span>
<span style="color:blue">10194</span>
<span style="color:blue">BasketID</span>
<span style="color:blue">N</span>
<span style="color:blue">C16</span>
<span style="color:blue">2</span> <span style="color:blue">，</span> <span style="color:blue">5</span> <span style="color:blue">号篮子，填</span> <span style="color:blue">“1100100000000000”</span>
<span style="color:blue">10214</span>
<span style="color:blue">InvestorName</span>
<span style="color:blue">N</span>
<span style="color:blue">投资者名称</span>
<span style="color:blue">C32</span>
<span style="color:blue">竞买申报类别</span>
<span style="color:blue">1 =</span> <span style="color:blue">竞买预约</span>
<span style="color:blue">10238</span>
<span style="color:blue">BidTransType</span>
<span style="color:blue">N</span>
<span style="color:blue">*N1</span>
<span style="color:blue">2 =</span> <span style="color:blue">竞买申报</span>
<span style="color:blue">3 =</span> <span style="color:blue">单一主体中标应价申报</span>
- 31 -

技术文档
<span style="color:blue">竞买申报方式</span>
<span style="color:blue">1 =</span> <span style="color:blue">单一主体中标</span>
<span style="color:blue">10239</span>
<span style="color:blue">BidExecInstType</span>
<span style="color:blue">N</span>
<span style="color:blue">*N1</span>
<span style="color:blue">2 =</span> <span style="color:blue">多主体单一价格中标</span>
<span style="color:blue">3 =</span> <span style="color:blue">多主体多重价格中标</span>
<span style="color:blue">432</span>
<span style="color:blue">ExpireDate</span>
<span style="color:blue">N</span>
<span style="color:blue">竞买日期：</span> <span style="color:blue">YYYYMMDD</span>
<span style="color:blue">*N8</span>
<span style="color:blue">198</span>
<span style="color:blue">SecondaryOrderID</span>
<span style="color:blue">N</span>
<span style="color:blue">应价申报对应的订单编号（也即竞买申报编号）</span>
<span style="color:blue">C18</span>
<span style="color:blue">110</span>
<span style="color:blue">MinQty</span>
<span style="color:blue">N</span>
<span style="color:blue">最低成交数量，预留</span>
<span style="color:blue">N12</span>
<span style="color:blue">注：新增委托时扩展字段与业务的对照关系参见下表，删除委托时仅</span> <span style="color:blue">Side</span> <span style="color:blue">、</span> <span style="color:blue">QuoteID</span> <span style="color:blue">、</span> <span style="color:blue">MemberID</span>
<span style="color:blue">和</span> <span style="color:blue">TraderCode</span> <span style="color:blue">有效。</span>
<span style="color:blue">MDStreamID</span>
<span style="color:blue">MD211</span>
<span style="color:blue">MD212</span>
<span style="color:blue">MD213</span>
<span style="color:blue">MD214</span>
<span style="color:blue">MD215</span>
<span style="color:blue">MD216</span> <span style="color:blue">8</span>
<span style="color:blue">确定</span>
<span style="color:blue">待定</span>
<span style="color:blue">现券</span>
<span style="color:blue">协议回</span>
<span style="color:blue">三方回</span>
<span style="color:blue">竞买</span>
<span style="color:blue">竞买</span>
<span style="color:blue">应价</span>
<span style="color:blue">域名</span>
<span style="color:blue">报价</span>
<span style="color:blue">报价</span>
<span style="color:blue">意向</span>
<span style="color:blue">购意向</span>
<span style="color:blue">购意向</span>
<span style="color:blue">预约</span>
<span style="color:blue">申报</span>
<span style="color:blue">申报</span> <span style="color:blue">9</span>
<span style="color:blue">Side</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">QuoteID</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">MemberID</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">TraderCode</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">FullAmountTrade</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">SettlType</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">ContractMultiplier</span>
<span style="color:blue">●</span>
<span style="color:blue">ExpirationDays</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">8</span> <span style="color:blue">不同竞买委托方式可根据</span> <span style="color:blue">BidTransType</span> <span style="color:blue">字段进行区分。</span>
<span style="color:blue">9</span> <span style="color:blue">仅适用于竞买单一主体中标。</span>
- 32 -

技术文档
<span style="color:blue">TotalValueTraded</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">BasketID</span>
<span style="color:blue">●</span>
<span style="color:blue">InvestorName</span>
<span style="color:blue">●</span>
<span style="color:blue">BidTransType</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">BidExecInstType</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">ExpireDate</span>
<span style="color:blue">●</span>
<span style="color:blue">SecondaryOrderID</span>
<span style="color:blue">●</span>
<span style="color:blue">MinQty</span> <span style="color:blue">10</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">2.5.4.2</span> <span style="color:blue">逐笔成交行情扩展字段</span>
<span style="color:blue">Tag</span>
<span style="color:blue">域名</span>
<span style="color:blue">必须</span>
<span style="color:blue">说明</span>
<span style="color:blue">类型</span>
<span style="color:blue">买方订单编号（</span> <span style="color:blue">QuoteID</span> <span style="color:blue">）</span>
<span style="color:blue">10116</span>
<span style="color:blue">BidApplSeqNum</span>
<span style="color:blue">Y</span>
<span style="color:blue">C18</span>
<span style="color:blue">无对应委托时填空</span>
<span style="color:blue">卖方订单编号（</span> <span style="color:blue">QuoteID</span> <span style="color:blue">）</span>
<span style="color:blue">10117</span>
<span style="color:blue">OfferApplSeqNum</span>
<span style="color:blue">Y</span>
<span style="color:blue">C18</span>
<span style="color:blue">无对应委托时填空</span>
<span style="color:blue">8504</span>
<span style="color:blue">TotalValueTraded</span>
<span style="color:blue">Y</span>
<span style="color:blue">成交金额</span>
<span style="color:blue">N17(2)</span>
<span style="color:blue">10</span> <span style="color:blue">仅适用于竞买多主体中标（含单一价格或多重价格中标）。</span>
- 33 -

技术文档
<span style="color:blue">成交方式</span>
<span style="color:blue">0 =</span> <span style="color:blue">匹配成交（预留）</span>
<span style="color:blue">1 =</span> <span style="color:blue">确定报价点击成交</span>
<span style="color:blue">2 =</span> <span style="color:blue">待定报价点击成交</span>
<span style="color:blue">3 =</span> <span style="color:blue">询价成交</span>
<span style="color:blue">10333</span>
<span style="color:blue">TradeMethod</span>
<span style="color:blue">Y</span>
<span style="color:blue">N2</span>
<span style="color:blue">6 =</span> <span style="color:blue">协商成交（含合并申报）</span>
<span style="color:blue">7 =</span> <span style="color:blue">竞买单一主体成交</span>
<span style="color:blue">10 =</span> <span style="color:blue">竞买多主体单一价格成交</span>
<span style="color:blue">11 =</span> <span style="color:blue">竞买多主体多重价格成交</span>
<span style="color:blue">边际价格</span>
<span style="color:blue">10243</span>
<span style="color:blue">MarginPrice</span>
<span style="color:blue">N</span>
<span style="color:blue">N14(5)</span>
<span style="color:blue">仅适用于竞买多主体成交</span>
- 34 -

技术文档
3
文件接收
同《 IS120 上海证券交易所行情网关 BINARY 数据接口规范》中的文件接收章节。
- 35 -

技术文档
4
转发行情
同《 IS120 上海证券交易所行情网关 BINARY 数据接口规范》中的转发行情章节。
- 36 -

技术文档
5
后记
上海证券交易所对本文档享有知识产权，未经上海证券交易所书面许可，任何单位和个人不
得将本文档用于其他商业目的。
本文档编写过程中，深受证券业界信息技术同仁讨论启发，特此致谢。对本文档有任何批评
指正意见，可通过电子邮件或服务电话进行反馈。
电子邮件： tech_support@sse.com.cn
服务电话： 4008888400-2
网站地址： https://www.sse.com.cn/ - 交易技术支持专区
通讯地址：上海市浦东新区浦东南路 528 号上交所技术公司技术开发总部
- 37 -

技术文档
附录一
计算校验和
以下为计算校验和的代码段：
const char* CalcChecksum(const char* buffer, uint32 len, char buffChecksum[4])
{
uint8 checksum = 0;
uint32 i = 0;
for (i = 0; i < len; i++)
{
checksum += (uint8)buffer[i];
}
sprintf(buffChecksum, “%03d”, checksum );
return bufCheckSum;
}
- 38 -

> **变更标注说明**：本文档中已用 `<span style="color:...">` 标注了变更内容（红色=修改/新增，蓝色=其他说明）。


<metadata>
{
  "title": "IS120_上海证券交易所行情网关STEP数据接口规范",
  "source_url": null,
  "raw_path": "knowledge\\raw\\sse\\技术接口\\20260612_IS120_上海证券交易所行情网关STEP数据接口规范0.61版_20260612.pdf",
  "markdown_path": "knowledge\\articles\\sse\\markdown\\技术接口\\IS120_上海证券交易所行情网关STEP数据接口规范0.61版_20260612.md",
  "file_hash": "sha256:0f0cc5f4638536f2ecbf330e65b65d706ac1bd0fd7d9122c9b37b826b78aa7c3",
  "file_format": "pdf",
  "page_count": 44,
  "doc_type": "interface_spec",
  "version": null,
  "previous_version": null,
  "public_date": "2026-05-11",
  "effective_date": null,
  "has_changes": true,
  "parse_status": "success",
  "parse_date": "2026-06-13T17:43:55.212900+00:00",
  "sub_category": null
}
</metadata>