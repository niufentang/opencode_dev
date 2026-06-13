上海证券交易所技术文档
上海证券交易所
市场参与者 EzSTEP 通用数据库
接口规格说明书
（ 1.00 版）
上海证券交易所
二 ○ 一二年二月

《上海证券交易所市场参与者 EzSTEP 通用数据库接口规格说明书》 1.00 版
发布说明
本文档为市场参与者通过 EzSTEP 接入上交所技术系统的通用数据库接口规格。
本文档由上海证券交易所制定并负责解释。
错误代码详见技术文档《 IS111 上海证券交易所报盘软件错误代码表》。
服务电话： 021-68644780
通信地址：上海市浦东南路 528 号上海证券交易所技术规划与服务部
网站地址： <span style="color:blue">http://www.sse.com.cn/</span> Æ 新交易系统专区

目录
<span style="color:blue">1</span> <span style="color:blue">数据格式约定</span> ...................................................................................................... 4
<span style="color:blue">2</span> <span style="color:blue">通用数据库接口规范</span> ........................................................................................... 5
<span style="color:blue">2.1</span> .......... <span style="color:blue">公共数据表</span> <span style="color:blue">pubdata</span> .............................................................................. 5
<span style="color:blue">2.2</span> .......... <span style="color:blue">请求及响应接口表</span> <span style="color:blue">reqresp</span> .................................................................... 5
<span style="color:blue">2.3</span> .......... <span style="color:blue">执行报告表</span> <span style="color:blue">execreport</span> ......................................................................... 7
<span style="color:blue">3</span> <span style="color:blue">STEP 消息约定</span> ..................................................................................................... 9
<span style="color:blue">3.1</span> .......... <span style="color:blue">消息文本结构</span> ......................................................................................... 9
<span style="color:blue">4</span> <span style="color:blue">后记</span> .................................................................................................................. 11

技术文档
1
数据格式约定
z
数据格式定义方式
（一）对于字符型字段，以 CX 格式表示，其中 X 代表长度；
（二）对于整数数字型字段，以 NX 格式表示，其中 X 代表数字型字符串总长度；
（三）对于带小数数字型字段，以 NX (Y) 格式表示，其中 X 代表数字型字符串总长度， Y 代表
小数位数。 X 包括一位小数点，整数部分最多不超过 X-Y-1 位，小数部分最多不超过 Y 位。带
小数数字型字段应包括所有小数位，如： N8(3) 的 123 ，填写为 123.000 。
z
文本文件、数据库文件及数据库接口中字段约定
（一）对于交易所输出的文件和数据库字段数据，字符型数据在原始数据基础上左对齐右补空
（消息文本字段除外），数字型数据右对齐左补空；对于市场参与者填报的字符型和数字型数
据，市场参与者系统应确保与消息中对应数据的一致性，避免因空格影响数据差异；市场参与
者系统在处理时应特别注意。
z
STEP 消息包字段约定
（一）消息构建和解析方法，可参考金融行业标准《证券交易数据交换协议》（简称
“ STEP ”） 1.00 版或 FIX 标准 4.4 版；
（二）字段长度定义为最大长度约束，无需左或右补空格定长，市场参与者系统应确保与数据
库中对应数据的一致性，避免因空格影响数据差异。
z
文件和接口数据格式其他约定
（一）对于任何字符型数据，取值中严禁包含“ | ”字符；对于会员内部编号，只允许字母、数
字和空格组合；
（二）长格式时间字段精度为秒，毫秒部分暂时补零，不作为实际精度。
（三）如数字数据超出字段定义溢出，将赋值 -1 。
市场参与者 EzSTEP 通用数据库接口规格说明书
第 4 页 共 11 页

技术文档
2
通用数据库接口规范
本部分描述了市场参与者系统同上交所技术系统之间的实时数据库接口（ MS SQL Server 数据
库），通过数据库实现 STEP 数据实时交换，将 STEP 协议的应用消息体通过数据库表的字段
与交易所交换数据。
注意建表时，数据库字段名均为小写字母。
2.1
公共数据表 pubdata
pubdata
公共数据表
描述：
公共数据由交易所后台向市场参与者单向发送。
上交所报盘机程序访问该表时，主要通过 pubnum 字段进行定位，故必须以 pubnum 为 Key
建立索引，或者作为主键。
字段名
字段描述
类型
pubnum
公共数据表记录编号，连续递增，不代表公共信息发布顺序。
4 字节
Integer
bcasttype
数据广播类型，取值根据具体业务定义。
C2
setid
产品集编号
C3
seqnum
产品集序号,同一个产品集内，记录不代表按照产品集序号的顺序写入 4 字节
Integer
recordtimest
记录写入时间，格式为 YYYYMMDD-HH:MM:SS.000
C21
amp
mdtext
消息文本， STEP 格式封装的市场公共数据，参见相关消息规范。
C1024
2.2
请求及响应接口表 reqresp
reqresp
请求及响应接口表
描述：
本数据库表接口为市场参与者提供一个单一的队列，市场参与者系统将申报数据写入申报接口
表，然后由上交所报盘机按序读取接口数据库表中记录，依次发送到后台。后台的确认信息将
市场参与者 EzSTEP 通用数据库接口规格说明书
第 5 页 共 11 页

