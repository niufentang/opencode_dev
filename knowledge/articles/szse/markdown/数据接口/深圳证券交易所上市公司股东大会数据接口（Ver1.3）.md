深圳证券交易所工程技术文档
工程技术标准
深圳证券交易所上市公司股东大会
数据接口
（ Ver 1.3 ）
深圳证券交易所
二○二二年十一月

工程技术标准
- I -
目 录
前 言 .................................................................................................................................................... 1
关于本文档 .......................................................................................................................................... 2
上市公司股东大会数据接口 .............................................................................................................. 3
1.
上市公司股东大会基本信息文件 ...................................................................................... 3
2.
股东大会基本信息校验文件 .............................................................................................. 9
深圳证券交易所 深圳证券交易所深交所上市公司股东大会数据接口

工程技术标准
第 1 页 共 10 页
前 言
一、 目标说明
为便于会员更好地为投资者提供交易系统网络投票服务，我所将通过交易网
络向各会员单位等市场参与者发送上市公司股东大会数据。每交易日收市后（通
常于 20:00 前）通过双向通信系统自动发送，接口库的文件名为
evoteparams_yyyymmdd.xml 。
二、 相关事宜
本版规范由深交所信息科技二部和深圳证券信息有限公司负责起草，负责对
本次修订部分的解释。
通信地址 ：深圳市深南大道 2012 号深圳证券交易所信息科技二部
邮政编码 ： 518038
联系电话 ： 0755-83991192 、 83990926 （深圳证券信息有限公司）
0755-82083500 、 88668863 （深交所信息科技二部）
E-mail
： ssegcb@szse.cn    vote@cninfo.com.cn
网站地址 ： www.szse.cn      www.cninfo.com.cn
网上咨询 ： http://www.szse.cn/szseWebTCS/
深圳证券交易所
二○一五年四月
深圳证券交易所 深圳证券交易所深交所上市公司股东大会数据接口

工程技术标准
第 2 页 共 10 页
关于本文档
修订历史
日期
版本
操作
说明
2015-03
Ver 0.9
创建文档
征求意见稿。
1 、修改上市公司股东大会信息的文件名称；
2 、删除 streamID 字段，修改相关字段的英文命名；
2015-04
Ver 1.0
修订文档
3 、修改公司简称、投票代码的长度，详细说明投票
代码的数据格式。
1 、详细说明投票代码、基础证券代码、基础证券简
称等字段的业务含义；
2015-05
Ver1.1
修订文档
2 、详细描述 MD5 码的长度及取值；
3 、将股东大会信息等文件详细示例。
2020-04
Ver1.2
修订文档
增加 SymbolEx 字段
2022-11
Ver1.3
修订文档
（本文档中橙色修订部分）
增加 CompanySymbolEx 字段
深圳证券交易所 深圳证券交易所深交所上市公司股东大会数据接口

工程技术标准
第 3 页 共 10 页
上市公司股东大会数据接口
1. 上市公司股东大会基本信息文件
1 ） 报送内容
上市公司股东大会基本信息包括但不限于投票代码、投票简称、基础证券
代码、投票时间、议案编号、议案类型、议案标题等，相关信息仅供参考。
2 ） 命名规则
evoteparams_yyyymmdd.xml
其中， yyyymmdd 为投票生效日。
3 ） 内容与格式
SecurityID
evoteparams_yyyymmdd.xml
投票议案公告文件
描述：
上市公司股东大会基本信息，包括投票议案和投票信息。其中yyyymmdd 为投票生效日。对于投票
代码、基础证券代码，代码不足8 位，将在代码后端补齐空格。
编号
字段名
类型
描述
备注
XML 字段名
1
投票代码
C 8
投票代码
必填
同一上市公司
的 A 股、 B 股
使用相同的投
票代码，该上
市公司的每期
优先股分别使
用一个不同的
投票代码。
SymbolEx
2
投票简称
C40
投票简称
Symbol
3
投票简称（扩）
C40
预留
存放长简称，若无长简称，
与投票简称内容一致
必填
UnderlyingSecuri
tyID
4
基础证券代码
C 8
对于普通股投票代码，若
为纯 B 股公司，本字段填
写为 B 股证券代码，否则
填写为 A 股证券代码。
对于优先股投票代码，本
字段填写为对应优先股的
证券代码。
U40
相应基础证券的证券简称 必填
CompanySymbol
Ex
5
基础证券简称
U 40
相应基础证券的证券简称 必填
CompanySymbol
6
基础证券简称
（扩）
深圳证券交易所 深圳证券交易所深交所上市公司股东大会数据接口

