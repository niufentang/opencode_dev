深市 ETF 交易结算模式调整技术变更指南
一． 说明
为方便市场参与各方更好地完成 “ 深市 ETF 交易结算模式调整 ” 相关技术准
备工作，深圳证券交易所（以下简称 “ 深交所 ” ）联合中国证券登记结算有限责任
公司（以下简称 “ 中国结算 ” ）深圳分公司制定本文档，供交易参与人和结算参与
人及其 IT 供应商变更技术系统时参考。
二． 业务简介
2.1 深市 ETF 交易申赎业务所涉及的担保结算模式调整
深市 ETF 现行 T+1 担保 DVP 结算模式调整为 A 股交收模式，所涉及业务
范围包括：深市所有 ETF 品种的交易业务及深市单市场 ETF 、货币 ETF 及实物
债券 ETF 品种的申购赎回业务。
2.2 深市 ETF 申赎业务所涉及的非担保结算模式调整
现金债券 ETF 、跨境 ETF 、商品期货 ETF ，赎回份额注销时点从 T+1 日日终
调整为 T 日日终。
以全额现金申购的现金债券 ETF ，从现行 T+1 日日终逐笔全额非担保交收结
算模式，调整为 T 日日间 RTGS 加 T 日日终逐笔全额非担保交收结算模式；以
全额现金申购的黄金 ETF ，从现行的 T 日日终逐笔全额非担保交收结算模式，
调整为 T 日日间 RTGS 加 T 日日终逐笔全额非担保交收结算模式。
2.3 深市 ETF 除权除息日调整
深市所有 ETF 品种的除权除息日，从 ETF 份额权益登记日（ R 日）当天，
调整为 ETF 份额权益登记日次一交易日（ R+1 日）。
2.4 深市跨市场 ETF 新增场内申赎担保结算模式
深市跨市场 ETF 取消原有场内全额现金申赎模式，新增“场内部分实物、部
分现金”申赎模式。深市组合券采用实物交收，非深市组合券采用全现金（替代）
交收。新申赎模式下，对于深市组合券及深市现金替代部分，深市组合券 T 日

日终过户，深市现金替代部分采用净额担保交收；对于非深市组合券所对应的现
金替代部分采用净额担保交收。申赎份额于 T 日日终完成登记和注销；现金差
额、现金替代退补款部分采用代收代付方式。跨市场 ETF 新申赎模式实施的净
额担保交收，比照单市场 ETF 申赎，均为 A 股交收模式。
2.5 深市 ETF 其他相关业务的调整
深市 ETF 调整为 A 股交收模式后， ETF 份额 T 日日终即完成交收，不再维
护在途 ETF 份额的可用额度，债券 ETF 的质押式回购业务、 ETF 融资融券业务
将参照现有 A 股交收模式进行。
2.6 深市 ETF 交易申赎份额使用规则的调整
对于黄金 ETF ， T 日买入的 ETF 份额， T 日可以现金赎回， T+1 日可以实物
赎回。
对于跨市场股票 ETF ，其 ETF 份额和深市组合证券的场内申赎股份使用规
则与本市场股票 ETF 类似：
T 日买入的 ETF 份额， T 日可用于场内赎回， T 日可用于场外赎回；
T 日买入的深市组合证券， T 日可用于场内申购， T 日可用于场外申购；
T 日场内申购的 ETF 份额， T 日可以卖出， T+1 日可以场内、场外赎回；
T 日场内赎回得到的深市组合证券， T 日可以卖出， T+1 日可用于场内、场
外申购；
T 日场内赎回得到的深市成份券现金替代和沪市成份券现金替代的资金， T
日可用；
T 日场外申购的 ETF 份额，在交收前不得卖出、赎回；
T 日场外赎回得到的深市组合证券，在交收前不得卖出、申购。
三． 交易数据接口修订
深市 ETF 交易结算模式调整，涉及跨市场股票 ETF 的交易接口变更，以及
黄金 ETF 、跨市场股票 ETF 的股份使用规则调整。
3.1 跨市场股票 ETF
（ 1 ）跨市场股票 ETF 的场内申赎 pcf 文件，继续使用现有的场内申赎 pcf
文件格式（ pcf_NNNNNNNN_YYYYMMDD.xml ），其成份证券信息将修改为：

多条非 159900 的深市成份证券、 1 条虚拟成份券 159900 、以及多条沪市成份证
券的记录。其中， 159900 记录的申购 / 赎回替代金额字段，仅表示所有沪市成份
证券现金替代的总金额，其申购替代金额和赎回替代金额取值可能不同。沪市成
份证券记录信息，仅做申购赎回参考使用，市场参与人技术系统不能使用沪市成
份证券信息进行委托、成交时的现金替代处理，而应该使用 159900 虚拟成份券
进行沪市成份证券份额的现金替代处理。
例如，某跨市场股票 ETF 跟踪指数有 10 只深市样本股和 10 只沪市样本股，
则场内申赎 pcf 文件应有 21 只成份证券记录： 10 只深市样本股成份证券信息、 1
只 159900 虚拟券、 10 只沪市样本股成份证券信息。 159900 的申购替代金额应等
于 10 只沪市成份券现金替代总金额 （ = ∑现金替代标志为 1 的沪市成份证券的前
一交易日收盘价 * 成份证券数 * （ 1+ 溢价比例） + ∑现金替代标志为 2 的沪市成份
证券的申购替代金额） ， 159900 的赎回替代金额应等于 10 只沪市成份券现金替
代总金额 （ = ∑现金替代标志为 1 的沪市成份证券的前一交易日收盘价 * 成份证券
数 * （ 1- 折价比例） + ∑现金替代标志为 2 的沪市成份证券的赎回替代金额） 。深
交所仅使用 10 只深市样本股成份证券和 159900 虚拟券信息。
跨市场股票 ETF 的 pcf 文件具体格式，请参见《深圳证券交易所数据文件交
换接口规范》的 “ETF 实时申购赎回业务参考信息（ pcf ） ” 章节、《深圳证券交
易所新一代交易系统基金公司数据接口规范》的 “PCF 文件 ” 章节。
（ 2 ）跨市场股票 ETF 的场内申赎成功执行报告的成份股记录重复组，将包
含多条非 159900 的深市成份证券、以及 1 条虚拟成份券 159900 。其中， 159900
虚拟券的 “ 现金替代金额 ” 表示沪市所有成份券的现金替代总金额。
（ 3 ）跨市场股票 ETF 的场外申赎（通过中国结算总部申报）的 pcf 文件、
委托回报处理等没有变化。场外申赎 pcf 文件的格式和内容，与场内申赎 pcf 文
件不同。
四． 结算数据接口修订
4.1 接口修订概述
（ 1 ）深市 ETF 交易结算模式调整，所涉及的需要调整的业务类别及其涵盖
的 ETF 品种如下表，业务类别及证券子类别含义可查看《深市登记结算数据接

口规范（结算参与人版）》中附件一及附件二，或查看 SJSGB.DBF 中 GBLB 为
‘YL’ 及 ‘ZZ’ 的数据：
结算模式调整
业务
类别
业务类别名称
涉及的 ETF 品种
所有 ETF 品种
JY00
集中竞价平台交易，综
合金融服务平台交易
（担保交收模式）
SGSF
实物申购份额
0- 单市场 ETF 、 6- 实物债
券 ETF
SGSZ
实物申购现金替代
0- 单市场 ETF 、 6- 实物债
券 ETF
SHSF
实物赎回份额
0- 单市场 ETF 、 6- 实物债
券 ETF
SHSZ
实物赎回现金替代
0- 单市场 ETF 、 6- 实物债
券 ETF
从现行 T+1DVP 模
式调整为 A 股交收
模式
SGXF 现金申购份额
4- 货币 ETF
SGXZ 现金申购现金替代
4- 货币 ETF
SHXF 现金赎回份额
4- 货币 ETF
SHXZ 现金赎回现金替代
4- 货币 ETF
SGXF 现金申购份额
7- 现金债券 ETF
SGXZ 现金申购现金替代
7- 现金债券 ETF
从 T+1 日日终逐笔
全额非担保交收
调整为
T 日日间 RTGS 加 T
日日终逐笔全额非
担保交收
SGXF 现金申购份额
5- 黄金 ETF
从 T 日日终逐笔全
额非担保交收
调整为