技术文档
reqresp
请求及响应接口表
写入对应记录的确认数据字段。上交所报盘机程序访问该表时，主要通过 reqnum 字段进行
定位，故必须以 reqnum 为 Key 建立索引，或者作为主键。
字段名
字段描述
类型
reqnum
请求及响应表记录编号，通常从 1 开始， <span style="color:red">必须连续递增</span> 。
4 字节
Integer
如果请求及响应表完全损坏，市场参与人启用备份数据库，那么为继
续后续的报单业务，则需要在新的空请求及响应表中直接写入后续订
单。后续订单的 reqnum 编号可以重新从 1 开始。
C3
reqid
请求业务类型编号，交易所据此处理不同的业务请求，取值：
BII
大宗意向
BPT
大宗交易
QBD
报价入库
QBW
报价出库
QNE
报价回购
QCA
报价回购提前购回
RNE
初始交易
RNR
购回交易
<span style="color:red">EEC</span> <span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">申购</span>
<span style="color:red">EER</span> <span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">赎回</span>
<span style="color:red">ZII</span> <span style="color:red">转融通非指定对手方申报</span>
<span style="color:red">ZPT</span> <span style="color:red">转融通指定对手方申报</span>
C10
reff
会员内部编号。（建议用满10 位，避免用空格填补）
对于订单申报或成交申报，为会员内部编号 ClOrdID ；
对于意向申报，为会员内部编号 IOIID ；
在所有申报业务范围内，会员内部编号必须唯一，交易系统不重复处
理前台提交的相同业务 PBU 相同的 reff 的订单，并以此编号重复作为
订单重复依据。
市场参与者 EzSTEP 通用数据库接口规格说明书
第 6 页 共 11 页

技术文档
<span style="color:red">该字段为</span> <span style="color:red">reqtext</span> <span style="color:red">消息包中对应</span> 会员内部编号 <span style="color:red">字段的重复，取值必须与</span>
<span style="color:red">reqtext</span> <span style="color:red">消息包中对应</span> 会员内部编号 <span style="color:red">字段相同，该字段用于订单唯一性</span>
<span style="color:red">标识，也可方便市场参与者数据库检索使用。</span>
C6
securityid
证券代码。
<span style="color:red">该字段用于订单发送路由，取值必须与</span> <span style="color:red">reqtext</span> <span style="color:red">中对应字段相同。</span>
C5
pbu
PBU 代码。
<span style="color:red">该字段用于订单唯一性标识，取值必须与</span> <span style="color:red">reqtext</span> <span style="color:red">中对应字段相同。</span>
recordtimesta
C21
申报请求记录写入时间，格式为 YYYYMMDD-HH:MM:SS.000
mp
时间精度为秒，毫秒部分暂时补零
C1
报盘发送状态，
‘R’ 表示该记录还没有发送；
’F’ 表示后台判断为废单；
’E’ 表示前台判断为废单；
ordstatus
‘O’ 表示上交所成功接收该笔订单或撤单。
柜台系统可以通过该字段来判断是否已经向上交所发送该申报，对于
废单， remark 字段给出错误代码。在 resptext 中有对应的字段组合标
识出错误类型，并给出错误代码。
C5
错误代码信息，由报盘系统填写，供柜台系统读取错误信息，进行错
误处理（ <span style="color:red">取值待定</span> ）
remark
<span style="color:red">该字段与</span> <span style="color:red">resptext</span> <span style="color:red">中相关字段重复，取值相同，交易所反馈的数据以</span>
<span style="color:red">resptext</span> <span style="color:red">为准，该字段仅供方便市场参与者数据库检索使用。</span>
响应确认记录写入顺序编号，递增但不一定连续，由报盘系统填写，
4 字节
localrespnum
供柜台系统检索响应数据。
Integer
reqtext
请求消息文本， STEP 格式封装的申报数据，参见相关消息规范。
C1024
resptext
响应消息文本， STEP 格式封装的确认数据，参见相关消息规范。
C1024
2.3
执行报告表 execreport
execreport
执行报告表
描述：
市场参与者 EzSTEP 通用数据库接口规格说明书
第 7 页 共 11 页