工程技术标准
第 4 页 共 10 页
RegDate
编号
字段名
类型
描述
备注
XML 字段名
7
股权登记日
N8
不同投票代码可能不同 ,
格式： yyyymmdd
LastTradeDate
8
最后交易日
N8
不同投票代码可能不同 ,
格式： yyyymmdd
9
股东大会开始日
N8
格式： yyyymmdd
必填
MeetingBeginDate
10
股东大会结束日
N8
格式： yyyymmdd
必填
MeetingEndDate
11
股东大会类型
C 4
临时 / 年度
必填
MeetingType
12
股东大会名称
C 500
股东大会名称
必填
MeetingDesc
13
股东大会编码
C10
股东大会唯一序列号
必填
MeetingSeq
必填
ProposalID
14
议案编号
C10
投票议案（组）编号及子
议案编号。
整数编号代表普通议案。
例如： 1 表示普通议案 1 。
带二位小数的编号代表议
案组及子议案。例如： 2.00
表示议案组 2 的标题， 2.01
表示议案组 2 的第一个子
议案， 2.02 表示议案组 2
的第二个子议案。
必填
ProposalType
15
议案名称
C 1000
必填
ProposalName
16
议案类型
C 1
L= 累计投票议案
P= 普通议案
非必填
ElectionNum
17
累计投票应选数
N4
若填写，则必须填写正整
数
必填
ShareHolderRole
18
股东身份
C 50
A 股股东 /B 股股东 / 优先
股股东 / 恢复表决权的优
先股股东
非必填
ShareClass
19
议案关系
C 100
议案关系
非必填
ProposalRelation
20
股份类别
C 20
A 股 /B 股 / 优先股 / 恢复表
决权优先股
必填
refcode
21
投票代码指引
C150
股东议案的投票代码指
引。用以在议案股东类别
和投票代码之间建立关
联，方便程序自动化处理
注：投票代码、基础证券代码定义为 C （ 8 ），目前只启用前六位字符，比如
平安银行的普通股投票代码为“ 360001 ”、基础证券代码为“ 000001 ”。中文
信息采用 UTF-8 编码、简体中文。 数据类型 Cx 表示最多 x 个字节， Ux 表示最多
x 个 UTF-8 字符，下同。
深圳证券交易所 深圳证券交易所深交所上市公司股东大会数据接口

工程技术标准
第 5 页 共 10 页
股东大会信息文件示例如下（ evoteparams_20150420.xml ）：
<?xml version="1.0" encoding="UTF-8"?>
<rootvote>
<company>
<UnderlyingSecurityID>002097  </UnderlyingSecurityID>
<CompanySymbol> 山河智能 </CompanySymbol>
<CompanySymbolEx> 山河智能扩位简称 </CompanySymbolEx>
<MeetingSeq>22053</MeetingSeq>
<votecodelist>
<SecurityID LastTradeDate="" RegDate="20150415" ShareClass="A 股 " Symbol=" 山河投票 "
SymbolEx=" 山河投票 ">362097  </SecurityID>
</votecodelist>
<MeetingBeginDate>20150420</MeetingBeginDate>
<MeetingEndDate>20150420</MeetingEndDate>
<MeetingDesc> 山河智能 2015 年第二次临时股东大会 </MeetingDesc>
<MeetingType> 临时 </MeetingType>
<volist>
<vote ProposalID="1" ProposalName=" 关于修改公司章程的议案 " ProposalType="P"
ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="362097  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="2" ProposalName=" 关于补选第五届董事会董事的议案 " ProposalType="P"
ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="362097  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="3" ProposalName=" 股东大会中小投资者单独计票及披露办法 "
ProposalType="P" ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="362097  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="4" ProposalName=" 股东大会中小投资者单独计票及披露办法 "
ProposalType="P" ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="362097  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
</volist>
</company>
<company>
<UnderlyingSecurityID>000890  </UnderlyingSecurityID>
<CompanySymbol> 法 尔 胜 </CompanySymbol>
<CompanySymbolEx> 法 尔 胜扩位简称 </CompanySymbolEx>
<MeetingSeq>21930</MeetingSeq>
<votecodelist>
<SecurityID LastTradeDate="" RegDate="20150410" ShareClass="A 股 " Symbol=" 法尔投票 "
SymbolEx=" 法尔投票 ">360890  </SecurityID>
</votecodelist>
<MeetingBeginDate>20150420</MeetingBeginDate>
<MeetingEndDate>20150420</MeetingEndDate>
<MeetingDesc> 法 尔 胜 2014 年度股东大会 </MeetingDesc>
<MeetingType> 年度 </MeetingType>
<volist>
<vote ProposalID="1" ProposalName=" 审议修改公司《章程》的议案 " ProposalType="P"
ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
深圳证券交易所 深圳证券交易所深交所上市公司股东大会数据接口

