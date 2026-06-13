上海证券交易所技术文档
IS120 上海证券交易所行情网关
BINARY 数据接口规范
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
<span style="color:blue">3</span> <span style="color:blue">、添加了固收迁移互联网平台后新增行情信息（含债券非匹配</span>
<span style="color:blue">成交快照行情及各类逐笔行情等）。</span>
<span style="color:blue">4</span> <span style="color:blue">、移除原固收文件行情接口包括：</span> <span style="color:blue">se015cjhqYYYMMDD001.txt</span>
<span style="color:blue">（固收成交行情文件）、</span> <span style="color:blue">se015cjmxYYYMMDD001.txt</span> <span style="color:blue">（固收成交</span>
<span style="color:blue">明细文件）、</span> <span style="color:blue">se015qdbjYYYMMDD001.txt</span> <span style="color:blue">（固收确定报价文件）</span>
<span style="color:blue">和</span> <span style="color:blue">se015zqxxYYYMMDD001.txt</span> <span style="color:blue">（固收证券信息文件）。</span>
5 、 <span style="color:blue">[新增] 新增接收</span> <span style="color:blue">products_yyyymmdd.xml</span> <span style="color:blue">（证券产品基础信息文件）、</span>
<span style="color:blue">bondmbrs_yyyymmdd.xml</span> <span style="color:blue">（债券交易参与人信息文件）和</span>
<span style="color:blue">bondtrdrs_yyyymmdd.xml</span> <span style="color:blue">（债券交易员信息文件）。</span>
2026-03-20
0.60
配合 txt 版 ETF 定义文件下线，删除相关描述。
2025-10-17
0.59
支持 ETF 公告文件 xml 版，调整 2.4.2.2 集中竞价类行情快照扩
展字段章节 IOPV 行情与 ETF 公告文件关联关系描述。
2025-08-01
0.58
在市场状态消息（ MsgType=M101 ）、行情快照消息
（ MsgType=M102 ）中增加独立 IOPV 行情描述。
2023-08-14
0.57
1 、明确 PreCloseIOPV （基金 T-1 日收盘时刻 IOPV ）、 IOPV （基
金 IOPV ）字段适用范围以及和 ETF 公告文件的关联关系。

2 、增加基金通行情接收相关描述。
2022-04-13
0.56
增加期权基础信息第二版文件接收相关描述。
2022-03-21
0.55
增加 B 转 H 行情文件接收相关描述。
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
引言 ................................................................................................................................................... 1
1.1
名词释义 ................................................................................................................................1
2
BINARY 实时行情 ...........................................................................................................................2
2.1
会话机制 ................................................................................................................................2
2.1.1
消息序号 .....................................................................................................................3
2.1.2
会话安全 .....................................................................................................................3
2.1.3
建立行情会话 .............................................................................................................4
2.1.4
行情数据发布 .............................................................................................................4
2.1.5
关闭行情会话 .............................................................................................................4
2.1.6
心跳 .............................................................................................................................4
2.1.7
行情网关主动关闭行情会话的情况 .........................................................................5
2.2
协议介绍 ................................................................................................................................5
2.2.1
字段说明 .....................................................................................................................5
2.2.2
BINARY 消息头 .........................................................................................................6
2.2.3
BINARY 消息尾 .........................................................................................................6
2.3
会话消息 ................................................................................................................................8
2.3.1
登录消息（ MsgType=S001 ） ................................................................................... 8
2.3.2
注销消息（ MsgType=S002 ） ................................................................................... 8
2.3.3
心跳消息（ MsgType=S003 ） ................................................................................... 9
2.4
公共消息 ..............................................................................................................................10

2.4.1
频道心跳（ MsgType=P001 ） ................................................................................. 10
2.4.2
重传消息（ MsgType=P002 ） ................................................................................. 10
2.5
应用消息 ..............................................................................................................................12
2.5.1
应用消息通用约定 ...................................................................................................12
2.5.2
市场状态消息（ MsgType=M101 ） ........................................................................14
2.5.3
行情快照消息（ MsgType=M102 ） ........................................................................16
2.5.4
逐笔行情消息（ MsgType=M201 ） ........................................................................25
3
文件接收 ......................................................................................................................................... 31
4
转发行情 ......................................................................................................................................... 33
后记 ...................................................................................................................................................... 34

技术文档
1
引言
上海证券交易所行情网关数据接口规范包括 BINARY 与 STEP 两卷，本卷主要介绍 BINARY
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
- 1 -

技术文档
2
BINARY 实时行情
本章描述市场参与者与信息服务商等用户行情系统，通过 BINARY 协议接入上海证券交易
所行情网关 MDGW 进行行情数据传输的机制和相关数据交换格式。
2.1
会话机制
用户行情系统（ VSS ）通过 TCP 方式接收行情网关（ MDGW ）发布的流式行情。
交互示意图如下：
V SS
M D G W
建立TC P连接
TC P 连接
连接接受
登录消息(M sgType= S001)
登录请求
登录失败(M sgType= S002)
登录处理
登录成功(M sgType= S001)
心跳消息(M sgType= S003)
发送心跳
心跳消息(M sgType= S003)
心跳响应
频道心跳（M sgType= P001）
频道心跳接收
市场状态消息（M sgType= M 101）
市场状态接收
业务消息
行情快照消息（M sgType= M 102）
行情快照接收
逐笔行情消息（M sgType= M 201）
逐笔行情接收
注销消息(M sgType= S002)
发送注销请求
注销处理
注销消息(M sgType= S002)
BINARY 协议交互图 <span style="color:blue">（业务消息）</span>
- 2 -

技术文档
V SS
M D G W
建立TC P连接
TC P连接
连接接受
登录消息(M sgType= S001)
登录请求
登录处理
登录失败(M sgType= S002)
登录成功(M sgType= S001)
心跳消息(M sgType= S003)
发送心跳
心跳消息(M sgType= S003)
心跳响应
重传消息(M sgType= P002)
发送重传请求
逐笔行情消息(M sgType= M 201)
重传处理
重传消息(M sgType= P002)
注销消息(M sgType= S002)
发送注销请求
注销处理
注销消息(M sgType= S002)
<span style="color:blue">BINARY</span> <span style="color:blue">协议交互图（重传消息）</span>
2.1.1
消息序号
会话双方收发的每条消息都被分配有一个消息序号 MsgSeqNum 来唯一标识。参与通信的每
一端都需要维护一对序号（ NxtIn, NxtOut ）， NxtIn 表示下一个期望的入向消息序号， NxtOut 表
示下一个出向消息序号。消息序号一般在每次会话过程中从 1 开始，在整个会话过程中连续递增，
直到该会话过程全部结束。
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
VSS 发送的第一个消息必须是登录消息，如果 VSS 登录成功，则 MDGW 发送一个登录消
息作为应答。如果 VSS 登录失败， MDGW 则在发送一个含失败说明的注销消息后由 VSS 主动
关闭连接。 VSS 必须在收到 MDGW 的登录消息之后才允许发送其他消息。
2.1.4
行情数据发布
在完成建立行情会话之后， MDGW 将向 VSS 发送行情数据消息。行情数据消息格式将在 <span style="color:blue">第</span>
<span style="color:blue">5</span> <span style="color:blue">章</span> “ 应用消息 ” 中详细叙述。 MDGW 目前发布的行情 <span style="color:blue">快照消息不支持重传，逐笔行情消息支持</span>
<span style="color:blue">重传应用消息不支持重传</span> 。
2.1.5
关闭行情会话
行情会话的正常关闭是通过连接双方互相发送注销消息完成的。 MDGW 和 VSS 均可以主动
发送注销消息，接收方需要回传注销消息作为应答。如果超过预定时间（一般为 5 秒）没有收到
对方回传的注销消息，任何一方均有权主动关闭连接。
2.1.6
心跳
连接双方在数据发送的空闲期间应主动发送心跳消息，通过心跳消息可以监控行情会话的状
- 4 -

