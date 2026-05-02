上海证券交易所技术文档
上海证券交易所
独立 IOPV 行情
市场参与者技术实施指南
2.0 版
上海证券交易所
二〇二六年三月

技术文档
文档摘要
本文档是上海证券交易所（以下简称 “ 本所 ” ）独立 IOPV 行情市场参与者技术
实施指南 。
特别申明
⚫ 本指南为技术实施指南，所涉相关业务规定以本所业务规则为准。
⚫ 本指南根据本所相关规则、业务方案、公告通知制定。
⚫ 本所保留对本指南的解释与修改权。
联系方式
技术服务 QQ 群：
298643611
技术服务电话：
4008888400-2
电子邮件：
tech_support@sse.com.cn
技术服务微信公众号： SSE-TechService

技术文档
一、 概述
<span style="color:red">为提升基金净值估算（</span> <span style="color:red">IOPV</span> <span style="color:red">）行情的发布效率与系统可靠性，本所推出独立的</span>
<span style="color:red">IOPV</span> <span style="color:red">行情发布通道。本项目将通过三个阶段，逐步以新增的外部源行情通道，替代现</span>
<span style="color:red">有竞价撮合系统行情中的</span> <span style="color:red">IOPV</span> <span style="color:red">数据。</span>
本文档为上海证券交易所独立 IOPV 行情市场参与者技术实施指南，对市场参与者
相关的技术实施提出建议。
二、 项目阶段总览
为提升市场效率，共做 <span style="color:red">三两</span> 阶段安排：
（一）第一阶段
本所向市场机构以试运行的形式发布外部源 IOPV 行情 <span style="color:red">（行情流</span> <span style="color:red">SecurityType=14</span> <span style="color:red">及</span>
<span style="color:red">行情文件</span> <span style="color:red">mktdte.txt</span> <span style="color:red">）</span> ，各市场机构应保持以现有渠道（ SecurityType=1 及 mktdt00.txt ）
接收 IOPV ，外部源行情渠道的 IOPV 仅供参考，不应用作正式用途。
此阶段外部源 IOPV 行情与现有渠道保持一致。
市场机构可在此阶段逐步完成技术就绪，为后续正式切换外部源行情渠道做好准
备。
（二）第二阶段
正式发布外部源 IOPV 行情，市场机构应切换外部源 IOPV 行情为生产 <span style="color:red">主用使用</span> 。
<span style="color:red">原渠道（</span> <span style="color:red">SecurityType=1</span> <span style="color:red">及</span> <span style="color:red">mktdt00.txt</span> <span style="color:red">）中</span> <span style="color:red">IOPV</span> <span style="color:red">字段将保留至第三阶段开始前，但不</span>
<span style="color:red">再建议使用。原渠道（</span> <span style="color:red">SecurityType=1</span> <span style="color:red">及</span> <span style="color:red">mktdt00.txt</span> <span style="color:red">）中</span> <span style="color:red">IOPV</span> <span style="color:red">行情将逐步减少转发直</span>
<span style="color:red">至不再通过此渠道发布，原渠道中</span> <span style="color:red">IOPV</span> <span style="color:red">相关字段会保留并填写为</span> <span style="color:red">0</span> <span style="color:red">（表示无意义），</span>
<span style="color:red">以避免系统兼容性问题。</span>
<span style="color:red">（三）第三阶段</span>
<span style="color:red">第二阶段开始</span> <span style="color:red">3</span> <span style="color:red">个月后，进入第三阶段，原渠道（</span> <span style="color:red">SecurityType=1</span> <span style="color:red">及</span> <span style="color:red">mktdt00.txt</span> <span style="color:red">）</span>
<span style="color:red">中</span> <span style="color:red">IOPV</span> <span style="color:red">字段将会标记为无意义。市场机构应确保所有系统已完全脱离对原渠道</span> <span style="color:red">IOPV</span>
<span style="color:red">数据的依赖。</span>
第 1 页 共 6 页