SGXZ 现金申购现金替代
5- 黄金 ETF
T 日日间 RTGS 加 T
日日终逐笔全额非
担保交收
SHXF 现金赎回份额
2- 跨境 ETF 、 7- 现金债券
ETF 、 8- 商品期货 ETF
赎回份额注销时点
从 T+1 日日终调整
为 T 日日终
（ 2 ）深市跨市场 ETF （子类 ‘3’ ）取消了原有场内全额现金申赎模式，不再
使用 SGXZ 、 SHXZ 、 SGXF 、 SHXF 这四个业务类别。新增的场内实物申赎模式，
其申购份额、申购现金替代、申购组合券、赎回份额、赎回现金替代、赎回组合
券业务采用 SGSF 、 SGSZ 、 SGSQ 、 SHSF 、 SHSZ 、 SHSQ 业务类别；所采用的
交收方式同单市场 ETF ，为 A 股交收模式。
新增 SGDZ 、 SHDZ 业务类别， SGDZ 为通过中国证券登记结算有限责任公
司总部（以下简称 “ 中国结算总部 ” ）申购的深市跨市场 ETF 现金替代业务， SHDZ
为通过中国结算总部赎回的深市跨市场 ETF 现金替代业务。
申购赎回现金差额、现金替代退补款、申购税费 / 组合券过户费、赎回税费 /
组合券过户费业务采用 EFXC 、 EFTB 、 SGFY 、 SHFY 业务类别。调整以后，深
市跨市场 ETF 申赎涉及的业务类别及名称如下表：
业务类别
业务类别名称
SGSF
实物申购份额
SGSZ
实物申购现金替代
SGSQ
实物申购组合券
SHSF
实物赎回份额
SHSZ
实物赎回现金替代
SHSQ
实物赎回组合券
EFTB
ETF 申购赎回现金替代多退少补
EFXC
ETF 申购赎回现金差额
SGFY
ETF 申购税费、组合券过户费
SHFY
ETF 赎回税费、组合券过户费
<span style="color:red">SGDZ</span>
<span style="color:red">通过中国结算总部申购的</span> <span style="color:red">ETF</span> <span style="color:red">现金替代</span>
<span style="color:red">SHDZ</span>
<span style="color:red">通过中国结算总部赎回的</span> <span style="color:red">ETF</span> <span style="color:red">现金替代</span>
4.2 清算明细库 SJSMXn.DBF
4.2.1 SJSMX0.DBF
（ 1 ） SJSMX0.DBF 中，业务类别 SGXF （ ETF 现金申购份额）、 SGXZ （ ETF
现金申购现金替代）不再包含跨市场 ETF 的数据；

（ 2 ）现金债券 ETF 的申购从 T+1 日日终逐笔全额非担保交收结算模式调整
为 T 日日间 RTGS 加 T 日日终逐笔全额非担保交收结算模式，其清算明细数据
由 SJSMX1.DBF 调整为通过 SJSMX0.DBF 发送，即 SJSMX0.DBF 中业务类别
SGXZ 和 SGXF 中新增了上述 ETF 品种的数据；
（ 3 ）现金债券 ETF 、跨境 ETF 及商品期货 ETF 的赎回份额注销时点从 T+1
日日终调整为 T 日日终，其清算明细数据由 SJSMX1.DBF 调整为通过
SJSMX0.DBF 发送，即 SJSMX0.DBF 中 SHXF （ ETF 现金赎回份额）新增了上
述 ETF 品种的数据。调整后的 SJSMX0.DBF 业务类别含义如下表：
SJSMX0.DBF 业务类别含义表
业务类别
业务类别含义
SGXF
黄金 ETF 、跨境 ETF 、商品期货 ETF 、 <span style="color:red">现金债</span>
<span style="color:red">券</span> <span style="color:red">ETF</span> 现金申购份额
SGXZ
黄金 ETF 、跨境 ETF 、商品期货 ETF 、 <span style="color:red">现金债</span>
<span style="color:red">券</span> <span style="color:red">ETF</span> 现金申购现金替代
SHXF
黄金 ETF 、 <span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、商品期货</span> <span style="color:red">ETF</span> <span style="color:red">、现金债</span>
<span style="color:red">券</span> <span style="color:red">ETF</span> 现金赎回份额
（ 4 ） SJSMX0.DBF 中，黄金 ETF 现金申购份额、现金申购现金替代明细数
据的交收方式字段由 ‘N’ 变为 ‘R’ ，调整以后业务类别为 SGXF 、 SGXZ 、 SHXF 的
数据，其字段含义见下表：
字段名
业务类别
SGXF （ <span style="color:red">黄金</span> <span style="color:red">ETF</span> <span style="color:red">、</span>
<span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、商品期</span>
<span style="color:red">货</span> <span style="color:red">ETF</span> <span style="color:red">、现金债券</span>
<span style="color:red">ETF</span> <span style="color:red">现金申购份</span>
<span style="color:red">额</span> ）
SGXZ （ <span style="color:red">黄金</span> <span style="color:red">ETF</span> <span style="color:red">、</span>
<span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、商品期</span>
<span style="color:red">货</span> <span style="color:red">ETF</span> <span style="color:red">、现金债券</span>
<span style="color:red">ETF</span> <span style="color:red">现金申购现</span>
<span style="color:red">金替代</span> ）
SHXF （ <span style="color:red">黄金</span> <span style="color:red">ETF</span> <span style="color:red">、</span>
<span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、商品期</span>
<span style="color:red">货</span> <span style="color:red">ETF</span> <span style="color:red">、现金债券</span>
<span style="color:red">ETF</span> <span style="color:red">现金赎回份</span>
<span style="color:red">额</span> ）
MXJSZH
结算账号
结算账号
结算账号
MXBFZH
备付金账户
备付金账户
备付金账户
MXSJLX
‘01’
‘01’
‘01’
MXYWLB
‘SGXF’
‘SGXZ’
‘SHXF’
MXZQDM
ETF 证券代码
ETF 证券代码
ETF 证券代码
MXJYDY
交易单元
交易单元
交易单元
MXTGDY
托管单元
托管单元
托管单元
MXZQZH
证券账户
证券账户
证券账户
MXDDBH
订单编号
订单编号
订单编号
MXYYB
营业部代码
营业部代码
营业部代码

业务流水号
业务流水号
业务流水号
MXZXBH
执行编号
执行编号
执行编号
MXYWLS
H
MXCJSL
成交数量
0
成交数量
MXQSSL
清算数量（ = 成交
数量）
0
清算数量（ = 成交
数量）
MXCJJG
MXQSJG
MXXYJY
MXPCBS
MXZQLB
‘EF’
‘EF’
‘EF’
MXZQZL
证券子类别
证券子类别
证券子类别
MXGFXZ
‘00’
‘00’
‘00’
MXJSFS
<span style="color:red">‘R’</span>
<span style="color:red">‘R’</span>
‘N’
MXHBDH
货币代号
货币代号
货币代号
MXQSBJ
现金替代金额
MXYHS
MXJYJSF
MXJGGF
MXGHF
MXJSF
MXSXF
MXQSYJ