技术文档
态。心跳最小间隔由登录消息中的 HeartBtIntl 域确定。
连接双方在发送任何消息后，应立即重新设置心跳间隔计时器。如果 VSS 超过 2 个 HeartBtIntl
指定周期没有收到 MDGW 发送的任何消息，则行情会话被视为可能存在异常， VSS 需要重新建
立行情会话。
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
每条 BINARY 消息由消息头、消息体和消息尾组成，消息最大长度为 8K 字节。
2.2.1
字段说明
所有数值型字段采用高字节序（ BIG_ENDIAN ）编码。字段类型说明如下：
类型
说明
char[x]
代表该字段为字符串， x 代表该字符串的最大字节数， x 为大于零的数字，例如
char[5] 代表最大长度为 5 字节的字符串；当最大长度大于实际长度时，右补空格。
字符串使用 GBK 编码。
- 5 -

技术文档
int 、 uint
代表该字段为整型数值，如 uint32 表示 32 位无符号整数， int64 表示 64 位有符
号整数
Nx 、 Nx(y)
与 int 、 uint 一并使用，用于给出该整型数值实际表示的业务字段的长度（精度） :
Nx 代表最大长度为 x 位数字的整数； Nx(y) 代表最大长度为 x 位数字，其中最末
y 位数字为小数部分。
2.2.2
BINARY 消息头
每一个会话或应用消息都有一个消息头，该消息头指明消息类型、消息体长度、消息序号和
发送时间等信息。
消息头格式如下：
域名
说明
类型
MsgType
消息类型
char[4]
SendingTime
发送时间，格式： YYYYMMDDHHmmSSsss
uint64
MsgSeqNum
消息序号
uint64
BodyLength
消息体长度
uint32
说明：
1.
当消息为市场状态消息或行情快照消息 <span style="color:blue">或逐笔行情消息</span> 时， SendingTime 为交易所时间。
2.2.3
BINARY 消息尾
每一个会话或应用消息都有一个消息尾，并以此终止。
消息尾包含一个 CheckSum 字段，其值是计算从消息头开始（包括消息头）到消息体结束的
校验和。计算校验和的代码段可参考附录一 “ 计算校验和 ” 。
消息尾格式如下：
- 6 -

技术文档
域名
说明
类型
CheckSum
校验和
uint32
- 7 -

技术文档
2.3
会话消息
会话消息格式将在以下各节中予以介绍，并定义会话消息格式。
连接双方均可生成会话消息。
2.3.1
登录消息（ MsgType=S001 ）
登录消息应是在行情会话开始时 VSS 发送的第一个消息。 MDGW 只作为登录的接受方，
不会作为登录的发起方。
HeartBtInt 域用来指定心跳消息的发送时间间隔，必须设置为大于 0 的整数。 VSS 需要在登
录消息中填入预期的心跳时间间隔， MDGW 在回传登录消息时返回的 HeartBtInt 域作为协商后
的心跳时间间隔。
登录请求消息格式如下：
域名
说明
类型
标准消息头
MsgType = S001
SenderCompID
发送方代码
char[32]
TargetCompID
接收方代码
char[32]
HeartBtInt
心跳间隔，单位为秒
uint16
char[8]
ApplVerID
协议版本，格式为 mm.nn ，其中 mm 为主版本号， nn 为子版本
号，如 0.30 ， 12.22
标准消息尾
2.3.2
注销消息（ MsgType=S002 ）
注销消息是发起或确认行情会话终止的消息。未经注销消息交换而断开连接，一律视为非正
- 8 -

技术文档
常的断开。
连接双方在发送注销消息之后不应发送任何消息。
注销消息格式如下：
域名
说明
类型
标准消息头
MsgType = S002
uint32
SessionStatus
Logout 时的会话状态
0
正常注销
【 1– 999 】一般情况注销，重连可以恢复
【 1000 – 9999 】严重情况注销，建议切换服务器
Text
文本
char[256]
标准消息尾
2.3.3
心跳消息（ MsgType=S003 ）
心跳消息用于监控通信连接的状况。
当连接的任何一方在心跳时间间隔（由 HeartBtInt 域指定）时间内没有接收或发送任何数据
的时候，需要产生一个心跳消息并发送出去。如果接收方在 2 倍心跳时间间隔内都没有收到任
何消息的时候，那么可认为行情会话出现异常，可以立即关闭 TCP 连接。
心跳消息格式如下：
域名
说明
类型
标准消息头
MsgType = S003, BodyLength =0
标准消息尾
- 9 -

技术文档
<span style="color:blue">2.4</span>
<span style="color:blue">公共消息</span>
<span style="color:blue">2.4.1</span>
<span style="color:blue">频道心跳（</span> <span style="color:blue">MsgType=P001</span> <span style="color:blue">）</span>
<span style="color:blue">逐笔行情支持在数据发送的空闲期间每</span> <span style="color:blue">3</span> <span style="color:blue">秒发送一次心跳，如数据一直处于发送忙状态，则</span>
<span style="color:blue">可能出现频道心跳超过</span> <span style="color:blue">3s</span> <span style="color:blue">。</span>
<span style="color:blue">域名</span>
<span style="color:blue">说明</span>
<span style="color:blue">类型</span>
<span style="color:blue">标准消息头</span>
<span style="color:blue">MsgType=P001</span>
<span style="color:blue">uint8</span>
<span style="color:blue">SecurityType</span>
<span style="color:blue">证券类型</span>
<span style="color:blue">13 =</span> <span style="color:blue">债券（非匹配成交）</span>
<span style="color:blue">频道号</span>
<span style="color:blue">ChannelNO</span>
<span style="color:blue">uint16, N4</span>
<span style="color:blue">100 =</span> <span style="color:blue">非匹配成交逐笔行情</span>
<span style="color:blue">该频道已发布的最大消息记</span>
<span style="color:blue">ApplLastSeqNum</span>
<span style="color:blue">uint64</span>
<span style="color:blue">录号</span>
<span style="color:blue">频道结束标志</span>
<span style="color:blue">Y =</span> <span style="color:blue">行情更新已结束</span>
<span style="color:blue">EndOfChannel</span>
<span style="color:blue">char[1]</span>
<span style="color:blue">N =</span> <span style="color:blue">行情更新未结束</span>
<span style="color:blue">标准消息尾</span>
<span style="color:blue">2.4.2</span>
<span style="color:blue">重传消息（</span> <span style="color:blue">MsgType=P002</span> <span style="color:blue">）</span>
<span style="color:blue">重传消息用于请求可重传频道下的行情数据。</span>
<span style="color:blue">针对可重传的应用类消息(各类逐笔行情消息)，若应用类消息缺失，用户可向上发送重传消</span>
<span style="color:blue">息，代表重传请求。上游以“请求-应答”的方式处理重传请求，根据重传消息中指定的起始、</span>
- 10 -

