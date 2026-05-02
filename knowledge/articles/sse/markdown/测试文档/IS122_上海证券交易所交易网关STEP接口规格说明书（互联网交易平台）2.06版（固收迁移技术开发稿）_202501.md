上海证券交易所
交易网关 STEP 接口规格说明书
（互联网交易平台 <span style="color:red">固收迁移技术开发稿</span> ）
2.0 <span style="color:red">56</span> 版
二〇二 <span style="color:red">五</span> 年 <span style="color:red">一</span> 月

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
2022-02
0.30
开发稿
（ 2 ）新订单申报中申报价格修改为非必填，对基金通报价交易，
申报价格必填；基金通转入转出，申报价格为空；
2022-02
1.00
正式稿
1. 增加询价业务类接口
2022-04
1.10
开发稿
2. 增加订阅机制
3. 转入转出不支持撤单
1. 修改消息流图：报价方撤销报价处理，删除撤单成功执行报告；
2. 修改报价、报价状态回报、转发报价 tag 453 后接重复组字段
表述， “ 询价 ” 修改为 “ 报价 ”
2022-07
1.11
开发稿
3. 修改 tag 693 QuoteRespID 字段类型为 C18
4. 删除报价状态回报（ Quote Status Report ）中 tag 693
QuoteRespID
5. 报价回复新增字段： tag131 QuoteReqID ，用于匹配成交
1. 询价申报中订单价格上下限字段，增加字段说明 “ 预留，暂不
启用 ”
2. 调整询价处理消息流图：转发询价请求、转发报价请求去掉
orderID ；报价撤销成功回报去掉 ordID=or00003 ；报价撤销成功
2022-08
1.12
正式稿
回报的报价状态调整为 QuoteStatus=Cancelled
3. 转发询价请求、转发报价请求不再提供 orderID ，字段调整为
非必填
4. 询价状态回报、报价状态回报中 OrderID 调整为非必填，补充
字段说明
2023.07
1.13
开发稿
要约 / 现金选择权（要约预受 / 现金选择权登记、要约撤销 / 现金选

日期
版本
状态
说明
择权注销）、开放式基金相关业务（申赎、分红选择、份额转出）、
融资融券非交易业务（余券划转、还券划转、担保品划入、担保
品划出、券源划入、券源划出）、网络密码服务（密码激活 / 注销），
将从竞价撮合平台迁移至互联网交易平台
1. 新订单申报时，更新开放式基金转托管转出业务与分红选择业
务的 AppID 。
2. 3.2.1 章节中删除网络密码服务业务执行报告分区，新增消息类
型，删除 4.4 章节消息类型与业务类型映射表。
3. 4.4.1 章节中，调整券源划入 / 划出业务的买卖方向，补充关于
融资融券非交易业务的含义说明；新增申报编号字段；统一非交
2023.09
1.14
开发稿
易业务价格、数量的填写要求；修订 Text 字段填写要求及发起方
营业部代码范围。
4. 4.4.3.1.1 章节中补充对于价格、数量的描述。
5. 4.4.4.1.1 章节中删除 TimeInForce ， ValidationCode 类型调整为
C8 。
若申报订单中参与方信息重复申报，则以最后一次取值为准，覆
2023.10
1.15
开发稿
盖前序重复内容。
<span style="color:red">补充了原固定收益系统迁移至互联网交易平台一债通模块相关业</span>
<span style="color:red">务申报接口内容，包括</span> <span style="color:red">:</span>
<span style="color:red">1.</span> <span style="color:red">业务类型章节添加了新增的业务类型</span>
<span style="color:red">2.</span> <span style="color:red">询价处理消息流中添加了通过公开行情发布的场景</span>
<span style="color:red">3.</span> <span style="color:red">添加了意向申报和成交申报两类消息流图</span>
<span style="color:red">2023.12</span>
<span style="color:red">2.00</span>
<span style="color:red">开发稿</span>
<span style="color:red">4.</span> <span style="color:red">4.4.1</span> <span style="color:red">章节新订单申报中添加相关字段适配新增业务</span>
<span style="color:red">5.</span> <span style="color:red">4.4.2.1</span> <span style="color:red">询价请求中删除了询价请求编号（</span> <span style="color:red">QuoteReqID</span> <span style="color:red">）字段，</span>
<span style="color:red">添加了询价请求类型（</span> <span style="color:red">QuoteRequestType</span> <span style="color:red">）字段；</span> <span style="color:red">4.4.2.7</span> <span style="color:red">章节中</span>
<span style="color:red">[删除] 删除了报价回复消息编号（</span> <span style="color:red">QuoteRespID</span> <span style="color:red">）</span>
<span style="color:red">6.</span> <span style="color:red">4.4.2</span> <span style="color:red">章节中添加相关字段适配新增业务</span>
<span style="color:red">7.</span> <span style="color:red">[新增] 新增了</span> <span style="color:red">4.4.3</span> <span style="color:red">和</span> <span style="color:red">4.4.4</span> <span style="color:red">两类申报消息</span>

日期
版本
状态
说明
<span style="color:red">8.</span> <span style="color:red">4.4.5.1</span> <span style="color:red">中添加相关字段适配新增业务</span>
<span style="color:red">1.</span> <span style="color:red">对于成交申报，支持对质押券各自设置份额类型和限售期</span>
<span style="color:red">2.</span> <span style="color:red">对于各类业务的非通用必填项添加了业务分类对照表</span>
<span style="color:red">3.</span> <span style="color:red">调整补充约定和补充条款字段标签；调整了成交申报中的相关</span>
<span style="color:red">字段：原</span> <span style="color:red">RepurchaseTerm</span> <span style="color:red">（回购期限）调整为</span> <span style="color:red">ExpirationDays</span> <span style="color:red">（期</span>
<span style="color:red">限），原</span> <span style="color:red">ExecType</span> <span style="color:red">（执行报告类型）调整为</span> <span style="color:red">TrdAckStatus</span> <span style="color:red">（成交</span>
<span style="color:red">申报响应类型），原</span> <span style="color:red">OrdStatus</span> <span style="color:red">（订单状态）调整为</span> <span style="color:red">TrdRptStatus</span>
<span style="color:red">2024.03</span>
<span style="color:red">2.01</span>
<span style="color:red">开发稿</span>
<span style="color:red">（成交申报状态），原</span>
<span style="color:red">OrdRejReason</span>
<span style="color:red">调整为</span>
<span style="color:red">TradeReportRejectReason</span> <span style="color:red">；意向申报响应原</span> <span style="color:red">OrdRejReason</span> <span style="color:red">调整为</span>
<span style="color:red">QuoteRejectReason</span>
<span style="color:red">4.</span> <span style="color:red">调整总成交金额、总到期结算金额、总回购利息字段为预留字</span>
<span style="color:red">段，原质权人名称字段调整为逆回购方账户名称</span>
<span style="color:red">5.</span> <span style="color:red">新订单申报中对于基金通业务，结算会员代码调整为非必填</span>
<span style="color:red">1.</span> <span style="color:red">4.4.4</span> <span style="color:red">成交申报中删除</span> <span style="color:red">OrigTradeDate</span> <span style="color:red">（</span> <span style="color:red">1125</span> <span style="color:red">）字段</span>
<span style="color:red">2.</span> <span style="color:red">4.4.4</span> <span style="color:red">成交申报中将</span> <span style="color:red">LastQty</span> <span style="color:red">（</span> <span style="color:red">32</span> <span style="color:red">）调整为</span> <span style="color:red">CashOrderQty</span> <span style="color:red">（</span> <span style="color:red">152</span> <span style="color:red">）</span>
<span style="color:red">3.</span> <span style="color:red">4.4.2</span> <span style="color:red">询价报价消息体中</span> <span style="color:red">SecurityID</span> <span style="color:red">（</span> <span style="color:red">48</span> <span style="color:red">）调整为</span> <span style="color:red">C12</span> <span style="color:red">，</span> <span style="color:red">ExecID</span>
<span style="color:red">（</span> <span style="color:red">17</span> <span style="color:red">）由</span> <span style="color:red">C10</span> <span style="color:red">调整为</span> <span style="color:red">C16</span> <span style="color:red">，</span> <span style="color:red">QuoteID</span> <span style="color:red">（</span> <span style="color:red">117</span> <span style="color:red">）调整为</span> <span style="color:red">C18</span>
<span style="color:red">4.</span> <span style="color:red">根据市场反馈，</span> <span style="color:red">4.4.4</span> <span style="color:red">成交申报中增加</span> <span style="color:red">TEXT</span> <span style="color:red">（</span> <span style="color:red">58</span> <span style="color:red">）</span>
<span style="color:red">2024.03</span>
<span style="color:red">2.02</span>
<span style="color:red">开发稿</span>
<span style="color:red">5.</span> <span style="color:red">转发成交申报调整为与成交申报一致</span>
<span style="color:red">6.</span> <span style="color:red">PreTradeAnonymity</span> <span style="color:red">字段删除</span> <span style="color:red">“9=</span> <span style="color:red">不指定</span> <span style="color:red">”</span> <span style="color:red">枚举值</span>
<span style="color:red">7.</span> <span style="color:red">QuoteRespType</span> <span style="color:red">字段将</span> <span style="color:red">“2=Counter</span> <span style="color:red">，重报</span> <span style="color:red">”</span> <span style="color:red">枚举值改为预留</span>
<span style="color:red">8.</span> <span style="color:red">报价及转发报价重复组中相关字段统一调整为</span> <span style="color:red">“</span> <span style="color:red">报价发起方</span> <span style="color:red">”</span> <span style="color:red">，</span>
<span style="color:red">报价回复重复组中相关字段统一调整为</span> <span style="color:red">“</span> <span style="color:red">报价回复方</span> <span style="color:red">”</span>
<span style="color:red">1.</span> <span style="color:red">添加了三方回购申报接口</span>
<span style="color:red">2.</span> <span style="color:red">添加了竞买业务的申报接口（预留，暂不启用）</span>
<span style="color:red">2024.06</span>
<span style="color:red">2.03</span>
<span style="color:red">开发稿</span>
<span style="color:red">3.</span> <span style="color:red">3.2.2.2.3</span> <span style="color:red">询价方与报价方成交（转发请求）和</span> <span style="color:red">3.2.2.3</span> <span style="color:red">报价处理</span>
<span style="color:red">消息流图中对待定报价和确定报价的限定范围申报添加了成交后</span>
<span style="color:red">更新转发订单信息的说明</span>

日期
版本
状态
说明
<span style="color:red">4.</span> <span style="color:red">3.2.1</span> <span style="color:red">业务类型中私募可交换债转股修改为允许撤单</span>
<span style="color:red">5.</span> <span style="color:red">4.2</span> <span style="color:red">中增加了中文编码的说明</span>
<span style="color:red">6.</span> <span style="color:red">4.4.2.1</span> <span style="color:red">和</span> <span style="color:red">4.4.2.4</span> <span style="color:red">中对于冰山订单数量（</span> <span style="color:red">DisplayQty</span> <span style="color:red">）字段不允</span>
<span style="color:red">许填</span> <span style="color:red">0</span> <span style="color:red">；</span> <span style="color:red">4.4.2.2</span> <span style="color:red">中询价拒绝码调整为非必填。</span>
<span style="color:red">7.</span> <span style="color:red">4.4.2.3</span> <span style="color:red">转发询价请求和</span> <span style="color:red">4.4.2.6</span> <span style="color:red">转发报价中移除冰山订单数量</span>
<span style="color:red">字段，同时对于双边报价限定范围发布的情况明确将拆分为两笔</span>
<span style="color:red">对外发送</span>
<span style="color:red">8.</span> <span style="color:red">增加了</span> <span style="color:red">4.4.2.8</span> <span style="color:red">转发报价回复消息，</span>
<span style="color:red">9.</span> <span style="color:red">4.4.3.1</span> <span style="color:red">意向申报中，</span> <span style="color:red">SecurityID</span> <span style="color:red">调整为非必填；对于协议回购</span>
<span style="color:red">意向申报调整</span> <span style="color:red">ExpirationDays</span> <span style="color:red">为必填，</span> <span style="color:red">SettlDate</span> <span style="color:red">为选填</span>
<span style="color:red">10. 4.4.1</span> <span style="color:red">和</span> <span style="color:red">4.4.5</span> <span style="color:red">中银行间托管账户由</span> <span style="color:red">C13</span> <span style="color:red">调整为</span> <span style="color:red">C11</span>
<span style="color:red">11. 4.4.4</span> <span style="color:red">成交申报中为兼容迁移前存续期合约，补回了</span>
<span style="color:red">OrigTradeDate</span> <span style="color:red">（</span> <span style="color:red">1125</span> <span style="color:red">）字段；对于协议回购批量申报，</span> <span style="color:red">N</span> <span style="color:red">笔质押</span>
<span style="color:red">券将生成</span> <span style="color:red">N</span> <span style="color:red">笔响应，并拆分为</span> <span style="color:red">N</span> <span style="color:red">笔转发成交申报给对手方逐一确</span>
<span style="color:red">认。</span>
<span style="color:red">12. 4.4.4.2</span> <span style="color:red">转发成交申报中增加</span> 到期续做 <span style="color:red">类型字段，</span> <span style="color:red">4.4.4.3</span> <span style="color:red">中增</span>
<span style="color:red">加对于协议回购批量申报逐笔响应的说明并将发起方业务单元调</span>
<span style="color:red">整为非必填</span>
<span style="color:red">13. 4.4.4.4</span> <span style="color:red">成交确认中发起方投资者账户调整为非必填，增加了期</span>
<span style="color:red">限、结算场所、结算周期和结算方式字段，增加了对于成交报告</span>
<span style="color:red">模式下被动成交方的字段填写说明</span>
<span style="color:red">14. 4.4.5.1.1</span> <span style="color:red">执行报告中增加了结算场所、结算时间和结算方式字</span>
<span style="color:red">段</span>
<span style="color:red">15. 4.4.2.2</span> <span style="color:red">询价请求响应、</span> <span style="color:red">4.4.2.5</span> <span style="color:red">报价状态回报、</span> <span style="color:red">4.4.3.3</span> <span style="color:red">意向申报</span>
<span style="color:red">响应、</span> <span style="color:red">4.4.4.3</span> <span style="color:red">成交申报响应、</span> <span style="color:red">4.4.4.4</span> <span style="color:red">成交确认和</span> <span style="color:red">4.4.5.1</span> <span style="color:red">执行报告</span>
<span style="color:red">中增加</span> <span style="color:red">ExecMethod</span> <span style="color:red">（</span> <span style="color:red">2405</span> <span style="color:red">）字段表征申报订单来源</span>
<span style="color:red">16. 4.4.7.1</span> <span style="color:red">申报拒绝（</span> <span style="color:red">Order Reject</span> <span style="color:red">）新增了意向申报和成交申报</span>
<span style="color:red">消息，并将</span> <span style="color:red">SecurityID</span> <span style="color:red">调整为非必填</span>
<span style="color:red">17.</span> <span style="color:red">移除各申报重复组中的发起方交易参与人代码</span>

日期
版本
状态
说明
<span style="color:red">1.</span> <span style="color:red">4.4.4.1</span> <span style="color:red">成交申报、</span> <span style="color:red">4.4.4.2</span> <span style="color:red">转发成交申报、</span> <span style="color:red">4.4.4.3</span> <span style="color:red">成交申报响应、</span>
<span style="color:red">4.4.4.4</span> <span style="color:red">成交确认修订了</span> <span style="color:red">EventType</span> <span style="color:red">（</span> <span style="color:red">865</span> <span style="color:red">）字段的使用方式，</span> <span style="color:red">Rest</span>
<span style="color:red">rictedMonth</span> <span style="color:red">（</span> <span style="color:red">10332</span> <span style="color:red">）格式修改为</span> <span style="color:red">N4</span> <span style="color:red">，三方回购提前终止时修改</span>
<span style="color:red">对提前终止后的到期结算金额和回购利息使用字段的表述</span>
<span style="color:red">2.</span> <span style="color:red">4.4.2.3/4.4.2.6/4.4.2.8/4.4.4.2</span> <span style="color:red">转发询价、转发报价、转发报价</span>
<span style="color:red">回复、转发成交申报请求中重复组中移除发起方业务交易单元号</span>
<span style="color:red">和发起方营业部代码字段，转发报价回复中增加</span> <span style="color:red">PartitionNo</span> <span style="color:red">（</span> <span style="color:red">10</span>
<span style="color:red">197</span> <span style="color:red">）和</span> <span style="color:red">ReportIndex</span> <span style="color:red">（</span> <span style="color:red">10179</span> <span style="color:red">）、发起方投资者账户调整为非必填；</span>
<span style="color:red">转发成交申报中增加了投资者账户；转发询价、转发报价、转发</span>
<span style="color:red">意向申报重复组中增加了对手方机构代码字段</span>
<span style="color:red">3.</span> <span style="color:red">4.4.2.5</span> <span style="color:red">报价状态回报中明确买卖数量在撤单时表示剩余数量</span>
<span style="color:red">4.</span> <span style="color:red">4.4.3.1</span> <span style="color:red">意向申报中对于现券和协议回购意向申报撤单时调整</span> <span style="color:red">S</span>
<span style="color:red">2024.11</span>
<span style="color:red">2.04</span>
<span style="color:red">开发稿</span>
<span style="color:red">ecurityID</span> <span style="color:red">（</span> <span style="color:red">48</span> <span style="color:red">）为必填，</span> <span style="color:red">4.4.3.3</span> <span style="color:red">意向申报响应中添加了</span> <span style="color:red">IOITrans</span>
<span style="color:red">Type</span> <span style="color:red">（</span> <span style="color:red">28</span> <span style="color:red">）字段</span>
<span style="color:red">5.</span> <span style="color:red">4.4.4.1</span> <span style="color:red">成交申报中对于现券和协议回购申报撤单时调整</span> <span style="color:red">Securi</span>
<span style="color:red">tyID</span> <span style="color:red">（</span> <span style="color:red">48</span> <span style="color:red">）为必填</span>
<span style="color:red">6.</span> <span style="color:red">4.4.4.3</span> <span style="color:red">成交申报响应中将发起方业务单元调整为非必填，增加</span>
<span style="color:red">了</span> <span style="color:red">ShareProperty(10331)</span> <span style="color:red">、</span> <span style="color:red">RestrictedMonth(10332)</span> <span style="color:red">和</span> <span style="color:red">ContractMulti</span>
<span style="color:red">plier(231)</span> <span style="color:red">字段</span>
<span style="color:red">7.</span> <span style="color:red">4.4.4.4</span> <span style="color:red">和</span> <span style="color:red">4.4.5.1</span> <span style="color:red">在成交回报中添加了对手方的信息，</span> <span style="color:red">4.4.4.4</span>
<span style="color:red">成交确认中增加了</span> <span style="color:red">ShareProperty(10331)</span> <span style="color:red">、</span> <span style="color:red">RestrictedMonth(10332)</span>
<span style="color:red">和</span> <span style="color:red">ContractMultiplier(231)</span> <span style="color:red">字段，</span> <span style="color:red">4.4.5.1</span> <span style="color:red">中增加了竞买申报自动发</span>
<span style="color:red">起场景的响应描述</span>
<span style="color:red">8.</span> <span style="color:red">账户名称字段由</span> <span style="color:red">C120</span> <span style="color:red">扩为</span> <span style="color:red">C180</span> <span style="color:red">，备注字段由</span> <span style="color:red">C900</span> <span style="color:red">调整为</span> <span style="color:red">C</span>
<span style="color:red">600</span> <span style="color:red">，同时增加了场务应急成交录入的场景说明</span>
<span style="color:red">1.</span> <span style="color:red">4.4.4.1</span> <span style="color:red">成交申报、</span> <span style="color:red">4.4.4.2</span> <span style="color:red">转发成交申报、</span> <span style="color:red">4.4.4.3</span> <span style="color:red">成交申报响应、</span>
<span style="color:red">2025.1</span>
<span style="color:red">2.05</span>
<span style="color:red">开发稿</span>
<span style="color:red">4.4.4.4</span> <span style="color:red">成交确认增加债券借贷业务相关字段及填报说明（预留，</span>
<span style="color:red">暂不启用），协议回购批量申报时要求质押券不可重复</span>

日期
版本
状态
说明
<span style="color:red">2.</span> <span style="color:red">3.2.2.2</span> <span style="color:red">询价报价处理消息流图、</span> <span style="color:red">3.2.2.3</span> <span style="color:red">报价处理消息流图、</span> <span style="color:red">3.</span>
<span style="color:red">2.2.4.2</span> <span style="color:red">意向申报撤销请求处理（转发请求）、</span> <span style="color:red">3.2.2.5.3.2</span> <span style="color:red">成交请求</span>
<span style="color:red">模式</span> <span style="color:red">-</span> <span style="color:red">撤单处理中根据实际协议字段统一了</span> <span style="color:red">QuoteReqID</span> <span style="color:red">、</span> <span style="color:red">QuoteRe</span>
<span style="color:red">spID</span> <span style="color:red">、</span> <span style="color:red">QuoteID</span> <span style="color:red">、</span> <span style="color:red">OrderID</span> <span style="color:red">、</span> <span style="color:red">TradeID</span> <span style="color:red">等字段的描述方式</span>
<span style="color:red">3.</span> <span style="color:red">4.4.2.5</span> <span style="color:red">报价状态回报中增加了报价回复响应中</span> <span style="color:red">QuoteID</span> <span style="color:red">填写方</span>
<span style="color:red">式的说明</span>
<span style="color:red">4.</span> <span style="color:red">4.4.5.1</span> <span style="color:red">执行报告中对于</span> <span style="color:red">OrderID</span> <span style="color:red">[删除] 删除了“仅订单申报成功</span> <span style="color:red">Exe</span>
<span style="color:red">cType=0</span> <span style="color:red">时有效”字样</span>
<span style="color:red">5.</span> <span style="color:red">4.4.4.4</span> <span style="color:red">成交确认中增加</span> <span style="color:red">TotalValueTraded</span> <span style="color:red">（</span> <span style="color:red">8504</span> <span style="color:red">）字段</span>
<span style="color:red">1.</span> <span style="color:red">3.2.1</span> <span style="color:red">业务类型中对于三方回购转入转出修改笔误，不允许撤</span>
<span style="color:red">单</span>
<span style="color:red">2.</span> <span style="color:red">4.4.4.1</span> <span style="color:red">成交申报（</span> <span style="color:red">Trade</span> <span style="color:red">Capture</span> <span style="color:red">Report,</span> <span style="color:red">MsgType=AE)</span> <span style="color:red">中</span> <span style="color:red">Ori</span>
<span style="color:red">gTradeDate</span> <span style="color:red">字段格式调整为</span> <span style="color:red">date</span>
<span style="color:red">3.</span> <span style="color:red">4.4.2.1</span> <span style="color:red">询价请求（</span> <span style="color:red">Quote</span> <span style="color:red">Request,</span> <span style="color:red">MsgType=R</span> <span style="color:red">）、</span> <span style="color:red">4.4.2.4</span> <span style="color:red">报价</span>
<span style="color:red">（</span> <span style="color:red">Quote,</span> <span style="color:red">MsgType=S</span> <span style="color:red">）、</span> <span style="color:red">4.4.3.1</span> <span style="color:red">意向申报（</span> <span style="color:red">IOI,</span> <span style="color:red">Indication</span> <span style="color:red">of</span> <span style="color:red">Int</span>
<span style="color:red">erest,</span> <span style="color:red">MsgType=6)</span> <span style="color:red">及转发请求中对于</span> <span style="color:red">CounterpartyParticipantCode</span>
<span style="color:red">2025.2</span>
<span style="color:red">2.06</span>
<span style="color:red">开发稿</span>
<span style="color:red">字段和机构代码字段允许输入特殊符号‘</span> <span style="color:red">-</span> <span style="color:red">’</span>
<span style="color:red">4.</span> <span style="color:red">4.4.4</span> <span style="color:red">成交申报类中不再要求填写账户名称字段，对于成交报告</span>
<span style="color:red">申报模式的被动成交方，订单所有者类型（</span> <span style="color:red">OwnerType</span> <span style="color:red">）填‘</span> <span style="color:red">103</span> <span style="color:red">’</span>
<span style="color:red">5.</span> <span style="color:red">4.4.5.1</span> <span style="color:red">执行报告（</span> <span style="color:red">Execution</span> <span style="color:red">Report,</span> <span style="color:red">MsgType</span> <span style="color:red">=</span> <span style="color:red">8</span> <span style="color:red">）中对于竞</span>
<span style="color:red">买预约自动发起时申报来源（</span> <span style="color:red">ExecMethod</span> <span style="color:red">）字段与预约时相同，</span>
<span style="color:red">对手方选择‘匿名’且为‘净额结算’时相关字段调整为填写‘</span> <span style="color:red">a</span>
<span style="color:red">nonymous</span> <span style="color:red">’（转发报价、转发询价请求、转发报价回复时作类似</span>
<span style="color:red">处理）。</span>

目
录
1 前言 .................................................................................................................................................1
1.1 目的 ......................................................................................................................................1
1.2 术语和定义 ......................................................................................................................... 1
1.3 参考文档 ............................................................................................................................. 1
1.4 联系方式 ............................................................................................................................. 1
2 系统简介 .........................................................................................................................................2
2.1 系统接入 ............................................................................................................................. 2
2.2 业务范围 ............................................................................................................................. 2
3 交互机制 .........................................................................................................................................4
3.1 会话机制 ............................................................................................................................. 4
3.1.1 建立会话 .................................................................................................................. 4
3.1.2 关闭会话 .................................................................................................................. 4
3.1.3 维持会话 .................................................................................................................. 4
3.1.4 其他约定 .................................................................................................................. 5
3.2 申报与回报 ......................................................................................................................... 6
3.2.1 业务类型 .................................................................................................................. 6
3.2.2 消息流图 .................................................................................................................. 8
3.2.3 平台状态 ................................................................................................................ 26
3.2.4 重复订单 ................................................................................................................ 27
3.2.5 执行报告 ................................................................................................................ 28
3.3 恢复场景 ........................................................................................................................... 29
3.4 订阅机制 ........................................................................................................................... 30
4 消息定义 .......................................................................................................................................31
4.1 消息结构与约定 ............................................................................................................... 31
4.2 数据类型 ........................................................................................................................... 31
4.2.1 STEP 格式约定 .......................................................................................................31
4.2.2 STEP 消息头 ...........................................................................................................32
4.2.3 STEP 消息尾 ...........................................................................................................32
4.2.4 STEP 消息完整性 ...................................................................................................33
4.3 会话消息 ........................................................................................................................... 34
4.3.1 登录消息（ MsgType=A ） ....................................................................................34
4.3.2 注销消息（ MsgType=5 ） .....................................................................................35
4.3.3 心跳消息（ MsgType=0 ） .....................................................................................35
4.3.4 测试请求消息（ MsgType=1 ） .............................................................................35
4.3.5 重发请求消息（ MsgType=2 ） .............................................................................36
4.3.6 会话拒绝消息（ MsgType=3 ） .............................................................................36
4.3.7 序号重设消息（ MsgType=4 ） .............................................................................36
4.4 应用消息 ........................................................................................................................... 38
4.4.1 订单业务类 ............................................................................................................ 38
4.4.2 询价报价业务类 .................................................................................................... 47
4.4.3 意向申报类 ............................................................................................................ 69
4.4.4 成交申报类 ............................................................................................................ 73