MXQTFY
MXZJJE
MXSFJE
0
收付净额
0
MXCJRQ
T 日
T 日
T 日
MXQSRQ
T 日
T 日
T 日
MXJSRQ
T 日
T 日
T 日
MXFSRQ
T 日
T 日
T 日
MXQTRQ
MXSCDM
MXJYFS
‘03’
‘03’
‘03’
组合券证券代码
MXZQDM2
MXTGDY2
MXDDBH2
MXCWDH
MXPPHM
MXFJSM
MXBYBZ
（ 5 ）为配合基金管理人代收代付的后续优化， SJSMX0.DBF 中管理人的份
额记录的 MXJYDY 字段从填写 “ 投资者方的交易单元 ” 修改为填写 “ 投资者方的
托管单元 ” 。同时， SJSMX1.DBF 、 SJSMX2.DBF 及 SJSJG.DBF 接口也做相应调
整。
4.2.2 SJSMX1.DBF

（ 1 ） SJSMX1.DBF 中， SHXF 业务类别中不再包含跨市场 ETF 、跨境 ETF
及商品期货 ETF 的数据； SGSF 、 SGSZ 、 SGSQ 、 SHSF 、 SHSZ 、 SHSQ 业务类
别新增了跨市场 ETF 的数据。调整后的 SJSMX1.DBF 业务类别含义参见下表：
SJSMX1.DBF 业务类别含义表
业务类别
业务类别含义
JY00
集中竞价平台交易，综合金融服务平台交易（担保交收
模式）
SGSF
申购份额，包括单市场 ETF 、实物债券 ETF 、 <span style="color:red">跨市场</span>
<span style="color:red">ETF</span>
SGSZ
申购现金替代，包括单市场 ETF 、实物债券 ETF 、 <span style="color:red">跨市</span>
<span style="color:red">场</span> <span style="color:red">ETF</span>
SGSQ
申购组合券，包括单市场 ETF 、实物债券 ETF 、 <span style="color:red">跨市场</span>
<span style="color:red">ETF</span>
SHSF
赎回份额，包括单市场 ETF 、实物债券 ETF 、 <span style="color:red">跨市场</span>
<span style="color:red">ETF</span>
SHSZ
赎回现金替代，包括单市场 ETF 、实物债券 ETF 、 <span style="color:red">跨市</span>
<span style="color:red">场</span> <span style="color:red">ETF</span>
SHSQ
赎回组合券，包括单市场 ETF 、实物债券 ETF 、 <span style="color:red">跨市场</span>
<span style="color:red">ETF</span>
SGXF
申购份额，包括货币 ETF
SGXZ
申购现金替代，包括货币 ETF
SHXF
赎回份额，包括货币 ETF
SHXZ
赎回现金替代，包括货币 ETF
（ 2 ）所有 ETF 品种的交易及单市场 ETF 、实物债券 ETF 、货币 ETF 、跨市
场 ETF 场内的申赎结算模式均采用 A 股交收模式。 SJSMX1.DBF 中上述业务所
涉及到的业务类别，交收方式字段为 ‘Y’ 的数据均调整为 ‘A’ ； SGSQ 及 SHSQ 业
务类别的数据，交收方式字段为 ‘A’ ，保持不变。调整以后，各业务类别的字段
含义详见下表：
字段名
SHSF （ ETF
赎回份额）
SGSF （ ETF
申购份额）
SHSZ （ ETF
赎回现金
替代）
业务类别
JY00 （所有
ETF 的交
易）
SGSZ （ ETF
申购现金
替代）
MXJSZH
结算账号
结算账号
结算账号
结算账号
结算账号
MXBFZH
备付金账户 备付金账户 备付金账户 备付金账户 备付金账户
MXSJLX
‘01’
‘01’
‘01’
‘01’
‘01’
MXYWLB ‘JY00’
‘SGSF’
‘SGSZ’
‘SHSF’
‘SHSZ’
MXZQDM ETF 代码
ETF 代码
ETF 代码
ETF 代码
ETF 代码

业务流水号 业务流水号 业务流水号 业务流水号 业务流水号
MXJYDY
交易单元
交易单元
交易单元
交易单元
交易单元
MXTGDY
托管单元
托管单元
托管单元
托管单元
托管单元
MXZQZH
证券账户
证券账户
证券账户
证券账户
证券账户
MXDDBH
订单编号
订单编号
订单编号
订单编号
订单编号
MXYYB
营业部代码 营业部代码 营业部代码 营业部代码 营业部代码
MXZXBH
执行编号
执行编号
执行编号
执行编号
执行编号
MXYWLS
H
MXCJSL
成交数量
成交数量
成交数量
MXQSSL
清算数量
清算数量
清算数量
MXCJJG
交易回报价
格
MXQSJG
最终清算价
格
MXXYJY
信用交易标
志
MXPCBS
平仓标志
组合券代码
组合券代码
MXZQLB
‘EF’
‘EF’
‘EF’
‘EF’
‘EF’
MXZQZL
证券子类别 证券子类别 证券子类别 证券子类别 证券子类别
MXGFXZ
‘00’
‘00’
‘00’
‘00’
‘00’
MXJSFS
‘A’
‘A’
‘A’
‘A’
‘A’
MXHBDH
货币代号
货币代号
货币代号
货币代号
货币代号
MXQSBJ
清算本金
清算本金
清算本金
MXYHS
印花税
MXJYJSF
交易经手费
MXJGGF
监管规费
MXGHF
过户费
MXJSF
结算费
MXSXF
MXQSYJ
MXQTFY
MXZJJE
MXSFJE
收付净额
收付净额
收付净额
MXCJRQ
T 日
T 日
T 日
T 日
T 日
MXQSRQ
T 日
T 日
T 日
T 日
T 日
MXJSRQ
T+1 日
T+1 日
T+1 日
T+1 日
T+1 日
MXFSRQ
T 日
T 日
T 日
T 日
T 日
MXQTRQ
MXSCDM
MXJYFS
‘01’ 或 ‘02’
‘03’
‘03’
‘03’
‘03’
MXZQDM
2