技术文档
<span style="color:blue">结束序号返回需要重传的数据，并在重传完成后返回一个重传消息，告知重传完成；若重传失</span>
<span style="color:blue">败，则返回一个重传消息，告知重传失败。上游系统仅支持一个缺口消息正在重传，当上游收</span>
<span style="color:blue">到多个重传请求时，其他请求消息会返回重传失败。</span>
<span style="color:blue">对于逐笔行情数据可通过频道代码和消息记录号判断是否有消息丢失，当收到的消息记录</span>
<span style="color:blue">号</span> <span style="color:blue"><=</span> <span style="color:blue">本频道已经收到的最大消息记录号时，说明已经收到过该消息，此时应忽略该消息。当收</span>
<span style="color:blue">到的消息记录号</span> <span style="color:blue">></span> <span style="color:blue">已经收到的最大消息记录号</span> <span style="color:blue">+1</span> <span style="color:blue">（如已收的最大消息记录号</span> <span style="color:blue">=100</span> <span style="color:blue">，新的消息记录</span>
<span style="color:blue">号</span> <span style="color:blue">=102</span> <span style="color:blue">）说明发生了消息丢失，此时应通过发送重传请求恢复丢失的数据。</span>
<span style="color:blue">域名</span>
<span style="color:blue">说明</span>
<span style="color:blue">类型</span>
<span style="color:blue">标准消息头</span>
<span style="color:blue">MsgType=P002</span>
<span style="color:blue">频道号</span>
<span style="color:blue">uint16,</span>
<span style="color:blue">ChannelNO</span>
<span style="color:blue">N4</span>
<span style="color:blue">100 =</span> <span style="color:blue">非匹配成交逐笔行情</span>
<span style="color:blue">重传类别</span>
<span style="color:blue">ResendType</span>
<span style="color:blue">uint8</span>
<span style="color:blue">1 =</span> <span style="color:blue">逐笔行情</span>
<span style="color:blue">重传起始消息记录号</span>
<span style="color:blue">ApplBegSeqNum</span>
<span style="color:blue">uint64</span>
<span style="color:blue">取值大于</span> <span style="color:blue">0</span>
<span style="color:blue">重传结束消息记录号</span>
<span style="color:blue">当取值为</span> <span style="color:blue">0</span> <span style="color:blue">时，交易所会将此字段设置为该频道已发布的最大消息</span>
<span style="color:blue">ApplEndSeqNum</span>
<span style="color:blue">uint64</span>
<span style="color:blue">记录号；应答时取值为实际传输的最大消息记录号。</span>
<span style="color:blue">仅在重传应答消息中有效，取值如下：</span>
<span style="color:blue">1 =</span> <span style="color:blue">全部完成</span>
<span style="color:blue">ResendStatus</span>
<span style="color:blue">uint8</span>
<span style="color:blue">2 =</span> <span style="color:blue">部分完成（有部分请求的数据未返回）</span>
- 11 -

技术文档
<span style="color:blue">3 =</span> <span style="color:blue">无权限</span>
<span style="color:blue">4 =</span> <span style="color:blue">数据不可用</span>
<span style="color:blue">5 =</span> <span style="color:blue">重传请求正在处理中</span>
<span style="color:blue">99 =</span> <span style="color:blue">其他</span>
<span style="color:blue">仅在重传应答消息中有效。</span>
<span style="color:blue">RejectText</span>
<span style="color:blue">char[32]</span>
<span style="color:blue">填写重传拒绝的原因（如有）。</span>
<span style="color:blue">标准消息尾</span>
<span style="color:blue">注：</span>
<span style="color:blue">1</span> <span style="color:blue">、</span> <span style="color:blue">VSS</span> <span style="color:blue">应主动缓存逐笔消息，避免频繁发送重传请求，禁止定时或不必要的反复进行重传数据行为。</span>
<span style="color:blue">2</span> <span style="color:blue">、建议每次请求回补的数据不大于</span> <span style="color:blue">200</span> <span style="color:blue">条。</span>
<span style="color:blue">3</span> <span style="color:blue">、当收到</span> <span style="color:blue">ResendStatus=2</span> <span style="color:blue">的重传应答时，建议对于未传输数据重新发起重传请求。</span>
<span style="color:blue">4</span> <span style="color:blue">、对于无效字段，字符类型字段填空格，数值类型字段填</span> <span style="color:blue">0</span> <span style="color:blue">。</span>
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
<span style="color:blue">1</span>
<span style="color:blue">MD003</span>
<span style="color:blue">债券分销类产品</span>
<span style="color:blue">MD004</span>
<span style="color:blue">基金类产品（含公募</span> <span style="color:blue">REITs</span> <span style="color:blue">）</span>
<span style="color:blue">2</span>
<span style="color:blue">MD301</span>
<span style="color:blue">期权类产品</span>
- 12 -

技术文档
<span style="color:blue">MD101</span>
<span style="color:blue">国债预发行产品</span>
<span style="color:blue">3</span>
<span style="color:blue">MD102</span>
<span style="color:blue">盘后固定价格</span>
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
<span style="color:blue">d)</span>
<span style="color:blue">对于债券分销，成交金额为每笔成交的</span> <span style="color:blue">“</span> <span style="color:blue">价格</span> <span style="color:blue">*</span> <span style="color:blue">数量</span> <span style="color:blue">*10”</span> <span style="color:blue">的总和；对于债券现券，成交金额为每笔</span>
<span style="color:blue">成交的</span> <span style="color:blue">“</span> <span style="color:blue">价格</span> <span style="color:blue">*</span> <span style="color:blue">数量</span> <span style="color:blue">*10”</span> <span style="color:blue">的总和；对于通用质押式回购，成交金额为</span> <span style="color:blue">100*</span> <span style="color:blue">成交数量</span> <span style="color:blue">*10</span> <span style="color:blue">。</span>
<span style="color:blue">1</span> <span style="color:blue">包含债券现券匹配成交及质押式回购类产品。</span>
<span style="color:blue">2</span> <span style="color:blue">包含债券现券非匹配成交、协议回购、三方回购产品。</span>
- 13 -