技术文档
三、 市场接口调整说明
《 IS120_ 上海证券交易所行情网关 BINARY 数据接口规范》
<span style="color:red">第一阶段：</span> 在市场状态消息（ MsgType=M101 ）、行情快照消息（ MsgType=M102 ）中
增加独立 IOPV 行情描述。
<span style="color:red">第二阶段：接口无变更。</span>
<span style="color:red">第三阶段：下线竞价撮合系统行情（股票、基金、指数及债券分销）中</span> <span style="color:red">IOPV</span> <span style="color:red">行情，</span>
<span style="color:red">相关字段标记为“无意义”。</span>
《 IS120_ 上海证券交易所行情网关 STEP 数据接口规范》
<span style="color:red">第一阶段：</span> 在市场状态消息（ MsgType=h ）、行情快照消息（ MsgType=W ）中增加独
立 IOPV 行情描述。
<span style="color:red">第二阶段：接口无变更。</span>
<span style="color:red">第三阶段：下线竞价撮合系统行情（股票、基金、指数及债券分销）中</span> <span style="color:red">IOPV</span> <span style="color:red">行情，</span>
<span style="color:red">相关字段标记为“无意义”。</span>
《 IS124_ 上海证券交易所市场数据文件交换接口规格说明书》
<span style="color:red">第一阶段：</span> 新增外部源行情文件 mktdte.txt 。
<span style="color:red">第二阶段：接口无变更。</span>
<span style="color:red">第三阶段：下线竞价撮合系统行情文件</span> <span style="color:red">mktdt00.txt</span> <span style="color:red">中</span> <span style="color:red">IOPV</span> <span style="color:red">行情，相关字段标记为</span>
<span style="color:red">“无意义”。</span>
四、 市场参与者技术实施建议及注意事项
为了提升证券行情发布的及时性，本所拟对行情发布架构进行优化，新增外部源行
情通道，包含行情网关 MDGW 实时流（ SecurityType=14 ）和行情文件 mktdte.txt 两部
分。
第 2 页 共 6 页

技术文档
上线初期仅包含 IOPV 行情（ MDStreamID=MDE01 ），其产品范围与竞价撮合系统
行情（ SecurityType=1 及 mktdt00.txt ）中 ETF 产品范围一致，对于不发布 IOPV 的
ETF ，行情中填写默认值 0 ，代表无意义。
详细说明如下：
（一）行情网关 MDGW 接口（ BINARY/STEP ）
<span style="color:red">第一阶段：</span>
1. 市场状态消息（ MsgType=M101/h ）中增加 SecurityType=14 消息，旨在传递行情
产品数目（ TotNoRelatedSym 字段），对应市场状态（ TradingSessionID ）填空无意义。
2. 行情快照消息（ MsgType=M102/W ）中增加 IOPV 行情
（ MDStreamID=MDE01 ），其 PreClosePx 昨收盘、 TotalVolumeTraded 成交数量、
NumTrades 成交笔数、 TotalValueTraded 成交金额字段取值为 0 ， TradingPhaseCode 实时
阶段及标志取值为空。行情条目类别为 w 时， MDEntryPx 表示基金 T-1 日收盘时刻
IOPV ，此条目仅当 MDStreamID= MD004 时有意义，当 MDStreamID= MDE01 时无意
义，该字段取 0 时无意义；行情条目类别为 v 时， MDEntryPx 表示基金 IOPV ，此条
目仅当 MDStreamID= MD004 或 MDE01 时有意义，该字段取 0 时无意义。
<span style="color:red">第二阶段：接口无调整。</span>
<span style="color:red">第三阶段：</span>
<span style="color:red">行情快照消息（</span> <span style="color:red">MsgType=M102/W</span> <span style="color:red">）</span> <span style="color:red">IOPV</span> <span style="color:red">行情（</span> <span style="color:red">MDStreamID=MDE01</span> <span style="color:red">）中，行情</span>
<span style="color:red">条目类别为</span> <span style="color:red">w</span> <span style="color:red">时，</span> <span style="color:red">MDEntryPx</span> <span style="color:red">表示基金</span> <span style="color:red">T-1</span> <span style="color:red">日收盘时刻</span> <span style="color:red">IOPV</span> <span style="color:red">，数据内容无意义此条目</span>
<span style="color:red">仅当</span> <span style="color:red">MDStreamID= MD004</span> <span style="color:red">时有意义，当</span> <span style="color:red">MDStreamID= MDE01</span> <span style="color:red">时无意义，该字段取</span>
<span style="color:red">0</span> <span style="color:red">时无意义；行情条目类别为</span> <span style="color:red">v</span> <span style="color:red">时，</span> <span style="color:red">MDEntryPx</span> <span style="color:red">表示基金</span> <span style="color:red">IOPV</span> <span style="color:red">，此条目仅当</span>
<span style="color:red">MDStreamID=</span> <span style="color:red">MD004</span> <span style="color:red">或</span> <span style="color:red">MDE01</span> <span style="color:red">时有意义，该字段取</span> <span style="color:red">0</span> <span style="color:red">时无意义。</span>
（二）文件接口（外部源行情文件 mktdte.txt ）
<span style="color:red">第一阶段：</span>
文件头、尾与 mktdt00.txt 类似。文件体目前仅有 MDStreamID= MDE01 一种，表示
IOPV 行情，包含： SecurityID 证券代码、 Symbol 证券简称、 IOPV 、 Timestamp 时间
第 3 页 共 6 页