4.4.5 执行报告类 ............................................................................................................ 95
4.4.6 网络密码服务（ Password Service, MsgType = U006 ） ...................................102
4.4.7 其它消息 .............................................................................................................. 104
附录 .................................................................................................................................................108
附录一计算校验和 .............................................................................................................. 108
附录二 PBU 及说明 ............................................................................................................. 109
附录三错误代码说明 .......................................................................................................... 110
附录四“用户私有信息”说明 .......................................................................................... 111

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
1 前言
1.1 目的
本接口规范描述了上海证券交易所（以下称本所）交易网关与市场参与者系统之间以 STEP 协议进行
交易数据交换时所采用的交互机制、消息格式、消息定义和数据内容。目前，本接口规范仅适用于本所互
联网交易平台提供的各类业务。
文档采用的术语及消息内容与 STEP 数据接口规范具有对应关系，可互为参考。
1.2 术语和定义
名词
含义
TDGW
交易网关 TraDing GateWay
<span style="color:red">MDGW</span>
<span style="color:red">行情网关</span> <span style="color:red">Market Data GateWay</span>
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
1.4 联系方式
技术服务 QQ 群：
298643611
技术服务电话：
4008888400-2 (8:00-20:00)
电子邮件：
tech_support@sse.com.cn
技术服务微信公众号： SSE-TechService （回复 00 进入人工服务）
1

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
2 系统简介
2.1 系统接入
为满足业务发展需求和提升交易服务水平，本所通过交易网关（ TDGW ）对接互联网交易平台系统，
提供实时交易流接口。 TDGW 对接交易系统及市场参与者系统（ OMS ）的示意图如下：
TDGW 通过交易业务单元（ PBU ）登录并接入交易系统， PBU 的配置由用户提前在 TDGW 端完成。
TDGW 每个平台开放一个端口供 OMS 建立会话， TDGW 仅接受 OMS 为每个平台建立一个 TCP/IP
连接，每个连接仅允许建立一个有效的会话。该会话既用于接收 OMS 的业务申报，又向 OMS 推送交易所
接收申报后产生的回报数据。
OMS 与 TDGW 间的连接为标准 TCP/IP 连接，由 OMS 负责发起。 OMS 与 TDGW 之间传输的数据是
非加密的，数据传输的安全性由部署的网络予以保证。
附录二对术语 PBU 在不同场景下的使用进行了说明。
2.2 业务范围
目前支持互联网交易平台相关业务：
业务
业务申报时间
基金通报价交易
基金通转入转出
9:30-11:30
基金通询价交易
13:00-15:00
开放式基金业务（申购、赎回、转托管转出、分红选择）
2

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
要约预受 / 现金选择权登记
要约撤销 / 现金选择权撤销
融资融券业务（余券划转、还券划转、担保品划转、券源划转）
网络密码服务
<span style="color:red">债券质押式协议回购</span>
<span style="color:red">债券质押式三方回购</span>
<span style="color:red">债券借贷（预留，暂不启用）</span>
<span style="color:red">协议回购意向申报</span>
<span style="color:red">三方回购意向申报</span>
<span style="color:red">债券现券意向申报</span>
<span style="color:red">确定报价</span>
<span style="color:red">待定报价</span>
<span style="color:red">一债通询价</span>
<span style="color:red">9:00-11:30</span>
<span style="color:red">现券协商成交</span>
<span style="color:red">13:00-15:30</span>
<span style="color:red">合并申报</span>
<span style="color:red">场务应急成交录入</span>
<span style="color:red">竞买（预留，暂不启用）</span>
<span style="color:red">三方回购转入转出</span>
<span style="color:red">双非可转债转股冻结</span>
<span style="color:red">私募可交换债换股</span>
<span style="color:red">债券回售（一债通）</span>
<span style="color:red">债券回售撤销</span>
<span style="color:red">债券转托管</span>
3

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
3.1.3 维持会话
在消息交换的空闲期间，连接双方通过 Heartbeat 心跳消息维持会话，即连接的任何一方在心跳时间间
4

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
5

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2 申报与回报
OMS 进行的新订单申报（ New Order Single ）、询价请求（ Quote Request ）、报价（ Quote ） <span style="color:red">、意向申</span>
<span style="color:red">报（</span> <span style="color:red">IOI</span> <span style="color:red">）和成交申报（</span> <span style="color:red">Trade Capture Report</span> <span style="color:red">）</span> 时，本所交易系统会进行前置检查，若检查未通过将返回订
单拒绝（ Order Reject ）、询价请求响应（ Quote Request Ask ）和报价状态回报（ QuoteStatusReport ） <span style="color:red">、意</span>
<span style="color:red">向申报响应（</span> <span style="color:red">IOI Response</span> <span style="color:red">）和成交申报响应（</span> <span style="color:red">Trade Capture Report Response</span> <span style="color:red">）</span> 消息。
对于通过前置校验的申报，交易系统根据业务的不同，向 OMS 返回相应的执行报告（ Execution Report ）、
转发询价请求（ Allege Quote Request ） <span style="color:red">、</span> 转发报价（ Allege Quote ） <span style="color:red">、转发意向申报（</span> <span style="color:red">Allege IOI</span> <span style="color:red">）和转发</span>
<span style="color:red">成交申报（</span> <span style="color:red">Allege Trade Capture Report</span> <span style="color:red">）</span> 消息。执行报告包括对申报的确认，如对新订单的确认或拒绝响
应 1 、撤单响应等； <span style="color:red">新订单申报及询价请求</span> 产生成交时，执行报告中会包含成交确认。
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
6

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
<span style="color:red">AJ</span> <span style="color:red">（报价回复）</span>
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
网络密码服务 <span style="color:red">2</span>
U006
600120
N
Y
N
<span style="color:red">债券质押式协议回购</span>
<span style="color:red">AE</span>
<span style="color:red">600130</span>
<span style="color:red">Y</span> <span style="color:red">3</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">债券质押式三方回购</span>
<span style="color:red">AE</span>
<span style="color:red">600140</span>
<span style="color:red">Y</span> <span style="color:red">3</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">协议回购意向申报</span>
<span style="color:red">6</span>
<span style="color:red">600150</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">三方回购意向申报</span>
<span style="color:red">6</span>
<span style="color:red">600160</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">债券现券意向申报</span>
<span style="color:red">6</span>
<span style="color:red">600170</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">S</span> <span style="color:red">（报价）</span>
<span style="color:red">确定报价</span>
<span style="color:red">600180</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">AJ</span> <span style="color:red">（报价回复）</span>
<span style="color:red">R</span> <span style="color:red">（询价）</span>
<span style="color:red">一债通询价</span>
<span style="color:red">S</span> <span style="color:red">（报价）</span>
<span style="color:red">600190</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">AJ</span> <span style="color:red">（报价回复）</span>
<span style="color:red">R</span> <span style="color:red">（待定报价发起）</span>
<span style="color:red">待定报价</span>
<span style="color:red">600200</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">S</span> <span style="color:red">（报价）</span>
7

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
业务
消息类型 (MsgType)
业务类型 (ApplID)
支持撤单
申报确认
成交确认
<span style="color:red">AJ</span> <span style="color:red">（报价回复）</span>
<span style="color:red">现券协商成交</span>
<span style="color:red">AE</span>
<span style="color:red">600210</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">合并申报</span>
<span style="color:red">AE</span>
<span style="color:red">600220</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">双非可转债转股冻结</span>
<span style="color:red">D</span>
<span style="color:red">600230</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">私募可交换债换股</span>
<span style="color:red">D</span>
<span style="color:red">600240</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">债券回售（一债通）</span>
<span style="color:red">D</span>
<span style="color:red">600250</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">债券回售撤销</span>
<span style="color:red">D</span>
<span style="color:red">600251</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">债券转托管</span>
<span style="color:red">D</span>
<span style="color:red">600260</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">N</span>
<span style="color:red">三方回购转入转出</span>
<span style="color:red">D</span>
<span style="color:red">600270</span>
<span style="color:red">NY</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">竞买（预留，暂不启用）</span>
<span style="color:red">D</span>
<span style="color:red">600290</span>
<span style="color:red">Y</span> <span style="color:red">4</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">债券借贷（预留，暂不启用）</span> <span style="color:red">AE</span>
<span style="color:red">600300</span>
<span style="color:red">Y</span> <span style="color:red">3</span>
<span style="color:red">Y</span>
<span style="color:red">Y</span>
<span style="color:red">场务应急成交录入</span>
<span style="color:red">AE</span>
<span style="color:red">600310</span>
<span style="color:red">N</span>
<span style="color:red">N</span>
<span style="color:red">Y</span>
注：
1 、 Y 为是， N 为否。
<span style="color:red">2</span> <span style="color:red">、</span> 网络密码服务业务，申报响应消息不进执行报告（ Execution Report ）。
<span style="color:red">3</span> <span style="color:red">、协议回购、三方回购部分成交申报不支持撤单，包括：协议回购到期确认、债券借贷到期结算（债</span>
<span style="color:red">券结算且场内结算）、三方回购到期购回三方回购补券申报。</span>
<span style="color:red">4</span> <span style="color:red">、在应价方提交有效的应价申报前，可以撤销竞买发起申报；采用单一主体中标方式的，应价申报</span>
<span style="color:red">不可撤销；采用多主体中标方式的，应价申报可以在应价申报时间截止前撤销。</span>
3.2.2 消息流图
3.2.2.1 新订单处理消息流图
3.2.2.1.1 新订单申报
适用于互联网交易平台。
订单（ OrdType=2 ）消息流如下：
8

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
暂不支持市价订单。
3.2.2.1.2 新订单撤单
支持撤单的业务类型见前述章节业务类型表。
9

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.2 询价 <span style="color:red">报价</span> 处理消息流图
询价 <span style="color:red">报价</span> 交易 <span style="color:red">总体上</span> 可以分为两个阶段：询价阶段和报价阶段。
在询价阶段，询价方申报询价请求，交易系统转发询价请求给报价方（一个或多个），报价方可以选
择进行报价也可以不进行报价。若报价方不进行报价，询价在超时后会自动失效，整个交易过程结束。
在报价阶段，报价方对询价请求进行报价，交易系统将报价转发给询价方。若报价方想要修改报价，
需将原报价撤销后重新发起报价。询价方可以选择接受或不接受报价方的报价。若询价方接受报价，则申
报一笔报价回复，交易系统对报价及报价回复进行撮合成交并发送成交回报执行报告，同时转发询价撤销
消息告知其余报价方。若询价方不接受报价，报价在询价失效后也自动失效。
询价未成交前，询价方可以撤销询价。报价未成交前，报价方可以撤销报价。 <span style="color:red">对于基金通询价，</span> 若询
价交易超过总时长仍未成交，则需通过询价请求响应及报价状态回报将失效消息转发至相关方。
<span style="color:red">此消息流适用于：基金通询价、一债通询价和待定报价。</span>
<span style="color:red">对于基金通或一债通询价，用户仅可在限定范围内发布询价信息；对于待定报价，用户可针对全市场</span>
<span style="color:red">或在限定范围内发起报价。对于发送给全市场的消息，将通过公开行情对外发布；对于限定范围内发布的</span>
<span style="color:red">询报价消息，则将该消息转发给对应对手方。</span>
10

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.2.1 询价方撤销询价请求处理 <span style="color:red">（转发请求）</span>
11

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.2.2 <span style="color:red">询价</span> 报价方撤销报价处理 <span style="color:red">（转发请求）</span>
12

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">3.2.2.2.3</span> 询价方与报价方成交 <span style="color:red">（转发请求）</span>
<span style="color:red">询价发起方报价回复确认成交后，模式一将通知其他报价方此询价被撤销，模式二将通知其他报价方</span>
<span style="color:red">更新报价数量。基金通询价和待定报价全部成交适用于模式一，待定报价部分成交适用于模式二。</span>
13

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
14

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">3.2.2.2.4</span> <span style="color:red">询价方拒绝报价方报价（转发请求）</span>
<span style="color:red">3.2.2.2.5</span> <span style="color:red">询价报价请求处理（公开行情）</span>
<span style="color:red">对于公开行情中询价发起方拒绝报价的场景，可参见询价方拒绝报价方报价（转发请求）章节。</span>
15

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
16

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">3.2.2.3</span> <span style="color:red">报价处理消息流图</span>
<span style="color:red">报价可对全市场或在限定范围内发起。面向全市场的报价，交易系统将以逐笔委托行情向市场发布报</span>
<span style="color:red">价信息，而对于限定范围的报价，交易系统将把报价消息转发给指定对手方。</span>
<span style="color:red">此消息流适用于确定报价。</span>
17

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">3.2.2.4</span> <span style="color:red">意向申报消息流图</span>
<span style="color:red">意向申报可对全市场或在限定范围内发起。面向全市场的意向申报，交易系统将以逐笔委托行情向市</span>
<span style="color:red">场发布意向申报信息，而对于限定范围的意向申报，交易系统将把意向申报请求转发给指定对手方。</span>
<span style="color:red">此消息流支持协议回购意向申报、三方回购意向申报和债券现券意向申报。其中协议回购意向申报和</span>
<span style="color:red">三方回购意向申报仅支持对全市场发起。</span>
<span style="color:red">3.2.2.4.1</span> <span style="color:red">意向申报撤销请求处理（公开行情）</span>
18

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">3.2.2.4.2</span> <span style="color:red">意向申报撤销请求处理（转发请求）</span>
<span style="color:red">特别地，对于债券现券意向申报，也支持在限定范围内发布意向报价，此时系统将把意向申报转发给</span>
<span style="color:red">指定的对手方。</span>
19

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">3.2.2.5</span> <span style="color:red">成交申报消息流图</span>
<span style="color:red">3.2.2.5.1</span> <span style="color:red">协议配对申报模式</span>
<span style="color:red">协议配对申报模式指交易双方各向互联网交易平台申报一笔订单，订单内容包括对手方信息、买卖方</span>
<span style="color:red">向和约定号等，当双方信息匹配后成交，订单未匹配前可以撤销。</span>
<span style="color:red">此模式适用于现券协商成交。</span>
20

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">3.2.2.5.2</span> <span style="color:red">成交报告申报模式</span>
<span style="color:red">成交报告申报模式指无需对手方手动确认、自动成交、不可撤单的各类申报。</span>
<span style="color:red">此模式适用于协议回购到期确认、三方回购到期购回和补券申报、债券借贷到期结算（债券结算且场</span>
<span style="color:red">内结算）、场务应急成交录入（由场务人员录入，实际交易双方均可收到成交确认）等。</span>
21

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">3.2.2.5.3</span> <span style="color:red">成交请求申报模式</span>
<span style="color:red">成交请求申报模式指一方发起经由交易服务转发至单个对手方，并由对手方手动确认（或拒绝）的各</span>
<span style="color:red">类申报。</span>
<span style="color:red">此模式适用于协议回购和三方回购的协商成交、提前终止、换券、</span> 到期续做 <span style="color:red">和解除质押申报，以及债</span>
<span style="color:red">券借贷的协商成交、到期结算、提前终止、质押券变更、到期续做、逾期结算和解除质押申报。</span>
<span style="color:red">3.2.2.5.3.1</span> <span style="color:red">申报处理</span>
22

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">3.2.2.5.3.2</span> <span style="color:red">撤单处理</span>
23

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">3.2.2.5.4</span> <span style="color:red">双边确认申报模式</span>
<span style="color:red">双边确认申报模式指中间方发起一笔包含买卖双方的订单，经交易系统转发给买卖双方分别确认后方</span>
<span style="color:red">可成交，任何一方拒绝该订单后此申报自动撤销。此模式适用于合并申报。</span>
<span style="color:red">3.2.2.5.4.1</span> <span style="color:red">两对手方均确认，成交达成</span>
24

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">3.2.2.5.4.2</span> <span style="color:red">某一对手方拒绝，自动撤销</span>
<span style="color:red">如两个对手方中任何一方拒绝该订单后此申报自动撤销。</span>
25

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
3.2.2.6 网络密码服务处理消息流图
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
26

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
<span style="color:red">IOI</span>
<span style="color:red">IOIID</span>
<span style="color:red">Trade Capture Report</span>
<span style="color:red">TradeReportID</span>
对于重复订单， TDGW 返回拒绝消息（ Order Reject ）。
27

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
28

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
息重新获取当日历史执行报告数据。
OMS 应对 TDGW 推送的执行报告进行数据持久化操作，且 OMS 应具备识别重复执行报告的能力，
避免重复处理。
3.3 恢复场景
OMS 与 TDGW 断开
在 OMS 重新与 TDGW 建立会话后，由于断连期间可能存在传输中的消息丢失， OMS 应对上下行两
个方向的消息进行恢复。建议 OMS 先对执行报告进行恢复，以尽可能更新断连前申报订单的状态。 OMS
可在恢复一段时间后，对仍然处于 “ 已报但未确认 ” 状态的订单进行重新申报。
TDGW 与 ITCS 断开
TDGW 与 ITCS 间连接断开时， TDGW 将通过 Logout （ SessionStatus=5006 ）消息注销与 OMS 间的会
话，并尝试切换备用 ITCS 。在 TDGW 未登录至交易系统期间， OMS 发起到 TDGW 的会话将无法成功。
TDGW 恢复登录，且 OMS 重建与 TDGW 间的会话后， OMS 对消息的恢复处理可与上一节描述相同。
29

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
30

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4 消息定义
4.1 消息结构与约定
每一条 STEP 消息由消息头、消息体和消息尾组成，消息最大长度为 4K 字节。
4.2 数据类型
数据类型相关说明如下：
1. 字符串类型用 CX 表示， X 表示字符串最大字节数，除特别声明，字符串只包含数字、大写字母、
小写字母以及空格；字符串实际长度小于字段类型最大长度时可以不补空格；字符串统一采用 <span style="color:red">UTF-8</span> <span style="color:red">编码，</span>
<span style="color:red">不可输入系统保留字符，包括</span> <span style="color:red">‘\r’</span> <span style="color:red">，</span> <span style="color:red">‘\t’</span> <span style="color:red">，</span> <span style="color:red">‘\’’</span> <span style="color:red">和</span> <span style="color:red">‘&’</span> <span style="color:red">。</span> <span style="color:red">ASCII</span> <span style="color:red">编码。</span>
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
价格 <span style="color:red">，对于债券单位为元；对于回购或借贷，表示利率，单位为</span> <span style="color:red">%</span> <span style="color:red">。</span>
quantity
N15(3)
数量 <span style="color:red">。对于债券，单位为千元面额；对于基金或公募</span> <span style="color:red">REITs</span> <span style="color:red">，单位为份；对于</span>
<span style="color:red">信用保护凭证，单位为</span> <span style="color:red">10</span> <span style="color:red">张。</span>
amount
N18(5)
金额 <span style="color:red">，单位为元</span>
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
4.2.1 STEP 格式约定
STEP 结构均采用依次排列 “ 标签 = 字段取值 <SOH>” 的方式组织，标签为数字字符，前后无空格 <span style="color:red">。</span> 除非
31

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
特别声明外，字段取值均为可打印 ASCII 码字符串表示，不得采用全角字母字符 <span style="color:red">；对于支持中文的字段，</span>
<span style="color:red">采用</span> <span style="color:red">UTF-8</span> <span style="color:red">编码。</span> <SOH> 为字段界定符，值为不可打印 ASCII 码字符：十六进制的 0x01 。
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
字符编码类型 <span style="color:red">，取值如下：</span>
C16
<span style="color:red">UTF-8</span>
4.2.3 STEP 消息尾
每一个会话或应用消息都有一个消息尾，并以此终止。消息尾可分隔多个消息，包含有 3 位数的校验
和值。
消息尾格式如下：
32

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
33

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
34

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
35

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
36

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
37

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.4 应用消息
4.4.1 订单业务类
4.4.1.1 新订单申报 <span style="color:red">（</span> <span style="color:red">New Order Single, MsgType = D</span> <span style="color:red">）</span>
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
1 <span style="color:red">=</span> 买（转入）
2 <span style="color:red">=</span> 卖（转出）
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
<span style="color:red">110</span>
<span style="color:red">MinQty</span>
<span style="color:red">最低成交数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
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
<span style="color:red">1091</span>
<span style="color:red">PreTradeAnonymity</span>
<span style="color:red">是否匿名报价，取值：匿名</span> <span style="color:red">=1</span> <span style="color:red">，显名</span> <span style="color:red">=0</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">63</span>
<span style="color:red">SettlType</span>
<span style="color:red">结算方式：</span> <span style="color:red">1=</span> <span style="color:red">净额结算，</span> <span style="color:red">2=RTGS</span> <span style="color:red">结算</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">担保券可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">2</span> <span style="color:red">；非担保券只能为</span> <span style="color:red">2</span> <span style="color:red">。特别地，</span>
38

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">对于公募可转债或公募</span> <span style="color:red">REITs</span> <span style="color:red">，只能填</span> <span style="color:red">1</span> <span style="color:red">。</span>
<span style="color:red">198</span>
<span style="color:red">SecondaryOrderID</span>
<span style="color:red">第二交易所订单编号</span>
<span style="color:red">N</span>
<span style="color:red">C16</span>
<span style="color:red">10238</span>
<span style="color:red">BidTransType</span>
<span style="color:red">竞买业务类型</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">1 =</span> <span style="color:red">竞买预约</span>
<span style="color:red">2 =</span> <span style="color:red">竞买申报</span>
<span style="color:red">3 =</span> <span style="color:red">应价申报</span>
<span style="color:red">10239</span>
<span style="color:red">BidExecInstType</span>
<span style="color:red">竞买成交方式</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">1 =</span> <span style="color:red">单一主体中标</span>
<span style="color:red">2 =</span> <span style="color:red">多主体单一价格中标</span>
<span style="color:red">3 =</span> <span style="color:red">多主体多重价格中标</span>
<span style="color:red">432</span>
<span style="color:red">ExpireDate</span>
<span style="color:red">失效日期</span>
<span style="color:red">N</span>
<span style="color:red">date</span>
<span style="color:red">529</span>
<span style="color:red">OrderRestrictions</span>
<span style="color:red">订单限制，表示是否竞买日自动发起竞买申报</span>
<span style="color:red">N</span>
<span style="color:red">Boolean</span>
<span style="color:red">Y =</span> <span style="color:red">是</span>
<span style="color:red">N =</span> <span style="color:red">否</span>
58
Text
用户私有信息
N
C32
453
NoPartyIDs
参与方个数，取值 =1 <span style="color:red">4</span> ，后接重复组，依次包含发
Y
N2
起方的投资者账户、业务交易单元号、 <span style="color:red">三方回购</span>
<span style="color:red">专用账户、三方回购专户对应交易单元号、交易</span>
<span style="color:red">员一债通账户、银行间托管账号、</span> 营业部代码、
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
<span style="color:red">发起方三方回</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">填写三方回购专用账户。</span>
<span style="color:red">N</span>
<span style="color:red">C13</span>
39

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">购专用账户</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">107</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方三方回</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">购专用账户</span>
<span style="color:red">发起方三方回</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方三方回购专用账户对应交易单元号</span>
<span style="color:red">N</span>
<span style="color:red">C8</span>
<span style="color:red">购专户对应交</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">106</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方三方回</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">易单元号</span>
<span style="color:red">购专用账户对应交易单元号</span>
<span style="color:red">发起方交易员</span>
448
PartyID
<span style="color:red">交易员一债通账户</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">一债通账户</span>
452
PartyRole
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">员一债通账户</span>
<span style="color:red">银行间托管帐</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">银行间托管账号。债券转托管时适用。</span>
<span style="color:red">N</span>
<span style="color:red">C11</span>
<span style="color:red">号</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">28</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为银行间托管账号</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
发起方营业部
448
PartyID
发起方营业部代码
Y
C8
代码
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为发起方的营业
Y
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
40

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
适用于互联网交易平台业务
各业务填写字段说明如下：
ApplID
业务类型
相关字段填写说明
1.Price 字段必填
2.OrderQty 申报数量单位为份；
600020
基金通报价交易
3. 投资者中国结算开放式基金账户、投资者中国结算交易账户、销
售人代码、券商网点号码为必填
4. OrdType 必填
1. 投资者中国结算开放式基金账户、投资者中国结算交易账户、销
售人代码、券商网点号码为必填
600021
基金通转入转出
2.OrderQty 申报数量单位为份
3. OrdType 必填
1. Price 固定填 1 。
2.Side 固定填 1 。
600030
开放式基金申购
3.OrderQty 表示申购金额，单位为元，填写非 0 正整数，累加申购
金额为 100 元或其整数倍。
4. SecurityID 填写正股代码（ 519XXX ）。
1. Price 固定填 1 。
2.Side 固定填 2 。
600040
开放式基金赎回
3. OrderQty 表示赎回份额，单位为份，填写非 0 正整数，不支持小
数。
4. SecurityID 填写正股代码（ 519XXX ）。
1.Price 固定填 1 。
600050
开放式基金转托管转出
2. OrderQty 表示基金份额，单位为份，填写非 0 正整数，不支持小
41

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
ApplID
业务类型
相关字段填写说明
数。
3.Side 固定填 2 。
4. SecurityID 填写正股代码（ 519XXX ）。
5. 开放式基金转托管的目标方字段必填。
1.Price 固定填 1 。
2.Side 固定填 1 。
600060
开放式基金分红选择
3.OrderQty 固定填 1 。
4. SecurityID 填写正股代码（ 519XXX ）。
5. DividendSelect 必填， U= 红利转投， C= 现金分红。
1.Price 表示收购价，单位为元，填写非 0 正数。
2.Side 固定填 2 。
要约预受 / 现金选择权登
600070
3. OrderQty 表示收购数量，填写非 0 正整数。
记
4. SecurityID 填写标的证券正股代码。
5. 申报编号字段必填，填写 6 位数字。
1.Price 表示收购价，单位为元，填写非 0 正数。
2.Side 固定填 1 。
要约撤销 / 现金选择权注
600071
3. OrderQty 表示收购数量，填写非 0 正整数。
销
4. SecurityID 填写标的证券正股代码。
5. 申报编号字段必填，填写 6 位数字。
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
3. Side 固定填 1 。买入转义为标的证券从 “ 证券公司融券专用账户 ”
600080
融资融券余券划转
过户到 “ 证券公司信用交易担保证券账户 ” 。仅允许投资者信用账户
（ E 字头）申报。
4.OrderQty 表示划转数量 , 填写非 0 正整数，允许零散股。
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
600090
融资融券还券划转
3.Side 固定填 2 。卖出转义为标的证券从 “ 证券公司信用交易担保证
券账户 ” 过户到 “ 证券公司融券专用账户 ” 。仅允许投资者信用账户（ E
42

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
ApplID
业务类型
相关字段填写说明
字头）申报。
4. OrderQty 表示划转数量 , 填写非 0 正整数，允许零散股。
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
3.Side 固定填 1 。买入转义为标的证券从 “ 投资者普通证券账户 ” 过户
600100
融资融券担保品划入
到 “ 证券公司信用交易担保证券账户 ” 。仅允许投资者信用账户（ E
字头）申报。
4. OrderQty 划转数量 , 填写非 0 正整数，允许零散股。
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
3.Side 固定填 2 。卖出转义为标的证券从 “ 证券公司信用交易担保证
600101
融资融券担保品划出
券账户 ” 过户到 “ 投资者普通证券账户 ” 。仅允许投资者信用账户（ E
字头）申报。
4. OrderQty 划转数量 , 填写非 0 正整数，允许零散股。
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
600110
融资融券券源划入
3.Side 固定填 2 ，卖出转义为标的证券从 “ 证券公司自营账户 ” 过户到
“ 证券公司融券专用账户 ” 。仅允许证券公司自营账户申报。
4. OrderQty 划转数量 , 填写非 0 正整数，允许零散股。
1. SecurityID 表示转入的标的产品代码。
2. Price 固定填 1 。
600111
融资融券券源划出
3. Side 固定填 1 。买入转义为标的证券从 “ 证券公司融券专用账户 ”
过户到 “ 证券公司融券自营账户 ” 。仅允许证券公司自营账户申报。
4. OrderQty 划转数量 , 填写非 0 正整数，允许零散股。
<span style="color:red">600230</span>
<span style="color:red">双非可转债转股冻结</span>
1. <span style="color:red">参与方中需要填写交易员一债通账户；对转托管申报，银行间托</span>
<span style="color:red">600240</span>
<span style="color:red">私募可交换债换股</span>
<span style="color:red">管账号必填；三方回购转入转出时，专用账户及其对应的交易单元</span>
<span style="color:red">必填。</span>
<span style="color:red">600250</span>
<span style="color:red">债券回售（一债通）</span>
2. <span style="color:red">Side</span> <span style="color:red">：对于转托管、回售、转股冻结和换股，填</span> <span style="color:red">2</span> <span style="color:red">；对回售撤销</span>
<span style="color:red">600251</span>
<span style="color:red">债券回售撤销</span>
<span style="color:red">申报填</span> <span style="color:red">1</span> <span style="color:red">。对三方回购转入填</span> <span style="color:red">1</span> <span style="color:red">，转出填</span> <span style="color:red">2</span> <span style="color:red">。交易员仅可输入转股冻</span>
<span style="color:red">600260</span>
<span style="color:red">债券转托管</span>
43

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
ApplID
业务类型
相关字段填写说明
<span style="color:red">结，场务可进行转股解冻，转股解冻时方向（订单响应中）填</span> <span style="color:red">1</span> <span style="color:red">。</span>
<span style="color:red">600270</span>
<span style="color:red">三方回购转入转出</span>
3. <span style="color:red">OrderQty</span> <span style="color:red">必填。</span>
<span style="color:red">4.</span> <span style="color:red">其他非必填字段均不可填。</span>
1. <span style="color:red">BidTransType</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">，</span> <span style="color:red">Price</span> <span style="color:red">表示底价，</span> <span style="color:red">OrderQty</span> <span style="color:red">表示竞买数量</span>
2. <span style="color:red">参与方中交易员一债通账户必填</span>
<span style="color:red">竞买预约</span>
3. <span style="color:red">SettlType</span> <span style="color:red">、</span> <span style="color:red">BidExecInstType</span> <span style="color:red">、</span> <span style="color:red">PreTradeAnonymity</span> <span style="color:red">、</span> <span style="color:red">ExpireDate</span> <span style="color:red">、</span>
<span style="color:red">OrderRestrictions</span> <span style="color:red">必填，</span> <span style="color:red">ExpireDate</span> <span style="color:red">表示竞买申报日</span>
<span style="color:red">4.</span> <span style="color:red">MinQty</span> <span style="color:red">如选择多主体中标时必填，否则不可填</span>
<span style="color:red">1.</span> <span style="color:red">BidTransType</span> <span style="color:red">填</span> <span style="color:red">2</span> <span style="color:red">，</span> <span style="color:red">1.Price</span> <span style="color:red">表示底价，</span> <span style="color:red">OrderQty</span> <span style="color:red">表示竞买数量</span>
<span style="color:red">600290</span>
2. <span style="color:red">参与方中交易员一债通账户必填</span>
<span style="color:red">（预留，</span>
<span style="color:red">竞买申报</span>
3. <span style="color:red">MinQty</span> <span style="color:red">如选择多主体中标时必填，否则不可填</span>
<span style="color:red">暂不启</span>
<span style="color:red">4.</span> <span style="color:red">SettlType</span> <span style="color:red">、</span> <span style="color:red">BidExecInstType</span> <span style="color:red">、</span> <span style="color:red">PreTradeAnonymity</span> <span style="color:red">与竞买预约申报</span>
<span style="color:red">用）</span>
<span style="color:red">相同，本次不可修改</span>
1. <span style="color:red">BidTransType</span> <span style="color:red">填</span> <span style="color:red">3</span>
2. <span style="color:red">对于单一主体中标，</span> <span style="color:red">OrderQty</span> <span style="color:red">必须与竞买预约数量相等，</span> <span style="color:red">Price</span>
<span style="color:red">应价申报</span>
<span style="color:red">应当大于等于底价</span>
<span style="color:red">3.</span> <span style="color:red">参与方中交易员一债通账户必填</span> 、 <span style="color:red">PreTradeAnonymity</span> <span style="color:red">必填</span> ；
<span style="color:red">SecondaryOrderID</span> <span style="color:red">必填，表示应价对应的竞买申报编号</span>
说明：
1 、 OrdType 字段：开放式基金、要约 / 现金选择权、融资融券业务申报请求暂不启用。
2 、 Text 字段对于开放式基金、融资融券、要约 / 现金选择权非交易业务仅前 12 位有效。
3 、 “ 发起方营业部代码 ” 字段： 5 位数字表示，目前使用区间为 [00000 ， 65535] ，不足 5 位的左侧补 0 。
营业部代码可于本所网站会员专区查询，若无对应营业部代码，则该字段填写空格。
4 、 “ 结算会员代码 ” 字段： B 股结算会员代码，对于 A 股投资者取值无意义，对于 B 股境外投资者 C9
类账户此记录不能为空，直接填写中登公司公布的 B 股结算会员代码，不足 5 位的左侧补 0, 。对于 B 股境
内投资者 C1 类账户无意义，前 5 位有效。对于开放式基金、要约 / 现金选择权、融资融券非交易业务无意
义。
5 、 OwnerType 字段：开放式基金、要约 / 现金选择权、融资融券非交易业务申报请求暂不启用。
6 、参与方个数应小于等于 <span style="color:red">14</span> ，重复组个数应 <span style="color:red">与</span> 申报参与方个数相匹配并按序依次填写，非必填参与
方可跳过。若参与方重复申报，则允许覆盖并仅以最末尾上报值为准（后处理逻辑相同）。
44

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.4.1.2 撤单申报 <span style="color:red">（</span> <span style="color:red">Order Cancel, MsgType = F</span> <span style="color:red">）</span>
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
参与方个数，取值 = <span style="color:red">12</span> ，后接重复组，依次包含发起方的投资
者账户、业务交易单元号、 <span style="color:red">三方回购专用账户、三方回购专</span>
<span style="color:red">户对应交易单元号、交易员一债通账户、银行间托管账号、</span>
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
<span style="color:red">发起方三</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">填写三方回购专用账户。</span>
<span style="color:red">N</span>
<span style="color:red">C13</span>
<span style="color:red">方回购专</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">107</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方三方回购专用账户</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">用账户</span>
<span style="color:red">发起方三</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方三方回购专用账户对应交易单元号</span>
<span style="color:red">N</span>
<span style="color:red">C8</span>
<span style="color:red">方回购专</span>
<span style="color:red">取</span> <span style="color:red">106</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方三方回购专用账户</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">户对应交</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">对应交易单元号</span>
<span style="color:red">易单元号</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">交易员一债通账户</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">发起方交</span>
<span style="color:red">易员一债</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易员一债通账</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
45

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">通账户</span>
<span style="color:red">户</span>
<span style="color:red">银行间托管账号，填写</span> <span style="color:red">11</span> <span style="color:red">位银行间托管账号。债券转托管时</span>
<span style="color:red">N</span>
<span style="color:red">C11</span>
<span style="color:red">银行间托</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">适用。</span>
<span style="color:red">管帐号</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">28</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为银行间托管账号</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
448
PartyID
发起方营业部代码
Y
C8
发起方营
业部代码
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为发起方的营业部代码。
Y
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
1 、基金通报价交易 ApplID=600020 ，基金通转入转出 ApplID=600021 时，投资者中国结算开放式基
金账户、投资者中国结算交易账户、销售人代码、券商网点号码为必填。
2 、撤单申报中， APPIID 、发起方投资者账户、发起方业务交易单元号、 <span style="color:red">发起方三方回购专用账户、</span>
<span style="color:red">发起方三方回购专户对应交易单元号、发起方交易员一债通账户、银行间托管帐号、</span> 投资者中国结算开放
式基金账户、投资者中国结算交易账户、销售人代码、券商网点、 SecurityID 、 Side 取值应与原申报相同，
OrigClOrdID 的取值应与待撤原订单的 ClOrdID 相同。对于开放式基金、要约 / 现金选择权、融资融券非交
易业务，仅要求 ApplID 、发起方业务交易单元号、 SecurityID 取值应与待撤原订单相同， OrigClOrdID 的
取值应与待撤原订单的 ClOrdID 相同； Text 字段仅前 12 位有效。
3 、要约 / 现金选择权业务撤单申报时，申报编号字段必填，且需与原订单保持一致。
4 、发起方投资者账户、发起方营业部代码、 OwnerType 、 Side 字段对于开放式基金、要约 / 现金选择
46

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
权、融资融券非交易业务暂不启用。
4.4.2 询价 <span style="color:red">报价</span> 业务类
4.4.2.1 询价请求（ Quote Request <span style="color:red">, MsgType=R</span> ）
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
<span style="color:red">询价请求编号</span> <span style="color:red">,</span> <span style="color:red">主动撤单时填与写被撤委托的</span>
<span style="color:red">131</span>
<span style="color:red">QuoteReqID</span>
<span style="color:red">Y</span>
<span style="color:red">C18</span>
<span style="color:red">QuoteReqID</span> <span style="color:red">一致</span>
11
ClOrdID
会员内部编号
Y
C10
<span style="color:red">原始会员内部订单编号，指被撤单订单的</span>
<span style="color:red">41</span>
<span style="color:red">OrigClOrdID</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">ClOrdID</span>
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
订单申报时间
N
ntime
48
SecurityID
证券代码
Y
C <span style="color:red">12</span>
买卖方向，取值有：
<span style="color:red">0 =</span> <span style="color:red">双边报价</span>
54
Side
Y
C1
1 <span style="color:red">=</span> 买
2 <span style="color:red">=</span> 卖
订单数量
38
OrderQty
<span style="color:red">N</span>
quantity
<span style="color:red">特别地，</span> <span style="color:red">Side</span> <span style="color:red">为</span> <span style="color:red">0</span> <span style="color:red">时表示买入数量</span>
<span style="color:red">订单价格</span>
<span style="color:red">N</span>
<span style="color:red">price</span>
<span style="color:red">44</span>
<span style="color:red">Price</span>
<span style="color:red">特别地，</span> <span style="color:red">Side</span> <span style="color:red">为</span> <span style="color:red">0</span> <span style="color:red">时表示买入价格</span>
<span style="color:red">640</span>
<span style="color:red">Price2</span>
<span style="color:red">Side</span> <span style="color:red">为</span> <span style="color:red">0</span> <span style="color:red">时表示卖出价格</span>
<span style="color:red">N</span>
<span style="color:red">price</span>
47

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">32</span>
<span style="color:red">LastQty</span>
<span style="color:red">Side</span> <span style="color:red">为</span> <span style="color:red">0</span> <span style="color:red">时表示卖出数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">1138</span>
<span style="color:red">DisplayQty</span>
<span style="color:red">冰山订单数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
价格下限
2551
StartPriceRange
N
price
预留 <span style="color:red">字段</span> ，暂不启用
价格上限
2552
EndPriceRange
N
price
预留 <span style="color:red">字段</span> ，暂不启用
询价请求事务类型
10200
QuoteRequestTransType
0-New ，新订单
Y
C1
1-Cancel ，撤销
<span style="color:red">1091</span>
<span style="color:red">PreTradeAnonymity</span>
<span style="color:red">是否匿名报价，取值：匿名</span> <span style="color:red">=1</span> <span style="color:red">，显名</span> <span style="color:red">=0</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">8418</span>
<span style="color:red">FullAmountTrade</span>
<span style="color:red">是否全额成交：</span> <span style="color:red">1=</span> <span style="color:red">是，</span> <span style="color:red">2=</span> <span style="color:red">否</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">结算方式：</span> <span style="color:red">1=</span> <span style="color:red">净额结算，</span> <span style="color:red">2=RTGS</span> <span style="color:red">结算</span>
<span style="color:red">63</span>
<span style="color:red">SettlType</span>
<span style="color:red">担保券可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">2</span> <span style="color:red">；非担保券只能为</span> <span style="color:red">2</span> <span style="color:red">。特别</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">地，对于公募可转债或公募</span> <span style="color:red">REITs</span> <span style="color:red">，只能填</span> <span style="color:red">1</span> <span style="color:red">。</span>
<span style="color:red">结算场所：</span> <span style="color:red">1=</span> <span style="color:red">中国结算，</span> <span style="color:red">2=</span> <span style="color:red">中央结算</span>
<span style="color:red">双边托管券，可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">2</span> <span style="color:red">，单边托管券只能填</span>
<span style="color:red">207</span>
<span style="color:red">SecurityExchange</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">其实际托管方。预留字段，暂不启用。</span>
<span style="color:red">结算周期：</span>
<span style="color:red">0 = T+0</span>
<span style="color:red">1 = T+1</span>
<span style="color:red">10216</span>
<span style="color:red">SettlPeriod</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">2 = T+2</span>
<span style="color:red">3 = T+3</span>
<span style="color:red">预留字段，暂不启用</span>
126
ExpireTime
询价请求失效时间，预留 <span style="color:red">字段，暂不启用</span>
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
询价接收方参与人代码 <span style="color:red">，支持特殊符号‘</span> <span style="color:red">-</span> <span style="color:red">’</span>
N
C <span style="color:red">12</span>
参与方个数，取值 = <span style="color:red">8</span> ，后接重复组，依次包含
询价发起方的投资者账户、业务交易单元代
453
NoPartyIDs
Y
N2
码、营业部代码、 <span style="color:red">交易员一债通账户、</span> 投资者
中国结算开放式基金账户、投资者中国结算交
48

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
Y
C8
营业部
取 4001 ，表示当前 PartyID 的取值为询价发起
452
PartyRole
Y
N4
代码
方的营业部代码。
<span style="color:red">发起方</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">交易员一债通账户</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">交易员</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">一债通</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">交易员一债通账户</span>
<span style="color:red">账户</span>
投资者
448
PartyID
投资者场外开放式基金账户
N
C12
中国结
算开放
取 4010 ，表示当前 PartyID 的取值为发起方的
N
N4
452
PartyRole
式基金
场外开放式基金账户。
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
49

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">1</span> <span style="color:red">、对于询价请求订单申报，</span> <span style="color:red">TransactTime</span> <span style="color:red">选填，其他非必填字段要求如下：</span>
<span style="color:red">业务类型（</span> <span style="color:red">ApplID</span> <span style="color:red">）</span>
<span style="color:red">填写说明</span>
<span style="color:red">基金通询价（</span> <span style="color:red">600022</span> <span style="color:red">）</span>
<span style="color:red">1.</span> <span style="color:red">Side</span> <span style="color:red">仅可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">2</span> <span style="color:red">，</span> <span style="color:red">OrderQty</span> <span style="color:red">表示对应方向数量</span>
<span style="color:red">2.</span> <span style="color:red">投资者中国结算开放式基金账户、投资者中国结算交易账户、销售人代</span>
<span style="color:red">码、券商网点号码为必填</span>
<span style="color:red">3.</span> <span style="color:red">“</span> <span style="color:red">询价接收方参与人个数</span> <span style="color:red">”</span> <span style="color:red">字段可填</span> <span style="color:red">[0,50]</span> <span style="color:red">，填</span> <span style="color:red">0</span> <span style="color:red">时，</span> <span style="color:red">“</span> <span style="color:red">询价接收方参与人</span>
<span style="color:red">代码</span> <span style="color:red">”</span> <span style="color:red">字段必须为空，表示向市场该产品对应全部做市商发起询价</span>
<span style="color:red">待定报价（</span> <span style="color:red">600200</span> <span style="color:red">）</span>
<span style="color:red">1.</span> <span style="color:red">SettlType</span> <span style="color:red">、</span> <span style="color:red">FullAmountTrade</span> <span style="color:red">、</span> <span style="color:red">PreTradeAnonymity</span> <span style="color:red">必填</span>
<span style="color:red">2.</span> <span style="color:red">NoCounterpartyParticipant</span> <span style="color:red">必填，可填</span> <span style="color:red">[0,5]</span> <span style="color:red">，</span> <span style="color:red">0</span> <span style="color:red">表示发送给全市场；如指</span>
<span style="color:red">定范围发送，</span> <span style="color:red">CounterpartyParticipantCode</span> <span style="color:red">必填</span>
<span style="color:red">3.</span> <span style="color:red">DisplayQty</span> <span style="color:red">选填，需要为最小变动单位的正整数倍；</span> <span style="color:red">DisplayQty</span> <span style="color:red">和</span>
<span style="color:red">FullAmountTrade=1</span> <span style="color:red">不可同时申报。如指定范围发送，不支持冰山订单。</span>
<span style="color:red">4.</span> <span style="color:red">支持双边报价：如</span> <span style="color:red">Side</span> <span style="color:red">填</span> <span style="color:red">0</span> <span style="color:red">，则</span> <span style="color:red">OrderQty</span> <span style="color:red">、</span> <span style="color:red">Price</span> <span style="color:red">、</span> <span style="color:red">LastQty</span> <span style="color:red">、</span> <span style="color:red">Price2</span> <span style="color:red">均需</span>
<span style="color:red">填写；否则仅填写对应方向的价格和数量即可</span>
<span style="color:red">5.</span> <span style="color:red">发起方交易员信息必填</span>
<span style="color:red">一债通询价（</span> <span style="color:red">600190</span> <span style="color:red">）</span>
<span style="color:red">1.</span> <span style="color:red">Side</span> <span style="color:red">仅可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">2</span>
<span style="color:red">2.</span> <span style="color:red">OrderQty</span> <span style="color:red">、</span> <span style="color:red">PreTradeAnonymity</span> <span style="color:red">、</span> <span style="color:red">SettlType</span> <span style="color:red">必填</span>
<span style="color:red">3.</span> <span style="color:red">NoCounterpartyParticipant</span> <span style="color:red">必填，可填</span> <span style="color:red">[0,5]</span> <span style="color:red">，填</span> <span style="color:red">0</span> <span style="color:red">时表示发给潜在投资者；</span>
<span style="color:red">大于</span> <span style="color:red">0</span> <span style="color:red">时，</span> <span style="color:red">CounterpartyParticipantCode</span> <span style="color:red">必填</span>
<span style="color:red">4.</span> <span style="color:red">发起方交易员信息必填</span>
<span style="color:red">2</span> <span style="color:red">、对于待定报价双边报价，如在限定范围内发布，将拆分为两笔子订单转发给对手方；如全市场发</span>
<span style="color:red">布，则拆分为两笔子订单通过逐笔行情对外发布。</span>
<span style="color:red">“</span> <span style="color:red">询价接收方参与人个数</span> <span style="color:red">”</span> <span style="color:red">字段为</span> <span style="color:red">0</span> <span style="color:red">时，</span> <span style="color:red">“</span> <span style="color:red">询价接收方参与人代码</span> <span style="color:red">”</span> <span style="color:red">字段必须为空，表示向市场该产品对</span>
<span style="color:red">应全部做市商发起询价。</span>
<span style="color:red">询价请求（</span> <span style="color:red">Quote Request</span> <span style="color:red">）中询价请求编号</span> <span style="color:red">QuoteReqID</span> <span style="color:red">前</span> <span style="color:red">10</span> <span style="color:red">位有效。</span>
4.4.2.2 询价请求响应（ Quote Request Ack <span style="color:red">, MsgType=R</span> ）
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
50

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
询价请求编号， <span style="color:red">交易所唯一化处理后的询价请</span>
131
QuoteReqID
Y
C18
<span style="color:red">求</span> <span style="color:red">ID</span>
11
ClOrdID
会员内部编号
Y
C10
<span style="color:red">原始会员内部订单编号，指被撤单订单的</span>
<span style="color:red">41</span>
<span style="color:red">OrigClOrdID</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">ClOrdID</span>
<span style="color:red">申报来源</span>
<span style="color:red">2405</span>
<span style="color:red">ExecMethod</span>
<span style="color:red">0 =</span> <span style="color:red">网页端申报</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">1 =</span> <span style="color:red">接口端（</span> <span style="color:red">TDGW</span> <span style="color:red">）申报</span>
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
订单申报时间
N
ntime
48
SecurityID
证券代码
Y
C <span style="color:red">12</span>
买卖方向，取值有：
<span style="color:red">0 =</span> <span style="color:red">双边</span>
54
Side
Y
C1
1 <span style="color:red">=</span> 买
2 <span style="color:red">=</span> 卖
订单数量 <span style="color:red">，撤单时表示剩余数量</span>
38
OrderQty
<span style="color:red">Side</span> <span style="color:red">为</span> <span style="color:red">0</span> <span style="color:red">时表示买入数量，双边撤单时表示买</span>
<span style="color:red">N</span>
quantity
<span style="color:red">入剩余数量</span>
<span style="color:red">Side</span> <span style="color:red">为</span> <span style="color:red">0</span> <span style="color:red">时表示卖出数量，双边撤单时表示卖</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">32</span>
<span style="color:red">LastQty</span>
<span style="color:red">出剩余数量</span>
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
51

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
QuoteRequestStatus=0 时为交易所订单编号，
QuoteRequestStatus=4 时为被撤询价单交易所
订单编号
17
ExecID
订单执行编号
N
C16
询价请求事务类型
10200
QuoteRequestTransType
0-New ，新订单
Y
C1
1-Cancel ，撤销
询价请求类型
303
QuoteRequestType
101=Submit ，提交
Y
C3
102=Alleged ，转发
询价请求状态
0=Accepted ，已接受
10222
QuoteRequestStatus
4=Cancelled ，已撤销
Y
C1
5=Rejected ，已拒绝
7=Expired ，已超时
658
QuoteRequestRejectReason
订单拒绝码
<span style="color:red">YN</span>
C5
10237
QuoteRequestRejectText
订单拒绝原因说明
N
C32
126
ExpireTime
询价请求失效时间，预留 <span style="color:red">字段，暂不启用</span>
N
ntime
10300
NoCounterpartyParticipant
询价接收方参与人个数
Y
N10
→
10301 CounterpartyParticipantCode
询价接收方参与人代码 <span style="color:red">，支持特殊符号‘</span> <span style="color:red">-</span> <span style="color:red">’</span>
N
C <span style="color:red">812</span>
参与方个数，取值 = <span style="color:red">8</span> ，后接重复组，依次包含
询价发起方的投资者账户、业务交易单元代码、
营业部代码、 <span style="color:red">交易员一债通账户、</span> 投资者中国
453
NoPartyIDs
Y
N2
结算开放式基金账户、投资者中国结算交易账
户、销售人代码、券商网点号码。
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
业务交
交易单元号。
52

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
Y
C8
营业部
取 4001 ，表示当前 PartyID 的取值为询价发起
452
PartyRole
Y
N4
代码
方的营业部代码。
<span style="color:red">发起方</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">交易员一债通账户</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">交易员</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">一债通</span>
<span style="color:red">易员一债通账户</span>
<span style="color:red">账户</span>
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
投资者
448
PartyID
投资者中国结算交易账户
N
C17
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
<span style="color:red">说明：</span>
<span style="color:red">对于双边报价撤单，如双边订单中有一笔撤销成功，一笔因已成交或其他原因撤销失败，返回撤销成</span>
<span style="color:red">功（已撤销）；如两笔均因已成交或其他原因撤销失败，返回撤销失败（已拒绝）。</span>
4.4.2.3 转发询价请求（ Allege Quote Request <span style="color:red">, MsgType=R</span> ）
标签
字段名
字段描述
必须
类型
53

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
C <span style="color:red">12</span>
买卖方向， <span style="color:red">表示询价发起方的方向，</span> 取值有：
54
Side
1 <span style="color:red">=</span> 买
Y
C1
2 <span style="color:red">=</span> 卖
<span style="color:red">44</span>
<span style="color:red">Price</span>
<span style="color:red">订单价格</span>
<span style="color:red">N</span>
<span style="color:red">price</span>
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
询价请求事务类型
10200
QuoteRequestTransType
0-New ，新订单
Y
C1
1-Cancel ，撤销
询价请求类型
303
QuoteRequestType
101=Submit ，提交
Y
C3
102=Alleged ，转发
10222
QuoteRequestStatus
询价请求状态
Y
C1
54

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
0=Accepted ，已接受
4=Cancelled ，已撤销
5=Rejected ，已拒绝
7=Expired ，已超时
8=Filled ，已成交
<span style="color:red">8418</span>
<span style="color:red">FullAmountTrade</span>
<span style="color:red">是否全额成交：</span> <span style="color:red">1=</span> <span style="color:red">是，</span> <span style="color:red">2=</span> <span style="color:red">否。</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">63</span>
<span style="color:red">SettlType</span>
<span style="color:red">结算方式：</span> <span style="color:red">1=</span> <span style="color:red">净额结算，</span> <span style="color:red">2=RTGS</span> <span style="color:red">结算</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">结算场所：</span> <span style="color:red">1=</span> <span style="color:red">中国结算，</span> <span style="color:red">2=</span> <span style="color:red">中央结算</span>
<span style="color:red">207</span>
<span style="color:red">SecurityExchange</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">预留字段，暂不启用</span>
<span style="color:red">结算周期：</span>
<span style="color:red">0 = T+0</span>
<span style="color:red">1 = T+1</span>
<span style="color:red">10216</span>
<span style="color:red">SettlPeriod</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">2 = T+2</span>
<span style="color:red">3 = T+3</span>
<span style="color:red">预留字段，暂不启用</span>
126
ExpireTime
询价请求失效时间，预留 <span style="color:red">字段，暂不启用</span>
N
ntime
参与方个数，取值 = <span style="color:red">7</span> ，后接重复组，依次包含询价发
起方的投资者账户、 <span style="color:red">交易员一债通账户、对手方交易</span>
<span style="color:red">参与人机构代码、发起方</span> 投资者中国结算开放式基金
453
NoPartyIDs
Y
N2
账户、投资者中国结算交易账户、销售人代码、券商
网点号码。
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
<span style="color:red">询价发起方业务交易单元代码，填写</span> <span style="color:red">5</span> <span style="color:red">位业务交易单</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方业</span>
<span style="color:red">N</span>
<span style="color:red">C8</span>
<span style="color:red">元号。</span>
<span style="color:red">务交易单</span>
<span style="color:red">取</span> <span style="color:red">1</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方业务交易单</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">元号</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">元号。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">询价发起方营业部代码</span>
<span style="color:red">N</span>
<span style="color:red">C8</span>
<span style="color:red">发起方营</span>
<span style="color:red">取</span> <span style="color:red">4001</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为询价发起方的营</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">业部代码</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">业部代码。</span>
55

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">交易员一债通账户</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">发起方交</span>
<span style="color:red">易员一债</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易员</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">通账户</span>
<span style="color:red">一债通账户</span>
<span style="color:red">对手方</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">对手方交易参与人机构代码，支持特殊符号‘</span> <span style="color:red">-</span> <span style="color:red">’</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">机构代</span>
<span style="color:red">取</span> <span style="color:red">37</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为对手方的交易参</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">码</span>
<span style="color:red">与人代码</span>
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
基金通询价交易 <span style="color:red">（</span> <span style="color:red">600022</span> <span style="color:red">）</span> 时，投资者中国结算开放式基金账户、投资者中国结算交易账户、销售人
代码、券商网点号码为必填。
<span style="color:red">一债通询价（</span> <span style="color:red">600190</span> <span style="color:red">）、待定报价（</span> <span style="color:red">600200</span> <span style="color:red">）时，发起方交易员一债通账户、对手方机构代码必填。</span>
<span style="color:red">如询价方选择‘匿名’且为‘净额结算’时，发起方交易员一债通账户、发起方投资者账户（如有）填</span>
<span style="color:red">‘</span> <span style="color:red">anonymous</span> <span style="color:red">’。</span>
4.4.2.4 报价（ Quote <span style="color:red">, MsgType=S</span> ）
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
1166
QuoteMsgID
客户报价消息编号，类似 CIOrderID 会员内部编号
Y
C10
56

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">41</span>
<span style="color:red">OrigClOrdID</span>
<span style="color:red">被撤订单的</span> <span style="color:red">QuoteMsgID</span>
<span style="color:red">N</span>
C1 <span style="color:red">0</span>
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
订单申报时间
N
ntime
当报价是对询价请求的响应时，填写转发询价请求的
131
QuoteReqID
N
C18
QuoteReqID <span style="color:red">或公开报价行情中的</span> <span style="color:red">QuoteID</span>
48
SecurityID
证券代码
Y
C <span style="color:red">612</span>
132
BidPx
买报价 BidSize>0 时必须填写 <span style="color:red">（表示报价发起方买）</span>
N
price
133
OfferPx
卖报价 OfferSize>0 时必须填写 <span style="color:red">（表示报价发起方卖）</span> N
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
<span style="color:red">1138</span>
<span style="color:red">DisplayQty</span>
<span style="color:red">冰山订单数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
62
ValidUntilTime
报价有效时间，预留 <span style="color:red">字段，暂不启用</span>
N
ntime
是否匿名
1091
PreTradeAnonymity
0= 显名
N
C1
1= 匿名 <span style="color:red">9=</span> <span style="color:red">不指定</span>
<span style="color:red">8418</span>
<span style="color:red">FullAmountTrade</span>
<span style="color:red">是否全额成交：</span> <span style="color:red">1=</span> <span style="color:red">是，</span> <span style="color:red">2=</span> <span style="color:red">否。</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">结算方式：</span> <span style="color:red">1=</span> <span style="color:red">净额结算，</span> <span style="color:red">2=RTGS</span> <span style="color:red">结算。</span>
<span style="color:red">63</span>
<span style="color:red">SettlType</span>
<span style="color:red">担保券可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">2</span> <span style="color:red">；非担保券只能为</span> <span style="color:red">2</span> <span style="color:red">。特别地，对于</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">公募可转债或公募</span> <span style="color:red">REITs</span> <span style="color:red">，只能填</span> <span style="color:red">1</span> <span style="color:red">。</span>
<span style="color:red">结算场所：</span> <span style="color:red">1=</span> <span style="color:red">中国结算，</span> <span style="color:red">2=</span> <span style="color:red">中央结算</span>
<span style="color:red">双边托管券，可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">2</span> <span style="color:red">，单边托管券只能填其实际</span>
<span style="color:red">207</span>
<span style="color:red">SecurityExchange</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">托管方。目前仅可填</span> <span style="color:red">1</span> <span style="color:red">。</span>
<span style="color:red">预留字段，暂不启用。</span>
<span style="color:red">结算周期：</span>
<span style="color:red">10216</span>
<span style="color:red">SettlPeriod</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">0 = T+0</span>
57

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">1 = T+1</span>
<span style="color:red">2 = T+2</span>
<span style="color:red">3 = T+3</span>
<span style="color:red">预留字段，暂不启用</span>
<span style="color:red">报价接收方参与人个数</span>
<span style="color:red">10300</span>
<span style="color:red">NoCounterpartyParticipant</span>
<span style="color:red">N</span>
<span style="color:red">N10</span>
<span style="color:red">撤单时不适用。</span>
<span style="color:red">103</span>
<span style="color:red">→</span>
<span style="color:red">CounterpartyParticipantCode</span> <span style="color:red">报价接收方参与人代码，支持特殊符号</span> <span style="color:red">’-’</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">01</span>
参与方个数，取值 = <span style="color:red">8</span> ，后接重复组，依次包含报价发
起方的投资者账户、业务交易单元代码、营业部代码、
<span style="color:red">交易员一债通账户、</span> 投资者中国结算开放式基金账户、
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
<span style="color:red">报价询价</span> 发起方营业部代码
Y
C8
发起方营
取 4001 ，表示当前 PartyID 的取值为报价发起方的营
452
PartyRole
业部代码
Y
N4
业部代码。
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">报价发起方交易员一债通账户</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">发起方交</span>
<span style="color:red">易员一债</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易员一</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">通账户</span>
<span style="color:red">债通账户</span>
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
452
PartyRole
取 4011 ，表示当前 PartyID 的取值为发起方的场外交
N
N4
58

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
<span style="color:red">1</span> <span style="color:red">、基金通询价交易（</span> <span style="color:red">ApplID=600022</span> <span style="color:red">）时，投资者中国结算开放式基金账户、投资者中国结算交易账</span>
<span style="color:red">户、销售人代码、券商网点号码为必填。</span>
<span style="color:red">2</span> <span style="color:red">、报价（</span> <span style="color:red">Quote</span> <span style="color:red">）中报价请求编号</span> <span style="color:red">QuoteID</span> <span style="color:red">前</span> <span style="color:red">10</span> <span style="color:red">位有效。</span>
<span style="color:red">3</span> <span style="color:red">、基金通询价交易</span> <span style="color:red">ApplID=600022</span> <span style="color:red">时，投资者中国结算开放式基金账户、投资者中国结算交易账户、</span>
<span style="color:red">销售人代码、券商网点号码为必填。</span> 2 、报价消息 <span style="color:red">体中</span> 支持以下报价方式 <span style="color:red">，其中确定报价支持双边报价（双</span>
<span style="color:red">边报价撤销时需要同时撤销，也即</span> <span style="color:red">BidSize</span> <span style="color:red">和</span> <span style="color:red">OfferSize</span> <span style="color:red">均填</span> <span style="color:red">0</span> <span style="color:red">），其他业务仅支持单边报价。</span>
报价方式
BidSize （ 134 ）
OfferSize （ 135 ）
买报价
>0
=0
卖报价
=0
>0
<span style="color:red">双边报价</span>
<span style="color:red">>0</span>
<span style="color:red">>0</span>
撤销报价
=0
=0
<span style="color:red">3</span> <span style="color:red">、对于确定报价、一债通询价和待定报价，发起方交易员信息必填，</span> <span style="color:red">TransactTime</span> <span style="color:red">选填，其他非必</span>
<span style="color:red">填字段要求如下：</span>
<span style="color:red">业务类型（</span> <span style="color:red">ApplID</span> <span style="color:red">）</span>
<span style="color:red">填写说明</span>
<span style="color:red">确定报价（</span> <span style="color:red">600180</span> <span style="color:red">）</span>
<span style="color:red">1.</span> <span style="color:red">SettlType</span> <span style="color:red">、</span> <span style="color:red">FullAmountTrade</span> <span style="color:red">、</span> <span style="color:red">PreTradeAnonymity</span> <span style="color:red">必填</span>
<span style="color:red">2.</span> <span style="color:red">NoCounterpartyParticipant</span> <span style="color:red">必填，可填</span> <span style="color:red">[0,5]</span> <span style="color:red">，</span> <span style="color:red">0</span> <span style="color:red">表示发送给全市场；如指定范</span>
<span style="color:red">围发送，</span> <span style="color:red">CounterpartyParticipantCode</span> <span style="color:red">必填</span>
<span style="color:red">3.</span> <span style="color:red">DisplayQty</span> <span style="color:red">选填，需要为最小变动单位的正整数倍；</span> <span style="color:red">DisplayQty</span> <span style="color:red">和</span>
<span style="color:red">FullAmountTrade=1</span> <span style="color:red">不可同时申报。如指定范围发送，不支持冰山订单</span>
<span style="color:red">4.</span> <span style="color:red">支持双边报价：</span> <span style="color:red">BidPx/BidSize</span> <span style="color:red">和</span> <span style="color:red">OfferPx/OfferSize</span> <span style="color:red">需要至少填写一对</span>
<span style="color:red">一债通询价（</span> <span style="color:red">600190</span> <span style="color:red">）</span>
<span style="color:red">1.</span> <span style="color:red">QuoteReqID</span> <span style="color:red">必填</span>
<span style="color:red">2.</span> <span style="color:red">BidPx/BidSize</span> <span style="color:red">和</span> <span style="color:red">OfferPx/OfferSize</span> <span style="color:red">需要填写其中一对，例如询价请求中</span> <span style="color:red">Side</span>
<span style="color:red">为买，此处应当填</span> <span style="color:red">OfferPx</span> <span style="color:red">和</span> <span style="color:red">OfferSize</span>
59

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">待定报价（</span> <span style="color:red">600200</span> <span style="color:red">）</span>
<span style="color:red">1.</span> <span style="color:red">QuoteReqID</span> <span style="color:red">必填</span>
<span style="color:red">2.</span> <span style="color:red">BidSize</span> <span style="color:red">或</span> <span style="color:red">OfferSize</span> <span style="color:red">中的任一个必填，如如询价请求中</span> <span style="color:red">Side</span> <span style="color:red">为买，此处应当</span>
<span style="color:red">填</span> <span style="color:red">OfferSize</span>
<span style="color:red">4</span> <span style="color:red">、对于确定报价或待定报价，如在限定范围内发布，将拆分为两笔子订单转发给对手方；如全市场</span>
<span style="color:red">发布，则拆分为两笔子订单通过逐笔行情对外发布。</span>
4.4.2.5 报价状态回报（ Quote Status Report <span style="color:red">, MsgType=AI</span> ）
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
<span style="color:red">41</span>
<span style="color:red">OrigClOrdID</span>
<span style="color:red">被撤单订单的</span> <span style="color:red">QuoteMsgID</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">申报来源</span>
<span style="color:red">2405</span>
<span style="color:red">ExecMethod</span>
<span style="color:red">0 =</span> <span style="color:red">网页端申报</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">1 =</span> <span style="color:red">接口端（</span> <span style="color:red">TDGW</span> <span style="color:red">）申报</span>
报价请求编号 <span style="color:red">主动撤单时填与被撤委托的</span> <span style="color:red">QuoteID</span>
117
QuoteID
Y
C18
<span style="color:red">一致</span>
当报价是对询价请求的响应时，填写转发询价请求
131
QuoteReqID
N
C18
的 QuoteReqID <span style="color:red">或公开报价行情中的</span> <span style="color:red">QuoteID</span>
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
297
QuoteStatus
0=Accepted ，接受
N
C1
4=Cancelled ，已撤销
60

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
C <span style="color:red">612</span>
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
买数量 <span style="color:red">，撤单时表示买入剩余数量</span>
N
quantity
135
OfferSize
卖数量 <span style="color:red">，撤单时表示卖出剩余数量</span>
N
quantity
交易所订单编号
37
OrderID
QuoteStatus=0 时为交易所订单编号， QuoteStatus=4
N
C16
时为被撤报价单交易所订单编号
17
ExecID
执行编号
N
C1 <span style="color:red">06</span>
62
ValidUntilTime
报价失效时间，预留 <span style="color:red">字段，暂不启用</span>
N
ntime
参与方个数，取值 = <span style="color:red">8</span> ，后接重复组，依次包含报价
发起方的投资者账户业务交易单元代码、营业部代
码、 <span style="color:red">交易员一债通账户、</span> 投资者中国结算开放式基
453
NoPartyIDs
Y
N2
金账户、投资者中国结算交易账户、销售人代码、
券商网点号码。
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
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">交易员一债通账户</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">发起方</span>
<span style="color:red">交易员</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">一债通</span>
<span style="color:red">员一债通账户</span>
61

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">账户</span>
发起方
448
PartyID
报价发起方营业部代码
Y
C8
营业部
取 4001 ，表示当前 PartyID 的取值为报价发起方的
452
PartyRole
Y
N4
代码
营业部代码。
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
<span style="color:red">说明：</span>
<span style="color:red">1</span> <span style="color:red">、对于基金通询价，</span> <span style="color:red">SecurityID</span> <span style="color:red">（</span> <span style="color:red">48</span> <span style="color:red">）左数前六位有效，</span> <span style="color:red">ExecID</span> <span style="color:red">（</span> <span style="color:red">17</span> <span style="color:red">）左数前</span> <span style="color:red">10</span> <span style="color:red">位有效，且均不补</span>
<span style="color:red">空格。</span>
<span style="color:red">2</span> <span style="color:red">、对于响应中的</span> <span style="color:red">QuoteID</span> <span style="color:red">字段，如申报为报价，填写交易所唯一化处理后的报价请求</span> <span style="color:red">ID</span> <span style="color:red">；如申报为</span>
<span style="color:red">报价回复，且回复中填写了</span> <span style="color:red">QuoteID</span> <span style="color:red">，则响应中与申报时填写字段相同。</span>
4.4.2.6 转发报价（ Allege Quote <span style="color:red">, MsgType=S</span> ）
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
62

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
1180
ApplID
业务类型
Y
C6
当报价是对询价请求的响应时，填写询价请求的
131
QuoteReqID
N
C18
QuoteReqID <span style="color:red">或公开报价行情中的</span> <span style="color:red">OrderID</span>
<span style="color:red">QuoteReqID</span> <span style="color:red">对应的会员内部编号，不适用于基金通</span>
<span style="color:red">11</span>
<span style="color:red">ClOrdID</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">询价</span>
117
QuoteID
报价请求编号，交易所唯一化处理后的报价请求 ID
Y
C18
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
<span style="color:red">YN</span>
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
C <span style="color:red">612</span>
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
<span style="color:red">1138</span>
<span style="color:red">DisplayQty</span>
<span style="color:red">冰山订单数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
37
OrderID
交易所订单编号
N
C16
17
ExecID
执行编号
N
C1 <span style="color:red">06</span>
<span style="color:red">8418</span>
<span style="color:red">FullAmountTrade</span>
<span style="color:red">是否全额成交：</span> <span style="color:red">1=</span> <span style="color:red">是，</span> <span style="color:red">2=</span> <span style="color:red">否。</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">63</span>
<span style="color:red">SettlType</span>
<span style="color:red">结算方式：</span> <span style="color:red">1=</span> <span style="color:red">净额结算，</span> <span style="color:red">2=RTGS</span> <span style="color:red">结算</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">结算场所：</span> <span style="color:red">1=</span> <span style="color:red">中国结算，</span> <span style="color:red">2=</span> <span style="color:red">中央结算</span>
<span style="color:red">207</span>
<span style="color:red">SecurityExchange</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">预留字段，暂不启用。</span>
<span style="color:red">结算周期：</span>
<span style="color:red">0 = T+0</span>
<span style="color:red">10216</span>
<span style="color:red">SettlPeriod</span>
<span style="color:red">1 = T+1</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">2 = T+2</span>
<span style="color:red">3 = T+3</span>
63

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">预留字段，暂不启用。</span>
62
ValidUntilTime
报价失效时间，预留 <span style="color:red">字段，暂不启用</span>
N
ntime
参与方个数，取值 = <span style="color:red">7</span> ，后接重复组，依次包含报价
发起方的投资者账户、 <span style="color:red">报价发起方业务交易单元代</span>
<span style="color:red">码、报价发起方营业部代码、发起方交易员一债通</span>
453
NoPartyIDs
Y
N2
<span style="color:red">账户、对手方交易参与人机构代码、发起方的</span> 投资
者中国结算开放式基金账户、投资者中国结算交易
账户、销售人代码、券商网点号码。
发起方投
448
PartyID
报价发起方投资者帐户
<span style="color:red">YN</span>
C13
资者账户
452
PartyRole
取 5 ，表示当前 PartyID 的取值为发起方投资者帐户
<span style="color:red">NY</span>
N4
<span style="color:red">报价发起方业务交易单元代码，填写</span> <span style="color:red">5</span> <span style="color:red">位业务交易</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方业</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">单元号。</span>
<span style="color:red">务交易单</span>
<span style="color:red">取</span> <span style="color:red">1</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方业务交易单</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">元号</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">元号。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">报价发起方营业部代码</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">发起方营</span>
<span style="color:red">取</span> <span style="color:red">4001</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为询价发起方的</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">业部代码</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">营业部代码。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">报价发起方交易员一债通账户</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">发起方交</span>
<span style="color:red">易员一债</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易员</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">通账户</span>
<span style="color:red">一债通账户</span>
<span style="color:red">对手方</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">对手方交易参与人机构代码，支持特殊符号‘</span> <span style="color:red">-</span> <span style="color:red">’</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">机构代</span>
<span style="color:red">取</span> <span style="color:red">37</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为对手方的交易参</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">码</span>
<span style="color:red">与人代码</span>
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
64

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
<span style="color:red">说明：</span>
<span style="color:red">确定报价（</span> <span style="color:red">600180</span> <span style="color:red">）、一债通询价（</span> <span style="color:red">600190</span> <span style="color:red">）、待定报价（</span> <span style="color:red">600200</span> <span style="color:red">）时，发起方交易员一债通账户、</span>
<span style="color:red">对手方机构代码必填。如询价方或报价方选择‘匿名’且为‘净额结算’时，发起方交易员一债通账户、</span>
<span style="color:red">发起方投资者账户（如有）填‘</span> <span style="color:red">anonymous</span> <span style="color:red">’。</span>
4.4.2.7 报价回复（ Quote Response <span style="color:red">, MsgType=AJ</span> ）
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
<span style="color:red">693</span>
<span style="color:red">QuoteRespID</span>
<span style="color:red">报价回复消息编号</span>
<span style="color:red">Y</span>
<span style="color:red">C18</span>
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
C <span style="color:red">612</span>
报价回复类型
1=Hit/Lift ，接受
694
QuoteRespType
N
C1
2=Counter ，重报 <span style="color:red">（枚举值预留，暂不启用）</span>
6 <span style="color:red">-=</span> Pass ，拒绝
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
65

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
38
OrderQty
申报数量
N
quantity
报价回复成交类型，取值：
40
OrdType
Y=Negotiated Trade ，表示点击成交报价交易
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
C1 <span style="color:red">08</span>
ID <span style="color:red">或公开报价行情中的</span> <span style="color:red">OrderID</span>
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
报价有效时间，预留 <span style="color:red">字段，暂不启用</span>
N
ntime
参与方个数，取值 = <span style="color:red">8</span> ，后接重复组，依次包含 <span style="color:red">报</span>
<span style="color:red">价回复</span> 发起方的投资者账户、业务交易单元、营
业部代码、 <span style="color:red">交易员一债通账户、</span> 投资者中国结算
453
NoPartyIDs
Y
N2
开放式基金账户、投资者中国结算交易账户、销
售人代码、券商网点号码。
448
PartyID
<span style="color:red">报价回复方</span> 投资者帐户
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
<span style="color:red">报价回复方询价发起方</span> 业务交易单元代码，填写 5
448
PartyID
发起方业
Y
C8
位业务交易单元号。
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
<span style="color:red">报价回复方</span> 营业部代码
Y
C8
发起方营
取 4001 ，表示当前 PartyID 的取值为询价发起方
452
PartyRole
业部代码
Y
N4
的营业部代码。
448
PartyID
<span style="color:red">报价回复方交易员一债通账户</span>
N
C10
<span style="color:red">发起方交</span>
<span style="color:red">易员一债</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易</span>
452
PartyRole
N
N4
<span style="color:red">通账户</span>
<span style="color:red">员一债通账户</span>
投资者中 448
PartyID
投资者场外开放式基金账户
N
C12
66

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
国结算开
取 4010 ，表示当前 PartyID 的取值为发起方的场
放式基金
452
PartyRole
N
N4
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
1 、 <span style="color:red">对于</span> 基金通询价交易 <span style="color:red">（</span> <span style="color:red">600022</span> <span style="color:red">）</span> ，投资者中国结算开放式基金账户、投资者中国结算交易账户、
销售人代码、券商网点号码为必填 <span style="color:red">；点击成交时报价请求编号（</span> <span style="color:red">QuoteID</span> <span style="color:red">）必填，匹配成交时询价请求编</span>
<span style="color:red">号（</span> <span style="color:red">QuoteReqID</span> <span style="color:red">）必填；报价回复类型（</span> <span style="color:red">QuoteRespType</span> <span style="color:red">）仅可填</span> <span style="color:red">1</span> <span style="color:red">，如未接受，超时自动失效</span> 。
2 、 <span style="color:red">对于确定报价、一债通询价和待定报价，报价回复方交易员信息必填，</span> <span style="color:red">NoQuote</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">，</span> <span style="color:red">QuoteID</span> <span style="color:red">必</span>
<span style="color:red">填，</span> <span style="color:red">TransactTime</span> <span style="color:red">选填，其他非必填字段要求如下：</span>
<span style="color:red">业务类型（</span> <span style="color:red">ApplID</span> <span style="color:red">）</span>
<span style="color:red">填写说明</span>
<span style="color:red">确定报价（</span> <span style="color:red">600180</span> <span style="color:red">）</span>
<span style="color:red">OrderQty</span> <span style="color:red">必填；</span> <span style="color:red">OrdType</span> <span style="color:red">填</span> <span style="color:red">‘Y’</span>
<span style="color:red">一债通询价（</span> <span style="color:red">600190</span> <span style="color:red">）</span>
<span style="color:red">QuoteRespType</span> <span style="color:red">必填，仅可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">6</span> <span style="color:red">，不支持填</span> <span style="color:red">2</span> <span style="color:red">；</span> <span style="color:red">OrdType</span> <span style="color:red">填</span> <span style="color:red">‘Y’</span>
<span style="color:red">待定报价（</span> <span style="color:red">600200</span> <span style="color:red">）</span>
<span style="color:red">QuoteRespType</span> <span style="color:red">必填，仅可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">6</span> <span style="color:red">，不支持填</span> <span style="color:red">2</span> <span style="color:red">；</span> <span style="color:red">OrdType</span> <span style="color:red">填</span> <span style="color:red">‘Y’</span>
<span style="color:red">4.4.2.8</span> <span style="color:red">转发报价回复（</span> <span style="color:red">Allege Quote Response, MsgType=AJ</span> <span style="color:red">）</span>
<span style="color:red">标签</span>
<span style="color:red">字段名</span>
<span style="color:red">字段描述</span>
<span style="color:red">必须</span>
<span style="color:red">类型</span>
<span style="color:red">消息头</span>
<span style="color:red">MsgType=AJ</span>
<span style="color:red">10197</span>
<span style="color:red">PartitionNo</span>
<span style="color:red">平台内分区号</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">10179</span>
<span style="color:red">ReportIndex</span>
<span style="color:red">执行报告编号，从</span> <span style="color:red">1</span> <span style="color:red">开始连续递增编号</span>
<span style="color:red">Y</span>
<span style="color:red">N16</span>
<span style="color:red">1180</span>
<span style="color:red">ApplID</span>
<span style="color:red">业务类型</span>
<span style="color:red">Y</span>
<span style="color:red">C6</span>
<span style="color:red">1166</span>
<span style="color:red">QuoteMsgID</span>
<span style="color:red">客户报价消息编号</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
67

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">报价类别</span>
<span style="color:red">537</span>
<span style="color:red">QuoteType</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">1=Tradeable</span> <span style="color:red">，表示可交易的报价</span>
<span style="color:red">订单所有者类型</span>
<span style="color:red">1=</span> <span style="color:red">个人投资者</span>
<span style="color:red">522</span>
<span style="color:red">OwnerType</span>
<span style="color:red">Y</span>
<span style="color:red">N3</span>
<span style="color:red">103=</span> <span style="color:red">机构投资者</span>
<span style="color:red">104=</span> <span style="color:red">自营交易</span>
<span style="color:red">60</span>
<span style="color:red">TransactTime</span>
<span style="color:red">报价发起时间</span>
<span style="color:red">N</span>
<span style="color:red">ntime</span>
<span style="color:red">48</span>
<span style="color:red">SecurityID</span>
<span style="color:red">证券代码</span>
<span style="color:red">Y</span>
<span style="color:red">C12</span>
<span style="color:red">报价回复类型</span>
<span style="color:red">694</span>
<span style="color:red">QuoteRespType</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">6=Pass</span> <span style="color:red">，拒绝</span>
<span style="color:red">54</span>
<span style="color:red">Side</span>
<span style="color:red">买卖方向，取值有：</span> <span style="color:red">1</span> <span style="color:red">表示买，</span> <span style="color:red">2</span> <span style="color:red">表示卖</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">44</span>
<span style="color:red">Price</span>
<span style="color:red">申报价格</span>
<span style="color:red">N</span>
<span style="color:red">price</span>
<span style="color:red">38</span>
<span style="color:red">OrderQty</span>
<span style="color:red">申报数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">报价回复成交类型，取值：</span>
<span style="color:red">40</span>
<span style="color:red">OrdType</span>
<span style="color:red">Y=Negotiated Trade</span> <span style="color:red">，表示点击成交报价交易</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">2=Limit</span> <span style="color:red">，表示匹配成交报价交易</span>
<span style="color:red">10199</span>
<span style="color:red">NoQuote</span>
<span style="color:red">报价消息个数</span>
<span style="color:red">Y</span>
<span style="color:red">-></span>
<span style="color:red">117</span>
<span style="color:red">QuoteID</span>
<span style="color:red">报价请求编号，交易所唯一化处理后的报价请求</span> <span style="color:red">ID</span>
<span style="color:red">N</span>
<span style="color:red">C18</span>
<span style="color:red">-></span>
<span style="color:red">10225</span>
<span style="color:red">QuotePrice</span>
<span style="color:red">报价价格</span>
<span style="color:red">N</span>
<span style="color:red">price</span>
<span style="color:red">-></span>
<span style="color:red">10226</span>
<span style="color:red">QuoteQty</span>
<span style="color:red">报价数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">131</span>
<span style="color:red">QuoteReqID</span>
<span style="color:red">询价请求编号</span>
<span style="color:red">N</span>
<span style="color:red">C18</span>
<span style="color:red">62</span>
<span style="color:red">ValidUntilTime</span>
<span style="color:red">报价有效时间，预留字段，暂不启用</span>
<span style="color:red">N</span>
<span style="color:red">ntime</span>
<span style="color:red">参与方个数，取值</span> <span style="color:red">=6</span> <span style="color:red">，后接重复组，依次包含报价</span>
<span style="color:red">回复方的投资者账户、交易员一债通账户、投资者</span>
<span style="color:red">453</span>
<span style="color:red">NoPartyIDs</span>
<span style="color:red">Y</span>
<span style="color:red">N2</span>
<span style="color:red">中国结算开放式基金账户、投资者中国结算交易账</span>
<span style="color:red">户、销售人代码、券商网点号码。</span>
<span style="color:red">发起方</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">报价回复方投资者帐户</span>
<span style="color:red">N</span>
<span style="color:red">C13</span>
<span style="color:red">投资者</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">5</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方投资者帐户</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">账户</span>
<span style="color:red">发起方</span> <span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">报价回复方交易员一债通账户</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
68

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">交易员</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易员</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">一债通</span>
<span style="color:red">一债通账户</span>
<span style="color:red">账户</span>
<span style="color:red">投资者</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">投资者场外开放式基金账户</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">中国结</span>
<span style="color:red">算开放</span>
<span style="color:red">取</span> <span style="color:red">4010</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的场外</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">式基金</span>
<span style="color:red">开放式基金账户。</span>
<span style="color:red">账户</span>
<span style="color:red">投资者</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">投资者中国结算交易账户</span>
<span style="color:red">N</span>
<span style="color:red">C17</span>
<span style="color:red">中国结</span>
<span style="color:red">取</span> <span style="color:red">4011</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的场外</span>
<span style="color:red">算交易</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">交易账户。</span>
<span style="color:red">账户</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">销售人代码</span>
<span style="color:red">N</span>
<span style="color:red">C9</span>
<span style="color:red">销售人</span>
<span style="color:red">取</span> <span style="color:red">117</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的销售代</span>
<span style="color:red">代码</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">码。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">券商网点号码</span>
<span style="color:red">N</span>
<span style="color:red">C9</span>
<span style="color:red">券商网</span>
<span style="color:red">取</span> <span style="color:red">81</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的客户端</span>
<span style="color:red">点号码</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">编码或网点号码。</span>
<span style="color:red">说明：</span>
<span style="color:red">一债通询价（</span> <span style="color:red">600190</span> <span style="color:red">）、待定报价（</span> <span style="color:red">600200</span> <span style="color:red">）时，发起方交易员一债通账户必填。如询价方或报价方</span>
<span style="color:red">选择‘匿名’且为‘净额结算’时，发起方交易员一债通账户、发起方投资者账户（如有）填‘</span> <span style="color:red">anonymous</span> <span style="color:red">’。</span>
69

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">4.4.3</span> <span style="color:red">意向申报类</span>
<span style="color:red">4.4.3.1</span> <span style="color:red">意向申报（</span> <span style="color:red">IOI, Indication of Interest, MsgType=6)</span>
<span style="color:red">标签</span>
<span style="color:red">字段名</span>
<span style="color:red">字段描述</span>
<span style="color:red">必填</span>
<span style="color:red">类型</span>
<span style="color:red">35</span>
<span style="color:red">消息头</span>
<span style="color:red">MsgType=6</span>
<span style="color:red">1180</span>
<span style="color:red">ApplID</span>
<span style="color:red">业务类型</span>
<span style="color:red">Y</span>
<span style="color:red">C6</span>
<span style="color:red">23</span>
<span style="color:red">IOIID</span>
<span style="color:red">会员内部编号</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">订单所有者类型</span>
<span style="color:red">1=</span> <span style="color:red">个人投资者</span>
<span style="color:red">522</span>
<span style="color:red">OwnerType</span>
<span style="color:red">Y</span>
<span style="color:red">N3</span>
<span style="color:red">103=</span> <span style="color:red">机构投资者</span>
<span style="color:red">104=</span> <span style="color:red">自营交易</span>
<span style="color:red">意向申报事务类型</span>
<span style="color:red">28</span>
<span style="color:red">IOITransType</span>
<span style="color:red">N=New</span> <span style="color:red">，新申报</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">C=Cancel</span> <span style="color:red">，撤销申报</span>
<span style="color:red">26</span>
<span style="color:red">IOIRefID</span>
<span style="color:red">原意向申报</span> <span style="color:red">IOIID</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">54</span>
<span style="color:red">Side</span>
<span style="color:red">方向：</span> <span style="color:red">1=</span> <span style="color:red">买或正回购，</span> <span style="color:red">2=</span> <span style="color:red">卖或逆回购</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">48</span>
<span style="color:red">SecurityID</span>
<span style="color:red">证券代码</span>
<span style="color:red">YN</span>
<span style="color:red">C12</span>
<span style="color:red">44</span>
<span style="color:red">Price</span>
<span style="color:red">意向价格或回购利率</span>
<span style="color:red">N</span>
<span style="color:red">price</span>
<span style="color:red">38</span>
<span style="color:red">OrderQty</span>
<span style="color:red">证券数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">8911</span>
<span style="color:red">ExpirationDays</span>
<span style="color:red">期限（天），可填</span> <span style="color:red">[1,365]</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">64</span>
<span style="color:red">SettlDate</span>
<span style="color:red">首次结算日</span>
<span style="color:red">N</span>
<span style="color:red">date</span>
<span style="color:red">231</span>
<span style="color:red">ContractMultiplier</span>
<span style="color:red">折算比例（</span> <span style="color:red">%</span> <span style="color:red">）</span>
<span style="color:red">N</span>
<span style="color:red">N6(2)</span>
<span style="color:red">8504</span>
<span style="color:red">TotalValueTraded</span>
<span style="color:red">成交金额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">发布范围</span>
<span style="color:red">10300</span>
<span style="color:red">NoCounterpartyParticipant</span>
<span style="color:red">N</span>
<span style="color:red">N10</span>
<span style="color:red">撤单时不适用。</span>
<span style="color:red">→</span> <span style="color:red">10301</span>
<span style="color:red">CounterpartyParticipantCode</span> <span style="color:red">交易参与人机构代码，支持特殊符号‘</span> <span style="color:red">-</span> <span style="color:red">’</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">60</span>
<span style="color:red">TransactTime</span>
<span style="color:red">业务发生时间</span>
<span style="color:red">Y</span>
<span style="color:red">ntime</span>
<span style="color:red">左起顺序代表第</span> <span style="color:red">1</span> <span style="color:red">号至第</span> <span style="color:red">N</span> <span style="color:red">号篮子。例如指定</span> <span style="color:red">1</span> <span style="color:red">，</span>
<span style="color:red">10194</span>
<span style="color:red">BasketID</span>
<span style="color:red">N</span>
<span style="color:red">C16</span>
<span style="color:red">2</span> <span style="color:red">，</span> <span style="color:red">5</span> <span style="color:red">号篮子，填</span> <span style="color:red">“1100100000000000”</span>
<span style="color:red">453</span>
<span style="color:red">NoPartyIDs</span>
<span style="color:red">发起方重复组，依次包含发起方的交易员一债通</span>
<span style="color:red">Y</span>
<span style="color:red">N2</span>
70

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">账户、投资者帐户、业务交易单元、营业部代码。</span>
<span style="color:red">取值为</span> <span style="color:red">4</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方交易员一债通账户</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">员一债通账户</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方投资者帐户</span>
<span style="color:red">N</span>
<span style="color:red">C13</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">5</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方投资者帐</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">户</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方业务交易单元代码</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">1</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方业务交易</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">单元号。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方营业部代码</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">4001</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的营</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">业部代码。</span>
<span style="color:red">非必填字段填写说明：</span>
<span style="color:red">业务类型（</span> <span style="color:red">ApplID</span> <span style="color:red">）</span>
<span style="color:red">申报</span>
<span style="color:red">撤单</span>
<span style="color:red">1.</span> <span style="color:red">SecurityID</span> <span style="color:red">、</span> <span style="color:red">ExpirationDays</span> <span style="color:red">必填，</span> <span style="color:red">SecurityID</span> <span style="color:red">表示质押券代码</span>
<span style="color:red">2.</span> <span style="color:red">Price</span> <span style="color:red">、</span> <span style="color:red">OrderQty</span> <span style="color:red">、</span> <span style="color:red">ContractMultiplier</span> <span style="color:red">、</span> <span style="color:red">TotalValueTraded</span> <span style="color:red">、</span> <span style="color:red">SettlDate</span>
<span style="color:red">IOIRefID</span> <span style="color:red">、</span>
<span style="color:red">协议回购意向申报</span>
<span style="color:red">选填</span>
<span style="color:red">SecurityID</span>
<span style="color:red">（</span> <span style="color:red">600150</span> <span style="color:red">）</span>
<span style="color:red">3.</span> <span style="color:red">TotalValueTraded</span> <span style="color:red">计算方式为：债券成交金额</span> <span style="color:red">=</span> <span style="color:red">质押券数量</span> <span style="color:red">*10*</span>
<span style="color:red">必填</span>
<span style="color:red">单张质押券面值</span> <span style="color:red">*</span> <span style="color:red">折算比例</span> <span style="color:red">/100</span> <span style="color:red">；基金成交金额</span> <span style="color:red">=</span> <span style="color:red">质押券数量</span> <span style="color:red">*</span> <span style="color:red">竞</span>
<span style="color:red">价前收盘价</span> <span style="color:red">*</span> <span style="color:red">折算比例</span> <span style="color:red">/100</span> <span style="color:red">，四舍五入</span>
<span style="color:red">1.</span> <span style="color:red">ExpirationDays</span> <span style="color:red">、</span> <span style="color:red">BasketID</span> <span style="color:red">必填</span>
<span style="color:red">三方回购意向申报</span>
<span style="color:red">2.</span> <span style="color:red">发起方投资者账户必填，若为正回购方，填三方回购专用帐</span>
<span style="color:red">IOIRefID</span> <span style="color:red">必</span>
<span style="color:red">户，若为逆回购方，则填写其对应普通账户</span>
<span style="color:red">填</span>
<span style="color:red">（</span> <span style="color:red">600160</span> <span style="color:red">）</span>
<span style="color:red">3.</span> <span style="color:red">Price</span> <span style="color:red">、</span> <span style="color:red">TotalValueTraded</span> <span style="color:red">选填</span>
<span style="color:red">1.</span> <span style="color:red">SecurityID</span> <span style="color:red">、</span> <span style="color:red">Price</span> <span style="color:red">必填</span>
<span style="color:red">IOIRefID</span> <span style="color:red">、</span>
<span style="color:red">债券现券意向申报</span>
<span style="color:red">2.</span> <span style="color:red">OrderQty</span> <span style="color:red">选填</span>
<span style="color:red">SecurityID</span>
<span style="color:red">（</span> <span style="color:red">600170</span> <span style="color:red">）</span>
<span style="color:red">3.</span> <span style="color:red">NoCounterpartyParticipant</span> <span style="color:red">必填，可填</span> <span style="color:red">[0,5]</span> <span style="color:red">，填</span> <span style="color:red">0</span> <span style="color:red">时表示发送</span>
<span style="color:red">必填</span>
<span style="color:red">给全市场，否则</span> <span style="color:red">CounterpartyParticipantCode</span> <span style="color:red">必填</span>
71

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">4.</span> <span style="color:red">发起方投资者账户必填</span>
<span style="color:red">4.4.3.2</span> <span style="color:red">转发意向申报（</span> <span style="color:red">Allege IOI, MsgType=6)</span>
<span style="color:red">标签</span>
<span style="color:red">字段名</span>
<span style="color:red">字段描述</span>
<span style="color:red">必填</span>
<span style="color:red">类型</span>
<span style="color:red">35</span>
<span style="color:red">消息头</span>
<span style="color:red">MsgType=6</span>
<span style="color:red">10197</span>
<span style="color:red">PartitionNo</span>
<span style="color:red">平台内分区号</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">10179</span>
<span style="color:red">ReportIndex</span>
<span style="color:red">执行报告编号，从</span> <span style="color:red">1</span> <span style="color:red">开始连续递增编号</span>
<span style="color:red">Y</span>
<span style="color:red">N16</span>
<span style="color:red">1180</span>
<span style="color:red">ApplID</span>
<span style="color:red">业务类型</span>
<span style="color:red">Y</span>
<span style="color:red">C6</span>
<span style="color:red">意向申报类型</span>
<span style="color:red">694</span>
<span style="color:red">QuoteRespType</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">1=Alleged</span> <span style="color:red">，转发意向申报</span>
<span style="color:red">28</span>
<span style="color:red">IOITransType</span>
<span style="color:red">意向申报事务类型</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">693</span>
<span style="color:red">QuoteRespID</span>
<span style="color:red">交易所订单编号</span>
<span style="color:red">Y</span>
<span style="color:red">C16</span>
<span style="color:red">54</span>
<span style="color:red">Side</span>
<span style="color:red">方向，表示申报发起方的方向</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">48</span>
<span style="color:red">SecurityID</span>
<span style="color:red">证券代码</span>
<span style="color:red">Y</span>
<span style="color:red">C12</span>
<span style="color:red">44</span>
<span style="color:red">Price</span>
<span style="color:red">意向价格</span>
<span style="color:red">N</span>
<span style="color:red">price</span>
<span style="color:red">38</span>
<span style="color:red">OrderQty</span>
<span style="color:red">意向数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">60</span>
<span style="color:red">TransactTime</span>
<span style="color:red">业务发生时间</span>
<span style="color:red">Y</span>
<span style="color:red">ntime</span>
<span style="color:red">发起方重复组，依次包含发起方的交易员一债通账户、</span>
<span style="color:red">453</span>
<span style="color:red">NoPartyIDs</span>
<span style="color:red">Y</span>
<span style="color:red">N2</span>
<span style="color:red">对手方交易参与人机构代码。取值为</span> <span style="color:red">2</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方交易员一债通账户</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易员一债</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">通账户</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">对手方交易参与人机构代码，支持特殊符号‘</span> <span style="color:red">-</span> <span style="color:red">’</span>
<span style="color:red">Y</span>
<span style="color:red">C12</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">37</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为对手方的交易参与人</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">代码</span>
<span style="color:red">4.4.3.3</span> <span style="color:red">意向申报响应（</span> <span style="color:red">IOI Response, MsgType=AJ</span> <span style="color:red">）</span>
<span style="color:red">标签</span>
<span style="color:red">字段名</span>
<span style="color:red">字段描述</span>
<span style="color:red">必须</span>
<span style="color:red">类型</span>
<span style="color:red">消息头</span>
<span style="color:red">MsgType = AJ</span>
<span style="color:red">10197</span>
<span style="color:red">PartitionNo</span>
<span style="color:red">平台内分区号</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
72

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">10179</span>
<span style="color:red">ReportIndex</span>
<span style="color:red">执行报告编号，从</span> <span style="color:red">1</span> <span style="color:red">开始连续递增编号</span>
<span style="color:red">Y</span>
<span style="color:red">N16</span>
<span style="color:red">1180</span>
<span style="color:red">ApplID</span>
<span style="color:red">业务类型</span>
<span style="color:red">Y</span>
<span style="color:red">C6</span>
<span style="color:red">意向申报事务类型</span>
<span style="color:red">28</span>
<span style="color:red">IOITransType</span>
<span style="color:red">N=New</span> <span style="color:red">，新申报</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">C=Cancel</span> <span style="color:red">，撤销申报</span>
<span style="color:red">意向申报类型</span>
<span style="color:red">694</span>
<span style="color:red">QuoteRespType</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">2=Replace</span> <span style="color:red">，意向申报响应</span>
<span style="color:red">执行报告类型，取值有：</span>
<span style="color:red">0=Accepted</span> <span style="color:red">，订单申报成功</span>
<span style="color:red">150</span>
<span style="color:red">ExecType</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">4=Cancelled</span> <span style="color:red">，订单撤销成功</span>
<span style="color:red">8=Rejected</span> <span style="color:red">，订单申报拒绝</span>
<span style="color:red">23</span>
<span style="color:red">IOIID</span>
<span style="color:red">会员内部订单编号</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">申报来源</span>
<span style="color:red">2405</span>
<span style="color:red">ExecMethod</span>
<span style="color:red">0 =</span> <span style="color:red">网页端申报</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">1 =</span> <span style="color:red">接口端（</span> <span style="color:red">TDGW</span> <span style="color:red">）申报</span>
<span style="color:red">48</span>
<span style="color:red">SecurityID</span>
<span style="color:red">证券代码</span>
<span style="color:red">YN</span>
<span style="color:red">C12</span>
<span style="color:red">订单所有者类型，取值包括：</span>
<span style="color:red">1=</span> <span style="color:red">个人投资者</span>
<span style="color:red">522</span>
<span style="color:red">OwnerType</span>
<span style="color:red">Y</span>
<span style="color:red">N3</span>
<span style="color:red">103=</span> <span style="color:red">机构投资者</span>
<span style="color:red">104=</span> <span style="color:red">自营交易</span>
<span style="color:red">54</span>
<span style="color:red">Side</span>
<span style="color:red">买卖方向</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">44</span>
<span style="color:red">Price</span>
<span style="color:red">申报价</span>
<span style="color:red">N</span>
<span style="color:red">price</span>
<span style="color:red">26</span>
<span style="color:red">IOIRefID</span>
<span style="color:red">原始会员内部订单编号，</span> <span style="color:red">ExecType=4</span> <span style="color:red">时有效</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">300</span>
<span style="color:red">QuoteRejectReason</span>
<span style="color:red">订单拒绝码，</span> <span style="color:red">OrdStatus=8</span> <span style="color:red">时有效</span>
<span style="color:red">N</span>
<span style="color:red">C5</span>
<span style="color:red">693</span>
<span style="color:red">QuoteRespID</span>
<span style="color:red">交易所订单编号</span>
<span style="color:red">Y</span>
<span style="color:red">C16</span>
<span style="color:red">60</span>
<span style="color:red">TransactTime</span>
<span style="color:red">回报时间</span>
<span style="color:red">Y</span>
<span style="color:red">ntime</span>
<span style="color:red">参与方个数，取值</span> <span style="color:red">=5</span> <span style="color:red">，后接重复组，依次包含登录</span>
<span style="color:red">或订阅交易单元、发起方业务交易单元、发起方交</span>
<span style="color:red">453</span>
<span style="color:red">NoPartyIDs</span>
<span style="color:red">Y</span>
<span style="color:red">N2</span>
<span style="color:red">易员一债通账户、发起方投资者账户、发起方营业</span>
<span style="color:red">部代码。</span>
73

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方登录或订阅交易单元。</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">17</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为登录或订阅交易</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">单元。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方业务交易单元。</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">1</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方业务交易单</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">元。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方交易员一债通账户</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易员</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">一债通账户</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方投资者帐户，协议回购意向申报时不适用</span>
<span style="color:red">N</span>
<span style="color:red">C13</span>
<span style="color:red">→</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">5</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方投资者帐户。</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方营业部代码</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">4001</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的营业</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">部代码。</span>
<span style="color:red">4.4.4</span> <span style="color:red">成交申报类</span>
<span style="color:red">4.4.4.1</span> <span style="color:red">成交申报（</span> <span style="color:red">Trade Capture Report, MsgType=AE)</span>
<span style="color:red">必</span>
<span style="color:red">标签</span>
<span style="color:red">字段名</span>
<span style="color:red">字段描述</span>
<span style="color:red">类型</span>
<span style="color:red">填</span>
<span style="color:red">35</span>
<span style="color:red">消息头</span>
<span style="color:red">MsgType=AE</span>
<span style="color:red">1180</span>
<span style="color:red">ApplID</span>
<span style="color:red">业务类型</span>
<span style="color:red">Y</span>
<span style="color:red">C6</span>
<span style="color:red">571</span>
<span style="color:red">TradeReportID</span>
<span style="color:red">会员内部编号</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">828</span>
<span style="color:red">TrdType</span>
<span style="color:red">业务子类型，见附表</span>
<span style="color:red">N</span>
<span style="color:red">C3</span>
<span style="color:red">成交申报类型</span>
<span style="color:red">0=Submit</span> <span style="color:red">，提交成交申报</span>
<span style="color:red">856</span>
<span style="color:red">TradeReportType</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">2=Accept</span> <span style="color:red">，确认成交申报</span>
<span style="color:red">3=Decline</span> <span style="color:red">，拒绝成交申报</span>
<span style="color:red">487</span>
<span style="color:red">TradeReportTransType</span>
<span style="color:red">成交申报事务类别</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
74

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">0=New</span> <span style="color:red">，新申报</span>
<span style="color:red">1=Cancel</span> <span style="color:red">，撤销申报</span>
<span style="color:red">2=Replace</span> <span style="color:red">，响应</span>
<span style="color:red">订单所有者类型</span>
<span style="color:red">1=</span> <span style="color:red">个人投资者</span>
<span style="color:red">522</span>
<span style="color:red">OwnerType</span>
<span style="color:red">Y</span>
<span style="color:red">N3</span>
<span style="color:red">103=</span> <span style="color:red">机构投资者</span>
<span style="color:red">104=</span> <span style="color:red">自营交易</span>
<span style="color:red">原始交易会员内部编号，表示被撤消订单的会员内</span>
<span style="color:red">572</span>
<span style="color:red">TradeReportRefID</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">部编号</span>
<span style="color:red">买卖方向：</span> <span style="color:red">1=</span> <span style="color:red">买，</span> <span style="color:red">2=</span> <span style="color:red">卖</span>
<span style="color:red">对于回购：</span> <span style="color:red">1=</span> <span style="color:red">正回购，</span> <span style="color:red">2=</span> <span style="color:red">逆回购</span>
<span style="color:red">54</span>
<span style="color:red">Side</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">对于借贷：</span> <span style="color:red">F=</span> <span style="color:red">出借，</span> <span style="color:red">G=</span> <span style="color:red">借入</span>
<span style="color:red">对于合并申报且</span> <span style="color:red">TradeReportType</span> <span style="color:red">为</span> <span style="color:red">0</span> <span style="color:red">时：填</span> <span style="color:red">0</span>
<span style="color:red">申报价格（元）或回购利率（</span> <span style="color:red">%</span> <span style="color:red">）或借贷费率（</span> <span style="color:red">%</span> <span style="color:red">）</span>
<span style="color:red">44</span>
<span style="color:red">Price</span>
<span style="color:red">N</span>
<span style="color:red">price</span>
<span style="color:red">合并申报时代表买入价格</span>
<span style="color:red">申报价格</span> <span style="color:red">2</span>
<span style="color:red">640</span>
<span style="color:red">Price2</span>
<span style="color:red">N</span>
<span style="color:red">price</span>
<span style="color:red">合并申报时代表卖出价格（元）</span>
<span style="color:red">455</span>
<span style="color:red">SecurityAltID</span>
<span style="color:red">辅助证券代码</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">8903</span>
<span style="color:red">DeliveryQty</span>
<span style="color:red">证券交付数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">8911</span>
<span style="color:red">ExpirationDays</span>
<span style="color:red">期限（天），可填</span> <span style="color:red">[1,365]</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">64</span>
<span style="color:red">SettlDate</span>
<span style="color:red">首次结算日</span>
<span style="color:red">N</span>
<span style="color:red">date</span>
<span style="color:red">541</span>
<span style="color:red">MaturityDate</span>
<span style="color:red">到期日</span>
<span style="color:red">N</span>
<span style="color:red">date</span>
<span style="color:red">193</span>
<span style="color:red">SettlDate2</span>
<span style="color:red">到期结算日</span>
<span style="color:red">N</span>
<span style="color:red">date</span>
<span style="color:red">915</span>
<span style="color:red">AgreementDate</span>
<span style="color:red">协议日期</span>
<span style="color:red">N</span>
<span style="color:red">date</span>
<span style="color:red">8847</span>
<span style="color:red">UAInterestAccrualDays</span>
<span style="color:red">实际占款天数，可填</span> <span style="color:red">[1,365]</span>
<span style="color:red">N</span>
<span style="color:red">N3</span>
<span style="color:red">60</span>
<span style="color:red">TransactTime</span>
<span style="color:red">业务发生时间</span>
<span style="color:red">Y</span>
<span style="color:red">ntime</span>
<span style="color:red">8504</span>
<span style="color:red">TotalValueTraded</span>
<span style="color:red">总成交金额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">累计利息总额，代表总回购利息或债券借贷标的券</span>
<span style="color:red">TotalAccruedInterestA</span>
<span style="color:red">540</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">应计利息总额</span>
<span style="color:red">mt</span>
<span style="color:red">10330</span>
<span style="color:red">TotalSettlCurrAmt</span>
<span style="color:red">总到期结算金额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
75

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">580</span>
<span style="color:red">NoDates</span>
<span style="color:red">违约宽限期（天），</span> <span style="color:red">[0,365]</span> <span style="color:red">。</span>
<span style="color:red">N</span>
<span style="color:red">N3</span>
<span style="color:red">订单限制</span>
<span style="color:red">对于协议回购表示</span> <span style="color:red">“</span> <span style="color:red">是否同意在违约情形下由质权</span>
<span style="color:red">方对该违约交易项下的质押券直接以拍卖、变卖等</span>
<span style="color:red">529</span>
<span style="color:red">OrderRestrictions</span>
<span style="color:red">方式进行处置</span> <span style="color:red">”</span> <span style="color:red">；对于三方回购表示</span> <span style="color:red">“</span> <span style="color:red">违约后担保品</span>
<span style="color:red">N</span>
<span style="color:red">Boolean</span>
<span style="color:red">是否由质权人处置</span> <span style="color:red">”</span> <span style="color:red">。</span>
<span style="color:red">Y =</span> <span style="color:red">是</span>
<span style="color:red">N =</span> <span style="color:red">否</span>
<span style="color:red">结算场所：</span> <span style="color:red">1=</span> <span style="color:red">中国结算，</span> <span style="color:red">2=</span> <span style="color:red">中央结算</span>
<span style="color:red">双边托管券，可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">2</span> <span style="color:red">，单边托管券只能填其实</span>
<span style="color:red">207</span>
<span style="color:red">SecurityExchange</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">际托管方。</span>
<span style="color:red">预留字段，暂不启用。</span>
<span style="color:red">结算周期：</span>
<span style="color:red">0 = T+0</span>
<span style="color:red">1 = T+1</span>
<span style="color:red">10216</span>
<span style="color:red">SettlPeriod</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">2 = T+2</span>
<span style="color:red">3 = T+3</span>
<span style="color:red">预留字段，暂不启用</span>
<span style="color:red">结算方式：</span> <span style="color:red">1=</span> <span style="color:red">净额结算，</span> <span style="color:red">2=RTGS</span> <span style="color:red">结算。</span>
<span style="color:red">63</span>
<span style="color:red">SettlType</span>
<span style="color:red">担保券可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">2</span> <span style="color:red">；非担保券只能为</span> <span style="color:red">2</span> <span style="color:red">。特别地，</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">对于公募可转债或公募</span> <span style="color:red">REITs</span> <span style="color:red">，只能填</span> <span style="color:red">1</span> <span style="color:red">。</span>
<span style="color:red">146</span>
<span style="color:red">NoRelatedSym</span>
<span style="color:red">合约结算个数</span>
<span style="color:red">N</span>
<span style="color:red">N1</span>
<span style="color:red">合约相关编号</span>
<span style="color:red">1=</span> <span style="color:red">代表当前合约，债券借贷代表当前合约或到期续</span>
<span style="color:red">→</span>
<span style="color:red">655</span>
<span style="color:red">ContraLegRefID</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">做时的原合约</span>
<span style="color:red">2=</span> <span style="color:red">代表新合约，债券借贷代表到期续做时的新合约</span>
<span style="color:red">结算形式</span>
<span style="color:red">0 =</span> <span style="color:red">现金，债券借贷代表现金结算</span>
<span style="color:red">→</span>
<span style="color:red">668</span>
<span style="color:red">DeliveryForm</span>
<span style="color:red">N</span>
<span style="color:red">C3</span>
<span style="color:red">2 =</span> <span style="color:red">实物，债券借贷代表债券结算</span>
<span style="color:red">101 =</span> <span style="color:red">其他，债券借贷代表部分现金结算</span>
<span style="color:red">→</span>
<span style="color:red">172</span>
<span style="color:red">SettlDeliveryType</span>
<span style="color:red">资金结算方式</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
76

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">1 =</span> <span style="color:red">场内结算</span>
<span style="color:red">2 =</span> <span style="color:red">场外结算</span>
<span style="color:red">→</span>
<span style="color:red">510</span>
<span style="color:red">NoDistribInsts</span>
<span style="color:red">交收账户重复组个数</span>
<span style="color:red">N</span>
<span style="color:red">N1</span>
<span style="color:red">F=</span> <span style="color:red">出借方</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">624</span>
<span style="color:red">LegSide</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">G=</span> <span style="color:red">借入方</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">498</span>
<span style="color:red">CashDistribAgentName</span>
<span style="color:red">资金交收机构名称，债券借贷代表资金开户行</span>
<span style="color:red">N</span>
<span style="color:red">C75</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">499</span>
<span style="color:red">CashDistribAgentCode</span>
<span style="color:red">资金交收机构代码，债券借贷代表支付系统行号</span>
<span style="color:red">N</span>
<span style="color:red">C18</span>
<span style="color:red">CashDistribAgentAcctN</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">500</span>
<span style="color:red">资金账户</span>
<span style="color:red">N</span>
<span style="color:red">C22</span>
<span style="color:red">umber</span>
<span style="color:red">CashDistribAgentAcctN</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">502</span>
<span style="color:red">资金账户名称</span>
<span style="color:red">N</span>
<span style="color:red">C87</span>
<span style="color:red">ame</span>
<span style="color:red">左起顺序代表第</span> <span style="color:red">1</span> <span style="color:red">号至第</span> <span style="color:red">N</span> <span style="color:red">号篮子。例如指定</span> <span style="color:red">1</span> <span style="color:red">，</span> <span style="color:red">2</span> <span style="color:red">，</span>
<span style="color:red">10194</span>
<span style="color:red">BasketID</span>
<span style="color:red">N</span>
<span style="color:red">C16</span>
<span style="color:red">5</span> <span style="color:red">号篮子，填</span> <span style="color:red">“1100100000000000”</span>
<span style="color:red">711</span>
<span style="color:red">NoUnderlyings</span>
<span style="color:red">证券个数</span>
<span style="color:red">N</span>
<span style="color:red">N2</span>
<span style="color:red">操作标识</span>
<span style="color:red">→</span>
<span style="color:red">865</span>
<span style="color:red">EventType</span>
<span style="color:red">21=</span> <span style="color:red">换入</span> <span style="color:red">/</span> <span style="color:red">补入券</span>
<span style="color:red">N</span>
<span style="color:red">C2</span>
<span style="color:red">22=</span> <span style="color:red">换出券</span>
<span style="color:red">→</span>
<span style="color:red">48</span>
<span style="color:red">SecurityID</span>
<span style="color:red">证券代码</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">→</span>
<span style="color:red">38</span>
<span style="color:red">OrderQty</span>
<span style="color:red">证券数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">份额类型</span>
<span style="color:red">→</span>
<span style="color:red">10331</span>
<span style="color:red">ShareProperty</span>
<span style="color:red">0 =</span> <span style="color:red">限售</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">1 =</span> <span style="color:red">非限售</span>
<span style="color:red">限售期（月），指初始登记限售期，可选：</span>
<span style="color:red">→</span>
<span style="color:red">10332</span>
<span style="color:red">RestrictedMonth</span>
<span style="color:red">N</span>
<span style="color:red">CN4</span>
<span style="color:red">0006</span> <span style="color:red">、</span> <span style="color:red">0012</span> <span style="color:red">、</span> <span style="color:red">0018</span> <span style="color:red">、</span> <span style="color:red">0024</span> <span style="color:red">。</span>
<span style="color:red">→</span>
<span style="color:red">231</span>
<span style="color:red">ContractMultiplier</span>
<span style="color:red">折算比例（</span> <span style="color:red">%</span> <span style="color:red">）</span>
<span style="color:red">N</span>
<span style="color:red">N6(2)</span>
<span style="color:red">→</span>
<span style="color:red">152</span>
<span style="color:red">CashOrderQty</span>
<span style="color:red">质押券面值总额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">→</span>
<span style="color:red">381</span>
<span style="color:red">GrossTradeAmt</span>
<span style="color:red">成交金额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">→</span>
<span style="color:red">159</span>
<span style="color:red">AccruedInterestAmt</span>
<span style="color:red">回购利息</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">→</span>
<span style="color:red">119</span>
<span style="color:red">SettlCurrAmt</span>
<span style="color:red">到期结算金额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">→</span>
<span style="color:red">880</span>
<span style="color:red">TrdMatchID</span>
<span style="color:red">辅助交易编号</span>
<span style="color:red">N</span>
<span style="color:red">C18</span>
77

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">债券借贷填写质押券冻结申请书号</span>
<span style="color:red">192</span>
<span style="color:red">OrderQty2</span>
<span style="color:red">本期回购结算利息</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">到期续做类型</span>
<span style="color:red">829</span>
<span style="color:red">TrdSubType</span>
<span style="color:red">N =</span> <span style="color:red">非第三方续做（原对手方）</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">Y =</span> <span style="color:red">第三方续做（新对手方）</span>
<span style="color:red">1125</span>
<span style="color:red">OrigTradeDate</span>
<span style="color:red">原成交日期，</span> <span style="color:red">YYYYMMDD</span>
<span style="color:red">N</span>
<span style="color:red">date</span>
<span style="color:red">当</span> <span style="color:red">TradeReportType</span> <span style="color:red">为</span> <span style="color:red">0</span> <span style="color:red">时，如为非首期合约，表</span>
<span style="color:red">示原合约成交编号；</span>
<span style="color:red">19</span>
<span style="color:red">ExecRefID</span>
<span style="color:red">N</span>
<span style="color:red">C16</span>
<span style="color:red">当</span> <span style="color:red">TradeReportType</span> <span style="color:red">为</span> <span style="color:red">2</span> <span style="color:red">或</span> <span style="color:red">3</span> <span style="color:red">时，表示待确认（拒</span>
<span style="color:red">绝）的申报的交易所订单编号。</span>
<span style="color:red">10248</span>
<span style="color:red">MemoEx</span>
<span style="color:red">扩展备注，支持中文</span>
<span style="color:red">N</span>
<span style="color:red">C96</span>
<span style="color:red">58</span>
<span style="color:red">Text</span>
<span style="color:red">用户私有信息</span>
<span style="color:red">N</span>
<span style="color:red">C32</span>
<span style="color:red">发起方重复组，依次包含发起方交易员一债通账</span>
<span style="color:red">户、业务单元、营业部代码、投资者账户、账户名</span>
<span style="color:red">453</span>
<span style="color:red">NoPartyIDs</span>
<span style="color:red">Y</span>
<span style="color:red">N2</span>
<span style="color:red">称、对手方交易员一债通账户</span> <span style="color:red">1</span> <span style="color:red">、对手方交易员一</span>
<span style="color:red">债通账户</span> <span style="color:red">2</span> <span style="color:red">。取值为</span> <span style="color:red">67</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方交易员一债通账户</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">员一债通账户</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方业务交易单元代码</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">1</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方业务交易</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">单元号。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方营业部代码</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">4001</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的营业</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">部代码。</span>
<span style="color:red">发起方投资者帐户，</span> <span style="color:red">TradeReportType</span> <span style="color:red">为</span> <span style="color:red">0</span> <span style="color:red">或</span> <span style="color:red">2</span> <span style="color:red">时</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">N</span>
<span style="color:red">C13</span>
<span style="color:red">必填。</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">5</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方投资者帐</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">户</span>
<span style="color:red">→</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方投资者账户名称。仅对债券借贷、协议回购</span>
<span style="color:red">N</span>
<span style="color:red">C120</span>
78

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">和三方回购有效，协商成交、到期续做申报发起时</span>
<span style="color:red">为发起方投资者账户名称，确认时</span>
<span style="color:red">（</span> <span style="color:red">TradeReportType=2</span> <span style="color:red">）填写方证券账户名称。其他</span>
<span style="color:red">申报无意义。</span>
<span style="color:red">取</span> <span style="color:red">38</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方投资者账</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">户名称</span>
<span style="color:red">对手方交易员一债通账户</span> <span style="color:red">1</span> <span style="color:red">，当合并申报时表示买</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">方交易员一债通账户</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">102</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为对手方的交易</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">员一债通账户</span>
<span style="color:red">对手方交易员一债通账户</span> <span style="color:red">2</span> <span style="color:red">，仅合并申报时有效表</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">示卖方交易员。其他申报无意义。</span>
<span style="color:red">→</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">57</span> <span style="color:red">，表示当前的</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为合并申报卖方</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">约定号，</span> <span style="color:red">TradeReportType=0</span> <span style="color:red">时可以填写，用于对</span>
<span style="color:red">手方定位订单信息。仅可填大小写英文字母或数</span>
<span style="color:red">664</span>
<span style="color:red">ConfirmID</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">字。</span>
<span style="color:red">10198</span>
<span style="color:red">Memo</span>
<span style="color:red">备注，可填写补充约定或补充条款，支持中文</span>
<span style="color:red">N</span>
<span style="color:red">C600</span>
<span style="color:red">说明：</span>
<span style="color:red">1</span> <span style="color:red">、业务申报填写说明</span>
<span style="color:red">ApplID</span>
<span style="color:red">TrdType</span>
<span style="color:red">描述</span>
<span style="color:red">填写说明</span>
79

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">ApplID</span>
<span style="color:red">TrdType</span>
<span style="color:red">描述</span>
<span style="color:red">填写说明</span>
<span style="color:red">131</span>
<span style="color:red">协商成交</span>
<span style="color:red">1.</span> <span style="color:red">Price</span> <span style="color:red">必填，表示回购利率；</span> <span style="color:red">ExpirationDays</span> <span style="color:red">必填，表示回购期限；</span>
<span style="color:red">SettlDate</span> <span style="color:red">必填，填当前交易日</span>
<span style="color:red">2.</span> <span style="color:red">MaturityDate</span> <span style="color:red">、</span> <span style="color:red">SettlDate2</span> <span style="color:red">和</span> <span style="color:red">UAInterestAccrualDays</span> <span style="color:red">必填，其中回</span>
<span style="color:red">购到期日</span> <span style="color:red">=</span> <span style="color:red">当前交易日</span> <span style="color:red">+</span> <span style="color:red">回购期限；到期结算日</span> <span style="color:red">=</span> <span style="color:red">首次结算日</span> <span style="color:red">+</span> <span style="color:red">实际占</span>
<span style="color:red">款天数</span>
<span style="color:red">3.</span> <span style="color:red">NoDates</span> <span style="color:red">、</span> <span style="color:red">OrderRestrictions</span> <span style="color:red">、投资者账户名称必填</span>
<span style="color:red">4.</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">必填，可填</span> <span style="color:red">[1,10]</span> <span style="color:red">，</span> <span style="color:red">SecurityID/OrderQty</span> <span style="color:red">填写对应</span>
<span style="color:red">质押券代码和数量；如质押券为公募</span> <span style="color:red">REITs</span> <span style="color:red">，需要填写</span>
<span style="color:red">ShareProperty</span> <span style="color:red">，如为公募</span> <span style="color:red">REITs</span> <span style="color:red">限售份额，需填写</span> <span style="color:red">RestrictedMonth</span> <span style="color:red">，</span>
<span style="color:red">指初始登记或扩募登记时中国结算提供的“挂牌年份”字段。批量</span>
<span style="color:red">申报时</span> <span style="color:red">N</span> <span style="color:red">支质押券将收到</span> <span style="color:red">N</span> <span style="color:red">笔响应，允许部分成功，</span> <span style="color:red">N</span> <span style="color:red">笔申报将分</span>
<span style="color:red">别转发至对手方逐一确认，确认后将生成</span> <span style="color:red">N</span> <span style="color:red">笔成交，确认一笔，成</span>
<span style="color:red">交一笔。批量申报时各支质押券不可重复。</span>
<span style="color:red">5.</span> <span style="color:red">ContractMultiplier</span> <span style="color:red">（折算比例）、</span> <span style="color:red">CashOrderQty</span> <span style="color:red">（面值总额）、</span>
<span style="color:red">GrossTradeAmt</span> <span style="color:red">（成交金额）、</span> <span style="color:red">AccruedInterestAmt</span> <span style="color:red">（回购利息）和</span>
<span style="color:red">SettlCurrAmt</span> <span style="color:red">（到期结算金额）必填，均为正数，保留两位小数，四</span>
<span style="color:red">舍五入，其中：</span>
<span style="color:red">协议回购</span>
<span style="color:red">（</span> <span style="color:red">600130</span> <span style="color:red">）</span>
<span style="color:red">债券面值总额</span> <span style="color:red">=</span> <span style="color:red">质押券数量</span> <span style="color:red">×10×</span> <span style="color:red">单张质押券面值</span>
<span style="color:red">基金或</span> <span style="color:red">REITs</span> <span style="color:red">面值总额</span> <span style="color:red">=</span> <span style="color:red">质押券数量</span> <span style="color:red">*</span> <span style="color:red">前收盘价</span>
<span style="color:red">成交金额</span> <span style="color:red">=</span> <span style="color:red">面值总额</span> <span style="color:red">×</span> <span style="color:red">折算比例</span> <span style="color:red">/100</span>
<span style="color:red">回购利息</span> <span style="color:red">=</span> <span style="color:red">成交金额</span> <span style="color:red">×</span> <span style="color:red">回购利率</span> <span style="color:red">/100×</span> <span style="color:red">实际占款天数</span> <span style="color:red">/365</span>
<span style="color:red">到期结算金额</span> <span style="color:red">=</span> <span style="color:red">成交金额</span> <span style="color:red">+</span> <span style="color:red">回购利息</span>
<span style="color:red">132</span>
<span style="color:red">到期确认</span>
<span style="color:red">1.</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">，</span> <span style="color:red">SecurityID/OrderQty</span> <span style="color:red">填写对应质押券代码和</span>
<span style="color:red">数量</span>
<span style="color:red">2.</span> <span style="color:red">OrigTradeDate</span> <span style="color:red">、</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填</span>
<span style="color:red">3.</span> <span style="color:red">Text</span> <span style="color:red">、</span> <span style="color:red">Memo</span> <span style="color:red">选填</span>
<span style="color:red">133</span>
到期续做 <span style="color:red">*</span>
<span style="color:red">1.</span> <span style="color:red">Price</span> <span style="color:red">必填，表示新回购利率；</span> <span style="color:red">ExpirationDays</span> <span style="color:red">必填，表示新回购</span>
<span style="color:red">期限；</span> <span style="color:red">SettlDate</span> <span style="color:red">必填，填当前交易日</span>
<span style="color:red">2.</span> <span style="color:red">MaturityDate</span> <span style="color:red">、</span> <span style="color:red">SettlDate2</span> <span style="color:red">和</span> <span style="color:red">UAInterestAccrualDays</span> <span style="color:red">必填，其中新</span>
<span style="color:red">回购到期日</span> <span style="color:red">=</span> <span style="color:red">当前交易日</span> <span style="color:red">+</span> <span style="color:red">新回购期限；新到期结算日</span> <span style="color:red">=</span> <span style="color:red">首次结算日</span> <span style="color:red">+</span>
<span style="color:red">新实际占款天数</span>
<span style="color:red">3.</span> <span style="color:red">NoDates</span> <span style="color:red">、</span> <span style="color:red">OrderRestrictions</span> <span style="color:red">、</span> <span style="color:red">OrderQty2</span> <span style="color:red">（精确到小数点后两位）、</span>
<span style="color:red">TrdSubType</span> <span style="color:red">必填</span>
<span style="color:red">4.</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">，</span> <span style="color:red">SecurityID/OrderQty</span> <span style="color:red">表示对应质押券代码和</span>
<span style="color:red">数量；如质押券为公募</span> <span style="color:red">REITs</span> <span style="color:red">，</span> <span style="color:red">ShareProperty</span> <span style="color:red">必填，若为公募</span> <span style="color:red">REITs</span>
<span style="color:red">限售份额，</span> <span style="color:red">RestrictedMonth</span> <span style="color:red">必填</span>
<span style="color:red">5.</span> <span style="color:red">ContractMultiplier</span> <span style="color:red">、</span> <span style="color:red">CashOrderQty</span> <span style="color:red">、</span> <span style="color:red">GrossTradeAmt</span> <span style="color:red">、</span>
<span style="color:red">AccruedInterestAmt</span> <span style="color:red">和</span> <span style="color:red">SettlCurrAmt</span> <span style="color:red">必填，表示新合约相关参数，计</span>
<span style="color:red">算方式同协商成交申报</span>
<span style="color:red">6.</span> <span style="color:red">OrigTradeDate</span> <span style="color:red">、</span> <span style="color:red">ExecRefID</span> <span style="color:red">、投资者账户名称必填，</span> <span style="color:red">Text</span> <span style="color:red">、</span>
<span style="color:red">C</span>
<span style="color:red">fi</span>
<span style="color:red">ID</span>
<span style="color:red">M</span>
<span style="color:red">选填</span>
80

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">ApplID</span>
<span style="color:red">TrdType</span>
<span style="color:red">描述</span>
<span style="color:red">填写说明</span>
<span style="color:red">1.</span> <span style="color:red">Price</span> <span style="color:red">必填，表示实际回购利率</span> ， <span style="color:red">ExpirationDays</span> <span style="color:red">、</span>
<span style="color:red">UAInterestAccrualDays</span> <span style="color:red">、</span> <span style="color:red">AccruedInterestAmt</span> <span style="color:red">和</span> <span style="color:red">SettlCurrAmt</span> <span style="color:red">必填，</span>
<span style="color:red">表示提前终止后的相应值</span>
<span style="color:red">134</span>
<span style="color:red">提前终止</span>
<span style="color:red">2.</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">，</span> <span style="color:red">SecurityID/OrderQty</span> <span style="color:red">表示对应质押券代码和</span>
<span style="color:red">数量</span>
<span style="color:red">3.</span> <span style="color:red">OrigTradeDate</span> <span style="color:red">、</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填</span> ， <span style="color:red">Text</span> <span style="color:red">、</span> <span style="color:red">ConfirmID</span> <span style="color:red">、</span> <span style="color:red">Memo</span> <span style="color:red">选填</span>
<span style="color:red">1.</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">填</span> <span style="color:red">2</span> <span style="color:red">，</span> <span style="color:red">EventType</span> <span style="color:red">必填</span>
<span style="color:red">2.</span> <span style="color:red">EventType</span> <span style="color:red">为</span> <span style="color:red">21</span> <span style="color:red">时，</span> <span style="color:red">SecurityID/OrderQty</span> <span style="color:red">填换入券代码和数量，</span>
<span style="color:red">如换入券为公募</span> <span style="color:red">REITs</span> <span style="color:red">，需要填写</span> <span style="color:red">ShareProperty</span> <span style="color:red">（仅可填</span> <span style="color:red">1</span> <span style="color:red">），</span>
<span style="color:red">135</span>
<span style="color:red">换券申报</span>
<span style="color:red">ContractMultiplier</span> <span style="color:red">（折算比例）、</span> <span style="color:red">CashOrderQty</span> <span style="color:red">（面值总额）、</span>
<span style="color:red">GrossTradeAmt</span> <span style="color:red">（成交金额）必填，换入券的成交金额应当与换出券</span>
<span style="color:red">相等；</span> <span style="color:red">EventType</span> <span style="color:red">为</span> <span style="color:red">22</span> <span style="color:red">时，</span> <span style="color:red">SecurityID</span> <span style="color:red">必填，表示被换出券。</span>
<span style="color:red">3.</span> <span style="color:red">OrigTradeDate</span> <span style="color:red">、</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填</span> ， <span style="color:red">Text</span> <span style="color:red">、</span> <span style="color:red">ConfirmID</span> <span style="color:red">、</span> <span style="color:red">Memo</span> <span style="color:red">选填</span>
<span style="color:red">136</span>
<span style="color:red">解除质押</span>
<span style="color:red">1.</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">，</span> <span style="color:red">SecurityID/OrderQty</span> <span style="color:red">表示对应质押券代码和</span>
<span style="color:red">数量</span>
<span style="color:red">2.</span> <span style="color:red">OrigTradeDate</span> <span style="color:red">、</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填</span> ， <span style="color:red">Text</span> <span style="color:red">、</span> <span style="color:red">ConfirmID</span> <span style="color:red">、</span> <span style="color:red">Memo</span> <span style="color:red">选填</span>
<span style="color:red">不适用</span>
<span style="color:red">到期续做</span>
<span style="color:red">前期合约</span>
<span style="color:red">137</span>
<span style="color:red">了结</span>
<span style="color:red">138</span>
<span style="color:red">到期续做</span>
<span style="color:red">合约新开</span>
<span style="color:red">不适用</span>
<span style="color:red">141</span>
<span style="color:red">协商成交</span>
<span style="color:red">三方回购</span>
<span style="color:red">（</span> <span style="color:red">600140</span> <span style="color:red">）</span>
<span style="color:red">1.</span> <span style="color:red">Price</span> <span style="color:red">必填，表示回购利率；</span> <span style="color:red">ExpirationDays</span> <span style="color:red">必填，表示回购期限；</span>
<span style="color:red">SettlDate</span> <span style="color:red">必填，填当前交易日</span>
<span style="color:red">2.</span> <span style="color:red">TotalValueTraded</span> <span style="color:red">、</span> <span style="color:red">MaturityDate</span> <span style="color:red">、</span> <span style="color:red">SettlDate2</span> <span style="color:red">和</span>
<span style="color:red">UAInterestAccrualDays</span> <span style="color:red">必填，其中回购到期日</span> <span style="color:red">=</span> <span style="color:red">当前交易日</span> <span style="color:red">+</span> <span style="color:red">回购期</span>
<span style="color:red">限；到期结算日</span> <span style="color:red">=</span> <span style="color:red">首次结算日</span> <span style="color:red">+</span> <span style="color:red">实际占款天数</span>
<span style="color:red">4.</span> <span style="color:red">OrderRestrictions</span> <span style="color:red">、</span> <span style="color:red">BasketID</span> <span style="color:red">、投资者账户名称必填</span>
<span style="color:red">3.</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">选填，可填</span> <span style="color:red">[1,3]</span> <span style="color:red">，</span> <span style="color:red">SecurityID/OrderQty</span> <span style="color:red">填写对应质</span>
<span style="color:red">押券代码和数量，质押券应当属于已选择的篮子</span>
<span style="color:red">4.</span> <span style="color:red">TotalAccruedInterestAmt</span> <span style="color:red">（回购利息）和</span> <span style="color:red">TotalSettlCurrAmt</span> <span style="color:red">（到期</span>
<span style="color:red">结算金额）必填，均为正数，保留两位小数，四舍五入，其中：</span>
<span style="color:red">回购利息</span> <span style="color:red">=</span> <span style="color:red">成交金额</span> <span style="color:red">×</span> <span style="color:red">回购利率</span> <span style="color:red">/100×</span> <span style="color:red">实际占款天数</span> <span style="color:red">/365</span>
<span style="color:red">到期结算金额</span> <span style="color:red">=</span> <span style="color:red">成交金额</span> <span style="color:red">+</span> <span style="color:red">回购利息</span>
5. <span style="color:red">发起方投资者账户必填，填三方回购专用账户；对手方接受时填</span>
<span style="color:red">写普通账户</span>
<span style="color:red">6.</span> <span style="color:red">Text</span> <span style="color:red">、</span> <span style="color:red">ConfirmID</span> <span style="color:red">、</span> <span style="color:red">Memo</span> <span style="color:red">选填</span>
<span style="color:red">142</span>
<span style="color:red">到期购回</span>
<span style="color:red">1.</span> <span style="color:red">OrigTradeDate</span> <span style="color:red">、</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填</span>
<span style="color:red">2.</span> <span style="color:red">Text</span> <span style="color:red">选填</span>
81

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">ApplID</span>
<span style="color:red">TrdType</span>
<span style="color:red">描述</span>
<span style="color:red">填写说明</span>
<span style="color:red">143</span>
到期续做
<span style="color:red">1.</span> <span style="color:red">Price</span> <span style="color:red">必填，表示新回购利率；</span> <span style="color:red">ExpirationDays</span> <span style="color:red">必填，表示新回购</span>
<span style="color:red">期限；</span> <span style="color:red">SettlDate</span> <span style="color:red">必填，填当前交易日</span>
<span style="color:red">2.</span> <span style="color:red">MaturityDate</span> <span style="color:red">、</span> <span style="color:red">SettlDate2</span> <span style="color:red">和</span> <span style="color:red">UAInterestAccrualDays</span> <span style="color:red">必填，其中新</span>
<span style="color:red">回购到期日</span> <span style="color:red">=</span> <span style="color:red">当前交易日</span> <span style="color:red">+</span> <span style="color:red">新回购期限；新到期结算日</span> <span style="color:red">=</span> <span style="color:red">首次结算日</span> <span style="color:red">+</span>
<span style="color:red">新实际占款天数</span>
<span style="color:red">3.</span> <span style="color:red">BasketID</span> <span style="color:red">、</span> <span style="color:red">OrigTradeDate</span> <span style="color:red">、</span> <span style="color:red">ExecRefID</span> <span style="color:red">、投资者账户名称、</span>
<span style="color:red">OrderRestrictions</span> <span style="color:red">必填，</span> <span style="color:red">TotalAccruedInterestAmt</span> <span style="color:red">（回购利息）和</span>
<span style="color:red">TotalSettlCurrAmt</span> <span style="color:red">（到期结算金额）必填，表示新合约相关参数，</span>
<span style="color:red">计算方式同协商成交申报</span>
<span style="color:red">4.</span> <span style="color:red">发起方投资者账户必填，填三方回购专用账户，对手方接受时填</span>
<span style="color:red">写普通账户</span>
<span style="color:red">1.</span> <span style="color:red">Price</span> <span style="color:red">必填，表示实际回购利率</span>
<span style="color:red">2.</span> <span style="color:red">ExpirationDays</span> <span style="color:red">、</span> <span style="color:red">UAInterestAccrualDays</span> <span style="color:red">、</span>
<span style="color:red">144</span>
<span style="color:red">提前终止</span>
<span style="color:red">TotalAccruedInterestAmtAccruedInterestAmt</span> <span style="color:red">和</span>
<span style="color:red">TotalSettlCurrAmtSettlCurrAmt</span> <span style="color:red">必填，表示提前终止后的相应值</span>
<span style="color:red">3.</span> <span style="color:red">OrigTradeDate</span> <span style="color:red">、</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填</span> ， <span style="color:red">Text</span> <span style="color:red">、</span> <span style="color:red">ConfirmID</span> <span style="color:red">、</span> <span style="color:red">Memo</span> <span style="color:red">选填</span>
<span style="color:red">1.</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">2</span> <span style="color:red">，填</span> <span style="color:red">1</span> <span style="color:red">时表示仅换出；</span> <span style="color:red">EventType</span> <span style="color:red">必填，</span>
<span style="color:red">145</span>
<span style="color:red">换券申报</span>
<span style="color:red">SecurityID/OrderQty</span> <span style="color:red">填对应换入或换出券代码和数量；换入券和换</span>
<span style="color:red">出券应当属于同一个篮子。</span>
<span style="color:red">2.</span> <span style="color:red">OrigTradeDate</span> <span style="color:red">、</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填</span> ， <span style="color:red">Text</span> <span style="color:red">、</span> <span style="color:red">ConfirmID</span> <span style="color:red">选填</span>
<span style="color:red">146</span>
<span style="color:red">解除质押</span>
<span style="color:red">1.</span> <span style="color:red">OrigTradeDate</span> <span style="color:red">、</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填</span>
<span style="color:red">2.</span> <span style="color:red">Text</span> <span style="color:red">、</span> <span style="color:red">ConfirmID</span> <span style="color:red">、</span> <span style="color:red">Memo</span> <span style="color:red">选填</span>
<span style="color:red">147</span>
<span style="color:red">补券申报</span>
<span style="color:red">1.</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">，</span> <span style="color:red">SecurityID/OrderQty</span> <span style="color:red">填对应补入券代码和数</span>
<span style="color:red">量</span>
<span style="color:red">2.</span> <span style="color:red">OrigTradeDate</span> <span style="color:red">、</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填，</span> <span style="color:red">Text</span> <span style="color:red">选填</span>
<span style="color:red">1.Price</span> <span style="color:red">必填，表示申报价格；</span> <span style="color:red">SettlType</span> <span style="color:red">、</span> <span style="color:red">ConfirmID</span> <span style="color:red">必填</span>
<span style="color:red">2.NoUnderlyings</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">，</span> <span style="color:red">SecurityID/OrderQty</span> <span style="color:red">填写交易券代码和数量</span>
<span style="color:red">成交</span>
<span style="color:red">现券协商成</span>
<span style="color:red">交（</span> <span style="color:red">600210</span> <span style="color:red">）</span>
<span style="color:red">不适用</span>
<span style="color:red">现券协商</span>
<span style="color:red">3.Text</span> <span style="color:red">、</span> <span style="color:red">Memo</span> <span style="color:red">选填</span>
<span style="color:red">合并申报</span> <span style="color:red">*</span>
<span style="color:red">（</span> <span style="color:red">600220</span> <span style="color:red">）</span>
<span style="color:red">不适用</span>
<span style="color:red">合并申报</span>
<span style="color:red">1.</span> <span style="color:red">Price</span> <span style="color:red">、</span> <span style="color:red">Price2</span> <span style="color:red">必填，分别表示买入价格和卖出价格</span>
<span style="color:red">2.</span> <span style="color:red">SettlType</span> <span style="color:red">必填，</span> <span style="color:red">Side</span> <span style="color:red">填</span> <span style="color:red">0</span>
<span style="color:red">3.</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">，</span> <span style="color:red">SecurityID/OrderQty</span> <span style="color:red">填写交易券代码和数量</span>
<span style="color:red">4.</span> <span style="color:red">对手方交易员一债通账户</span> <span style="color:red">2</span> <span style="color:red">和投资者账户必填</span> ， <span style="color:red">Text</span> <span style="color:red">选填</span>
<span style="color:red">债券借贷</span>
<span style="color:red">（</span> <span style="color:red">600300</span> <span style="color:red">）</span>
<span style="color:red">301</span>
<span style="color:red">协商成交</span>
<span style="color:red">1.</span> <span style="color:red">Price</span> <span style="color:red">必填，表示借贷费率</span>
<span style="color:red">2.</span> <span style="color:red">ExpirationDays</span> <span style="color:red">、</span> <span style="color:red">SettlDate</span> <span style="color:red">、</span> <span style="color:red">SettlDate2</span> <span style="color:red">必填，其中</span> <span style="color:red">ExpirationDays</span>
<span style="color:red">表示借贷期限，</span> <span style="color:red">SettlDate</span> <span style="color:red">填当前交易日，到期结算日</span> <span style="color:red">=</span> <span style="color:red">首次结算日</span> <span style="color:red">+</span>
<span style="color:red">借贷期限</span>
<span style="color:red">3.</span> <span style="color:red">NoRelatedSym</span> <span style="color:red">、</span> <span style="color:red">NoDistribInsts</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">，发起方资金账户、资金账户</span>
<span style="color:red">名称必填，资金开户行和支付系统行号选填</span>
<span style="color:red">4.</span> <span style="color:red">SecurityAltID/DeliveryQty</span> <span style="color:red">必填，表示标的券代码</span> <span style="color:red">/</span> <span style="color:red">数量</span>
82

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">ApplID</span>
<span style="color:red">TrdType</span>
<span style="color:red">描述</span>
<span style="color:red">填写说明</span>
<span style="color:red">5.</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">选填，可填</span> <span style="color:red">[1,20]</span> <span style="color:red">，</span> <span style="color:red">SecurityID/OrderQty</span> <span style="color:red">填写对应</span>
<span style="color:red">质押券代码和数量</span>
<span style="color:red">6.</span> <span style="color:red">TotalAccruedInterestAmt</span> <span style="color:red">必填，表示标的券应计利息总额</span>
<span style="color:red">7.</span> <span style="color:red">AgreementDate</span> <span style="color:red">必填，表示标的券下一付息日</span>
<span style="color:red">8.</span> <span style="color:red">SettlDeliveryType</span> <span style="color:red">必填，表示到期费用结算方式</span>
<span style="color:red">9.</span> <span style="color:red">TotalValueTraded</span> <span style="color:red">必填，表示借贷费用金额</span>
<span style="color:red">10.</span> <span style="color:red">MemoEx</span> <span style="color:red">选填，填写争议解决方式</span>
<span style="color:red">11.</span> <span style="color:red">Memo</span> <span style="color:red">选填，可填入补充约定内容</span>
<span style="color:red">302</span>
<span style="color:red">到期结算</span>
<span style="color:red">1.</span> <span style="color:red">SettlDeliveryType</span> <span style="color:red">必填</span>
<span style="color:red">2.</span> <span style="color:red">DeliveryForm</span> <span style="color:red">必填，表示到期结算方式</span>
<span style="color:red">3.</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填</span>
<span style="color:red">4.</span> <span style="color:red">SettlDeliveryType</span> <span style="color:red">必填，</span> <span style="color:red">SettlDeliveryType=2</span> <span style="color:red">时，资金账户、资</span>
<span style="color:red">金账户名称、资金开户行、支付系统行号必填</span>
<span style="color:red">5.</span> <span style="color:red">TotalSettlCurrAmt</span> <span style="color:red">选填，当</span> <span style="color:red">DeliveryForm =2</span> <span style="color:red">或</span> <span style="color:red">101</span> <span style="color:red">时必填，表</span>
<span style="color:red">示现金结算金额</span>
<span style="color:red">6.</span> <span style="color:red">DeliveryQty</span> <span style="color:red">选填，当</span> <span style="color:red">DeliveryForm =1</span> <span style="color:red">或</span> <span style="color:red">101</span> <span style="color:red">时必填，表示归还</span>
<span style="color:red">标的券数量</span>
<span style="color:red">303</span>
<span style="color:red">到期续做</span>
<span style="color:red">1.</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填</span>
<span style="color:red">2.</span> <span style="color:red">Price</span> <span style="color:red">必填，表示新借贷费率</span>
<span style="color:red">3.</span> <span style="color:red">ExpirationDays</span> <span style="color:red">、</span> <span style="color:red">SettlDate</span> <span style="color:red">、</span> <span style="color:red">SettlDate2</span> <span style="color:red">必填，其中</span> <span style="color:red">ExpirationDays</span>
<span style="color:red">表示新借贷期限，</span> <span style="color:red">SettlDate</span> <span style="color:red">填当前交易日，新到期结算日</span> <span style="color:red">=</span> <span style="color:red">当前交</span>
<span style="color:red">易日</span> <span style="color:red">+</span> <span style="color:red">新借贷期限</span>
<span style="color:red">4.</span> <span style="color:red">投资者账户、资金账户、资金账户名称必填</span>
<span style="color:red">5.</span> <span style="color:red">NoRelatedSym</span> <span style="color:red">填</span> <span style="color:red">2</span> <span style="color:red">，</span> <span style="color:red">ContraLegRefID</span> <span style="color:red">分别填</span> <span style="color:red">1</span> <span style="color:red">和</span> <span style="color:red">2</span> <span style="color:red">，</span> <span style="color:red">NoDistribInsts</span>
<span style="color:red">填</span> <span style="color:red">1</span>
<span style="color:red">6.</span> <span style="color:red">发起方资金账户、资金账户名称、资金开户行和支付系统行号选</span>
<span style="color:red">填，</span> <span style="color:red">SettlDeliveryType</span> <span style="color:red">为</span> <span style="color:red">2</span> <span style="color:red">时，发起方资金账户、资金账户名称、</span>
<span style="color:red">资金开户行和支付系统行号必填</span>
<span style="color:red">7.</span> <span style="color:red">SecurityAltID/DeliveryQty</span> <span style="color:red">填写新合约标的券代码、数量</span>
<span style="color:red">8.</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">选填，可填</span> <span style="color:red">[1,20]</span> <span style="color:red">，</span> <span style="color:red">SecurityID/OrderQty</span> <span style="color:red">填写变更</span>
<span style="color:red">的质押券代码和数量，</span> <span style="color:red">EventType</span> <span style="color:red">填写变更类型，</span> <span style="color:red">EventType=22</span> <span style="color:red">时</span>
<span style="color:red">TrdMatchID</span> <span style="color:red">必填，表示质押券的冻结申请书号</span>
<span style="color:red">9.</span> <span style="color:red">TotalAccruedInterestAmt</span> <span style="color:red">必填，表示新应计利息总额</span>
<span style="color:red">10.</span> <span style="color:red">AgreementDate</span> <span style="color:red">必填，表示新合约下一付息日</span>
<span style="color:red">11.</span> <span style="color:red">SettlDeliveryType</span> <span style="color:red">必填，表示到期费用结算方式</span>
<span style="color:red">12.</span> <span style="color:red">TotalValueTraded</span> <span style="color:red">必填，表示新借贷费用</span>
<span style="color:red">13.</span> <span style="color:red">MemoEx</span> <span style="color:red">选填，填写新争议解决方式</span>
<span style="color:red">14.</span> <span style="color:red">Memo</span> <span style="color:red">选填，可填入新补充约定内容</span>
<span style="color:red">1.</span> <span style="color:red">SettlDeliveryType</span> <span style="color:red">必填</span>
<span style="color:red">304</span>
<span style="color:red">提前终止</span>
<span style="color:red">2.</span> <span style="color:red">DeliveryForm</span> <span style="color:red">必填，表示到期结算方式</span>
<span style="color:red">3.</span> <span style="color:red">UAInterestAccrualDays</span> <span style="color:red">必填，表示实际借贷期限，</span> <span style="color:red">MaturityDate</span>
<span style="color:red">必填，表示提前终止日</span>
<span style="color:red">4.</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填</span>
<span style="color:red">5.</span> <span style="color:red">SettlDeliveryType</span> <span style="color:red">必填，</span> <span style="color:red">SettlDeliveryType=2</span> <span style="color:red">时，资金账户、资</span>
<span style="color:red">金账户名称、资金开户行、支付系统行号必填</span>
83

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">ApplID</span>
<span style="color:red">TrdType</span>
<span style="color:red">描述</span>
<span style="color:red">填写说明</span>
<span style="color:red">6.</span> <span style="color:red">TotalSettlCurrAmt</span> <span style="color:red">选填，当</span> <span style="color:red">DeliveryForm =2</span> <span style="color:red">或</span> <span style="color:red">101</span> <span style="color:red">时必填，表</span>
<span style="color:red">示现金结算金额</span>
<span style="color:red">7.</span> <span style="color:red">DeliveryQty</span> <span style="color:red">选填，当</span> <span style="color:red">DeliveryForm =1</span> <span style="color:red">或</span> <span style="color:red">101</span> <span style="color:red">时必填，表示归还</span>
<span style="color:red">标的券数量</span>
<span style="color:red">8.</span> <span style="color:red">TotalValueTraded</span> <span style="color:red">必填，表示实际借贷费用金额</span>
<span style="color:red">305</span>
<span style="color:red">质押券变</span>
<span style="color:red">更申报</span>
<span style="color:red">1.</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">选填，可填</span> <span style="color:red">[1,20]</span> <span style="color:red">，</span> <span style="color:red">SecurityID/OrderQty</span> <span style="color:red">填写对应</span>
<span style="color:red">质押券代码和数量，</span> <span style="color:red">EventType</span> <span style="color:red">填写变更类型，</span> <span style="color:red">EventType=22</span> <span style="color:red">时</span>
<span style="color:red">TrdMatchID</span> <span style="color:red">必填，表示质押券的冻结申请书号</span>
<span style="color:red">2.</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填</span>
<span style="color:red">306</span>
<span style="color:red">解除质押</span>
<span style="color:red">ExecRefID</span> <span style="color:red">必填；</span>
<span style="color:red">1.</span> <span style="color:red">SettlDeliveryType</span> <span style="color:red">必填；</span>
<span style="color:red">307</span>
<span style="color:red">逾期结算</span>
<span style="color:red">2.</span> <span style="color:red">DeliveryForm</span> <span style="color:red">必填，表示逾期结算方式</span>
<span style="color:red">3.</span> <span style="color:red">UAInterestAccrualDays</span> <span style="color:red">必填，表示实际借贷期限，</span> <span style="color:red">MaturityDate</span>
<span style="color:red">必填，表示实际结算日；</span>
<span style="color:red">4.</span> <span style="color:red">ExecRefID</span> <span style="color:red">必填；</span>
<span style="color:red">5.</span> <span style="color:red">SettlDeliveryType</span> <span style="color:red">必填，</span> <span style="color:red">SettlDeliveryType=2</span> <span style="color:red">时，资金账户、资</span>
<span style="color:red">金账户名称、资金开户行、支付系统行号必填</span>
<span style="color:red">6.</span> <span style="color:red">TotalSettlCurrAmt</span> <span style="color:red">选填，当</span> <span style="color:red">DeliveryForm =2</span> <span style="color:red">或</span> <span style="color:red">101</span> <span style="color:red">时必填，表</span>
<span style="color:red">示现金结算金额；</span>
<span style="color:red">7.</span> <span style="color:red">DeliveryQty</span> <span style="color:red">选填，当</span> <span style="color:red">DeliveryForm =1</span> <span style="color:red">或</span> <span style="color:red">101</span> <span style="color:red">时必填，表示归还</span>
<span style="color:red">标的券数量</span>
<span style="color:red">8.</span> <span style="color:red">TotalValueTraded</span> <span style="color:red">必填，表示实际借贷费用金额</span>
<span style="color:red">场务应急成</span>
<span style="color:red">不适用</span>
<span style="color:red">不适用</span>
<span style="color:red">不适用，交易员无需申报订单，如交易员已绑定，绑定的交易单元</span>
<span style="color:red">可收到成交确认</span>
<span style="color:red">交录入</span>
<span style="color:red">（</span> <span style="color:red">600310</span> <span style="color:red">）</span>
<span style="color:red">注</span> <span style="color:red">1</span> <span style="color:red">：对于协议回购</span> 到期续做 <span style="color:red">（</span> <span style="color:red">TrdType: 133</span> <span style="color:red">），如对手方确认后将生成两笔成交，一笔为</span> 到期续做 <span style="color:red">前期合</span>
<span style="color:red">约了结（</span> <span style="color:red">137</span> <span style="color:red">），另一笔为</span> 到期续做 <span style="color:red">合约新开（</span> <span style="color:red">138</span> <span style="color:red">）。</span>
<span style="color:red">注</span> <span style="color:red">2</span> <span style="color:red">：对于合并申报，将拆分为两笔申报转发给两个对手方。对手双方均确认后也将生成两笔成交（对于</span>
<span style="color:red">中间方来说），一笔为中间方与买方的成交，另一笔为中间方与卖方的成交。</span>
<span style="color:red">注</span> <span style="color:red">3</span> <span style="color:red">：对于债券借贷到期续做（</span> <span style="color:red">TrdType: 303</span> <span style="color:red">），仅生成一笔成交，该笔成交包含原合约到期结算及新开合</span>
<span style="color:red">约信息。</span>
<span style="color:red">2</span> <span style="color:red">、业务撤单或确认或拒绝填写说明</span>
<span style="color:red">ApplID</span>
<span style="color:red">TrdType</span>
<span style="color:red">描述</span>
<span style="color:red">撤单</span>
<span style="color:red">对手方确认</span>
<span style="color:red">对手方拒绝</span>
<span style="color:red">ExecRefID</span> <span style="color:red">、</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">、</span> <span style="color:red">Sec</span>
<span style="color:red">131</span>
<span style="color:red">协商成交</span>
<span style="color:red">TradeReportRefI</span>
<span style="color:red">ExecRefID</span> <span style="color:red">、</span>
<span style="color:red">协议回购</span>
<span style="color:red">urityID</span> <span style="color:red">、投资者账户、账户名称</span>
<span style="color:red">D</span> <span style="color:red">必填，</span> <span style="color:red">Text</span> <span style="color:red">选</span>
<span style="color:red">NoUnderlyin</span>
<span style="color:red">133</span>
到期续做
<span style="color:red">填。对于协议回</span>
<span style="color:red">必填，</span> <span style="color:red">Text</span> <span style="color:red">选填</span>
<span style="color:red">gs</span> <span style="color:red">、</span> <span style="color:red">SecurityI</span>
<span style="color:red">（</span> <span style="color:red">600130</span> <span style="color:red">）</span>
<span style="color:red">购、合并申报和</span>
<span style="color:red">D</span> <span style="color:red">必填，</span> <span style="color:red">Eve</span>
<span style="color:red">134</span>
<span style="color:red">提前终止</span>
<span style="color:red">ExecRefID</span> <span style="color:red">、</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">、</span> <span style="color:red">Sec</span>
84

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">135</span>
<span style="color:red">换券申报</span>
<span style="color:red">现券协商成交，</span> <span style="color:red">N</span>
<span style="color:red">urityID</span> <span style="color:red">必填，</span> <span style="color:red">EventType</span> <span style="color:red">换券时</span>
<span style="color:red">ntType</span> <span style="color:red">换券</span>
<span style="color:red">oUnderlyings</span> <span style="color:red">、</span> <span style="color:red">Se</span>
<span style="color:red">必填，</span> <span style="color:red">Text</span> <span style="color:red">选填</span>
<span style="color:red">时必填，</span> <span style="color:red">Text</span>
<span style="color:red">136</span>
<span style="color:red">解除质押</span>
<span style="color:red">选填</span>
<span style="color:red">curityID</span> <span style="color:red">必填，</span> <span style="color:red">E</span>
<span style="color:red">ventType</span> <span style="color:red">换券时</span>
<span style="color:red">141</span>
<span style="color:red">协商成交</span>
<span style="color:red">ExecRefID</span> <span style="color:red">、投资者账户、逆回购</span>
<span style="color:red">必填，内容与申</span>
<span style="color:red">方证券账户名称必填，</span> <span style="color:red">Text</span> <span style="color:red">选填</span>
<span style="color:red">143</span>
到期续做
<span style="color:red">三方回购</span>
<span style="color:red">ExecRefID</span> <span style="color:red">必</span>
<span style="color:red">报时一致；协议</span>
<span style="color:red">144</span>
<span style="color:red">提前终止</span>
<span style="color:red">（</span> <span style="color:red">600140</span> <span style="color:red">）</span>
<span style="color:red">填，</span> <span style="color:red">Text</span> <span style="color:red">选填</span>
<span style="color:red">回购批量申报撤</span>
<span style="color:red">ExecRefID</span> <span style="color:red">必填，</span> <span style="color:red">Text</span> <span style="color:red">选填</span>
<span style="color:red">145</span>
<span style="color:red">换券申报</span>
<span style="color:red">单时，允许仅针</span>
<span style="color:red">146</span>
<span style="color:red">解除质押</span>
<span style="color:red">对一笔或几笔质</span>
<span style="color:red">ExecRefID</span> <span style="color:red">、</span>
<span style="color:red">押券部分撤单。</span>
<span style="color:red">ExecRefID</span> <span style="color:red">、</span> <span style="color:red">NoUnderlyings</span> <span style="color:red">、</span> <span style="color:red">Sec</span>
<span style="color:red">NoUnderlyin</span>
<span style="color:red">合并申报</span>
<span style="color:red">不适用</span>
<span style="color:red">合并申报</span>
<span style="color:red">urityID</span> <span style="color:red">、投资者账户必填，</span> <span style="color:red">Text</span>
<span style="color:red">gs</span> <span style="color:red">、</span> <span style="color:red">SecurityI</span>
<span style="color:red">（</span> <span style="color:red">600220</span> <span style="color:red">）</span>
<span style="color:red">选填</span>
<span style="color:red">D</span> <span style="color:red">必填，</span> <span style="color:red">Text</span>
<span style="color:red">选填</span>
<span style="color:red">现券协商成交</span>
<span style="color:red">不适用</span>
<span style="color:red">协商成交</span>
<span style="color:red">不适用</span>
<span style="color:red">不适用</span>
<span style="color:red">（</span> <span style="color:red">600210</span> <span style="color:red">）</span>
<span style="color:red">301</span>
<span style="color:red">协商成交</span>
<span style="color:red">债券借贷</span>
<span style="color:red">TradeReportRefI</span>
<span style="color:red">ExecRefID</span> <span style="color:red">必</span>
<span style="color:red">填</span>
<span style="color:red">（</span> <span style="color:red">600300</span> <span style="color:red">）</span>
<span style="color:red">D</span> <span style="color:red">必填</span>
<span style="color:red">303</span>
<span style="color:red">到期续做</span>
<span style="color:red">ExecRefID</span> <span style="color:red">、对手方一债通账户、</span>
<span style="color:red">投资者账户、投资者账户名称、</span>
<span style="color:red">交易单元必填；</span>
<span style="color:red">协商成交时，</span> <span style="color:red">NoRelatedSym</span> <span style="color:red">、</span> <span style="color:red">No</span>
<span style="color:red">DistribInsts</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">，资金账户、资金</span>
<span style="color:red">账户名称必填，资金开户行、支</span>
<span style="color:red">付系统行号选填；</span>
<span style="color:red">到期续作时，</span> <span style="color:red">NoRelatedSym</span> <span style="color:red">填</span> <span style="color:red">2</span> <span style="color:red">，</span>
<span style="color:red">ContraLegRefID</span> <span style="color:red">分别填</span> <span style="color:red">1</span> <span style="color:red">和</span> <span style="color:red">2</span> <span style="color:red">，</span>
<span style="color:red">NoDistribInsts</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">，若</span> <span style="color:red">ContraLeg</span>
<span style="color:red">RefID</span> <span style="color:red">填</span> <span style="color:red">1</span> <span style="color:red">，</span> <span style="color:red">SettlDeliveryType</span>
<span style="color:red">填</span> <span style="color:red">2</span> <span style="color:red">时，则发起方资金账户、资</span>
<span style="color:red">金账户名称、资金开户行和支付</span>
<span style="color:red">系统行号必填，若</span> <span style="color:red">ContraLegRefI</span>
<span style="color:red">D</span> <span style="color:red">填</span> <span style="color:red">2</span> <span style="color:red">时，则资金账户、资金账</span>
<span style="color:red">户名称必填，资金开户行、支付</span>
<span style="color:red">系统行号选填；</span>
<span style="color:red">304</span>
<span style="color:red">提前终止</span>
<span style="color:red">302</span>
<span style="color:red">到期结算</span>
<span style="color:red">ExecRefID</span> <span style="color:red">必填；</span> <span style="color:red">SettlDeliveryTy</span>
<span style="color:red">pe=2</span> <span style="color:red">时对手方资金账户、资金账</span>
<span style="color:red">户名称、资金开户行、支付系统</span>
<span style="color:red">行号必填</span>
<span style="color:red">307</span>
<span style="color:red">逾期结算</span>
85

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">306</span>
<span style="color:red">解除质押</span>
<span style="color:red">ExecRefID</span> <span style="color:red">必填</span>
<span style="color:red">305</span>
<span style="color:red">质押券变更</span>
<span style="color:red">申报</span>
<span style="color:red">4.4.4.2</span> <span style="color:red">转发成交申报（</span> <span style="color:red">Allege</span> <span style="color:red">Trade</span> <span style="color:red">Capture</span> <span style="color:red">Report,</span> <span style="color:red">MsgType=AE)</span>
<span style="color:red">必</span>
<span style="color:red">标签</span>
<span style="color:red">字段名</span>
<span style="color:red">字段描述</span>
<span style="color:red">类型</span>
<span style="color:red">填</span>
<span style="color:red">35</span>
<span style="color:red">消息头</span>
<span style="color:red">MsgType=AE</span>
<span style="color:red">10197</span>
<span style="color:red">PartitionNo</span>
<span style="color:red">平台内分区号</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">10179</span>
<span style="color:red">ReportIndex</span>
<span style="color:red">执行报告编号，从</span> <span style="color:red">1</span> <span style="color:red">开始连续递增编号</span>
<span style="color:red">Y</span>
<span style="color:red">N16</span>
<span style="color:red">1180</span>
<span style="color:red">ApplID</span>
<span style="color:red">业务类型</span>
<span style="color:red">Y</span>
<span style="color:red">C6</span>
<span style="color:red">1003</span>
<span style="color:red">TradeID</span>
<span style="color:red">交易所订单编号</span>
<span style="color:red">Y</span>
<span style="color:red">C16</span>
<span style="color:red">828</span>
<span style="color:red">TrdType</span>
<span style="color:red">业务子类型</span>
<span style="color:red">N</span>
<span style="color:red">C3</span>
<span style="color:red">成交申报类型</span>
<span style="color:red">856</span>
<span style="color:red">TradeReportType</span>
<span style="color:red">1=Alleged</span> <span style="color:red">，转发成交申报</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">3=Decline</span> <span style="color:red">，拒绝成交申报</span>
<span style="color:red">成交申报事务类别</span>
<span style="color:red">487</span>
<span style="color:red">TradeReportTransType</span>
<span style="color:red">0=New</span> <span style="color:red">，新申报</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">1=Cancel</span> <span style="color:red">，撤销申报</span>
<span style="color:red">被撤消订单的交易所订单编号，撤销申报</span>
<span style="color:red">1126</span>
<span style="color:red">OrigTradeID</span>
<span style="color:red">N</span>
<span style="color:red">C16</span>
<span style="color:red">必填</span>
<span style="color:red">买卖方向：</span> <span style="color:red">1=</span> <span style="color:red">买，</span> <span style="color:red">2=</span> <span style="color:red">卖</span>
<span style="color:red">54</span>
<span style="color:red">Side</span>
<span style="color:red">若为回购，则：</span> <span style="color:red">1=</span> <span style="color:red">正回购，</span> <span style="color:red">2=</span> <span style="color:red">逆回购</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">若为借贷，则：</span> <span style="color:red">F=</span> <span style="color:red">出借，</span> <span style="color:red">G=</span> <span style="color:red">借入</span>
<span style="color:red">44</span>
<span style="color:red">Price</span>
<span style="color:red">申报价格或回购利率</span>
<span style="color:red">N</span>
<span style="color:red">price</span>
<span style="color:red">455</span>
<span style="color:red">SecurityAltID</span>
<span style="color:red">辅助证券代码</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">8903</span>
<span style="color:red">DeliveryQty</span>
<span style="color:red">证券交付数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">8911</span>
<span style="color:red">ExpirationDays</span>
<span style="color:red">期限（天）</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">64</span>
<span style="color:red">SettlDate</span>
<span style="color:red">首次结算日</span>
<span style="color:red">N</span>
<span style="color:red">date</span>
<span style="color:red">541</span>
<span style="color:red">MaturityDate</span>
<span style="color:red">到期日</span>
<span style="color:red">N</span>
<span style="color:red">date</span>
86

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">193</span>
<span style="color:red">SettlDate2</span>
<span style="color:red">到期结算日</span>
<span style="color:red">N</span>
<span style="color:red">date</span>
<span style="color:red">915</span>
<span style="color:red">AgreementDate</span>
<span style="color:red">协议日期</span>
<span style="color:red">N</span>
<span style="color:red">date</span>
<span style="color:red">8847</span>
<span style="color:red">UAInterestAccrualDays</span>
<span style="color:red">实际占款天数</span>
<span style="color:red">N</span>
<span style="color:red">N3</span>
<span style="color:red">60</span>
<span style="color:red">TransactTime</span>
<span style="color:red">业务发生时间</span>
<span style="color:red">N</span>
<span style="color:red">ntime</span>
<span style="color:red">8504</span>
<span style="color:red">TotalValueTraded</span>
<span style="color:red">总成交金额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">累计利息总额，代表总回购利息或债券借</span>
<span style="color:red">TotalAccruedInterestAm</span>
<span style="color:red">540</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">贷标的券应计利息总额</span>
<span style="color:red">t</span>
<span style="color:red">10330</span>
<span style="color:red">TotalSettlCurrAmt</span>
<span style="color:red">总到期结算金额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">580</span>
<span style="color:red">NoDates</span>
<span style="color:red">违约宽限期（天）</span>
<span style="color:red">N</span>
<span style="color:red">N3</span>
<span style="color:red">订单限制</span>
<span style="color:red">对于协议回购表示</span> <span style="color:red">“</span> <span style="color:red">是否同意在违约情形</span>
<span style="color:red">下由质权方对该违约交易项下的质押券直</span>
<span style="color:red">接以拍卖、变卖等方式进行处置</span> <span style="color:red">”</span> <span style="color:red">；；对于</span>
<span style="color:red">529</span>
<span style="color:red">OrderRestrictions</span>
<span style="color:red">N</span>
<span style="color:red">Boolean</span>
<span style="color:red">三方回购表示</span> <span style="color:red">“</span> <span style="color:red">违约后担保品是否由质权</span>
<span style="color:red">人处置</span> <span style="color:red">”</span> <span style="color:red">。</span>
<span style="color:red">Y=</span> <span style="color:red">是；</span>
<span style="color:red">N=</span> <span style="color:red">否</span>
<span style="color:red">结算场所：</span> <span style="color:red">1=</span> <span style="color:red">中国结算，</span> <span style="color:red">2=</span> <span style="color:red">中央结算</span>
<span style="color:red">双边托管券，可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">2</span> <span style="color:red">，单边托管券只能</span>
<span style="color:red">207</span>
<span style="color:red">SecurityExchange</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">填其实际托管方。预留字段，暂不启用。</span>
<span style="color:red">结算周期：</span>
<span style="color:red">0 = T+0</span>
<span style="color:red">1 = T+1</span>
<span style="color:red">10216</span>
<span style="color:red">SettlPeriod</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">2 = T+2</span>
<span style="color:red">3 = T+3</span>
<span style="color:red">预留字段，暂不启用</span>
<span style="color:red">63</span>
<span style="color:red">SettlType</span>
<span style="color:red">结算方式：</span> <span style="color:red">1=</span> <span style="color:red">净额结算，</span> <span style="color:red">2=RTGS</span> <span style="color:red">结算</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">146</span>
<span style="color:red">NoRelatedSym</span>
<span style="color:red">合约结算个数</span>
<span style="color:red">N</span>
<span style="color:red">N1</span>
<span style="color:red">合约相关编号</span>
<span style="color:red">→</span>
<span style="color:red">655</span>
<span style="color:red">ContraLegRefID</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">1=</span> <span style="color:red">代表当前合约，债券借贷代表当前合约</span>
87

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">或到期续做时的原合约</span>
<span style="color:red">2=</span> <span style="color:red">代表新合约，债券借贷代表续做时的新</span>
<span style="color:red">合约</span>
<span style="color:red">结算形式</span>
<span style="color:red">0 =</span> <span style="color:red">现金，债券借贷代表现金结算</span>
<span style="color:red">→</span>
<span style="color:red">668</span>
<span style="color:red">DeliveryForm</span>
<span style="color:red">N</span>
<span style="color:red">C3</span>
<span style="color:red">2 =</span> <span style="color:red">实物，债券借贷代表债券结算</span>
<span style="color:red">101 =</span> <span style="color:red">其他，债券借贷代表部分现金结算</span>
<span style="color:red">资金结算方式</span>
<span style="color:red">→</span>
<span style="color:red">172</span>
<span style="color:red">SettlDeliveryType</span>
<span style="color:red">1 =</span> <span style="color:red">场内结算</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">2 =</span> <span style="color:red">场外结算</span>
<span style="color:red">→</span>
<span style="color:red">510</span>
<span style="color:red">NoDistribInsts</span>
<span style="color:red">交收账户重复组个数</span>
<span style="color:red">N</span>
<span style="color:red">N1</span>
<span style="color:red">F=</span> <span style="color:red">出借方</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">624</span>
<span style="color:red">LegSide</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">G=</span> <span style="color:red">借入方</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">498</span>
<span style="color:red">CashDistribAgentName</span>
<span style="color:red">资金交收机构名称</span>
<span style="color:red">N</span>
<span style="color:red">C75</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">499</span>
<span style="color:red">CashDistribAgentCode</span>
<span style="color:red">资金交收机构代码</span>
<span style="color:red">N</span>
<span style="color:red">C18</span>
<span style="color:red">CashDistribAgentAcctN</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">500</span>
<span style="color:red">资金账户</span>
<span style="color:red">N</span>
<span style="color:red">C22</span>
<span style="color:red">umber</span>
<span style="color:red">CashDistribAgentAcctN</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">502</span>
<span style="color:red">资金账户名称</span>
<span style="color:red">N</span>
<span style="color:red">C87</span>
<span style="color:red">ame</span>
<span style="color:red">左起顺序代表第</span> <span style="color:red">1</span> <span style="color:red">号至第</span> <span style="color:red">N</span> <span style="color:red">号篮子。例如指</span>
<span style="color:red">10194</span>
<span style="color:red">BasketID</span>
<span style="color:red">N</span>
<span style="color:red">C16</span>
<span style="color:red">定</span> <span style="color:red">1</span> <span style="color:red">，</span> <span style="color:red">2</span> <span style="color:red">，</span> <span style="color:red">5</span> <span style="color:red">号篮子，填</span> <span style="color:red">“1100100000000000”</span>
<span style="color:red">711</span>
<span style="color:red">NoUnderlyings</span>
<span style="color:red">证券个数</span>
<span style="color:red">N</span>
<span style="color:red">N2</span>
<span style="color:red">操作标识</span>
<span style="color:red">→</span>
<span style="color:red">865</span>
<span style="color:red">EventType</span>
<span style="color:red">21=</span> <span style="color:red">换入</span> <span style="color:red">/</span> <span style="color:red">补入券</span>
<span style="color:red">N</span>
<span style="color:red">C2</span>
<span style="color:red">22=</span> <span style="color:red">换出券</span>
<span style="color:red">→</span>
<span style="color:red">48</span>
<span style="color:red">SecurityID</span>
<span style="color:red">质押券代码</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">→</span>
<span style="color:red">38</span>
<span style="color:red">OrderQty</span>
<span style="color:red">质押券数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">份额类型</span>
<span style="color:red">→</span>
<span style="color:red">10331</span>
<span style="color:red">ShareProperty</span>
<span style="color:red">0=</span> <span style="color:red">限售；</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">1=</span> <span style="color:red">非限售</span>
88

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">→</span>
<span style="color:red">10332</span>
<span style="color:red">RestrictedMonth</span>
<span style="color:red">限售期（月）</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">→</span>
<span style="color:red">231</span>
<span style="color:red">ContractMultiplier</span>
<span style="color:red">折算比例（</span> <span style="color:red">%</span> <span style="color:red">）</span>
<span style="color:red">N</span>
<span style="color:red">N6(2)</span>
<span style="color:red">→</span>
<span style="color:red">152</span>
<span style="color:red">CashOrderQty</span>
<span style="color:red">质押券面值总额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">→</span>
<span style="color:red">381</span>
<span style="color:red">GrossTradeAmt</span>
<span style="color:red">成交金额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">→</span>
<span style="color:red">159</span>
<span style="color:red">AccruedInterestAmt</span>
<span style="color:red">回购利息</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">→</span>
<span style="color:red">119</span>
<span style="color:red">SettlCurrAmt</span>
<span style="color:red">到期结算金额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">→</span>
<span style="color:red">880</span>
<span style="color:red">TrdMatchID</span>
<span style="color:red">辅助交易编号</span>
<span style="color:red">N</span>
<span style="color:red">C18</span>
<span style="color:red">192</span>
<span style="color:red">OrderQty2</span>
<span style="color:red">本期回购结算利息</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">到期续做类型</span>
<span style="color:red">829</span>
<span style="color:red">TrdSubType</span>
<span style="color:red">N =</span> <span style="color:red">非第三方续做</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">Y =</span> <span style="color:red">第三方续做</span>
<span style="color:red">1125</span>
<span style="color:red">OrigTradeDate</span>
<span style="color:red">原成交日期</span>
<span style="color:red">N</span>
<span style="color:red">date</span>
<span style="color:red">TradeReportType</span> <span style="color:red">为</span> <span style="color:red">1</span> <span style="color:red">时，对非首期于存续</span>
<span style="color:red">19</span>
<span style="color:red">ExecRefID</span>
<span style="color:red">期合约表示原成交编号；为</span> <span style="color:red">3</span> <span style="color:red">时表示被拒</span>
<span style="color:red">N</span>
<span style="color:red">C16</span>
<span style="color:red">绝订单的交易所订单编号。</span>
<span style="color:red">10248</span>
<span style="color:red">MemoEx</span>
<span style="color:red">扩展备注，支持中文</span>
<span style="color:red">N</span>
<span style="color:red">C96</span>
<span style="color:red">发起方重复组，依次包含发起方的交易员</span>
<span style="color:red">一债通账户、交易单元、营业部代码、投</span>
<span style="color:red">资者账户、投资者账户名称，对手方交易</span>
<span style="color:red">453</span>
<span style="color:red">NoPartyIDs</span>
<span style="color:red">Y</span>
<span style="color:red">N2</span>
<span style="color:red">参与人代码以及对手方交易员信息。取值</span>
<span style="color:red">为</span> <span style="color:red">5</span> <span style="color:red">。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方交易员一债通账户</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">的交易员一债通账户</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方投资者帐户</span>
<span style="color:red">N</span>
<span style="color:red">C13</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">5</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方投</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">资者帐户</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方投资者账户名称。</span>
<span style="color:red">N</span>
<span style="color:red">C180</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">38</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">投资者账户名称</span>
89

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">对手方参与人机构代码，支持特殊符号‘</span> <span style="color:red">-</span> <span style="color:red">’</span> <span style="color:red">Y</span>
<span style="color:red">C12</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">37</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为对手方</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">的交易参与人代码</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">对手方交易员一债通账户</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">102</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为对手方</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">的交易员一债通账户</span>
<span style="color:red">664</span>
<span style="color:red">ConfirmID</span>
<span style="color:red">约定号，仅可填大小写英文字母或数字</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">备注，可填写补充约定或补充条款，支持</span>
<span style="color:red">10198</span>
<span style="color:red">Memo</span>
<span style="color:red">N</span>
<span style="color:red">C600</span>
<span style="color:red">中文</span>
<span style="color:red">说明：</span>
<span style="color:red">1</span> <span style="color:red">、对于协议回购批量申报</span> <span style="color:red">N</span> <span style="color:red">笔质押券校验通过后，将生成</span> <span style="color:red">N</span> <span style="color:red">笔转发成交申报给对手方，每笔仅有一</span>
<span style="color:red">笔质押券。</span>
<span style="color:red">4.4.4.3</span> <span style="color:red">成交申报响应（</span> <span style="color:red">Trade Capture Report Response, MsgType=AR</span> <span style="color:red">）</span>
<span style="color:red">标签</span>
<span style="color:red">字段名</span>
<span style="color:red">字段描述</span>
<span style="color:red">必须</span>
<span style="color:red">类型</span>
<span style="color:red">消息头</span>
<span style="color:red">MsgType = AR</span>
<span style="color:red">10197</span>
<span style="color:red">PartitionNo</span>
<span style="color:red">平台内分区号</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">10179</span>
<span style="color:red">ReportIndex</span>
<span style="color:red">执行报告编号，从</span> <span style="color:red">1</span> <span style="color:red">开始连续递增编号</span>
<span style="color:red">Y</span>
<span style="color:red">N16</span>
<span style="color:red">1180</span>
<span style="color:red">ApplID</span>
<span style="color:red">业务类型</span>
<span style="color:red">Y</span>
<span style="color:red">C6</span>
<span style="color:red">828</span>
<span style="color:red">TrdType</span>
<span style="color:red">业务子类型</span>
<span style="color:red">N</span>
<span style="color:red">C3</span>
<span style="color:red">856</span>
<span style="color:red">TradeReportType</span>
<span style="color:red">成交申报类型</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">487</span>
<span style="color:red">TradeReportTransType</span>
<span style="color:red">成交申报事务类别</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">成交申报响应类型，取值有：</span>
<span style="color:red">8912</span>
<span style="color:red">TrdAckStatus</span>
<span style="color:red">0=Accepted</span> <span style="color:red">，订单申报成功</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">8=Rejected</span> <span style="color:red">，订单申报拒绝</span>
<span style="color:red">571</span>
<span style="color:red">TradeReportID</span>
<span style="color:red">会员内部订单编号</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">申报来源</span>
<span style="color:red">2405</span>
<span style="color:red">ExecMethod</span>
<span style="color:red">0 =</span> <span style="color:red">网页端申报</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">1 =</span> <span style="color:red">接口端（</span> <span style="color:red">TDGW</span> <span style="color:red">）申报</span>
<span style="color:red">1003</span>
<span style="color:red">TradeID</span>
<span style="color:red">交易所订单编号</span>
<span style="color:red">Y</span>
<span style="color:red">C16</span>
<span style="color:red">1126</span>
<span style="color:red">OrigTradeID</span>
<span style="color:red">被撤订单交易所订单编号</span>
<span style="color:red">N</span>
<span style="color:red">C16</span>
90

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">522</span>
<span style="color:red">OwnerType</span>
<span style="color:red">订单所有者类型</span>
<span style="color:red">Y</span>
<span style="color:red">N3</span>
<span style="color:red">买卖方向，取值：</span>
<span style="color:red">54</span>
<span style="color:red">Side</span>
<span style="color:red">1=</span> <span style="color:red">买（正回购）</span> <span style="color:red">/2=</span> <span style="color:red">卖（逆回购）</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">F=</span> <span style="color:red">出借</span> <span style="color:red">/G=</span> <span style="color:red">借入</span>
<span style="color:red">44</span>
<span style="color:red">Price</span>
<span style="color:red">申报价格</span>
<span style="color:red">N</span>
<span style="color:red">price</span>
<span style="color:red">455</span>
<span style="color:red">SecurityAltID</span>
<span style="color:red">辅助证券代码</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">8903</span>
<span style="color:red">DeliveryQty</span>
<span style="color:red">证券交付数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">左起顺序代表第</span> <span style="color:red">1</span> <span style="color:red">号至第</span> <span style="color:red">N</span> <span style="color:red">号篮子。例如指定</span> <span style="color:red">1</span> <span style="color:red">，</span>
<span style="color:red">10194</span>
<span style="color:red">BasketID</span>
<span style="color:red">N</span>
<span style="color:red">C16</span>
<span style="color:red">2</span> <span style="color:red">，</span> <span style="color:red">5</span> <span style="color:red">号篮子，填</span> <span style="color:red">“1100100000000000”</span>
<span style="color:red">711</span>
<span style="color:red">NoUnderlyings</span>
<span style="color:red">证券个数</span>
<span style="color:red">N</span>
<span style="color:red">N2</span>
<span style="color:red">操作标识</span>
<span style="color:red">→</span>
<span style="color:red">865</span>
<span style="color:red">EventType</span>
<span style="color:red">21=</span> <span style="color:red">换入</span> <span style="color:red">/</span> <span style="color:red">补入券</span>
<span style="color:red">N</span>
<span style="color:red">C2</span>
<span style="color:red">22=</span> <span style="color:red">换出券</span>
<span style="color:red">→</span>
<span style="color:red">48</span>
<span style="color:red">SecurityID</span>
<span style="color:red">证券代码</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">→</span>
<span style="color:red">38</span>
<span style="color:red">OrderQty</span>
<span style="color:red">申报数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">份额类型</span>
<span style="color:red">→</span>
<span style="color:red">10331</span>
<span style="color:red">ShareProperty</span>
<span style="color:red">0 =</span> <span style="color:red">限售</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">1 =</span> <span style="color:red">非限售</span>
<span style="color:red">→</span>
<span style="color:red">10332</span>
<span style="color:red">RestrictedMonth</span>
<span style="color:red">限售期（月）</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">→</span>
<span style="color:red">231</span>
<span style="color:red">ContractMultiplier</span>
<span style="color:red">折算比例（</span> <span style="color:red">%</span> <span style="color:red">）</span>
<span style="color:red">N</span>
<span style="color:red">N6(2)</span>
<span style="color:red">→</span>
<span style="color:red">381</span>
<span style="color:red">GrossTradeAmt</span>
<span style="color:red">成交金额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">→</span>
<span style="color:red">880</span>
<span style="color:red">TrdMatchID</span>
<span style="color:red">辅助交易编号</span>
<span style="color:red">N</span>
<span style="color:red">C18</span>
<span style="color:red">成交申报状态，取值有：</span>
<span style="color:red">0=Unmatched</span> <span style="color:red">，已挂单未成交</span>
<span style="color:red">939</span>
<span style="color:red">TrdRptStatus</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">4=Cancelled</span> <span style="color:red">，已撤销</span>
<span style="color:red">8=Rejected</span> <span style="color:red">，已拒绝</span>
<span style="color:red">572</span>
<span style="color:red">TradeReportRefID</span>
<span style="color:red">原始会员内部订单编号，撤单时有效</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">751</span>
<span style="color:red">TradeReportRejectReason</span>
<span style="color:red">订单拒绝码，</span> <span style="color:red">TrdRptStatus=8</span> <span style="color:red">时有效</span>
<span style="color:red">N</span>
<span style="color:red">N5</span>
<span style="color:red">60</span>
<span style="color:red">TransactTime</span>
<span style="color:red">回报时间</span>
<span style="color:red">Y</span>
<span style="color:red">ntime</span>
<span style="color:red">58</span>
<span style="color:red">Text</span>
<span style="color:red">用户私有信息</span>
<span style="color:red">N</span>
<span style="color:red">C32</span>
91

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">参与方个数，取值</span> <span style="color:red">=5</span> <span style="color:red">，后接重复组，依次包含登</span>
<span style="color:red">录或订阅交易单元、发起方业务交易单元、交易</span>
<span style="color:red">453</span>
<span style="color:red">NoPartyIDs</span>
<span style="color:red">Y</span>
<span style="color:red">N2</span>
<span style="color:red">员一债通账户、投资者账户、营业部代码。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方登录或订阅交易单元。</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">17</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为登录或订阅交</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">易单元。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方业务交易单元。</span>
<span style="color:red">NY</span>
<span style="color:red">C8</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">1</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方业务交</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">NY</span>
<span style="color:red">N4</span>
<span style="color:red">易单元。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方交易员一债通账户</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">易员一债通账户</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方投资者帐户</span>
<span style="color:red">N</span>
<span style="color:red">C13</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">5</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方投资者</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">帐户。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方营业部代码</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">4001</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的营</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">业部代码。</span>
<span style="color:red">说明：</span>
<span style="color:red">1</span> <span style="color:red">、对于协议回购协商成交批量申报，</span> <span style="color:red">N</span> <span style="color:red">笔质押券将收到</span> <span style="color:red">N</span> <span style="color:red">笔响应，每笔响应仅有一只质押券，可能</span>
<span style="color:red">出现部分成功的场景；撤单时，允许对批量申报的多笔质押券中仅对某一只或某几只进行撤单，每只质押</span>
<span style="color:red">券，将收到一个撤单响应，也可能出现部分成功的场景。</span>
<span style="color:red">4.4.4.4</span> <span style="color:red">成交确认（</span> <span style="color:red">Trade Capture Report, MsgType=AE</span> <span style="color:red">）</span>
<span style="color:red">标签</span>
<span style="color:red">字段名</span>
<span style="color:red">字段描述</span>
<span style="color:red">必须</span>
<span style="color:red">类型</span>
<span style="color:red">消息头</span>
<span style="color:red">MsgType = AE</span>
<span style="color:red">10197</span>
<span style="color:red">PartitionNo</span>
<span style="color:red">平台内分区号</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">10179</span>
<span style="color:red">ReportIndex</span>
<span style="color:red">执行报告编号，从</span> <span style="color:red">1</span> <span style="color:red">开始连续递增编号</span>
<span style="color:red">Y</span>
<span style="color:red">N16</span>
<span style="color:red">1180</span>
<span style="color:red">ApplID</span>
<span style="color:red">业务类型</span>
<span style="color:red">Y</span>
<span style="color:red">C6</span>
<span style="color:red">828</span>
<span style="color:red">TrdType</span>
<span style="color:red">业务子类型</span>
<span style="color:red">N</span>
<span style="color:red">C3</span>
<span style="color:red">571</span>
<span style="color:red">TradeReportID</span>
<span style="color:red">会员内部订单编号</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
92

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">申报来源</span>
<span style="color:red">2405</span>
<span style="color:red">ExecMethod</span>
<span style="color:red">0 =</span> <span style="color:red">网页端申报</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">1 =</span> <span style="color:red">接口端（</span> <span style="color:red">TDGW</span> <span style="color:red">）申报</span>
<span style="color:red">1003</span>
<span style="color:red">TradeID</span>
<span style="color:red">交易所订单编号</span>
<span style="color:red">Y</span>
<span style="color:red">C16</span>
<span style="color:red">订单所有者类型，取值包括：</span>
<span style="color:red">1=</span> <span style="color:red">个人投资者</span>
<span style="color:red">522</span>
<span style="color:red">OwnerType</span>
<span style="color:red">Y</span>
<span style="color:red">N3</span>
<span style="color:red">103=</span> <span style="color:red">机构投资者</span>
<span style="color:red">104=</span> <span style="color:red">自营交易</span>
<span style="color:red">成交申报类型</span>
<span style="color:red">856</span>
<span style="color:red">TradeReportType</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">0=Submit</span> <span style="color:red">，提交成交申报</span>
<span style="color:red">成交申报事务类别</span>
<span style="color:red">487</span>
<span style="color:red">TradeReportTransType</span>
<span style="color:red">0=New</span> <span style="color:red">，新申报</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">2=Replace</span> <span style="color:red">，响应</span>
<span style="color:red">执行报告类型，取值有：</span>
<span style="color:red">8912</span>
<span style="color:red">TrdAckStatus</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">F=Trade</span> <span style="color:red">，成交</span>
<span style="color:red">当前申报的状态，取值有：</span>
<span style="color:red">939</span>
<span style="color:red">TrdRptStatus</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">2=Matched</span> <span style="color:red">，已成交</span>
<span style="color:red">54</span>
<span style="color:red">Side</span>
<span style="color:red">买卖方向</span>
<span style="color:red">Y</span>
<span style="color:red">C1</span>
<span style="color:red">31</span>
<span style="color:red">LastPx</span>
<span style="color:red">成交价格</span>
<span style="color:red">N</span>
<span style="color:red">price</span>
<span style="color:red">17</span>
<span style="color:red">ExecID</span>
<span style="color:red">成交编号</span>
<span style="color:red">Y</span>
<span style="color:red">C16</span>
<span style="color:red">8504</span>
<span style="color:red">TotalValueTraded</span>
<span style="color:red">总成交金额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">455</span>
<span style="color:red">SecurityAltID</span>
<span style="color:red">辅助证券代码</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">8903</span>
<span style="color:red">DeliveryQty</span>
<span style="color:red">证券交付数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">8911</span>
<span style="color:red">ExpirationDays</span>
<span style="color:red">期限（天）</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">1125</span>
<span style="color:red">OrigTradeDate</span>
<span style="color:red">原成交日期</span>
<span style="color:red">N</span>
<span style="color:red">date</span>
<span style="color:red">19</span>
<span style="color:red">ExecRefID</span>
<span style="color:red">原成交编号</span>
<span style="color:red">N</span>
<span style="color:red">C16</span>
<span style="color:red">146</span>
<span style="color:red">NoRelatedSym</span>
<span style="color:red">合约结算个数</span>
<span style="color:red">N</span>
<span style="color:red">N1</span>
<span style="color:red">合约相关编号</span>
<span style="color:red">→</span>
<span style="color:red">655</span>
<span style="color:red">ContraLegRefID</span>
<span style="color:red">1=</span> <span style="color:red">代表当前合约，债券借贷代表当前合约</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">或到期续做时的原合约</span>
93

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">2=</span> <span style="color:red">代表新合约，债券借贷代表续做时的新</span>
<span style="color:red">合约</span>
<span style="color:red">结算形式</span>
<span style="color:red">0 =</span> <span style="color:red">现金，债券借贷代表现金结算</span>
<span style="color:red">→</span>
<span style="color:red">668</span>
<span style="color:red">DeliveryForm</span>
<span style="color:red">N</span>
<span style="color:red">C3</span>
<span style="color:red">2 =</span> <span style="color:red">实物，债券借贷代表债券结算</span>
<span style="color:red">101 =</span> <span style="color:red">其他，债券借贷代表部分现金结算</span>
<span style="color:red">资金结算方式</span>
<span style="color:red">→</span>
<span style="color:red">172</span>
<span style="color:red">SettlDeliveryType</span>
<span style="color:red">1 =</span> <span style="color:red">场内结算</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">2 =</span> <span style="color:red">场外结算</span>
<span style="color:red">→</span>
<span style="color:red">510</span>
<span style="color:red">NoDistribInsts</span>
<span style="color:red">交收账户重复组个数</span>
<span style="color:red">N</span>
<span style="color:red">N1</span>
<span style="color:red">F=</span> <span style="color:red">出借方</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">624</span>
<span style="color:red">LegSide</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">G=</span> <span style="color:red">借入方</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">498</span>
<span style="color:red">CashDistribAgentName</span>
<span style="color:red">资金交收机构名称</span>
<span style="color:red">N</span>
<span style="color:red">C75</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">499</span>
<span style="color:red">CashDistribAgentCode</span>
<span style="color:red">资金交收机构代码</span>
<span style="color:red">N</span>
<span style="color:red">C18</span>
<span style="color:red">CashDistribAgentAcct</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">500</span>
<span style="color:red">资金账户</span>
<span style="color:red">N</span>
<span style="color:red">C22</span>
<span style="color:red">Number</span>
<span style="color:red">CashDistribAgentAcct</span>
<span style="color:red">→</span>
<span style="color:red">→</span>
<span style="color:red">502</span>
<span style="color:red">资金账户名称</span>
<span style="color:red">N</span>
<span style="color:red">C87</span>
<span style="color:red">Name</span>
<span style="color:red">左起顺序代表第</span> <span style="color:red">1</span> <span style="color:red">号至第</span> <span style="color:red">N</span> <span style="color:red">号篮子。例如指</span>
<span style="color:red">10194</span>
<span style="color:red">BasketID</span>
<span style="color:red">N</span>
<span style="color:red">C16</span>
<span style="color:red">定</span> <span style="color:red">1</span> <span style="color:red">，</span> <span style="color:red">2</span> <span style="color:red">，</span> <span style="color:red">5</span> <span style="color:red">号篮子，填</span> <span style="color:red">“1100100000000000”</span>
<span style="color:red">711</span>
<span style="color:red">NoUnderlyings</span>
<span style="color:red">证券个数</span>
<span style="color:red">N</span>
<span style="color:red">N2</span>
<span style="color:red">操作标识</span>
<span style="color:red">→</span>
<span style="color:red">865</span>
<span style="color:red">EventType</span>
<span style="color:red">21=</span> <span style="color:red">换入</span> <span style="color:red">/</span> <span style="color:red">补入券</span>
<span style="color:red">N</span>
<span style="color:red">C2</span>
<span style="color:red">22=</span> <span style="color:red">换出券</span>
<span style="color:red">→</span>
<span style="color:red">48</span>
<span style="color:red">SecurityID</span>
<span style="color:red">证券代码</span>
<span style="color:red">N</span>
<span style="color:red">C12</span>
<span style="color:red">→</span>
<span style="color:red">32</span>
<span style="color:red">LastQty</span>
<span style="color:red">成交数量</span>
<span style="color:red">N</span>
<span style="color:red">quantity</span>
<span style="color:red">份额类型</span>
<span style="color:red">→</span>
<span style="color:red">10331</span>
<span style="color:red">ShareProperty</span>
<span style="color:red">0 =</span> <span style="color:red">限售</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">1 =</span> <span style="color:red">非限售</span>
<span style="color:red">→</span>
<span style="color:red">10332</span>
<span style="color:red">RestrictedMonth</span>
<span style="color:red">限售期（月），指初始登记限售期</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
94

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">→</span>
<span style="color:red">231</span>
<span style="color:red">ContractMultiplier</span>
<span style="color:red">折算比例（</span> <span style="color:red">%</span> <span style="color:red">）</span>
<span style="color:red">N</span>
<span style="color:red">N6(2)</span>
<span style="color:red">→</span>
<span style="color:red">381</span>
<span style="color:red">GrossTradeAmt</span>
<span style="color:red">成交金额</span>
<span style="color:red">N</span>
<span style="color:red">amount</span>
<span style="color:red">→</span>
<span style="color:red">880</span>
<span style="color:red">TrdMatchID</span>
<span style="color:red">辅助交易编号</span>
<span style="color:red">N</span>
<span style="color:red">C18</span>
<span style="color:red">结算场所：</span> <span style="color:red">1=</span> <span style="color:red">中国结算，</span> <span style="color:red">2=</span> <span style="color:red">中央结算</span>
<span style="color:red">双边托管券，可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">2</span> <span style="color:red">，单边托管券只能</span>
<span style="color:red">207</span>
<span style="color:red">SecurityExchange</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">填其实际托管方。预留字段，暂不启用。</span>
<span style="color:red">结算周期：</span>
<span style="color:red">0 = T+0</span>
<span style="color:red">1 = T+1</span>
<span style="color:red">10216</span>
<span style="color:red">SettlPeriod</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">2 = T+2</span>
<span style="color:red">3 = T+3</span>
<span style="color:red">预留字段，暂不启用</span>
<span style="color:red">结算方式：</span>
<span style="color:red">63</span>
<span style="color:red">SettlType</span>
<span style="color:red">1 =</span> <span style="color:red">净额结算</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">2 = RTGS</span> <span style="color:red">结算</span>
<span style="color:red">8500</span>
<span style="color:red">OrderEntryTime</span>
<span style="color:red">订单申报时间</span>
<span style="color:red">N</span>
<span style="color:red">ntime</span>
<span style="color:red">60</span>
<span style="color:red">TransactTime</span>
<span style="color:red">回报时间</span>
<span style="color:red">Y</span>
<span style="color:red">ntime</span>
<span style="color:red">58</span>
<span style="color:red">Text</span>
<span style="color:red">用户私有信息</span>
<span style="color:red">N</span>
<span style="color:red">C32</span>
<span style="color:red">参与方个数，取值</span> <span style="color:red">=8</span> <span style="color:red">，后接重复组，依次</span>
<span style="color:red">包含发起方投资者账户、登录或订阅交易</span>
<span style="color:red">单元、业务交易单元、交易员一债通账户、</span>
<span style="color:red">453</span>
<span style="color:red">NoPartyIDs</span>
<span style="color:red">Y</span>
<span style="color:red">N2</span>
<span style="color:red">营业部代码、对手方交易员一债通账户、</span>
<span style="color:red">投资者账户、账户名称。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方投资者帐户</span>
<span style="color:red">Y</span>
<span style="color:red">C13</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">5</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方投</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">资者帐户。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方登录或订阅交易单元。</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">17</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为登录或订</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">阅交易单元。</span>
<span style="color:red">→</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方业务交易单元。</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
95

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">取</span> <span style="color:red">1</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方业</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">务交易单元。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方交易员一债通账户</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">的交易员一债通账户</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">发起方营业部代码</span>
<span style="color:red">Y</span>
<span style="color:red">C8</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">4001</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">的营业部代码。</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">对手方交易员一债通账户。</span>
<span style="color:red">Y</span>
<span style="color:red">C10</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">102</span> <span style="color:red">，表示当前的</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为对手</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">Y</span>
<span style="color:red">N4</span>
<span style="color:red">方交易员一债通账户</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">对手方投资者帐户</span>
<span style="color:red">NY</span>
<span style="color:red">C13</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">39</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为对手方投</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">YN</span>
<span style="color:red">N4</span>
<span style="color:red">资者帐户</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">证券帐户名称，支持中文。</span>
<span style="color:red">N</span>
<span style="color:red">C1280</span>
<span style="color:red">→</span>
<span style="color:red">取</span> <span style="color:red">36</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为对手方投</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">资者帐户名称</span>
<span style="color:red">说明：</span>
<span style="color:red">1</span> <span style="color:red">、对于成交报告申报模式的被动成交方，也将收到成交确认。其中：申报来源（</span> <span style="color:red">ExecMethod</span> <span style="color:red">）填</span> <span style="color:red">0</span> <span style="color:red">，</span>
<span style="color:red">订单所有者类型（</span> <span style="color:red">OwnerType</span> <span style="color:red">）填‘</span> <span style="color:red">103</span> <span style="color:red">’，营业部代码填‘</span> <span style="color:red">99999</span> <span style="color:red">’；会员内部订单编号（</span> <span style="color:red">TradeReportID</span> <span style="color:red">）</span>
<span style="color:red">按照网页端申报自动生成；登录或订阅交易单元、业务交易单元同首期申报数据，如首期本方通过网页端</span>
<span style="color:red">申报，则此成交实时仍仅供网页端查看。</span>
4.4.5 执行报告类
4.4.5.1 执行报告 <span style="color:red">（</span> <span style="color:red">Execution Report, MsgType = 8</span> <span style="color:red">）</span>
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
96

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
1180
ApplID
业务类型
Y
C6
执行报告类型，取值有：
0= <span style="color:red">Accepted</span> <span style="color:red">，</span> 订单申报成功
150
ExecType
4= <span style="color:red">Cancelled</span> <span style="color:red">，</span> 订单撤销成功
Y
C1
8= <span style="color:red">Rejected</span> <span style="color:red">，</span> 订单申报拒绝
F= <span style="color:red">Trade</span> <span style="color:red">，</span> 成交回报
会员内部订单编号，针对询价交易申报，询价方取
11
ClOrdID
Y
C10
ClOrdID ，报价方取 QuoteMsgID
<span style="color:red">申报来源</span>
<span style="color:red">2405</span>
<span style="color:red">ExecMethod</span>
<span style="color:red">0 =</span> <span style="color:red">网页端申报</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">1 =</span> <span style="color:red">接口端（</span> <span style="color:red">TDGW</span> <span style="color:red">）申报</span>
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
<span style="color:red">N</span>
quantity
151
LeavesQty
剩余数量
<span style="color:red">N</span>
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
39
OrdStatus
Y
C1
0= <span style="color:red">Unmatched</span> <span style="color:red">，</span> 已挂单未成交
97

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
1= <span style="color:red">Partially Matched</span> <span style="color:red">，</span> 部分成交
2= <span style="color:red">Matched</span> <span style="color:red">，</span> 已成交
4= <span style="color:red">Cancelled</span> <span style="color:red">，</span> 已撤消
8= <span style="color:red">Rejected</span> <span style="color:red">，</span> 已拒绝
<span style="color:red">结算场所：</span> <span style="color:red">1=</span> <span style="color:red">中国结算，</span> <span style="color:red">2=</span> <span style="color:red">中央结算</span>
<span style="color:red">SecurityExchang</span>
<span style="color:red">双边托管券，可填</span> <span style="color:red">1</span> <span style="color:red">或</span> <span style="color:red">2</span> <span style="color:red">，单边托管券只能填其实际托</span>
<span style="color:red">207</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">e</span>
<span style="color:red">管方。预留字段，暂不启用。</span>
<span style="color:red">结算周期：</span>
<span style="color:red">0 = T+0</span>
<span style="color:red">1 = T+1</span>
<span style="color:red">10216</span>
<span style="color:red">SettlPeriod</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
<span style="color:red">2 = T+2</span>
<span style="color:red">3 = T+3</span>
<span style="color:red">预留字段，暂不启用</span>
<span style="color:red">63</span>
<span style="color:red">SettlType</span>
<span style="color:red">结算方式：</span> <span style="color:red">1=</span> <span style="color:red">净额结算，</span> <span style="color:red">2=RTGS</span> <span style="color:red">结算</span>
<span style="color:red">N</span>
<span style="color:red">C1</span>
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
交易所订单编号 , 取值为数字 <span style="color:red">，仅订单申报成功</span>
37
OrderID
Y
C16
<span style="color:red">ExecType=0</span> <span style="color:red">时有效</span>
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
用户私有信息
N
C32
参与方个数，取值 =1 <span style="color:red">6</span> ，后接重复组，依次包含发起方
投资者账户、登录或订阅交易单元、发起方业务交易
单元、 <span style="color:red">发起方交易员一债通账户、银行间托管帐号、</span>
453
NoPartyIDs
Y
N2
发起方营业部代码、结算会员代码、投资者中国结算
开放式基金账户、投资者中国结算交易账户、销售人
98

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
代码、券商网点号码、开放式基金转托管的目标方、
申报编号 <span style="color:red">和对手方的一债通账户、投资者账户和投资</span>
<span style="color:red">者账户名称</span> 。
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
<span style="color:red">发起方</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">交易员一债通账户</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">交易员</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易员一</span>
<span style="color:red">一债通</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">债通账户</span>
<span style="color:red">账户</span>
<span style="color:red">银行间</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">银行间托管账号。债券转托管时适用。</span>
<span style="color:red">N</span>
<span style="color:red">C11</span>
<span style="color:red">托管帐</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">28</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为银行间托管账号</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">号</span>
发起方
448
PartyID
发起方营业部代码
Y
C8
营业部
取 4001 ，表示当前 PartyID 的取值为发起方的营业部
452
PartyRole
Y
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
99

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
号
452
PartyRole
取 4003 ，表示当前 PartyID 的取值为申报代码
N
N4
<span style="color:red">对手方</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">对手方交易员一债通账户</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">一债通</span>
<span style="color:red">取</span> <span style="color:red">102</span> <span style="color:red">，表示当前的</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为对手方交易员一</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">账户</span>
<span style="color:red">债通账户</span>
<span style="color:red">对手方</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">对手方投资者帐户或三方回购专户</span>
<span style="color:red">N</span>
<span style="color:red">C13</span>
<span style="color:red">投资者</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">取</span> <span style="color:red">39</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为对手方投资者帐户</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">帐户</span>
<span style="color:red">对手方</span>
<span style="color:red">448</span>
<span style="color:red">PartyID</span>
<span style="color:red">对手方帐户名称，支持中文。</span>
<span style="color:red">N</span>
<span style="color:red">C180</span>
<span style="color:red">证券帐</span>
<span style="color:red">取</span> <span style="color:red">36</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为对手方投资者帐户</span>
<span style="color:red">452</span>
<span style="color:red">PartyRole</span>
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">户名称</span>
<span style="color:red">名称</span>
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
100

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
成交回报：
ExecType=F, OrdStatus =1/2/8
其中， ExecType=F,OrdStatus=8 时表示订单申报进入订单簿后因某种程序原因无法被撮合成交。
2 、对于开放式基金、要约 / 现金选择权、融资融券非交易业务， OwnerType 字段暂不启用。
3 、对于价格、数量字段说明如下：
开放式基
融资融券
要约 / 现金选
<span style="color:red">回售撤销</span> <span style="color:red">/</span> <span style="color:red">转托管</span> <span style="color:red">/</span> <span style="color:red">三</span>
<span style="color:red">报告类型</span>
字段
<span style="color:red">转股</span> <span style="color:red">/</span> <span style="color:red">转股</span> <span style="color:red">/</span> <span style="color:red">回售</span>
金非交易
非交易
择权非交易
<span style="color:red">方回购转入转出</span>
Price 申报
<span style="color:red">转股价格</span> <span style="color:red">/</span> <span style="color:red">换股价</span>
申报信息
<span style="color:red">无意义</span>
价格
<span style="color:red">格</span> <span style="color:red">/</span> <span style="color:red">回售价格</span>
OrderQty
申报信息
<span style="color:red">申报信息</span>
<span style="color:red">申报信息</span>
申报数量
申报成功
响应
LeavesQt
无意义
<span style="color:red">无意义</span>
<span style="color:red">无意义</span>
剩余数量
CxlQty
无意义
<span style="color:red">无意义</span>
<span style="color:red">无意义</span>
撤单数量
Price 申报
申报信息
<span style="color:red">无意义</span>
<span style="color:red">无意义</span>
价格
OrderQty
申报信息
<span style="color:red">申报信息</span>
<span style="color:red">申报信息</span>
申报数量
申报失败
响应
LeavesQt
无意义
<span style="color:red">无意义</span>
<span style="color:red">无意义</span>
剩余数量
CxlQty
无意义
<span style="color:red">无意义</span>
<span style="color:red">无意义</span>
撤单数量
Price 申报
被撤原申报
<span style="color:red">无意义</span>
<span style="color:red">无意义</span>
价格
OrderQty
被撤原申报
<span style="color:red">被撤原申报</span>
<span style="color:red">被撤原申报</span>
申报数量
撤单成功
响应
LeavesQt
无意义
<span style="color:red">无意义</span>
<span style="color:red">无意义</span>
剩余数量
CxlQty
无意义
<span style="color:red">无意义</span>
<span style="color:red">无意义</span>
撤单数量
<span style="color:red">4</span> <span style="color:red">、</span> <span style="color:red">对于三方回购转入转出（</span> <span style="color:red">600270</span> <span style="color:red">）成交，</span> <span style="color:red">LastPx</span> <span style="color:red">（成交价格）和</span> <span style="color:red">TotalValueTraded</span> <span style="color:red">（成交金额）无</span>
101

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
<span style="color:red">意义，</span> <span style="color:red">LastQty</span> <span style="color:red">（成交数量）为转入或转出数量。</span>
<span style="color:red">5</span> <span style="color:red">、对于一债通各类现券非匹配成交（点击成交、询价成交和竞买成交等），将在成交回报中返回对</span>
<span style="color:red">手方的一债通账户、证券账户和账户名称信息。如结算方式为净额结算且任意一方选择‘匿名’，则此字</span>
<span style="color:red">段将填写‘</span> <span style="color:red">anonymous</span> <span style="color:red">’；如结算方式为净额结算且双方均显名或者结算方式‘</span> <span style="color:red">RTGS</span> <span style="color:red">’，则将发送实际的</span>
<span style="color:red">交易信息；但如账户名称无法自动加载，将无此字段。</span>
6 、 <span style="color:red">如竞买预约时勾选了自动发起，且未再手动发起竞买预约，系统将在相应时点自动发起竞买申报。</span>
<span style="color:red">此时竞买预约发起方将收到竞买申报执行报告。此时会员内部订单编号（</span> <span style="color:red">TradeReportID</span> <span style="color:red">）由系统自动生成；</span>
<span style="color:red">申报来源（</span> <span style="color:red">ExecMethod</span> <span style="color:red">）、订单所有者类型（</span> <span style="color:red">OwnerType</span> <span style="color:red">）、营业部代码、登录或订阅交易单元、业务交</span>
<span style="color:red">易单元同预约数据。如预约时通过网页端申报，登录或订阅单元将填写交易员绑定的交易单元；如交易员</span>
<span style="color:red">未绑定，则此执行报告仅供网页端查看。</span>
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
参与方个数，取值 = <span style="color:red">8</span> ，后接重复组，依次包含登录或订阅
交易单元、发起方业务交易单元、 <span style="color:red">发起方</span> 营业部代码、 <span style="color:red">交易</span>
453
NoPartyIDs
Y
N2
<span style="color:red">员一债通账户、</span> 投资者中国结算开放式基金账户、投资者中
国结算交易账户、销售人代码、券商网点号码。
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
102

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
发起方
448
PartyID
发起方营业部代码
<span style="color:red">N</span>
C8
营业部
452
PartyRole
取 4001 ，表示当前 PartyID 的取值为发起方的营业部代码。
<span style="color:red">N</span>
N4
代码
<span style="color:red">发起方</span>
448
PartyID
<span style="color:red">交易员一债通账户</span>
<span style="color:red">N</span>
<span style="color:red">C10</span>
<span style="color:red">交易员</span>
<span style="color:red">取</span> <span style="color:red">101</span> <span style="color:red">，表示当前</span> <span style="color:red">PartyID</span> <span style="color:red">的取值为发起方的交易员一债通</span>
<span style="color:red">一债通</span>
452
PartyRole
<span style="color:red">N</span>
<span style="color:red">N4</span>
<span style="color:red">账户</span>
<span style="color:red">账户</span>
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
1. 发起方营业部代码字段对于开放式基金、要约 / 现金选择权、融资融券非交易业务暂不启用。
4.4.6 网络密码服务（ Password Service <span style="color:red">, MsgType = U006</span> ）
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
103

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
104

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
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
4.4.7.1 申报拒绝 <span style="color:red">（</span> <span style="color:red">Order Reject</span> <span style="color:red">）</span>
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
105

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
48
SecurityID
证券代码
<span style="color:red">YN</span>
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
<span style="color:red">意向申报（</span> <span style="color:red">Indication of Interest</span> <span style="color:red">）</span>
<span style="color:red">IOIID</span>
<span style="color:red">成交申报（</span> <span style="color:red">Trade Capture Report</span> <span style="color:red">）</span>
<span style="color:red">TradeReportID</span>
网络密码服务（ Password Service ）
ClOrdID
<span style="color:red">2</span> <span style="color:red">、对于成交申报类和意向申报类消息，</span> <span style="color:red">SecurityID</span> <span style="color:red">非必填；对于其他消息，</span> <span style="color:red">SecurityID</span> <span style="color:red">必填。</span>
4.4.7.2 平台状态 <span style="color:red">（</span> <span style="color:red">PlatformState</span> <span style="color:red">）</span>
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
6= 互联网交易平台
10181
PlatformStatus
平台状态：
Y
C1
106

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
0 = NotOpen ，未开放
1 = PreOpen ，预开放
2 = Open ，开放
3 = Break ，暂停
4 = Close ，关闭
4.4.7.3 执行报告分区信息 <span style="color:red">（</span> <span style="color:red">ExecRptInfo</span> <span style="color:red">）</span>
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
6 = 互联网交易平台
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
→
10197
PartitionNo
平台内分区号
Y
N4
执行报告分区信息提供 PBU 和分区列表，供 OMS 对执行报告流进行初始化和维护。其中 PBU 可能
为 OMS 所连接 TDGW 上的登录 PBU ，也可能为该 TDGW 上订阅的其他 PBU （仅包含订阅成功的 PBU ），
TDGW 在该循环体中首先给出登录 PBU ，后给出订阅的其他 PBU （如有）。
4.4.7.4 分区序号同步 <span style="color:red">（</span> <span style="color:red">ExecRptSync</span> <span style="color:red">）</span>
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
107

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
4.4.7.5 分区序号同步响应 <span style="color:red">（</span> <span style="color:red">ExecRptSyncRsp</span> <span style="color:red">）</span>
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
4.4.7.6 分区执行报告结束 <span style="color:red">（</span> <span style="color:red">ExecRptEndOfStream</span> <span style="color:red">）</span>
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
分区执行报告最大序号，本消息编入该分区执行报告编号
8563
EndReportIndex
Y
N16
序列。
TDGW 在闭市后向 OMS 自动发送一次，表示该执行报告流推送结束，后续该执行报告流上的序号将
不再增加，最大序号为 EndReportIndex 。
108

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
109

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
110

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
注：本表仅提供交易网关错误码，系统后台错误码参照 <span style="color:red">每日发送的</span> 互联网交易平台错误码信息文件。
111