技术文档
2.5.2
市场状态消息（ MsgType=M101 ）
市场状态消息用于交易所发布市场状态和产品数量等信息，会周期性发布以及在市场状态变
化时发布。
市场状态消息的格式如下：
域名
说明
类型
标准消息头
MsgType=M101
uint8
SecurityType
证券类型
1 = 股票、基金、指数及债券分销
2 = 衍生品
3 = 综合业务
12 = 债券 <span style="color:blue">（匹配成交）</span>
<span style="color:blue">13 =</span> <span style="color:blue">债券（非匹配成交）</span>
14 = 外部源行情
uint8
TradSesMode
交易盘交易模式
1 = 系统测试
2 = 模拟交易
3 = 产品（正常交易）
char[8]
TradingSessionID
市场行情状态：
该字段为 8 位字符串，左起每位表示特定的含义，无定义则填空格。
TotNoRelatedSym
最大产品数目（包括指数）
uint32
标准消息尾
- 14 -

技术文档
说明：
1. 衍生品指期权业务；
2. 综合业务指国债预发行、盘后固定价格交易业务；
3. 市场行情状态 (TradingSessionID) 为 8 位字符串，左起每位表示特定的含义，无定义则填空格。该字段
具体含义在不同证券类型时说明如下：
SecurityType = 1 3
第 1 位
‘S’ 表示全市场启动期间（开市前）
‘T’ 表示全市场处于交易期间（含中间休市）
‘E’ 表示全市场处于闭市期间
第 2 位
‘1’ 表示开盘集合竞价结束标志，未结束取 ‘0’
第 3 位
‘1’ 表示全市场行情结束标志，未结束取 ‘0’
第 4 位
‘1’ 表示上海市场行情结束标志，未结束取 ‘0’
SecurityType = 2
第 1 位
‘S’ 表示期权市场启动期间（开市前）
‘T’ 表示期权市场处于交易期间（含中间休市）
‘E’ 表示期权市场处于闭市期间
第 2 位
‘1’ 表示期权市场开盘集合竞价结束标志，未结束取 ‘0’
第 3 位
‘1’ 表示期权市场行情闭市标志，未闭市取 ‘0’
SecurityType = 3
第 1 位
‘S’ 表示综合业务市场启动期间（开市前）
‘T’ 表示综合业务市场处于交易期间（含中间休市）
‘E’ 表示综合业务市场处于闭市期间
第 2 位
‘1’ 表示综合业务市场开盘集合竞价结束标志，未结束取 ‘0’
第 3 位
‘1’ 表示综合业务市场收盘集合竞价结束标志，未结束取 ‘0’
第 4 位
‘1’ 表示国债预发行市场行情闭市标志，未闭市取 ‘0’
第 5 位
‘1’ 表示盘后固定价格交易行情闭市标志，未闭市取 ‘0’
3 SecurityType = 1 时，上海市场包括股票、基金、债券分销。全市场包括上海市场及指数。
- 15 -

技术文档
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
‘1’ 表示债券质押式回购、债券现券（除可转债及新标准券）行情结束标志，未结束取 ‘0’
<span style="color:blue">SecurityType = 13</span> <span style="color:blue">5</span>
<span style="color:blue">第</span> <span style="color:blue">1</span> <span style="color:blue">位</span>
<span style="color:blue">‘S’</span> <span style="color:blue">表示债券市场启动期间（开市前）</span>
<span style="color:blue">‘T’</span> <span style="color:blue">表示债券市场处于交易期间（含中间休市）</span>
<span style="color:blue">‘E’</span> <span style="color:blue">表示债券市场处于闭市期间</span>
<span style="color:blue">第</span> <span style="color:blue">2</span> <span style="color:blue">位</span>
<span style="color:blue">无意义</span>
<span style="color:blue">第</span> <span style="color:blue">3</span> <span style="color:blue">位</span>
<span style="color:blue">‘1’</span> <span style="color:blue">表示债券市场行情结束标志，未结束取</span> <span style="color:blue">‘0’</span>
<span style="color:blue">第</span> <span style="color:blue">4</span> <span style="color:blue">位</span>
<span style="color:blue">‘1’</span> <span style="color:blue">表示债券现券（可转债）行情结束标志，未结束取</span> <span style="color:blue">‘0’</span>
<span style="color:blue">第</span> <span style="color:blue">5</span> <span style="color:blue">位</span>
<span style="color:blue">‘1’</span> <span style="color:blue">表示协议回购、三方回购、债券现券（除可转债）等行情结束标志，未结束取</span> <span style="color:blue">‘0’</span> <span style="color:blue">。</span>
SecurityType = 14
第 1 位 - 第 8 位
全空格
2.5.3
行情快照消息（ MsgType=M102 ）
行情快照消息用于发布证券产品行情 , 交易所会周期性发布全量快照消息以及在行情变化时
发送增量快照消息。多条快照消息之间无数据依赖性， VSS 无需区分全量 / 增量消息，可直接替
换当前数据。
4 SecurityType = 12 时，债券市场 <span style="color:blue">（匹配成交）</span> 包含债券现券及质押式回购。
<span style="color:blue">5</span> <span style="color:blue">SecurityType = 13</span> <span style="color:blue">时，债券市场（非匹配成交）包含债券现券、协议回购、三方回购等。</span>
- 16 -

技术文档
消息格式如下：
域名
说明
类型
标准消息头
MsgType=M102
uint8
SecurityType
证券类型
1 = 股票、基金、指数及债券分销
2 = 衍生品
3 = 综合业务
12 = 债券 <span style="color:blue">（匹配成交）</span>
<span style="color:blue">13 =</span> <span style="color:blue">债券（非匹配成交）</span>
14 = 外部源行情
uint8
TradSesMode
交易盘交易模式
1 = 系统测试
2 = 模拟交易
3 = 产品（正常交易）
TradeDate
交易日期 YYYYMMDD
uint32, N8
LastUpdateTime
最新更新时间 HHMMSSsss
uint32, N9
MDStreamID
行情类别
char[5]
SecurityID
产品代码
char[8]
Symbol
产品简称
char[8]
PreClosePx
昨收盘
uint64, N13(5)
TotalVolumeTraded
成交数量
uint64, N16
- 17 -