技术文档
戳、 Reserved 预留字段。
外部源行情文件 mktdte.txt 仅会通过行情网关 MDGW 进行下发。 UT5 已 <span style="color:red">计划</span> 下
线，不会发布该文件。
<span style="color:red">mktdte.txt</span> <span style="color:red">文件名采用固定文件名规则，而非动态命名规则</span> <span style="color:red">1</span> <span style="color:red">，文件名中不包含环境</span>
<span style="color:red">号。无论在测试环境还是生产环境，其文件名均保持不变。请各市场机构根据上述规</span>
<span style="color:red">则，在切换环境时注意区分。</span>
<span style="color:red">注意：相对于竞价撮合系统行情（</span> <span style="color:red">mktdt00.txt</span> <span style="color:red">及</span> <span style="color:red">MDGW</span> <span style="color:red">实时流中</span>
<span style="color:red">MDStreamID=MD004</span> <span style="color:red">数据）中</span> <span style="color:red">IOPV</span> <span style="color:red">字段，外部源行情（</span> <span style="color:red">mktdte.txt</span> <span style="color:red">及</span> <span style="color:red">MDGW</span> <span style="color:red">实时流</span>
<span style="color:red">中</span> <span style="color:red">MDStreamID=MDE01</span> <span style="color:red">数据）中无基金</span> <span style="color:red">T-1</span> <span style="color:red">日收盘时刻</span> <span style="color:red">IOPV</span> <span style="color:red">。</span>
<span style="color:red">第二阶段：接口无调整。</span>
<span style="color:red">第三阶段：</span>
<span style="color:red">下线竞价撮合系统行情文件</span> <span style="color:red">mktdt00.txt</span> <span style="color:red">中</span> <span style="color:red">IOPV</span> <span style="color:red">行情，</span> <span style="color:red">PreCloseIOPV</span> <span style="color:red">基金</span> <span style="color:red">T-1</span> <span style="color:red">日收</span>
<span style="color:red">盘时刻</span> <span style="color:red">IOPV</span> <span style="color:red">、</span> <span style="color:red">IOPV</span> <span style="color:red">基金</span> <span style="color:red">IOPV</span> <span style="color:red">字段标记为无意义。</span>
（三）行情网关 <span style="color:red">软件</span> 升级说明
市场参与者可通过升级行情网关版本（ MDGW_1.2.10 及以上），接收新增外部源行
情数据。存量生产版本接收其他行情类数据不受影响，其中传输方式使用 Udp 高速地
面和 Udp 卫星链路的用户，日志提示： task marketDataTask unknown securityType 14 ，
为正常现象，请忽略。
<span style="color:red">（四）其他项目关联关系说明</span>
<span style="color:red">由</span> <span style="color:red">IOPV</span> <span style="color:red">外部源机构提供的</span> <span style="color:red">IOPV</span> <span style="color:red">行情数据，本所将统一通过独立</span> <span style="color:red">IOPV</span> <span style="color:red">行情渠道</span>
<span style="color:red">发布，不会通过现有渠道（</span> <span style="color:red">SecurityType=1</span> <span style="color:red">及</span> <span style="color:red">mktdt00.txt</span> <span style="color:red">）发布。因此，为保障能接收</span>
<span style="color:red">完整的</span> <span style="color:red">IOPV</span> <span style="color:red">行情数据（含未来外部源数据），各市场机构必须在</span> <span style="color:red">IOPV</span> <span style="color:red">外部源业务上</span>
<span style="color:red">线前完成独立</span> <span style="color:red">IOPV</span> <span style="color:red">行情渠道的接入。</span>
<span style="color:red">1</span> <span style="color:red">动态文件名规则：如撮合系统行情文件，文件名为</span> <span style="color:red">mktdt+ [</span> <span style="color:red">环境号</span> <span style="color:red">]+.txt</span> <span style="color:red">，其中环境号会随部署环境变化。例如：在生产环境</span>
<span style="color:red">（</span> <span style="color:red">00</span> <span style="color:red">环境）中文件名为</span> <span style="color:red">mktdt00.txt</span> <span style="color:red">，在测试环境（如</span> <span style="color:red">88</span> <span style="color:red">环境）中文件名为</span> <span style="color:red">mktdt88.txt</span> <span style="color:red">。</span>
第 4 页 共 6 页