工程技术标准
第 6 页 共 10 页
</vrolelist>
</vote>
<vote ProposalID="2" ProposalName=" 审议公司《 2014 年度报告正文及摘要》 " ProposalType="P"
ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="3" ProposalName=" 审议公司《 2014 年度董事会工作报告》 " ProposalType="P"
ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="4" ProposalName=" 审议公司《 2014 年度监事会工作报告》 " ProposalType="P"
ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="5" ProposalName=" 审议公司《 2014 年度财务决算报告》 " ProposalType="P"
ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="6" ProposalName=" 审议公司 2014 年度利润分配预案 " ProposalType="P"
ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="7" ProposalName=" 审议公司《关于 2015 年度日常关联交易预计》的议案 "
ProposalType="P" ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="8" ProposalName=" 审议续聘江苏公证天业会计师事务所（特殊普通合伙）为本
公司 2015 年度审计机构的议案 " ProposalType="P" ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="9" ProposalName=" 审议续聘江苏世纪同仁律师事务所的议案 "
ProposalType="P" ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="10.00" ProposalName=" 审议关于公司董事会变更独立董事的议案 "
ProposalType="L" ProposalRelation="" ElectionNum="3">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="10.01" ProposalName=" 程龙生 " ProposalType="L" ProposalRelation=""
ElectionNum="3">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote
ProposalID="10.02"
ProposalName=" 周辉 "
ProposalType="L"
ProposalRelation=""
深圳证券交易所 深圳证券交易所深交所上市公司股东大会数据接口

工程技术标准
第 7 页 共 10 页
ElectionNum="3">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="10.03" ProposalName=" 李明辉 " ProposalType="L" ProposalRelation=""
ElectionNum="3">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
<vote ProposalID="11" ProposalName=" 审议《公司未来三年回报规划》 " ProposalType="P"
ProposalRelation="" ElectionNum="">
<vrolelist>
<ShareHolderRole refcode="360890  ">A 股股东 </ShareHolderRole>
</vrolelist>
</vote>
</volist>
</company>
</rootvote>
schema 文件示例如下（ evoteparams.xsd ）：
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema
xmlns:xs="http://www.w3.org/2001/XMLSchema"
elementFormDefault="qualified"
attributeFormDefault="unqualified">
<xs:element name="rootvote">
<xs:complexType>
<xs:sequence>
<xs:element name="company" maxOccurs="unbounded">
<xs:complexType>
<xs:sequence>
<xs:element name="UnderlyingSecurityID" type="companycodetype"/>
<xs:element name="CompanySymbol" type="xs:string"/>
<xs:element name="CompanySymbolEx" type="xs:string"/>
<xs:element name="MeetingSeq" type="xs:string"/>
<xs:element name="votecodelist" type="votecodelisttype"/>
<xs:element name="MeetingBeginDate" type="datetype"/>
<xs:element name="MeetingEndDate" type="datetype"/>
<xs:element name="MeetingDesc" type="xs:string"/>
<xs:element name="MeetingType" type="meetingtypetype"/>
<xs:element name="volist" type="volisttype"/>
</xs:sequence>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:complexType>
</xs:element>
<xs:complexType name="votecodelisttype">
<xs:sequence>
<xs:element name="SecurityID" type="votecodetype" minOccurs="1" maxOccurs="unbounded"/>
</xs:sequence>
</xs:complexType>
<xs:complexType name="volisttype">
<xs:sequence>
<xs:element name="vote" type="votetype" minOccurs="1" maxOccurs="unbounded"/>
</xs:sequence>
</xs:complexType>
<xs:complexType name="votetype">
<xs:sequence>
<xs:element name="vrolelist">
<xs:complexType>
<xs:sequence>
<xs:element
name="ShareHolderRole"
type="vroletype"
minOccurs="1"
maxOccurs="unbounded"/>
深圳证券交易所 深圳证券交易所深交所上市公司股东大会数据接口