技术文档
NumTrades
成交笔数
uint64, N16
TotalValueTraded
成交金额
uint64, N16(2)
TradingPhaseCode
实时阶段及标志
char[8]
ExtendFields
扩展字段
标准消息尾
说明：
<span style="color:blue">字段无意义或无该字段行情数据时，字符填空格，数值填</span> <span style="color:blue">0</span> <span style="color:blue">；数值字段取值超过约定格式最大值时，取最</span>
<span style="color:blue">大值，如</span> <span style="color:blue">N10</span> <span style="color:blue">取</span> <span style="color:blue">9999999999</span> <span style="color:blue">；</span>
<span style="color:blue">行情类别</span> <span style="color:blue">(MDStreamID)</span> <span style="color:blue">及其扩展字段如下：</span>
<span style="color:blue">SecurityType</span>
<span style="color:blue">MDStreamID</span>
<span style="color:blue">说明</span>
<span style="color:blue">ExtendFields</span>
<span style="color:blue">MD001</span>
<span style="color:blue">指数类产品</span>
<span style="color:blue">详见</span> <span style="color:blue">2.4.2.1</span> <span style="color:blue">节</span>
<span style="color:blue">MD002</span>
<span style="color:blue">股票（</span> <span style="color:blue">A</span> <span style="color:blue">、</span> <span style="color:blue">B</span> <span style="color:blue">股）类产品</span>
<span style="color:blue">详见</span> <span style="color:blue">2.4.2.2</span> <span style="color:blue">节</span>
<span style="color:blue">1</span>
<span style="color:blue">MD003</span>
<span style="color:blue">债券分销类产品</span>
<span style="color:blue">MD004</span>
<span style="color:blue">基金类产品（含公募</span> <span style="color:blue">REITs</span> <span style="color:blue">）</span>
<span style="color:blue">2</span>
<span style="color:blue">MD301</span>
<span style="color:blue">期权类产品</span>
<span style="color:blue">MD101</span>
<span style="color:blue">国债预发行产品</span>
<span style="color:blue">3</span>
<span style="color:blue">MD102</span>
<span style="color:blue">盘后固定价格</span>
<span style="color:blue">12</span>
<span style="color:blue">MD201</span>
<span style="color:blue">债券类产品</span> <span style="color:blue"></span>
<span style="color:blue">14</span>
<span style="color:blue">MDE01</span>
<span style="color:blue">IOPV</span>
1.
当 SecurityType = 14 且 MDStreamID =MDE01 时， PreClosePx 昨收盘、 TotalVolumeTraded 成交数量、
NumTrades 成交笔数、 TotalValueTraded 成交金额字段取值为 0 ， TradingPhaseCode 实时阶段及标志取
值为空。
<span style="color:blue">对数量单位说明如下：</span>
<span style="color:blue">产品价格、金额单位，除</span> <span style="color:blue">B</span> <span style="color:blue">股为美元外，其他为人民币元；</span>
<span style="color:blue">指数的成交数量</span> <span style="color:blue">(TradeVolume)</span> <span style="color:blue">为参与计算相应指数的交易数量，股票指数交易数量单位是</span> <span style="color:blue">100</span> <span style="color:blue">股，基</span>
<span style="color:blue">金指数的交易数量单位是</span> <span style="color:blue">100</span> <span style="color:blue">份，债券指数的交易数量单位是千元面额；指数成交金额</span>
- 18 -

技术文档
<span style="color:blue">(TotalValueTraded)</span> <span style="color:blue">为参与计算相应指数的成交金额；</span>
<span style="color:blue">各类产品数量与成交数量单位，股票为股，基金、公募</span> <span style="color:blue">REITs</span> <span style="color:blue">为份，债券与回购为千元面额，期权合</span>
<span style="color:blue">约的数量单位为张；</span>
<span style="color:blue">对于债券分销，成交金额为每笔成交的</span> <span style="color:blue">“</span> <span style="color:blue">价格</span> <span style="color:blue">*</span> <span style="color:blue">数量</span> <span style="color:blue">*10”</span> <span style="color:blue">的总和；对于债券现券，成交金额为每笔成交</span>
<span style="color:blue">的</span> <span style="color:blue">“</span> <span style="color:blue">价格</span> <span style="color:blue">*</span> <span style="color:blue">数量</span> <span style="color:blue">*10”</span> <span style="color:blue">的总和；对于质押式回购，成交金额为</span> <span style="color:blue">100*</span> <span style="color:blue">成交数量</span> <span style="color:blue">*10</span> <span style="color:blue">。</span>
2.
实时阶段及标志 (TradingPhaseCode) 为 8 位字符串，左起每位表示特定的含义，无定义则填空格。该
字段具体含义在不同行情类别时说明如下：
SecurityType = 1, MDStreamID= MD001
全为空格（预留）
SecurityType = 1, MDStreamID= MD002 ， MD003 ， MD004
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
‘1’ 表示此产品可正常交易。
在产品进入开盘集合竞价、连续交易、收盘集合竞价、熔断（盘中集合竞价）状态时值为 ‘1’ ，
在产品进入停牌、熔断（暂停交易至闭市）状态时值为 ‘0’ ，且闭市后保持该产品闭市前的是
否可正常交易状态。
第 3 位
‘0’ 表示未上市
‘1’ 表示已上市
第 4 位
‘0’ 表示此产品在当前时段不接受进行新订单申报
‘1’ 表示此产品在当前时段可接受进行新订单申报。
仅在交易时段有效，在非交易时段无效。
- 19 -

技术文档
SecurityType = 2, MDStreamID= MD301
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
‘1’ 表示此产品在当前时段可接受进行新订单申报。
仅在交易时段有效，在非交易时段无效
- 20 -

技术文档
SecurityType = 3, MDStreamID= MD101
第 1 位
‘S’ 表示启动（开市前）时段
‘C’ 表示集合竞价时段
‘T’ 表示连续交易时段
‘E’ 表示闭市时段
‘P’ 表示停牌
SecurityType = 3, MDStreamID= MD102
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
在产品进入开盘集合竞价、连续交易状态时值为 ‘1’ ，在产品进入停牌状态时值为 ‘0’ ，且闭
市后保持该产品闭市前的是否可正常交易状态。
第 3 位
‘0’ 表示未上市
‘1’ 表示已上市
第 4 位
‘0’ 表示此产品在当前时段不接受进行新订单申报
‘1’ 表示此产品在当前时段可接受进行新订单申报
仅在交易时段有效，在非交易时段无效。
<span style="color:blue">SecurityType = 13, MDStreamID= MD210</span>
- 21 -

技术文档
<span style="color:blue">第</span> <span style="color:blue">1</span> <span style="color:blue">位</span>
<span style="color:blue">无意义</span>
<span style="color:blue">第</span> <span style="color:blue">2</span> <span style="color:blue">位</span>
<span style="color:blue">‘0’</span> <span style="color:blue">表示当前处于停牌状态</span>
<span style="color:blue">‘1’</span> <span style="color:blue">表示当前未处于停牌状态</span>
SecurityType = 14, MDStreamID= MDE01
第 1 位 - 第 8 位
全空格
2.5.3.1 指数行情快照扩展字段
域名
说明
类型
NoMDEntries
行情条目个数
uint16, N5
char[2]

MDEntryType
行情条目类别
3 ＝最新指数
4 ＝今开盘指数
5 ＝今收盘指数
7 ＝最高指数
8 ＝最低指数

MDEntryPx
指数点位
uint64, N13(5)
说明：
1.
适用于 MDStreamID=MD001 时。
- 22 -

