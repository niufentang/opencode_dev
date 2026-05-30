上海证券交易所技术文档
上海证券交易所
IOPV 外部源机构接入
市场参与者技术实施指南
1. <span style="color:red">1</span> 版
上海证券交易所
二〇二 <span style="color:red">六</span> 年 <span style="color:red">一</span> 月

技术文档
<span style="color:red">版本历史</span>
<span style="color:red">版本号</span>
<span style="color:red">调整内容</span>
<span style="color:red">V1.0</span> <span style="color:red">20250815</span>
<span style="color:red">1、创建说明</span>
<span style="color:red">V1.1</span> <span style="color:red">20260119</span>
<span style="color:red">1、新增独立接入IOPV要求。</span>
<span style="color:red">2、相关技术文档中新增错误码表。</span>
文档摘要
本文档是上海证券交易所（以下简称 “ 本所 ” ） IOPV 外部源机构接入市场参与
者技术实施指南 。
特别申明

本指南为技术实施指南，所涉相关业务规定以本所业务规则为准。

本指南根据本所相关规则、业务方案、公告通知制定。

本所保留对本指南的解释与修改权。
联系方式
技术服务 QQ 群：
298643611
技术服务电话：
4008888400-2
电子邮件：
tech_support@sse.com.cn
技术服务微信公众号： SSE-TechService

技术文档
1
简介
本文档为上海证券交易所 <span style="color:red">（以下简称“本所”）</span> 针对 IOPV 外部源机构接入业务，为
指导市场参与者尽快完成技术准备工作，特制定本指南。
2
业务说明
实时参考净值（以下简称 IOPV ）是 ETF 申赎清单中组合证券的实时市值，能为投
资者的二级市场交易及申赎提供价格参考。为更好完善 ETF 市场机制，本所拟推动支持
外部 IOPV 数据源接入并发布。
3
接口说明
《 IS419_ 上海证券交易所互联网交易平台市场参与者接口规格说明书（ IOPV 卷）》
获得 IOPV 上传资质的指定机构可以通过 HTTP 协议的 RESTful API 接口接入互联
网交易平台并上传 IOPV 数据。
（ 1 ）通过交易行情网或 VSEP 网络与交易所进行网络对接；
（ 2 ）上交所接受当日实时参考基金净值上传时间为当日 7:30 至 16:30 ；
（ 3 ）上传频率应不快 3 秒 / 幅（含 3 秒），若上传机构未上传最新基金净值，则下一
次对外发布揭示净值时将保留上次发布揭示的净值不变。
《 IS118_ 上海证券交易所特定参与者接口规格说明书（基金公司卷）》
配合 IOPV 外部源机构接入，调整如下：
（ 1 ） ETF 定义文件接口， IOPV 发布标记字段新增字段取值 C ，代表由第三方机
构（非中证指数公司）计算 IOPV ，经互联网交易平台转发，通过交易所行情发布；调
整取值 B 含义为：由中证指数公司计算 IOPV ，通过交易所行情发布。
（ 2 ） ETF 公告文件接口，对应 ETF 定义文件，调整 Publish （ PublishIOPVFlag ）
字段描述。
第 1 页共 3 页

技术文档
4
市场参与者技术实施建议及注意事项
（ 1 ）本所互联网交易平台提供双通道供上传机构发送 IOPV 数据，上传机构应通过
双通道分别上传且保证双路数据的一致性。具体双路上传地址将另行明确，相关机构可
先进行相关技术准备。
（ 2 ）本所对于上传的行情信息会进行防重复、防回流处理，请上传机构依据市场
接口中的相关要求完成相应技术处理。
（ 3 ） ETF 定义文件中 IOPV 发布标记字段（ 2.1 版为 Publish IOPV Flag 字段 /xml 版
为 PublishIOPVFlag 字段）新增通过互联网交易平台发布 IOPV 的取值 C ，调整取值 B
为“由中证指数公司计算 IOPV ，通过交易所行情发布”。所有通过互联网交易平台上传
发送 IOPV 数据的 ETF 产品，基金管理人应在该 ETF 定义文件中 Publish IOPV Flag
（ 2.1 版）或 PublishIOPVFlag （ xml 版）字段填写为 C 。
<span style="color:red">（</span> <span style="color:red">4</span> <span style="color:red">）行情接收方面，由</span> <span style="color:red">IOPV</span> <span style="color:red">外部源机构提供的数据，本所将统一通过独立</span> <span style="color:red">IOPV</span>
<span style="color:red">行情渠道发布，不会通过原竞价撮合系统行情（行情网关</span> <span style="color:red">SecurityType=1</span> <span style="color:red">及</span> <span style="color:red">mktdt00.txt</span> <span style="color:red">）</span>
<span style="color:red">转发。因此，为保障能接收完整的</span> <span style="color:red">IOPV</span> <span style="color:red">行情数据（含未来外部源数据），各市场机构必</span>
<span style="color:red">须完成独立</span> <span style="color:red">IOPV</span> <span style="color:red">行情渠道的接入。</span>
<span style="color:red">（</span> <span style="color:red">5</span> <span style="color:red">）</span> 市场参与者应充分评估上述变更对行情、申赎、交易等相关技术系统的影响，
做好相关技术系统维护、改造工作，根据本所要求利用本所提供的测试环境进行充分测
试验证，同时保障现有上交所股票、债券、基金、融资融券、股票期权等各类业务正常
运行。
5
相关技术文档
《 IS419_ 上海证券交易所互联网交易平台市场参与者接口规格说明书（ IOPV 卷） 1.0
版 _ 技术开发稿》 <span style="color:red">。</span>
《 IS118_ 上海证券交易所特定参与者接口规格说明书（基金公司卷） 2.2 版 _20250808
（ IOPV 外部源机构接入技术开发稿）》 <span style="color:red">。</span>
<span style="color:red">《</span> <span style="color:red">IS111_</span> <span style="color:red">上海证券交易所报盘软件错误代码表</span> <span style="color:red">3.29</span> <span style="color:red">版</span> <span style="color:red">_20260109(</span> <span style="color:red">固收迁移技术开发</span>
第 2 页共 3 页

技术文档
<span style="color:red">稿</span> <span style="color:red">)</span> <span style="color:red">》。</span>
第 3 页共 3 页

> **变更标注说明**：本文档中已用 `<span style="color:...">` 标注了变更内容（红色=修改/新增，蓝色=其他说明）。


<metadata>
{
  "title": "20260129_上海证券交易所IOPV外部源机构接入市场参与者技术实施指南_V1",
  "source_url": null,
  "raw_path": "knowledge\\raw\\sse\\测试文档\\20260129_上海证券交易所IOPV外部源机构接入市场参与者技术实施指南_V1.1_20260129.pdf",
  "markdown_path": "knowledge\\articles\\sse\\markdown\\测试文档\\上海证券交易所IOPV外部源机构接入市场参与者技术实施指南_V1.1_20260129.md",
  "file_hash": "sha256:fdb1ec0dd0c8f50f2b751e8e87d2e02a470db4a9c7f295512614e729d2656657",
  "file_format": "pdf",
  "page_count": 5,
  "doc_type": "guide",
  "version": "1",
  "previous_version": null,
  "public_date": null,
  "effective_date": null,
  "has_changes": true,
  "parse_status": "success",
  "parse_date": "2026-05-02T01:48:29.677234+00:00",
  "sub_category": null
}
</metadata>