上海证券交易所交易网关 STEP 接口规范（互联网交易平台）
附录四“用户私有信息”说明
对于应用消息中的 Text 字段（用户私有信息），有如下规则：
TDGW 返回给 OMS 的下行消息中 Text ，取该条下行消息所对应的上行消息（由 OMS 发送给 TDGW ）
中的 Text 字段值。
112

> **变更标注说明**：本文档中已用 `<span style="color:...">` 标注了变更内容（红色=修改/新增，蓝色=其他说明）。


<metadata>
{
  "title": "20250314_IS122_上海证券交易所交易网关STEP接口规格说明书（互联网交易平台）2",
  "source_url": null,
  "raw_path": "knowledge\\raw\\sse\\测试文档\\20250314_IS122_上海证券交易所交易网关STEP接口规格说明书（互联网交易平台）2.06版（固收迁移技术开发稿）_20250114.pdf",
  "markdown_path": "knowledge\\articles\\sse\\markdown\\测试文档\\IS122_上海证券交易所交易网关STEP接口规格说明书（互联网交易平台）2.06版（固收迁移技术开发稿）_202501.md",
  "file_hash": "sha256:381799d7fa3f99ddc0aa44b1e71125e0204e534781e9c6440d14b83d4307825c",
  "file_format": "pdf",
  "page_count": 121,
  "doc_type": "interface_spec",
  "version": null,
  "previous_version": null,
  "public_date": null,
  "effective_date": null,
  "has_changes": true,
  "parse_status": "success",
  "parse_date": "2026-05-02T01:47:57.402007+00:00",
  "sub_category": null
}
</metadata>