技术文档
2.5.3.2 <span style="color:blue">集中竞价类</span> 行情快照扩展字段
域名
说明
类型
NoMDEntries
行情条目个数
uint16, N5
行情条目类别
0= 买入
1= 卖出
2= 最新成交价
4= 今开盘价
5= 今收盘价
6 ＝今结算价
7 ＝当日最高成交价

MDEntryType
char[2]
8 ＝当日最低成交价
<span style="color:blue">9</span> <span style="color:blue">＝当日成交均价</span>
v ＝ IOPV
w= 前一日 IOPV
x ＝动态参考价格及虚拟匹配数量
z1= 昨日结算价
z2= 总持仓量
<span style="color:blue">z3=</span> <span style="color:blue">昨日成交均价</span>

MDEntryPx
价格
uint64, N13(5)

MDEntrySize
数量
uint64, N12
买卖盘序号 , 对应五档买入卖出价量

MDEntryPositionNo
的档位信息
uint8, N2
说明：
1.
适用于 MDStreamID=MD002 、 MD003 、 MD004 、 MD101 、 MD102 、 MD301 、 MD201 、 MDE01 <span style="color:blue">、</span> <span style="color:blue">MD210</span>
- 23 -

技术文档
时；
2.
行情条目类别为 0 或 1 时，表示该条目为买卖盘档位，此时 MDEntryPx 、 MDEntrySize 、
MDEntryPositionNo 分别表示买卖价格、数量和档位序号， MDEntryPositionNo 从 0 开始计数；
3.
行情条目类别为 w 时， MDEntryPx 表示基金 T-1 日收盘时刻 IOPV 6 ，此条目仅当 MDStreamID= MD004
时有意义，当 MDStreamID= MDE01 时无意义；行情条目类别为 v 时， MDEntryPx 表示基金 IOPV 7 ，
此条目仅当 MDStreamID= MD004 或 MDE01 时有意义；
4.
行情条目类别为 x 时 , MDEntryPx 表示动态参考价格、 MDEntrySize 表示虚拟匹配数量，仅当
MDStreamID=MD301 时有意义；
<span style="color:blue">5.</span>
行情条目类别为 z2 时， MDEntrySize 表示期权合约总持仓量，单位是 ( 张 ) ，仅当 MDStreamID=MD301
时有意义；
6.
<span style="color:blue">行情条目类别为</span> <span style="color:blue">9</span> <span style="color:blue">时，</span> <span style="color:blue">MDEntryPx</span> <span style="color:blue">表示债券非匹配成交的当日成交均价；行情条目类别为</span> <span style="color:blue">z3</span> <span style="color:blue">时，</span>
<span style="color:blue">MDEntryPx</span> <span style="color:blue">表示债券非匹配成交的昨日成交均价；</span>
7.
其他行情条目类别，将仅通过 MDEntryPx 表示相应值，其他字段无意义；
8.
在集合竞价时段内，当前买入价和当前卖出价中同时为虚拟开盘参考价格，即根据集合竞价算法计算
得出的虚拟撮合价格。同时申买量一和申卖量一为行情发布时刻的虚拟匹配量。申买量二为行情发布
时刻的买方虚拟未匹配量。申卖量二为行情发布时刻的卖方虚拟未匹配量；
9.
对期权产品（ MDStreamID=MD301 ），今日结算价通过期权收盘价格文件（ clpr03MMDD.txt ）揭示。
<span style="color:blue">10.</span> 对盘后固定价格行情（ MDStreamID=MD102 ） , 仅今日收盘价、买一数量、卖一数量有意义。其中，
买一数量表示当前未成交的买入申报总股数，卖一数量表示当前未成交的卖出申报总股数 <span style="color:blue">；</span>
11. <span style="color:blue">对债券非匹配成交快照行情（</span> <span style="color:blue">MDStreamID=MD210</span> <span style="color:blue">）</span> <span style="color:blue">,</span> <span style="color:blue">扩展字段中仅最新成交价、今开盘价、今收盘</span>
<span style="color:blue">价、当日最高成交价、当日最低成交价、当日成交均价和昨日成交均价有意义，均仅计入债券非匹配</span>
<span style="color:blue">成交（含点击成交、询价成交、竞买成交和协商成交）的交易；基础字段中前收盘价对于双边挂牌产</span>
<span style="color:blue">品填写其匹配成交收盘价，单边挂牌产品填写其非匹配成交参考价。</span>
<span style="color:blue">对于公募可转债和公募</span> <span style="color:blue">REITs</span> <span style="color:blue">，无当日成交均价、昨日成交均价和今收盘价信息，其今收盘价参考对</span>
<span style="color:blue">应匹配成交行情或盘后文件</span> 。
6 仅对 ETF 产品，此字段有效。该字段取 0 时，无意义。该字段不作除权除息等调整。
7 仅对 ETF 产品，此字段有效。该字段取 0 时，无意义。当 ETF 公告文件 PublishIOPVFlag 字段（是否需要发布 IOPV ）取值
为 1 时，此字段为对应产品的 IOPV 值；当 ETF 公告文件 PublishIOPVFlag 字段取值为 0 时，此字段固定取 0 ，无意义；
- 24 -

技术文档
<span style="color:blue">2.5.4</span>
<span style="color:blue">逐笔行情消息（</span> <span style="color:blue">MsgType=M201</span> <span style="color:blue">）</span>
<span style="color:blue">逐笔行情包括逐笔委托行情和逐笔成交行情，两者按照发生的顺序在一个数据流中发送。</span>
<span style="color:blue">同一个频道内的逐笔委托和逐笔成交消息的消息记录号（</span> <span style="color:blue">ApplSeqNum</span> <span style="color:blue">）统一连续编号，</span> <span style="color:blue">VSS</span> <span style="color:blue">需</span>
<span style="color:blue">通过逐笔序号的连续性判断是否丢包，并通过</span> <span style="color:blue">TCP</span> <span style="color:blue">连接向上发起重传请求。</span>
<span style="color:blue">消息格式如下：</span>
<span style="color:blue">域名</span>
<span style="color:blue">说明</span>
<span style="color:blue">类型</span>
<span style="color:blue">标准消息头</span>
<span style="color:blue">MsgType=M201</span>
<span style="color:blue">uint8</span>
<span style="color:blue">SecurityType</span>
<span style="color:blue">证券类型</span>
<span style="color:blue">13 =</span> <span style="color:blue">债券（非匹配成交）</span>
<span style="color:blue">ChannelNO</span>
<span style="color:blue">频道号</span>
<span style="color:blue">unit16, N4</span>
<span style="color:blue">ApplSeqNum</span>
<span style="color:blue">消息记录号，从</span> <span style="color:blue">1</span> <span style="color:blue">开始计数</span>
<span style="color:blue">uint64, N18</span>
<span style="color:blue">MDStreamID</span>
<span style="color:blue">行情类别</span>
<span style="color:blue">char[5]</span>
<span style="color:blue">SecurityID</span>
<span style="color:blue">产品代码</span>
<span style="color:blue">char[8]</span>
<span style="color:blue">TransactTime</span>
<span style="color:blue">委托或成交的行情生成时间：</span> <span style="color:blue">HHMMSSsss</span>
<span style="color:blue">uint32,N9</span>
<span style="color:blue">char[1]</span>
<span style="color:blue">类型：</span>
<span style="color:blue">对于逐笔委托：</span>
<span style="color:blue">0 =</span> <span style="color:blue">[新增] 新增委托订单</span>
<span style="color:blue">ExecType</span>
<span style="color:blue">4 =</span> <span style="color:blue">[删除] 删除委托订单</span>
<span style="color:blue">对于逐笔成交：</span>
<span style="color:blue">F =</span> <span style="color:blue">成交</span>
- 25 -