技术文档
市场参与者应充分评估上述变更对行情、申赎、交易等相关技术系统的影响，做好相
关技术系统维护、改造工作，根据本所要求利用本所提供的测试环境进行充分测试验证，
同时保障现有上交所股票、债券、基金、融资融券、股票期权等各类业务正常运行。
第 5 页 共 6 页

技术文档
五、 相关技术文档
《 IS120_ 上海证券交易所行情网关 BINARY 数据接口规范 0.60 版 _20260327 》
《 IS120_ 上海证券交易所行情网关 STEP 数据接口规范 0.60 版 _20260327 》
《 IS124_ 上海证券交易所市场数据文件交换接口规格说明书 3.20 版 _20260327 》
第 6 页 共 6 页

> **变更标注说明**：本文档中已用 `<span style="color:...">` 标注了变更内容（红色=修改/新增，蓝色=其他说明）。


<metadata>
{
  "title": "20260327_上海证券交易所独立IOPV行情市场参与者技术实施指南V2",
  "source_url": null,
  "raw_path": "knowledge\\raw\\sse\\技术指南\\20260327_上海证券交易所独立IOPV行情市场参与者技术实施指南V2.0_20260327.pdf",
  "markdown_path": "knowledge\\articles\\sse\\markdown\\技术指南\\上海证券交易所独立IOPV行情市场参与者技术实施指南V2.0_20260327.md",
  "file_hash": "sha256:16b8faa01d9b7ca782da9c4fcb50bbc1a3bca2aa97b51237dfebb03345a17662",
  "file_format": "pdf",
  "page_count": 8,
  "doc_type": "guide",
  "version": "2",
  "previous_version": null,
  "public_date": null,
  "effective_date": null,
  "has_changes": true,
  "parse_status": "success",
  "parse_date": "2026-05-02T01:47:03.166931+00:00",
  "sub_category": null
}
</metadata>