MXTGDY
2
MXDDBH
2
MXCWD
H
MXPPHM
MXFJSM
MXBYBZ
字段名
业务类别
SGXF （货币
ETF
申购份
额）
SGXZ （货币
ETF
申购资
金）
<span style="color:red">SHXF</span> <span style="color:red">（货币</span>
<span style="color:red">ETF</span>
<span style="color:red">赎回份</span>
<span style="color:red">额）</span>
业务流水号
业务流水号
业务流水号
业务流水号
SHXZ( 货币
ETF
赎回资
金）
MXJSZH
结算账号
结算账号
结算账号
结算账号
MXBFZH
备付金账户
备付金账户
备付金账户
备付金账户
MXSJLX
‘01’
‘01’
‘01’
‘01’
MXYWLB
‘SGXF’
‘SGXZ’
‘SHXF’
‘SHXZ’
MXZQDM
ETF 代码
ETF 代码
ETF 代码
ETF 代码
MXJYDY
交易单元
交易单元
交易单元
交易单元
MXTGDY
托管单元
托管单元
托管单元
托管单元
MXZQZH
证券账户
证券账户
证券账户
证券账户
MXDDBH
订单编号
订单编号
订单编号
订单编号
MXYYB
营业部代码
营业部代码
营业部代码
营业部代码
MXZXBH
执行编号
执行编号
执行编号
执行编号
MXYWLS
H
MXCJSL
成交数量
成交数量
MXQSSL
清算数量
清算数量
MXCJJG
MXQSJG
MXXYJY
MXPCBS
MXZQLB
‘EF’
‘EF’
‘EF’
‘EF’
MXZQZL
证券子类别
证券子类别
证券子类别
证券子类别
MXGFXZ
‘00’
‘00’
‘00’
‘00’
MXJSFS
‘A’
‘A’
‘A’
‘A’
MXHBDH
货币代号
货币代号
货币代号
货币代号
MXQSBJ
清算本金
清算本金
MXYHS
MXJSF

MXJGGF
MXGHF
MXJSF
MXSXF
MXQSYJ
MXQTFY
MXZJJE
MXSFJE
收付净额
收付净额
MXCJRQ
T 日
T 日
T 日
T 日
MXQSRQ
T 日
T 日
T 日
T 日
MXJSRQ
T+1 日
T+1 日
T+1 日
T+1 日
MXFSRQ
T 日
T 日
T 日
T 日
MXQTRQ
MXSCDM
MXJYFS
‘03’
‘03’
‘03’
‘03’
MXZQDM
2
MXTGDY
2
MXDDBH
2
MXCWDH
MXPPHM
MXFJSM
MXBYBZ
4.2.3 SJSMX2.DBF
（ 1 ）原 SJSMX2.DBF 中的 SGSZ 和 SHSZ 业务类别为通过中国结算总部申
赎的深市跨市场 ETF 的现金替代明细清算数据。调整以后，通过中国结算总部
申赎的深市跨市场 ETF 的现金替代业务采用的业务类别变更为 SGDZ 和 SHDZ 。
SJSMX2.DBF 中不再包含业务类别为 SGSZ 和 SHSZ 的数据，新增了业务类别为
SGDZ 和 SHDZ 的数据； SJSMX2.DBF 中的 SHXZ 业务类别中不再包括跨市场
ETF 赎回的现金替代的数据。调整后的业务类别含义表如下：
SJSMX2.DBF 业务类别含义表
业务类别
业务类别含义
SGFY
ETF 申购税费、组合券过户费
SHFY
ETF 赎回税费、组合券过户费
<span style="color:red">SGDZ</span>
<span style="color:red">通过中国结算总部申购的</span> <span style="color:red">ETF</span> <span style="color:red">现金替代</span>
<span style="color:red">SHDZ</span>
<span style="color:red">通过中国结算总部赎回的</span> <span style="color:red">ETF</span> <span style="color:red">现金替代</span>

SHXZ
ETF 赎回现金替代 - 代收付
EFXC
ETF 申购赎回现金差额
EFTB
ETF 申购赎回现金替代多退少补
EFSY
货币 ETF 收益
（ 2 ） SJSMX2.DBF 新增的 SGDZ 和 SHDZ 业务类别，字段含义见下表：
业务类别
字段名
<span style="color:red">SGDZ</span> <span style="color:red">（通过中国结算总部</span>
<span style="color:red">申购的</span> <span style="color:red">ETF</span> <span style="color:red">现金替代）</span>
<span style="color:red">SHDZ</span> <span style="color:red">（通过中国结算总部</span>
<span style="color:red">赎回的</span> <span style="color:red">ETF</span> <span style="color:red">现金替代）</span>
MXJSZH
<span style="color:red">结算账号</span>
<span style="color:red">结算账号</span>
MXBFZH
<span style="color:red">备付金账户</span>
<span style="color:red">备付金账户</span>
MXSJLX
<span style="color:red">‘01’</span>
<span style="color:red">‘01’</span>
MXYWLB
<span style="color:red">‘SGDZ’</span>
<span style="color:red">‘SHDZ’</span>
MXZQDM
<span style="color:red">ETF</span> <span style="color:red">代码</span>
<span style="color:red">ETF</span> <span style="color:red">代码</span>
MXJYDY
<span style="color:red">交易单元</span>
<span style="color:red">交易单元</span>
MXTGDY
<span style="color:red">托管单元</span>
<span style="color:red">托管单元</span>
MXZQZH
<span style="color:red">证券账户</span>
<span style="color:red">证券账户</span>
MXDDBH
<span style="color:red">订单编号</span>
<span style="color:red">订单编号</span>
MXYYB
<span style="color:red">营业部代码</span>
<span style="color:red">营业部代码</span>
MXZXBH
MXYWLSH
<span style="color:red">业务流水号</span>
<span style="color:red">业务流水号</span>
MXCJSL
MXQSSL
MXCJJG
MXQSJG
MXXYJY
MXPCBS
MXZQLB
<span style="color:red">‘EF’</span>
<span style="color:red">‘EF’</span>
MXZQZL
<span style="color:red">证券子类别</span>
<span style="color:red">证券子类别</span>
MXGFXZ
MXJSFS
<span style="color:red">‘Z’</span>
<span style="color:red">‘Z’</span>
MXHBDH
<span style="color:red">货币代号</span>
<span style="color:red">货币代号</span>
MXQSBJ
<span style="color:red">负数，应付申购现金替代</span>
<span style="color:red">正数，应收赎回现金替代</span>
MXYHS
MXJYJSF
MXJGGF
MXGHF
MXJSF
MXSXF
MXQSYJ
MXQTFY

MXZJJE
MXSFJE
<span style="color:red">负数，应付申购现金替代</span>
<span style="color:red">正数，应收赎回现金替代</span>
MXCJRQ
<span style="color:red">成交日期</span>
<span style="color:red">成交日期</span>
MXQSRQ
<span style="color:red">T</span> <span style="color:red">日</span>
<span style="color:red">T</span> <span style="color:red">日</span>
MXJSRQ
<span style="color:red">T+1</span> <span style="color:red">日</span>
<span style="color:red">T+1</span> <span style="color:red">日</span>
MXFSRQ
<span style="color:red">T</span> <span style="color:red">日</span>
<span style="color:red">T</span> <span style="color:red">日</span>
MXQTRQ
MXSCDM
MXJYFS
<span style="color:red">‘05’</span>
<span style="color:red">‘05’</span>
MXZQDM2
<span style="color:red">组合券代码（若基金公司</span>
<span style="color:red">不提供，可能为空）</span>
<span style="color:red">组合券代码（若基金公司</span>
<span style="color:red">不提供，可能为空）</span>
MXTGDY2
MXDDBH2
MXCWDH
MXPPHM
MXFJSM
MXBYBZ
（ 3 ） SJSMX2.DBF 中业务类别为 SGFY 及 SHFY 的数据，订单编号、营业
部代码、执行编号字段的值，调整为 “ 对于通过总部申赎的跨市场 ETF 填写空 ” 。
业务类别
字段名
SGFY （ ETF 申购组合券
过户费）
SHFY （ ETF 赎回组合券
过户费）
MXJSZH
结算账号
结算账号
MXBFZH
备付金账户
备付金账户
MXSJLX
‘01’
‘01’
MXYWLB
‘SGFY’
‘SHFY’
MXZQDM
ETF 代码
ETF 代码
MXJYDY
交易单元
交易单元
MXTGDY
托管单元
托管单元
MXZQZH
证券账户
证券账户
MXDDBH
<span style="color:red">订单编号</span>
<span style="color:red">对于通过总部申赎的跨市</span>
<span style="color:red">场</span> <span style="color:red">ETF</span> <span style="color:red">，填写空。</span>
<span style="color:red">订单编号</span>
<span style="color:red">对于通过总部申赎的跨市</span>
<span style="color:red">场</span> <span style="color:red">ETF</span> <span style="color:red">，填写空。</span>
MXYYB
<span style="color:red">营业部代码</span>
<span style="color:red">对于通过总部申赎的跨市</span>
<span style="color:red">场</span> <span style="color:red">ETF</span> <span style="color:red">，填写空。</span>
<span style="color:red">营业部代码</span>
<span style="color:red">对于通过总部申赎的跨市</span>
<span style="color:red">场</span> <span style="color:red">ETF</span> <span style="color:red">，填写空。</span>
MXZXBH
<span style="color:red">执行编号</span>
<span style="color:red">对于通过总部申赎的跨市</span>
<span style="color:red">场</span> <span style="color:red">ETF</span> <span style="color:red">，填写空。</span>
<span style="color:red">执行编号</span>
<span style="color:red">对于通过总部申赎的跨市</span>
<span style="color:red">场</span> <span style="color:red">ETF</span> <span style="color:red">，填写空。</span>
MXYWLSH
业务流水号
业务流水号

MXCJSL
MXQSSL
MXCJJG
MXQSJG
MXXYJY
MXPCBS
MXZQLB
‘EF’
‘EF’
MXZQZL
证券子类别
证券子类别
MXGFXZ
‘00’
‘00’
MXJSFS
‘A’
‘A’
MXHBDH
货币代号
货币代号
MXQSBJ
MXYHS
MXJYJSF
MXJGGF
MXGHF
组合券过户费
组合券过户费
MXJSF
MXSXF
MXQSYJ
MXQTFY
MXZJJE
MXSFJE
收付净额
收付净额
MXCJRQ
T-1 日
T-1 日
MXQSRQ
T 日
T 日
MXJSRQ
T+1 日
T+1 日
MXFSRQ
T 日
T 日
MXQTRQ
MXSCDM
MXJYFS
‘03’ 或 ‘05’
‘03’ 或 ‘05’
MXZQDM2
组合券代码
组合券代码
MXTGDY2
MXDDBH2
MXCWDH
MXPPHM
MXFJSM
MXBYBZ
4.3 明细结果库 SJSJG.DBF
（ 1 ） SJSJG.DBF 中，不再包含业务类别为 SGSZ （跨市场 ETF 申购现金替
代 - 代收付）、 SHSZ （跨市场 ETF 申购现金替代 - 代收付）的数据；业务类别 SGXF 、

SGXZ 、 SHXF 、 SHXZ 不再包含深市跨市场 ETF 品种的数据；
新增 SGDZ 、 SHDZ 业务类别，分别表示通过中国结算总部申购的跨市场 ETF
申购现金替代 - 代收代付、通过中国结算总部赎回的跨市场 ETF 赎回现金替代 -
代收代付的明细结果数据；
（ 2 ） SJSJG.DBF 中不再包含 SGSF （ ETF 实物申购资金交收违约的待处分证
券回报）、 SGXF （ ETF 现金申购资金交收违约的待处分证券回报）业务类别的数
据。调整以后的 SJSJG.DBF 业务类别表参看下表：
SJSJG.DBF 业务类别表
接口业务
类别
业务类别含义
业务大类
SGSF
黄金 ETF 实物申购份额
SHSF
黄金 ETF 实物赎回份额
SGXF
<span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、商品期货</span> <span style="color:red">ETF</span> <span style="color:red">、黄金</span> <span style="color:red">ETF</span> <span style="color:red">、现</span>
<span style="color:red">金债券</span> <span style="color:red">ETF</span> <span style="color:red">的现金申购份额</span>
SGXZ
<span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、商品期货</span> <span style="color:red">ETF</span> <span style="color:red">、黄金</span> <span style="color:red">ETF</span> <span style="color:red">、现</span>
<span style="color:red">金债券</span> <span style="color:red">ETF</span> <span style="color:red">的现金申购现金替代</span>
SHXF
<span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、商品期货</span> <span style="color:red">ETF</span> <span style="color:red">、黄金</span> <span style="color:red">ETF</span> <span style="color:red">、现</span>
<span style="color:red">金债券</span> <span style="color:red">ETF</span> <span style="color:red">的现金赎回份额</span>
SHXZ
ETF 申赎（非担保类）
与货币 ETF 收益交收结
果
<span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、商品期货</span> <span style="color:red">ETF</span> <span style="color:red">、黄金</span> <span style="color:red">ETF</span> <span style="color:red">、现</span>
<span style="color:red">金债券</span> <span style="color:red">ETF</span> <span style="color:red">的现金赎回现金替代</span> <span style="color:red">-</span> <span style="color:red">代收</span>
<span style="color:red">付</span>
<span style="color:red">SGDZ</span>
<span style="color:red">通过中国结算总部申购的跨市场</span> <span style="color:red">ETF</span> <span style="color:red">申</span>
<span style="color:red">购现金替代</span> <span style="color:red">-</span> <span style="color:red">代收付</span>
<span style="color:red">SHDZ</span>
<span style="color:red">通过中国结算总部申购的跨市场</span> <span style="color:red">ETF</span> <span style="color:red">赎</span>
<span style="color:red">回现金替代</span> <span style="color:red">-</span> <span style="color:red">代收付</span>
EFXC
ETF 申购赎回现金差额
EFTB
ETF 申购赎回现金替代多退少补
EFSY
货币 ETF 收益
FGCX
卖空冲销
担保净额 DVP 交收违约
待处置
JY00
集中交易或综合协议交易（担保交收）
交收违约的待处分证券回报
（ 3 ） SJSJG.DBF 中新增的 SGDZ 和 SHDZ 业务类别，字段含义参看下表：
业务类别
字段名
<span style="color:red">SGDZ</span> <span style="color:red">（中国结算总部申</span>
<span style="color:red">购的跨市场</span> <span style="color:red">ETF</span> <span style="color:red">申购现</span>
<span style="color:red">金替代</span> <span style="color:red">-</span> <span style="color:red">代收付）</span>
<span style="color:red">SHDZ</span> <span style="color:red">（中国结算总部申</span>
<span style="color:red">购的跨市场</span> <span style="color:red">ETF</span> <span style="color:red">赎回现</span>
<span style="color:red">金替代</span> <span style="color:red">-</span> <span style="color:red">代收付）</span>

JGJSZH
<span style="color:red">结算账号</span>
<span style="color:red">结算账号</span>
JGBFZH
<span style="color:red">备付金账户</span>
<span style="color:red">备付金账户</span>
JGSJLX
<span style="color:red">‘01’</span>
<span style="color:red">‘01’</span>
JGYWLB
<span style="color:red">‘SGDZ’</span>
<span style="color:red">‘SHDZ’</span>
JGZQDM
<span style="color:red">ETF</span> <span style="color:red">代码</span>
<span style="color:red">ETF</span> <span style="color:red">代码</span>
JGJYDY
<span style="color:red">交易单元</span>
<span style="color:red">交易单元</span>
JGTGDY
<span style="color:red">托管单元</span>
<span style="color:red">托管单元</span>
JGZQZH
<span style="color:red">证券账户</span>
<span style="color:red">证券账户</span>
JGDDBH
<span style="color:red">订单编号</span>
<span style="color:red">订单编号</span>
JGYYB
JGZXBH
JGYWLSH
<span style="color:red">业务流水号</span>
<span style="color:red">业务流水号</span>
JGCJSL
JGQSSL
JGJSSL
JGCJJG
JGQSJG
JGXYJY
JGPCBS
JGZQLB
<span style="color:red">‘EF’</span>
<span style="color:red">‘EF’</span>
JGZQZL
<span style="color:red">证券子类别</span>
<span style="color:red">证券子类别</span>
JGGFXZ
JGLTLX
JGJSFS
<span style="color:red">‘Z’</span>
<span style="color:red">‘Z’</span>
JGHBDH
<span style="color:red">货币代号</span>
<span style="color:red">货币代号</span>
JGQSBJ
<span style="color:red">负数，应付申购现金替代</span> <span style="color:red">正数，应收赎回现金替代</span>
JGYHS
JGJYJSF
JGJGGF
JGGHF
JGJSF
JGSXF
JGQSYJ
JGQTFY
JGZJJE
JGSFJE
<span style="color:red">负数，应付申购现金替代</span> <span style="color:red">正数，应收赎回现金替代</span>
JGJSBZ
<span style="color:red">‘Y’</span> <span style="color:red">或</span> <span style="color:red">‘N’</span>
<span style="color:red">‘Y’</span> <span style="color:red">或</span> <span style="color:red">‘N’</span>
JGZYDH
<span style="color:red">若</span> <span style="color:red">JGJSBZ</span> <span style="color:red">为</span> <span style="color:red">‘N’,</span> <span style="color:red">则是错</span>
<span style="color:red">误代号</span>
<span style="color:red">若</span> <span style="color:red">JGJSBZ</span> <span style="color:red">为</span> <span style="color:red">‘N’,</span> <span style="color:red">则是错</span>
<span style="color:red">误代号</span>
JGCJRQ
<span style="color:red">成交日期</span>
<span style="color:red">成交日期</span>
JGQSRQ
<span style="color:red">T-1</span> <span style="color:red">日</span>
<span style="color:red">T-1</span> <span style="color:red">日</span>

JGJSRQ
<span style="color:red">T</span> <span style="color:red">日</span>
<span style="color:red">T</span> <span style="color:red">日</span>
JGFSRQ
<span style="color:red">T</span> <span style="color:red">日</span>
<span style="color:red">T</span> <span style="color:red">日</span>
JGQTRQ
JGSCDM
JGJYFS
<span style="color:red">‘05’</span>
<span style="color:red">‘05’</span>
JGZQDM2
<span style="color:red">组合券代码</span> <span style="color:red">(</span> <span style="color:red">如基金公司</span>
<span style="color:red">不提供，则为空</span> <span style="color:red">)</span>
<span style="color:red">组合券代码</span> <span style="color:red">(</span> <span style="color:red">如基金公司</span>
<span style="color:red">不提供，则为空</span> <span style="color:red">)</span>
JGTGDY2
JGDDBH2
JGFJSM
JGBYBZ
（ 4 ） SJSJG.DBF 中，跨境 ETF 、现金债券 ETF 、商品期货 ETF 现金赎回份额
（ SHXF ），现金债券 ETF 现金申购份额（ SGXF ）及现金申购现金替代（ SGXZ ）
的明细结果数据的成交日期及清算日期从 T-1 日调整为 T 日；黄金 ETF 现金申购份
额（ SGXF ）及现金申购现金替代（ SGXZ ）明细结果数据的 JGJSFS 字段从 ‘N’ 调
整为： ‘R’ 或 ‘N’ 。调整以后，跨境 ETF 、现金债券 ETF 、商品期货 ETF 、黄金 ETF
现金申购赎回的明细结果数据具体字段含义见下表：
业务类别
字段名
SGXF （ <span style="color:red">黄金</span> <span style="color:red">ETF</span> <span style="color:red">、</span>
<span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、商品期货</span>
<span style="color:red">ETF</span> <span style="color:red">、现金债券</span> <span style="color:red">ETF</span>
<span style="color:red">现金申购份额</span> ）
SGXZ （ <span style="color:red">黄金</span> <span style="color:red">ETF</span> <span style="color:red">、</span>
<span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、商品期货</span>
<span style="color:red">ETF</span> <span style="color:red">、现金债券</span> <span style="color:red">ETF</span>
<span style="color:red">现金申购现金替代</span> ）
SHXF （ <span style="color:red">黄金</span> <span style="color:red">ETF</span> <span style="color:red">、</span>
<span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、商品期货</span>
<span style="color:red">ETF</span> <span style="color:red">、现金债券</span> <span style="color:red">ETF</span>
<span style="color:red">现金赎回份额</span> ）
JGJSZH
结算账号
结算账号
结算账号
JGBFZH
备付金账户
备付金账户
备付金账户
JGSJLX
‘01’
‘01’
‘01’
JGYWLB
‘SGXF’
‘SGXZ’
‘SHXF’
JGZQDM
证券代码
证券代码
证券代码
JGJYDY
交易单元
交易单元
交易单元
JGTGDY
托管单元
托管单元
托管单元
JGZQZH
证券账户
证券账户
证券账户
JGDDBH
订单编号
订单编号
订单编号
JGYYB
营业部代码
营业部代码
营业部代码
JGZXBH
执行编号
执行编号
执行编号
JGYWLSH
业务流水号
业务流水号
业务流水号
JGCJSL
成交数量
0
成交数量
JGQSSL
清算数量
0
清算数量
JGJSSL
交收数量
( 交收失败时为 0)
交收数量
( 交收失败时为 0)

JGCJJG
JGQSJG
JGXYJY
JGPCBS
JGZQLB
‘EF’
‘EF’
证券类别
JGZQZL
证券子类别
证券子类别
证券子类别
JGGFXZ
‘00’
‘00’
‘00’
JGLTLX
‘0’
‘0’
流通类型
JGJSFS
<span style="color:red">‘R’</span> <span style="color:red">或</span> <span style="color:red">‘N’</span>
<span style="color:red">‘R’</span> <span style="color:red">或</span> <span style="color:red">‘N’</span>
‘N’
JGHBDH
货币代号
货币代号
JGQSBJ
JGYHS
JGJYJSF
JGJGGF
JGGHF
JGJSF
JGSXF
JGQSYJ
JGQTFY
JGZJJE
JGSFJE
收付净额
JGJSBZ
‘Y’ 或 ‘N’
‘Y’ 或 ‘N’
‘Y’ 或 ‘N’
JGZYDH
若 JGJSBZ 为 ‘N’, 则
是错误代号
若 JGJSBZ 为 ‘N’, 则
是错误代号
若 JGJSBZ 为 ‘N’, 则
是错误代号
JGCJRQ
<span style="color:red">T</span> <span style="color:red">日</span>
<span style="color:red">T</span> <span style="color:red">日</span>
<span style="color:red">T</span> <span style="color:red">日</span>
JGQSRQ
<span style="color:red">T</span> <span style="color:red">日</span>
<span style="color:red">T</span> <span style="color:red">日</span>
<span style="color:red">T</span> <span style="color:red">日</span>
JGJSRQ
T 日
T 日
T 日
JGFSRQ
T 日
T 日
T 日
JGQTRQ
JGSCDM
JGJYFS
‘03’
‘03’
‘03’
JGZQDM2
组合券证券代码
JGTGDY2
JGDDBH2
JGFJSM
JGBYBZ
4.4 股份对账库 SJSDZ.DBF
当日场内交易和申赎的 ETF 份额变动会体现在当日的股份对账库中。

4.5 资金清算汇总库 SJSQS.DBF
（ 1 ） SJSQS.DBF 中， SGSZ 和 SHSZ 业务类别中不再包括跨市场 ETF 实物申赎
( 总部 ) 的代收代付业务的数据；新增 SGDZ 和 SHDZ 业务类别，分别表示通过中国
结算总部申购 ETF 现金替代、通过中国结算总部赎回 ETF 现金替代的资金清算数
据；
（ 2 ） SJSQS.DBF 中， SGXZ 和 SHXZ 业务类别中不再包括跨市场 ETF 全额现
金申购和全额现金赎回现金替代；调整后的 SJSQS.DBF 业务含义见下表 ：
SJSQS.DBF 业务含义表
业务类
别
相应业务含义
说明
JY00
QSZQDM 为证券类别
成交日期 = 清算日期（ B 股为清算日期 -2 ，延迟
交收除外），交收日期 = 清算日期 +1
集中竞价交易、综
合金融服务平台
（担保交收模式）
交易清算
SGSZ
ETF 申购现金替代
<span style="color:red">QSZQDM</span> <span style="color:red">为</span> <span style="color:red">ETF</span> <span style="color:red">证券代码（单市场</span> <span style="color:red">ETF</span> <span style="color:red">、实物</span>
<span style="color:red">债券</span> <span style="color:red">ETF</span> <span style="color:red">、跨市场</span> <span style="color:red">ETF</span> <span style="color:red">）。成交日期</span> <span style="color:red">=</span> <span style="color:red">清算日期，</span>
<span style="color:red">交收日期</span> <span style="color:red">=</span> <span style="color:red">清算日期</span> <span style="color:red">+1</span> <span style="color:red">。</span>
SHSZ
ETF 赎回现金替代
<span style="color:red">QSZQDM</span> <span style="color:red">为</span> <span style="color:red">ETF</span> <span style="color:red">证券代码（单市场</span> <span style="color:red">ETF</span> <span style="color:red">、实物</span>
<span style="color:red">债券</span> <span style="color:red">ETF</span> <span style="color:red">、跨市场</span> <span style="color:red">ETF</span> <span style="color:red">）。成交日期</span> <span style="color:red">=</span> <span style="color:red">清算日期，</span>
<span style="color:red">交收日期</span> <span style="color:red">=</span> <span style="color:red">清算日期</span> <span style="color:red">+1</span> <span style="color:red">。</span>
SGXZ
ETF 申购现金替代
QSZQDM 为 ETF 证券代码（ <span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、现金债</span>
<span style="color:red">券</span> <span style="color:red">ETF</span> <span style="color:red">、商品期货</span> <span style="color:red">ETF</span> <span style="color:red">、黄金</span> <span style="color:red">ETF</span> <span style="color:red">、货币</span> <span style="color:red">ETF</span> ）。
对于非担保模式（含 RTGS ）（ <span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、现金</span>
<span style="color:red">债券</span> <span style="color:red">ETF</span> <span style="color:red">、商品期货</span> <span style="color:red">ETF</span> <span style="color:red">、黄金</span> <span style="color:red">ETF</span> <span style="color:red">现金申购</span> ），
成交日期、清算日期和交收日期均为当日；对
于担保模式（货币 ETF ），成交日期 = 清算日期，
交收日期 = 清算日期 +1 。
对于非担保模式（含 RTGS ），按 “ 证券 ”+“ 托管
单元 ” ，分买入和卖出各下发一条记录。买入记
录中的卖出金额为 0 ，卖出记录中的买入金额为
0 。
SHXZ
ETF 赎回现金替代
QSZQDM 为 ETF 证券代码（ <span style="color:red">跨境</span> <span style="color:red">ETF</span> <span style="color:red">、现金债</span>
<span style="color:red">券</span> <span style="color:red">ETF</span> <span style="color:red">、商品期货</span> <span style="color:red">ETF</span> <span style="color:red">、黄金</span> <span style="color:red">ETF</span> <span style="color:red">、货币</span> <span style="color:red">ETF</span> ）。
对于代收代付（ <span style="color:red">黄金</span> <span style="color:red">ETF</span> <span style="color:red">、商品期货</span> <span style="color:red">ETF</span> <span style="color:red">、跨</span>
<span style="color:red">境</span> <span style="color:red">ETF</span> <span style="color:red">、现金债券</span> <span style="color:red">ETF</span> ），成交日期 = 空，交收
日期 = 清算日期 +1 ；对于担保模式（货币 ETF
现金赎回），成交日期 = 清算日期，交收日期 = 清
算日期 +1 。
对于代收代付，按 “ 证券 ”+“ 托管单元 ” ，分买入

业务类
别
相应业务含义
说明
和卖出各下发一条记录。买入记录中的卖出金
额为 0 ，卖出记录中的买入金额为 0 。
<span style="color:red">SGDZ</span>
<span style="color:red">通过中国结算总部</span>
<span style="color:red">申购</span> <span style="color:red">ETF</span> <span style="color:red">现金替代</span>
<span style="color:red">QSZQDM</span> <span style="color:red">为</span> <span style="color:red">ETF</span> <span style="color:red">证券代码（跨市场</span> <span style="color:red">ETF</span> <span style="color:red">实物</span>
<span style="color:red">申购），成交日期为空，清算日期为当日，交收</span>
<span style="color:red">日期</span> <span style="color:red">=</span> <span style="color:red">清算日期</span> <span style="color:red">+1</span> <span style="color:red">；按</span> <span style="color:red">“</span> <span style="color:red">证券</span> <span style="color:red">”+“</span> <span style="color:red">托管单元</span> <span style="color:red">”</span> <span style="color:red">，分</span>
<span style="color:red">买入和卖出各下发一条记录。买入记录中的卖</span>
<span style="color:red">出金额为</span> <span style="color:red">0</span> <span style="color:red">，卖出记录中的买入金额为</span> <span style="color:red">0</span> <span style="color:red">。</span>
<span style="color:red">SHDZ</span>
<span style="color:red">通过中国结算总部</span>
<span style="color:red">赎回</span> <span style="color:red">ETF</span> <span style="color:red">现金替代</span>
<span style="color:red">QSZQDM</span> <span style="color:red">为</span> <span style="color:red">ETF</span> <span style="color:red">证券代码（跨市场</span> <span style="color:red">ETF</span> <span style="color:red">实物</span>
<span style="color:red">赎回），成交日期为空，清算日期为当日，交收</span>
<span style="color:red">日期</span> <span style="color:red">=</span> <span style="color:red">清算日期</span> <span style="color:red">+1</span> <span style="color:red">；按</span> <span style="color:red">“</span> <span style="color:red">证券</span> <span style="color:red">”+“</span> <span style="color:red">托管单元</span> <span style="color:red">”</span> <span style="color:red">，分</span>
<span style="color:red">买入和卖出各下发一条记录。买入记录中的卖</span>
<span style="color:red">出金额为</span> <span style="color:red">0</span> <span style="color:red">，卖出记录中的买入金额为</span> <span style="color:red">0</span> <span style="color:red">。</span>
SGFY
ETF 申购税费、组
合券过户费
QSZQDM 为 ETF 证券代码。
成交日期 = 清算日期 -1 ，交收日期 = 清算日期 +1 。
本记录为上个交易日申购业务相关的费用。
SHFY
ETF 赎回税费、组
合券过户费
QSZQDM 为 ETF 证券代码。
成交日期 = 清算日期 -1 ，交收日期 = 清算日期 +1 。
本记录为上个交易日赎回业务相关的费用。
EFXC
ETF 申购赎回现金
差额
QSZQDM 为 ETF 证券代码。
成交日期为空，清算日期为当日，交收日期 = 清
算日期 +1 。
买入金额为补款金额，卖出金额为退款金额。
对于某 “ 证券 ”+“ 托管单元 ” ，分买入和卖出各下
发一条记录。买入记录中的卖出金额为 0 ，卖出
记录中的买入金额为 0 。
EFTB
ETF 申购赎回现金
替代多退少补
QSZQDM 为 ETF 证券代码。
成交日期为空，清算日期为当日，交收日期 = 清
算日期 +1 。
买入金额为补款金额，卖出金额表示退款金额。
对于某 “ 证券 ”+“ 托管单元 ” ，分买入和卖出各下
发一条记录。买入记录中的卖出金额为 0 ，卖出
记录中的买入金额为 0 。
EFSY
货币 ETF 收益
QSZQDM 为 ETF 证券代码。
成交日期为空，清算日期为当日，交收日期 = 清
算日期 +1 。
QSMCJE 为基金收益。
（ 3 ） SJSQS.DBF 中所涵盖的以担保方式交收的 ETF 交易、申赎相关的业务，
交收方式字段为 ‘Y’ 的变更为 ‘A’ 。
（ 4 ） SJSQS.DBF 中 ETF 品种涉及的业务类别的对应关系调整为下表：

ETF 品种
涉及的业务类别
单市场 ETF
SGSZ 、 SHSZ 、 EFXC 、 EFTB 、 SGFY 、 SHFY
实物债券 ETF
SGSZ 、 SHSZ 、 EFXC 、 EFTB 、 SGFY 、 SHFY
现金债券 ETF
SGXZ 、 SHXZ 、 EFXC 、 EFTB
跨市场 ETF
<span style="color:red">SGSZ</span> <span style="color:red">、</span> <span style="color:red">SHSZ</span> <span style="color:red">、</span> <span style="color:red">EFXC</span> <span style="color:red">、</span> <span style="color:red">EFTB</span> <span style="color:red">、</span> <span style="color:red">SGFY</span> <span style="color:red">、</span> <span style="color:red">SHFY</span> <span style="color:red">、</span> <span style="color:red">SGDZ</span> <span style="color:red">、</span>
<span style="color:red">SHDZ</span>
跨境 ETF
SGXZ 、 SHXZ 、 EFXC 、 EFTB
商品期货 ETF
SGXZ 、 SHXZ 、 EFXC 、 EFTB
黄金 ETF
SGXZ 、 SHXZ 、 EFXC 、 EFTB
货币 ETF
SGXZ 、 SHXZ 、 EFXC 、 EFTB
4.6 T+0 资金清算汇总库 SJSQS0.DBF
ETF 交易和申赎现金替代（担保类），从担保 DVP 模式调整为 A 股交收模
式。 SJSQS0 中所涵盖的以担保方式交收的 ETF 交易、申赎相关的业务，交收方
式字段为 ‘Y’ 的调整为 ‘A’ 。
SJSQS0 清算业务含义表（表 3-2 ）
新业务类别
相应业务含义
说明
JY00
交易
<span style="color:red">担保模式</span>
SGSZ
申购现金替代
<span style="color:red">担保模式</span>
SHSZ
赎回现金替代
<span style="color:red">担保模式</span>
SGXZ
申购现金替代
<span style="color:red">担保模式</span>
SHXZ
赎回现金替代
<span style="color:red">担保模式</span>
4.7 资金变动库 SJSZJ.DBF
SJSZJ.DBF 中， SGXZ 和 SHXZ 中不再包括跨市场 ETF 品种；新增 SGDZ
和 SHDZ 业务类别，分别表示通过中国结算总部申购 ETF 现金替代业务资金变
动和通过中国结算总部赎回 ETF 现金替代业务资金变动。调整后的 SJSZJ.DBF
业务类别含义如下表：
SJSZJ.DBF 中业务类别含义表
ZJYWLB
业务类别含义
ZJZQDM
SGFY
ETF 申购税费、组合券过户费
证券代码
SGSZ
ETF 申购现金替代
证券代码
SGXZ
ETF 申购现金替代
证券代码
SHFY
ETF 赎回税费、组合券过户费
证券代码

SHSZ
ETF 赎回现金替代
证券代码
SHXZ
ETF 赎回现金替代
证券代码
<span style="color:red">SGDZ</span>
<span style="color:red">通过中国结算总部申购</span> <span style="color:red">ETF</span> <span style="color:red">现金替代</span>
<span style="color:red">证券代码</span>
<span style="color:red">SHDZ</span>
<span style="color:red">通过中国结算总部赎回</span> <span style="color:red">ETF</span> <span style="color:red">现金替代</span>
<span style="color:red">证券代码</span>
4.8 资金余额库 SJSYE.DBF
SJSYE.DBF 中，原 T+1 担保 DVP 结算模式的 ETF 业务更改为 A 股交收模
式，在计算可提金额 SJSYE.YEKTZJ 时， ETF 交收净额与原 A 股交收净额合并
处理。
4.9 广播类信息库 SJSGB.DBF
SJSGB.DBF 中权益参数的发送日期发生调整，从 “ 权益参数在权益登记日（对
ETF 和 B 股为最后交易日）发送 ” 调整为 “ 权益参数在权益登记日（ B 股为最后交
易日）发送 ” 。
4.10 综合数据服务库 SJSFW.DBF
通过托管人结算的、采用担保结算模式的 ETF 申赎类业务纳入托管人结算保
证金额度的计算范围，其中 ETF 结算备付金账户的日均结算净额将合并计入其托
管人综合结算备付金的日均结算净额中，并进行保证金调整的计算。 SJSFW.DBF
中， FWSJLB 为 ‘0A’ （ A 股保证金调整计算明细数据）的数据，对于托管人托管
的 ETF 产品申购赎回的日均结算净额， FWZQZH 字段为对应的 ETF 产品的结算账
号。调整以后， SJSFW.DBF 中业务类别为 ‘0A’ 的数据，各字段含义如下：
字段名
数据类别说明含义
FWSJLB
0A
FWJSZH
结算账号
FWBFZH
备付金账户
FWTGDY
FWZQDM
<span style="color:red">对托管人托管产品的数据</span> <span style="color:red">,</span> <span style="color:red">为对应产品的股东代</span>
FWZQZH
<span style="color:red">码；对</span> <span style="color:red">ETF</span> <span style="color:red">结算账户的申购赎回数据，为</span> <span style="color:red">ETF</span> <span style="color:red">结</span>

<span style="color:red">算账号；其他情况本字段为空</span>
FWGFXZ
FWLTLX
本期保证金调整时间段内的权益类日均结算净
FWMRJE
额
本期保证金调整时间段内的固定收益类日均结
FWMCJE
算净额
FWZJYE
FWSL1
FWSL2
FWCLRQ
T 日
FWFSRQ
T 日
第 1 到第 8 个字符为本期保证金调整时间段的开
FWZYSM
始日期，第 9 到第 16 字符为本期保证金调整时间
段的结束日期。日期格式为 YYYYMMDD
FWBZSM
FWBYBZ
五． 联系方式
深圳证券交易所：
业务咨询： 0755-88668839, 0755-88668817
技术咨询： 0755-88668196, 0755-88668727
中国结算深圳分公司：
业务咨询： 0755-21899269
技术咨询： 0755-25946080
深圳证券交易所
中国证券登记结算有限责任公司深圳分公司
2019 年 4 月 8 日

> **变更标注说明**：本文档中已用 `<span style="color:...">` 标注了变更内容（红色=修改/新增，蓝色=其他说明）。


<metadata>
{
  "title": "20190509_深市ETF交易结算模式调整技术变更指南",
  "source_url": null,
  "raw_path": "knowledge\\raw\\szse\\技术指南\\20190509_深市ETF交易结算模式调整技术变更指南.pdf",
  "markdown_path": "knowledge\\articles\\szse\\markdown\\技术指南\\深市ETF交易结算模式调整技术变更指南.md",
  "file_hash": "sha256:b642ebc991ce6996ababe706c1d8c8d7a061cfda5fd71f7cc158dc5d7cbc266d",
  "file_format": "pdf",
  "page_count": 24,
  "doc_type": "guide",
  "version": null,
  "previous_version": null,
  "public_date": null,
  "effective_date": null,
  "has_changes": true,
  "parse_status": "success",
  "parse_date": "2026-06-13T17:45:48.213600+00:00",
  "sub_category": null
}
</metadata>