技术文档
<span style="color:blue">逐笔委托时表示委托价格，如意向申报时未</span>
<span style="color:blue">填写价格或删除委托订单时，则为</span> <span style="color:blue">0</span> <span style="color:blue">；</span>
<span style="color:blue">Price</span>
<span style="color:blue">uint64,N13(5)</span>
<span style="color:blue">逐笔成交时表示成交价格</span>
<span style="color:blue">逐笔委托时表示委托数量，如意向申报时未</span>
<span style="color:blue">填写数量或删除委托订单时，则为</span> <span style="color:blue">0</span> <span style="color:blue">；</span>
<span style="color:blue">OrderQty</span>
<span style="color:blue">uint64,N15(3)</span>
<span style="color:blue">逐笔成交时表示成交数量</span>
<span style="color:blue">ExtendFields</span>
<span style="color:blue">扩展字段</span>
<span style="color:blue">标准消息尾</span>
<span style="color:blue">2.5.4.1</span> <span style="color:blue">逐笔委托行情扩展字段</span>
<span style="color:blue">域名</span>
<span style="color:blue">说明</span>
<span style="color:blue">类型</span>
<span style="color:blue">char[1]</span>
<span style="color:blue">买卖方向</span>
<span style="color:blue">1 =</span> <span style="color:blue">买</span>
<span style="color:blue">Side</span>
<span style="color:blue">2 =</span> <span style="color:blue">卖</span>
<span style="color:blue">char[18]</span>
<span style="color:blue">订单编号，删除委托时表示被删除订单的</span>
<span style="color:blue">QuoteID</span>
<span style="color:blue">订单编号</span>
<span style="color:blue">报价方交易参与人机构代码</span>
<span style="color:blue">MemberID</span>
<span style="color:blue">char[12]</span>
<span style="color:blue">如发起方选择匿名，填空</span>
<span style="color:blue">报价交易员一债通账户</span>
<span style="color:blue">TraderCode</span>
<span style="color:blue">char[12]</span>
<span style="color:blue">如发起方选择匿名，填空</span>
- 26 -

技术文档
<span style="color:blue">是否全额成交</span>
<span style="color:blue">1 =</span> <span style="color:blue">是</span>
<span style="color:blue">FullAmountTrade</span>
<span style="color:blue">uint8, N1</span>
<span style="color:blue">2 =</span> <span style="color:blue">否</span>
<span style="color:blue">结算方式</span>
<span style="color:blue">SettlType</span>
<span style="color:blue">uint8, N1</span>
<span style="color:blue">1 =</span> <span style="color:blue">净额结算</span>
<span style="color:blue">2 =</span>
<span style="color:blue">RTGS</span>
<span style="color:blue">折算比例（</span> <span style="color:blue">%</span> <span style="color:blue">），如发起方未填写此字段，</span>
<span style="color:blue">ContractMultiplier</span>
<span style="color:blue">uint32,N5(2)</span>
<span style="color:blue">填</span> <span style="color:blue">0</span>
<span style="color:blue">ExpirationDays</span>
<span style="color:blue">期限（天），如发起方未填写此字段，填</span>
<span style="color:blue">uint16,N3</span>
<span style="color:blue">0</span>
<span style="color:blue">TotalValueTraded</span>
<span style="color:blue">成交金额，如发起方未填写此字段，填</span> <span style="color:blue">0</span>
<span style="color:blue">uint64,N16(2)</span>
<span style="color:blue">篮子信息</span>
<span style="color:blue">左起顺序代表第</span> <span style="color:blue">1</span> <span style="color:blue">号至第</span> <span style="color:blue">N</span> <span style="color:blue">号篮子。例如</span>
<span style="color:blue">BasketID</span>
<span style="color:blue">char[16]</span>
<span style="color:blue">指定</span> <span style="color:blue">1</span> <span style="color:blue">，</span> <span style="color:blue">2</span> <span style="color:blue">，</span> <span style="color:blue">5</span> <span style="color:blue">号篮子，填</span>
<span style="color:blue">“1100100000000000”</span>
<span style="color:blue">InvestorName</span>
<span style="color:blue">投资者名称</span>
<span style="color:blue">char[32]</span>
<span style="color:blue">竞买申报类别</span>
<span style="color:blue">1 =</span> <span style="color:blue">竞买预约</span>
<span style="color:blue">BidTransType</span>
<span style="color:blue">uint8, N1</span>
<span style="color:blue">2 =</span> <span style="color:blue">竞买申报</span>
<span style="color:blue">3 =</span> <span style="color:blue">单一主体中标应价申报</span>
- 27 -

技术文档
<span style="color:blue">竞买申报方式</span>
<span style="color:blue">1 =</span> <span style="color:blue">单一主体中标</span>
<span style="color:blue">BidExecInstType</span>
<span style="color:blue">uint8, N1</span>
<span style="color:blue">2 =</span> <span style="color:blue">多主体单一价格中标</span>
<span style="color:blue">3 =</span> <span style="color:blue">多主体多重价格中标</span>
<span style="color:blue">ExpireDate</span>
<span style="color:blue">竞买日期：</span> <span style="color:blue">YYYYMMDD</span>
<span style="color:blue">uint32,N8</span>
<span style="color:blue">应价申报对应的订单编号（也即竞买申报</span>
<span style="color:blue">SecondaryOrderID</span>
<span style="color:blue">char[18]</span>
<span style="color:blue">编号）</span>
<span style="color:blue">MinQty</span>
<span style="color:blue">最低成交数量，预留</span>
<span style="color:blue">uint64,N12</span>
<span style="color:blue">注：新增委托订单时扩展字段与业务的对照关系参见下表，删除委托订单时仅</span> <span style="color:blue">Side</span> <span style="color:blue">、</span> <span style="color:blue">QuoteID</span> <span style="color:blue">、</span>
<span style="color:blue">MemberID</span> <span style="color:blue">和</span> <span style="color:blue">TraderCode</span> <span style="color:blue">有效（其他字段均无意义）</span>
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
<span style="color:blue">ExpireDate</span>
<span style="color:blue">●</span>
<span style="color:blue">8</span> <span style="color:blue">不同竞买委托方式可根据</span> <span style="color:blue">BidTransType</span> <span style="color:blue">字段进行区分。</span>
<span style="color:blue">9</span> <span style="color:blue">仅适用于竞买单一主体中标应价申报。</span>
- 28 -