技术文档
execreport
执行报告表
上交所报盘机在接收到后台返回的执行报告之后，写入到接口数据库表中。市场参与者系统可
以从该表读取上交所处理申报后返回的执行报告数据。
上交所报盘机程序访问该表时，主要通过 execnum 字段进行定位，故必须以 execnum 为
Key 建立索引，或者作为主键。
字段名
字段描述
类型
execnum
执行报告表记录编号，连续递增，不代表在交易所成交顺序。
4 字节
Integer
bcasttype
数据广播类型，取值根据具体业务定义。
C2
setid
产品集编号
C3
seqnum
产品集序号 , 同一个产品集内，记录不代表按照产品集序号的顺序写
4 字节
入
Integer
recordtimesta
C21
记录写入时间，格式为 YYYYMMDD-HH:MM:SS.000
mp
时间精度为秒，毫秒部分暂时补零
execreportte
消息文本， STEP 格式封装的成交回报数据，参见相关消息规范
C1024
xt
市场参与者 EzSTEP 通用数据库接口规格说明书
第 8 页 共 11 页

技术文档
3
STEP 消息约定
本部分描述了市场参与者系统同上交所技术系统之间的接口消息文本格式，对应数据库接口表
中的各消息文本字段，采用 STEP 格式封装。
3.1
消息文本结构
考虑到接口是到基于数据库的消息模式， STEP 格式封装由消息头、消息体组成，无消息尾部
分。因无 STEP 会话层，故对 STEP 标准的消息头进行了删减，详见消息头表格。
消息头和消息体均采用依次排列“标签 = 字段取值 <SOH> ”的方式组织，标签为数字字符，前
后不得有空格，消息中字段取值除非特别声明，均以可打印 ASCII 码字符串表示，不得采用全
角字母字符， <SOH> 为字段界定符，其值为不可打印字符 ASCII 码：十六进制的 0x01 。
如字符型字段值为空，则采用“标签 = <SOH> ”的方式表示（等号后与分隔符间有一个空
格），如数字型字段值为空，采用缺省取值 0 。
为传输数组类的信息，消息支持 “ 重复组 ” ，字段在重复组里多次出现。通常字段名前缀为 “No”
字符的字段指明出现的次数，并位于重复组的开始处。除重复组内字段外任何其他字段不能多
次出现。
消息头定义如下：
标签 字段名
字段描述
类型
N5
9
BodyLength
消息体长度
消息的第一个字段，其值是计算出的消息长度字段分隔符后面
的字符数，包含其他字段分隔符<SOH> <span style="color:red">（即不含本字段后面的</span>
<span style="color:red">分隔符）</span> 。
C4
35
MsgType
消息类型
消息类型取值：
8 = 申报响应或执行报告（ Execution Report ）
D = 申报（ NewOrder Single ）
其他取值参见具体业务规范。
市场参与者 EzSTEP 通用数据库接口规格说明书
第 9 页 共 11 页

技术文档
结构图如下：
文档中消息文本必须严格按照接口字段定义顺序及重复组定义顺序封装。
消息包中与数据库字段重复的字段，必需确保取值一致，注意避免因空格填补差异而影响一致
性。
消息体格式参见各业务消息规范。
市场参与者 EzSTEP 通用数据库接口规格说明书
第 10 页 共 11 页

技术文档
4
后记
上海证券交易所对本文档享有知识产权，未经上海证券交易所书面许可，任何单位和个人
不得将本文档用于其他商业目的。
对本文档有任何批评指正意见，请发电子邮件到 spwu@sse.com.cn 或者致电 021-
68827268 。
市场参与者 EzSTEP 通用数据库接口规格说明书
第 11 页 共 11 页

> **变更标注说明**：本文档中已用 `<span style="color:...">` 标注了变更内容（红色=修改/新增，蓝色=其他说明）。


<metadata>
{
  "title": "<4D6963726F736F667420576F7264202D20B8BDBCFEB6FE20495331303820C9CFBAA3D6A4C8AFBDBBD2D7CBF9CAD0B3A1B2CED3EBD5DF20457A53544550CDA8D3C3CAFDBEDDBFE2BDD3BFDAB9E6B8F1CBB5C3F7CAE9312E303020B0E65F3230313230333236>",
  "source_url": null,
  "raw_path": "knowledge\\raw\\sse\\技术接口\\20120521_IS108 上海证券交易所 市场参与者EzSTEP通用数据库接口规格说明书1.00版_20120326.pdf",
  "markdown_path": "knowledge\\articles\\sse\\markdown\\技术接口\\IS108 上海证券交易所 市场参与者EzSTEP通用数据库接口规格说明书1.00版_20120326.md",
  "file_hash": "sha256:8acca417a00df8b2cdc170b70f0a16864b625b43dafc95b05ba33fc41f229d35",
  "file_format": "pdf",
  "page_count": 11,
  "doc_type": "interface_spec",
  "version": null,
  "previous_version": null,
  "public_date": null,
  "effective_date": null,
  "has_changes": true,
  "parse_status": "success",
  "parse_date": "2026-06-13T17:43:51.433584+00:00",
  "sub_category": null
}
</metadata>