工程技术标准
第 8 页 共 10 页
</xs:sequence>
</xs:complexType>
</xs:element>
</xs:sequence>
<xs:attribute name="ProposalID" type="xs:string" use="required"/>
<xs:attribute name="ProposalName" type="xs:string" use="required"/>
<xs:attribute name="ProposalType" type="vtypetype" use="required"/>
<xs:attribute name="ProposalRelation" type="xs:string"/>
<xs:attribute name="ElectionNum" type="xs:string"/>
</xs:complexType>
<xs:complexType name="votecodetype">
<xs:simpleContent>
<xs:extension base="companycodetype">
<xs:attribute name="LastTradeDate" type="xs:string"/>
<xs:attribute name="RegDate" type="datetype"/>
<xs:attribute name="ShareClass" type="stypetype"/>
<xs:attribute name="Symbol" type="xs:string"/>
<xs:attribute name="SymbolEx" type="xs:string"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>
<xs:simpleType name="companycodetype">
<xs:restriction base="xs:string">
<!-- 数字或空格，必须是 8 位 -->
<xs:pattern value="[0-9 ]{8}"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="datetype">
<xs:restriction base="xs:string">
<xs:pattern value="([0-9]{8})|([0-9]{0})"/>
<!-- 日期， YYYYMMDD-->
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="vtypetype">
<xs:restriction base="xs:string">
<xs:enumeration value="P">
<!-- 普通议案 -->
</xs:enumeration>
<xs:enumeration value="L">
<!-- 累计投票议案 -->
</xs:enumeration>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="vroletype">
<xs:simpleContent>
<xs:extension base="vrolebasetype">
<xs:attribute name="refcode" type="companycodetype" use="required"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>
<xs:simpleType name="vrolebasetype">
<xs:restriction base="xs:string">
<xs:enumeration value="A 股股东 "/>
<xs:enumeration value="B 股股东 "/>
<xs:enumeration value=" 优先股股东 "/>
<xs:enumeration value=" 恢复表决权的优先股股东 "/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="meetingtypetype">
<xs:restriction base="xs:string">
<xs:enumeration value=" 临时 "/>
<xs:enumeration value=" 年度 "/>
</xs:restriction>
</xs:simpleType>
深圳证券交易所 深圳证券交易所深交所上市公司股东大会数据接口

工程技术标准
第 9 页 共 10 页
<xs:simpleType name="stypetype">
<xs:restriction base="xs:string">
<xs:enumeration value="A 股 "/>
<xs:enumeration value="B 股 "/>
<xs:enumeration value=" 优先股 "/>
<xs:enumeration value=" 恢复表决权的优先股 "/>
</xs:restriction>
</xs:simpleType>
</xs:schema>
2. 股东大会基本信息校验文件
1 ） 命名规则
evoteparams_yyyymmddVd.xml （在股东大会信息文件后加了 Vd ），其中
yyyymmdd 为投票生效日。
2 ） 内容与格式
evoteparams_yyyymmddVd.xml
校验文件
描述：
提供校验信息，用于校验股东大会信息文件。
file
编号
字段名
描述
类型
备注
XML 字段名
1
文件名
对应股东大会基本信息文件文件
名
C 60
必填
必须校验
2
字节
数据文件大小
C 16
必填
size
3
日期
YYYYMMDD, 数据文件生成日期
C 8
必填
date
4
时间
24HHMMSS ，为数据文件生成时间 C 6
必填
time
companycount
5
公司数
公司数
C 6
必填
必须校验
votecount
6
议案数
议案数
C 12
必填
必须校验
md5
C 64
必填
必须校验
7
MD5
股东大会信息文件对应的 32 字节
MD5 校验码， 16 进制字符表示，
每个字节表示一个 16 进制字符，
字母均为大写
校验文件示例如下（ evoteparams_20150420Vd.xml ）：
<?xml version="1.0" encoding="UTF-8"?>
<validate >
<!-- 对应股东大会基本信息文件文件名 -->
<file>evoteparams_20150420.XML</file>
<!-- 数据文件大小 -->
<size>5812</size>
<!-- 数据文件生成日期 -->
<date>20150420</date>
<!-- 数据文件生成时间 -->
<time>161658</time>
<!-- 公司数 -->
深圳证券交易所 深圳证券交易所深交所上市公司股东大会数据接口

工程技术标准
第 10 页 共 10
页
<companycount>2</companycount>
<!-- 议案数 -->
<votecount>18</votecount>
<!-- 文件 MD5 码 (32 位 ) -->
<md5>09F6BCBEA0C8C3C7E9992A89023A58B3</md5>
</validate>
深圳证券交易所 深圳证券交易所深交所上市公司股东大会数据接口

<metadata>
{
  "title": "20221125_深圳证券交易所上市公司股东大会数据接口（Ver1",
  "source_url": null,
  "raw_path": "knowledge\\raw\\szse\\数据接口\\20221125_深圳证券交易所上市公司股东大会数据接口（Ver1.3）.pdf",
  "markdown_path": "knowledge\\articles\\szse\\markdown\\数据接口\\深圳证券交易所上市公司股东大会数据接口（Ver1.3）.md",
  "file_hash": "sha256:966a4df6140d9d9704b2b877d12dc58de41df2b008ce876a7a89c95ba9be4efa",
  "file_format": "pdf",
  "page_count": 12,
  "doc_type": "interface_spec",
  "version": "1",
  "previous_version": null,
  "public_date": null,
  "effective_date": null,
  "has_changes": false,
  "parse_status": "success",
  "parse_date": "2026-06-13T17:46:08.437956+00:00",
  "sub_category": null
}
</metadata>