技术文档
<span style="color:blue">ContractMultiplier</span>
<span style="color:blue">●</span>
<span style="color:blue">ExpirationDays</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
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
<span style="color:blue">SecondaryOrderID</span>
<span style="color:blue">●</span>
<span style="color:blue">MinQty</span> <span style="color:blue">10</span>
<span style="color:blue">●</span>
<span style="color:blue">●</span>
<span style="color:blue">2.5.4.2</span> <span style="color:blue">逐笔成交行情扩展字段</span>
<span style="color:blue">域名</span>
<span style="color:blue">说明</span>
<span style="color:blue">类型</span>
<span style="color:blue">买方订单编号（</span> <span style="color:blue">QuoteID</span> <span style="color:blue">）</span>
<span style="color:blue">BidApplSeqNum</span>
<span style="color:blue">char[18]</span>
<span style="color:blue">无对应委托时填空</span>
<span style="color:blue">卖方订单编号（</span> <span style="color:blue">QuoteID</span> <span style="color:blue">）</span>
<span style="color:blue">OfferApplSeqNum</span>
<span style="color:blue">char[18]</span>
<span style="color:blue">无对应委托时填空</span>
<span style="color:blue">TotalValueTraded</span>
<span style="color:blue">成交金额</span>
<span style="color:blue">uint64,N16(2)</span>
<span style="color:blue">10</span> <span style="color:blue">仅适用于竞买多主体中标（含单一价格或多重价格中标）。</span>
- 29 -

技术文档
<span style="color:blue">成交方式</span>
<span style="color:blue">0 =</span> <span style="color:blue">匹配成交（预留）</span>
<span style="color:blue">1 =</span> <span style="color:blue">确定报价点击成交</span>
<span style="color:blue">2 =</span> <span style="color:blue">待定报价点击成交</span>
<span style="color:blue">3 =</span> <span style="color:blue">询价成交</span>
<span style="color:blue">TradeMethod</span>
<span style="color:blue">uint8,N2</span>
<span style="color:blue">6 =</span> <span style="color:blue">协商成交（含合并申报）</span>
<span style="color:blue">7 =</span> <span style="color:blue">竞买单一主体成交</span>
<span style="color:blue">10 =</span> <span style="color:blue">竞买多主体单一价格成交</span>
<span style="color:blue">11 =</span> <span style="color:blue">竞买多主体多重价格成交</span>
<span style="color:blue">边际价格</span>
<span style="color:blue">MarginPrice</span>
<span style="color:blue">uint64,N13(5)</span>
<span style="color:blue">仅适用于竞买多主体成交</span>
- 30 -

技术文档
3
文件接收
用户可通过行情网关接收的行情及相关参考文件主要包括：
文件名
描述
csiYYYYMMDD.txt
指数通行情文件
reff03MMDD.txt
期权基础信息文件
reff0302YYYYMMDD.xml
期权基础信息第二版文件
trdses04.txt
港股通交易盘实时状态
mktdt04.txt
港股行情文件
mktdth.txt
B 转 H 行情文件
mktdt06.txt
基金通行情文件
cpxx0201MMDD.txt
产品信息文件第二版本第一批次
cpxx0202MMDD.txt
产品信息文件第二版本第二批次
fjyYYYYMMDD.txt
产品非交易基础数据
tpxxxxhhmmss.txt
盘中停牌公告文件
ztxxxxhhmmss.txt
债券盘中停牌公告文件
<span style="color:blue">products_yyyymmdd.xml</span>
<span style="color:blue">证券产品基础信息文件</span>
<span style="color:blue">bondmbrs_yyyymmdd.xml</span>
<span style="color:blue">债券交易参与人信息文件</span>
<span style="color:blue">bondtrdrs_yyyymmdd.xml</span>
<span style="color:blue">债券交易员信息文件</span>
<span style="color:blue">se015cjhqYYYMMDD001.txt</span>
<span style="color:blue">固收成交行情文件</span>
<span style="color:blue">se015cjmxYYYMMDD001.txt</span>
<span style="color:blue">固收成交明细文件</span>
- 31 -

技术文档
<span style="color:blue">se015qdbjYYYMMDD001.txt</span>
<span style="color:blue">固收确定报价文件</span>
<span style="color:blue">se015zqxxYYYMMDD001.txt</span>
<span style="color:blue">固收证券信息文件</span>
reff04MMDD.txt
港股通基础信息文件
exra04MMDD.txt
港股通参考汇率文件
zxjcMMDD.txt
港股通最小价差文件
具体文件格式及相关描述详见本所各平台市场参与者接口规格说明书。
- 32 -

技术文档
4
转发行情
目前，用户可通过本所行情网关转发任务获取的外部行情数据包括：

深交所 V5 行情
具体数据接口规范请参考《深圳证券交易所 Binary 行情数据接口规范》，对转发任务的网络
及带宽限制要求请参考《上海证券交易所行情网关用户网络接入指引》。
- 33 -

技术文档
后记
上海证券交易所对本文档享有知识产权，未经上海证券交易所书面许可，任何单位和个人不
得将本文档用于其他商业目的。
本文档编写过程中，深受证券业界信息技术同仁讨论启发，特此致谢。对本文档有任何批评
指正意见，可通过电子邮件或服务电话进行反馈。
电子邮件： tech_support@sse.com.cn
服务电话： 4008888400-2
网站地址： https://www.sse.com.cn/ - 交易技术支持专区
通讯地址：上海市浦东新区浦东南路 528 号上交所技术公司技术开发总部
- 34 -

技术文档
附录一、计算校验和（资料性附录）
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
- 35 -

> **变更标注说明**：本文档中已用 `<span style="color:...">` 标注了变更内容（红色=修改/新增，蓝色=其他说明）。


<metadata>
{
  "title": "IS120_上海证券交易所行情网关BINARY数据接口规范",
  "source_url": null,
  "raw_path": "knowledge\\raw\\sse\\技术接口\\20260612_IS120_上海证券交易所行情网关BINARY数据接口规范0.61版_20260612.pdf",
  "markdown_path": "knowledge\\articles\\sse\\markdown\\技术接口\\IS120_上海证券交易所行情网关BINARY数据接口规范0.61版_20260612.md",
  "file_hash": "sha256:adc18b5126f9d77e4506de0d68d370a0b81e07370e724df5bbf4b812be63754d",
  "file_format": "pdf",
  "page_count": 41,
  "doc_type": "interface_spec",
  "version": null,
  "previous_version": null,
  "public_date": "2026-05-11",
  "effective_date": null,
  "has_changes": true,
  "parse_status": "success",
  "parse_date": "2026-06-13T17:43:55.141296+00:00",
  "sub_category": null
}
</metadata>