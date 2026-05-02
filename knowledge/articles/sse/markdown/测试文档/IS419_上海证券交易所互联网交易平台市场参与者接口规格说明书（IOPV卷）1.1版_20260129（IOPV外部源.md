IOPV 外部源机构接入市场参与者接口规格说明书
上海证券交易所技术文档
上海证券交易所互联网交易平台
市场参与者接口规格说明书
（ IOPV 卷）
V1. <span style="color:red">1</span>
上海证券交易所
二〇二 <span style="color:red">六</span> 年 <span style="color:red">一</span> 月

IOPV 外部源机构接入市场参与者接口规格说明书
文档版本
日期
版本
状态
说明
2025.08.15
V1.0
开发稿
创建文档
<span style="color:red">2025.12.15</span>
<span style="color:red">V1.1</span>
<span style="color:red">开发稿</span>
<span style="color:red">1</span> <span style="color:red">、新增登录、修改登录密码接口；</span>
<span style="color:red">2</span> <span style="color:red">、调整公共报文头、请求及返回示例；</span>
<span style="color:red">3</span> <span style="color:red">、调整</span> <span style="color:red">2.2</span> <span style="color:red">章节数据类型定义</span>
<span style="color:red">4</span> <span style="color:red">、</span> <span style="color:red">3.1</span> <span style="color:red">章节新增产品不得重复要求；</span>
<span style="color:red">5</span> <span style="color:red">、修订</span> <span style="color:red">4.1</span> <span style="color:red">章节返回码；</span>

IOPV 外部源机构接入市场参与者接口规格说明书
目录
<span style="color:red">1.</span> <span style="color:red">接口适用范围</span> <span style="color:red">...............................................................................................................................</span> 4
<span style="color:red">2.</span> <span style="color:red">实时报文格式约定</span> <span style="color:red">.......................................................................................................................</span> 4
<span style="color:red">2.1.</span> <span style="color:red">报文通讯模式</span> <span style="color:red">...................................................................................................................</span> 4
<span style="color:red">2.2.</span> <span style="color:red">数据类型约定</span> <span style="color:red">...................................................................................................................</span> 4
<span style="color:red">2.3.</span> <span style="color:red">公共报文头定义</span> <span style="color:red">...............................................................................................................</span> 5
<span style="color:red">3.</span> <span style="color:red">接口说明</span> <span style="color:red">.......................................................................................................................................</span> 5
<span style="color:red">3.1.</span> <span style="color:red">消息流图</span> <span style="color:red">...........................................................................................................................</span> 5
<span style="color:red">3.1.1.</span> <span style="color:red">登录</span> <span style="color:red">...........................................................................................................................</span> 6
<span style="color:red">3.1.2.</span> <span style="color:red">[修改] 修改登录密码</span> <span style="color:red">...........................................................................................................</span> 7
<span style="color:red">3.2.</span> <span style="color:red">登录</span> <span style="color:red">...................................................................................................................................</span> 7
<span style="color:red">3.2.1.</span> <span style="color:red">获取随机数(/login/etf/getRandom)</span> <span style="color:red">...................................................................</span> 7
<span style="color:red">3.2.2.</span> <span style="color:red">登录认证(/login/etf/verify)</span> <span style="color:red">.............................................................................</span> 8
<span style="color:red">3.3.</span> <span style="color:red">[修改] 修改登录密码（</span> <span style="color:red">/login/etf/updatePwd</span> <span style="color:red">）</span> <span style="color:red">.....................................................................</span> 10
<span style="color:red">3.4.</span> <span style="color:red">IOPV 上传（</span> <span style="color:red">/upload/etf/netvalue</span> <span style="color:red">）</span> <span style="color:red">.............................................................................</span> 11

IOPV 外部源机构接入市场参与者接口规格说明书
<span style="color:red">1. 接口适用范围</span>
<span style="color:red">本接口规范适用于经上海证券交易所（以下简称“本所”）批准的IOPV 行情提供商，通</span>
<span style="color:red">过指定专用通信网络与本所行情接入系统建立连接。</span>
<span style="color:red">未经本所授权的机构不得接入。</span>
2. 实时报文格式约定
2.1. 报文通讯模式
获得IOPV 上传资质的指定机构 <span style="color:red">需</span> 通过RESTful API 接口接入 <span style="color:red">本所</span> 互联网交易平台 <span style="color:red">，</span> 并
上传IOPV 数据 <span style="color:red">。以</span> POST+JSON 方式提交 <span style="color:red">的</span> 报文 <span style="color:red">应</span> 采用UTF-8 编码。
<span style="color:red">通信层采用HTTPS（TLS）协议，基于服务端证书实现单向身份认证，保证传输通道的机</span>
<span style="color:red">密性与完整性。业务层采用基于非对称密钥的数字签名与验签机制，并结合账户名密码实现</span>
<span style="color:red">双因子安全校验。</span>
2.2. 数据类型约定
本规范使用的数据类型定义如下：
标识符
类型
C
字符型
N
数值型，并可参与数值计算
L
列表类型
数据处理规则：字符区分大小写。
Nx 、 Nx(y) ：代表该字段内容为数值， NX 代表该字符串为整数， X 为该整数的最大长
度； NX(Y) 代表该字符串为浮点数， X 代表该字符串的最大长度， Y 代表小数位数， <span style="color:red">X</span> <span style="color:red">包括</span>
<span style="color:red">一位小数点，此时整数部分最多不超过X-Y-1</span> <span style="color:red">位，</span> 小数部分最多不超过 Y 位。

IOPV 外部源机构接入市场参与者接口规格说明书
2.3. 公共报文头定义
请求参数：
字段名称
变量名
类型
长度
必填
备注
API 版本
version
C
10
Y
<span style="color:red">填写版本号，当前版本为</span> <span style="color:red">1.1</span> <span style="color:red">。</span>
<span style="color:red">填写示例“</span> <span style="color:red">1.1</span> <span style="color:red">”</span>
业务编码
bizId
C
3
Y
00 <span style="color:red">2</span> <span style="color:red">表示</span> IOPV <span style="color:red">业务</span>
机构代码
mctCode
C
5
Y
机构代码 , 由交易所分配
发送日期
sendDate
C
8
Y
yyyyMMdd ，当前交易日
发送时间
sendTime
C
9
Y
HHmmSSsss
<span style="color:red">说明：</span>
<span style="color:red">1、发送日期、发送时间表示请求发送的时间。</span>
响应参数:
字段名称
变量名
类型
长度
必填
备注
通讯返回码
code
C
6
Y
参考返回码列表
通讯返回错误
描述
message
C
24
Y
系统未知异常 , 其他各种可能
的错误
响应结果
data
N
详见第 <span style="color:red">3</span> 章响应参数
响应时间
respTime
C
17
Y
yyyyMMddHHmmSSsss
<span style="color:red">接口说明</span>
<span style="color:red">3.1.</span> <span style="color:red">消息流图</span>
<span style="color:red">本系统采用”通信层安全+业务层身份认证“的双层认证机制：</span>
<span style="color:red"></span>
<span style="color:red">通信层：基于HTTPS（TLS）的单向认证，用于保障传输通道安全；</span>
<span style="color:red"></span>
<span style="color:red">业务层：客户端使用本所颁发的业务签名证书，对随机数、会话标识及时间戳进行</span>
<span style="color:red">数字签名。本所通过验签确认客户端身份的真实性与不可抵赖性。业务签名认证通</span>
<span style="color:red">过后，系统继续校验登录账户名和密码。</span>

IOPV 外部源机构接入市场参与者接口规格说明书
<span style="color:red">3.1.1.</span>
<span style="color:red">登录</span>
<span style="color:red">1.</span>
<span style="color:red">验证方</span> <span style="color:red">B</span> <span style="color:red">产生随机数</span> <span style="color:red">Rb</span> <span style="color:red">并将随机数</span> <span style="color:red">Rb</span> <span style="color:red">发送至声称方</span> <span style="color:red">A</span> <span style="color:red">；</span>
<span style="color:red">2.</span>
<span style="color:red">声称方</span> <span style="color:red">A</span> <span style="color:red">产生随机数</span> <span style="color:red">Ra</span> <span style="color:red">，拼装</span> <span style="color:red">certsn||sessionID</span> <span style="color:red">作为标识符</span> <span style="color:red">B</span> <span style="color:red">，使用系统时间</span>
<span style="color:red">戳</span> <span style="color:red">time</span> <span style="color:red">作为</span> <span style="color:red">Text3</span> <span style="color:red">。</span> <span style="color:red">certsn</span> <span style="color:red">为客户端证书中解析出的证书序列号、</span> <span style="color:red">sessionID</span> <span style="color:red">为</span> <span style="color:red">HTTP</span> <span style="color:red">通</span>
<span style="color:red">信中服务端产生的会话</span> <span style="color:red">ID</span> <span style="color:red">；</span>
<span style="color:red">3.</span>
<span style="color:red">声称方使用约定的签名私钥对</span> <span style="color:red">Ra||Rb||Text2</span> <span style="color:red">签名得到</span> <span style="color:red">Ssa</span> <span style="color:red">。签名算法为</span> <span style="color:red">RSA</span> <span style="color:red">。</span>
<span style="color:red">Text2</span> <span style="color:red">为</span> <span style="color:red">certsn||sessionID||time</span> <span style="color:red">；</span>
<span style="color:red">4.</span>
<span style="color:red">声称方拼装</span> <span style="color:red">Token= Ra||Rb||B||Text3||Ssa</span> <span style="color:red">；</span>
<span style="color:red">5.</span>
<span style="color:red">声称方将自身签名证书</span> <span style="color:red">CertA</span> <span style="color:red">和</span> <span style="color:red">Token</span> <span style="color:red">、账户名密码发送至验证方</span> <span style="color:red">B</span> <span style="color:red">；</span>
<span style="color:red">6.</span>
<span style="color:red">一旦验证方</span> <span style="color:red">B</span> <span style="color:red">收到包含</span> <span style="color:red">Token</span> <span style="color:red">的消息，</span> <span style="color:red">B</span> <span style="color:red">验证</span> <span style="color:red">CertA</span> <span style="color:red">的合法性，然后验证签名</span>
<span style="color:red">结果</span> <span style="color:red">Ssa</span> <span style="color:red">的正确性，若一致则鉴别通过。</span>

IOPV 外部源机构接入市场参与者接口规格说明书
<span style="color:red">3.1.2.</span>
<span style="color:red">[修改] 修改登录密码</span>
<span style="color:red">3.2.</span> <span style="color:red">登录</span>
<span style="color:red">3.2.1.</span>
<span style="color:red">获取随机数(/login/etf/getRandom)</span>
<span style="color:red">功能描述：交易日</span> <span style="color:red">7:00-16:30</span> <span style="color:red">，指数机构通过互联网交易平台获取随机数</span>
<span style="color:red">接口路径：</span> <span style="color:red">/login/etf/getRandom</span>
<span style="color:red">数据格式：</span> <span style="color:red">Json</span>
<span style="color:red">请求方：市场机构</span>
<span style="color:red">请求参数：无</span>
<span style="color:red">响应参数:</span>
<span style="color:red">字段名称</span>
<span style="color:red">变量名</span>
<span style="color:red">类型</span>
<span style="color:red">长度</span>
<span style="color:red">必填</span>
<span style="color:red">备注</span>
<span style="color:red">随机数</span>
<span style="color:red">random</span>
<span style="color:red">C</span>
<span style="color:red">24</span>
<span style="color:red">Y</span>
<span style="color:red">Base64</span> <span style="color:red">编码，由服务端生成，</span>
<span style="color:red">用于后续客户端身份认证</span>
<span style="color:red">认证</span> <span style="color:red">ID</span>
<span style="color:red">sessionId</span>
<span style="color:red">C</span>
<span style="color:red">32</span>
<span style="color:red">Y</span>
<span style="color:red">服务端生成的认证</span> <span style="color:red">ID</span> <span style="color:red">，用于</span>
<span style="color:red">后续客户端身份认证</span>
<span style="color:red">请求示例</span> <span style="color:red">:</span>
<span style="color:red">body = {</span>

IOPV 外部源机构接入市场参与者接口规格说明书
<span style="color:red">"mctCode": "XXXXX",</span>
<span style="color:red">"sendDate": "20210502",</span>
<span style="color:red">"bizId": "001",</span>
<span style="color:red">"version": "1.0",</span>
<span style="color:red">"sendTime": "102020"</span>
<span style="color:red">}</span>
<span style="color:red">响应示例</span> <span style="color:red">:</span>
<span style="color:red">{</span>
<span style="color:red">"code": 200,</span>
<span style="color:red">"message": "</span> <span style="color:red">操作成功</span> <span style="color:red">",</span>
<span style="color:red">"data": {</span>
<span style="color:red">"random": "fdsgsfdhuhsfhuf",</span>
<span style="color:red">"sessionId": "sdfssfgfsdhghhh"</span>
<span style="color:red">},</span>
<span style="color:red">"respTime": "20260113085403955"</span>
<span style="color:red">}</span>
<span style="color:red">3.2.2.</span>
<span style="color:red">登录认证(/login/etf/verify)</span>
<span style="color:red">功能描述：交易日</span> <span style="color:red">7:00-16:30</span> <span style="color:red">，指数机构在申报实时参考净值前登录连接互联网交易平台</span>
<span style="color:red">接口路径：</span> <span style="color:red">/login/etf/verify</span>
<span style="color:red">数据格式：</span> <span style="color:red">Json</span>
<span style="color:red">请求方：市场机构</span>
<span style="color:red">请求参数：</span>
<span style="color:red">字段名称</span>
<span style="color:red">变量名</span>
<span style="color:red">类型</span>
<span style="color:red">长度</span>
<span style="color:red">必填</span>
<span style="color:red">备注</span>
<span style="color:red">签名证书</span>
<span style="color:red">cert</span>
<span style="color:red">C</span>
<span style="color:red">2048</span>
<span style="color:red">Y</span>
<span style="color:red">客户端自身签名证书（通过</span>
<span style="color:red">密钥载体</span> <span style="color:red">Ekey</span> <span style="color:red">获取），</span> <span style="color:red">Base64</span>
<span style="color:red">格式</span>
<span style="color:red">登录密码</span>
<span style="color:red">password</span>
<span style="color:red">C</span>
<span style="color:red">128</span>
<span style="color:red">Y</span>
<span style="color:red">账户认证方式：密码</span>
<span style="color:red">上传频率</span>
<span style="color:red">uploadFreq</span>
<span style="color:red">N</span>
<span style="color:red">3</span>
<span style="color:red">Y</span>
<span style="color:red">以秒为单位，范围为</span> <span style="color:red">[3, 900]</span>

IOPV 外部源机构接入市场参与者接口规格说明书
<span style="color:red">请求头中携带字段信息：</span>
<span style="color:red">字段名称</span>
<span style="color:red">变量名</span>
<span style="color:red">类型</span>
<span style="color:red">长度</span>
<span style="color:red">必填</span>
<span style="color:red">备注</span>
<span style="color:red">认证</span> <span style="color:red">ID</span>
<span style="color:red">sessionId</span>
<span style="color:red">C</span>
<span style="color:red">32</span>
<span style="color:red">Y</span>
<span style="color:red">服务端生成的认证</span> <span style="color:red">ID</span> <span style="color:red">，用于</span>
<span style="color:red">后续客户端身份认证</span>
<span style="color:red">身份认证</span> <span style="color:red">ID</span>
<span style="color:red">token</span>
<span style="color:red">C</span>
<span style="color:red">Y</span>
<span style="color:red">客户端根据签名算法生成的</span>
<span style="color:red">token</span> <span style="color:red">信息，服务端对其进行</span>
<span style="color:red">验签</span>
<span style="color:red">响应参数:</span>
<span style="color:red">字段名称</span>
<span style="color:red">变量名</span>
<span style="color:red">类型</span>
<span style="color:red">长度</span>
<span style="color:red">必填</span>
<span style="color:red">备注</span>
<span style="color:red">上传频率</span>
<span style="color:red">uploadFreq</span>
<span style="color:red">N</span>
<span style="color:red">3</span>
<span style="color:red">N</span>
<span style="color:red">以秒为单位，登录认证成功</span>
<span style="color:red">后返回</span>
<span style="color:red">说明：</span>
<span style="color:red">1、IOPV 上传时间间隔应以响应参数中的上传频率为准。</span>
<span style="color:red">请求示例：</span>
<span style="color:red">header = {</span>
<span style="color:red">"sessionId": "dhwkejdbjshk2332444....",</span>
<span style="color:red">"token": "sadifhkfhaew||uweirohfakjldjksa||......"</span>
<span style="color:red">}</span>
<span style="color:red">body = {</span>
<span style="color:red">"mctCode": "XXXXX",</span>
<span style="color:red">"sendDate": "20210502",</span>
<span style="color:red">"bizId": "001",</span>
<span style="color:red">"version": "1.0",</span>
<span style="color:red">"sendTime": "102020",</span>
<span style="color:red">"cert":"tuytuyg",</span>
<span style="color:red">"password":"tuygu",</span>
<span style="color:red">"uploadFreq":5</span>
<span style="color:red">}</span>
<span style="color:red">响应示例：</span>
<span style="color:red">{</span>

IOPV 外部源机构接入市场参与者接口规格说明书
<span style="color:red">"code": 200,</span>
<span style="color:red">"message": "</span> <span style="color:red">操作成功</span> <span style="color:red">",</span>
<span style="color:red">"data": {</span>
<span style="color:red">"uploadFreq": 5</span>
<span style="color:red">},</span>
<span style="color:red">"respTime": "20260113085403955"</span>
<span style="color:red">}</span>
<span style="color:red">3.3.</span> <span style="color:red">[修改] 修改登录密码（</span> <span style="color:red">/login/etf/updatePwd</span> <span style="color:red">）</span>
<span style="color:red">功能描述：交易日</span> <span style="color:red">7:00-16:30</span> <span style="color:red">，指数机构可通过该接口修改登录密码</span>
<span style="color:red">接口路径：</span> <span style="color:red">/login/etf/updatePwd</span>
<span style="color:red">数据格式：</span> <span style="color:red">Json</span>
<span style="color:red">请求方：市场机构</span>
<span style="color:red">请求参数：</span>
<span style="color:red">字段名称</span>
<span style="color:red">变量名</span>
<span style="color:red">类型</span>
<span style="color:red">长度</span>
<span style="color:red">必填</span>
<span style="color:red">备注</span>
<span style="color:red">登录密码</span>
<span style="color:red">oldLoginPwd</span>
<span style="color:red">C</span>
<span style="color:red">128</span>
<span style="color:red">Y</span>
<span style="color:red">新密码</span>
<span style="color:red">newLoginPwd</span>
<span style="color:red">C</span>
<span style="color:red">128</span>
<span style="color:red">Y</span>
<span style="color:red">更新后的密码，且不能登录</span>
<span style="color:red">密码相同</span>
<span style="color:red">请求头中携带字段信息：</span>
<span style="color:red">字段名称</span>
<span style="color:red">变量名</span>
<span style="color:red">类型</span>
<span style="color:red">长度</span>
<span style="color:red">必填</span>
<span style="color:red">备注</span>
<span style="color:red">认证ID</span>
<span style="color:red">sessionId</span>
<span style="color:red">C</span>
<span style="color:red">32</span>
<span style="color:red">Y</span>
<span style="color:red">服务端生成的认证ID，用于</span>
<span style="color:red">客户端身份认证，身份认证</span>
<span style="color:red">通过后才允许修改密码</span>
<span style="color:red">响应参数:无</span>
<span style="color:red">说明：</span>

IOPV 外部源机构接入市场参与者接口规格说明书
<span style="color:red">1、修改登录密码后，需重新登录。</span>
<span style="color:red">请求示例：</span>
<span style="color:red">header = {</span>
<span style="color:red">"sessionId": "dhwkejdbjshk2332444...."</span>
<span style="color:red">}</span>
<span style="color:red">body = {</span>
<span style="color:red">"mctCode": "XXXXX",</span>
<span style="color:red">"sendDate": "20210502",</span>
<span style="color:red">"bizId": "001",</span>
<span style="color:red">"version": "1.0",</span>
<span style="color:red">"sendTime": "102020",</span>
<span style="color:red">"oldLoginPwd":"tuytuyg",</span>
<span style="color:red">"newLoginPwd":"tuygu"</span>
<span style="color:red">}</span>
<span style="color:red">响应示例：</span>
<span style="color:red">{</span>
<span style="color:red">"code": 200,</span>
<span style="color:red">"message": "</span> <span style="color:red">操作成功</span> <span style="color:red">",</span>
<span style="color:red">"data": {},</span>
<span style="color:red">"respTime": "20260113085403955"</span>
<span style="color:red">}</span>
<span style="color:red">3.4.</span> <span style="color:red">IOPV 上传（</span> <span style="color:red">/upload/etf/netvalue</span> <span style="color:red">）</span>
<span style="color:red">功能描述：交易日</span> <span style="color:red">7:00-16:30</span> <span style="color:red">，市场机构申报实时参考净值</span>
<span style="color:red">接口路径：</span> <span style="color:red">/upload/etf/netvalue</span>
<span style="color:red">数据格式：</span> <span style="color:red">Json</span>
<span style="color:red">请求方：市场机构</span>

IOPV 外部源机构接入市场参与者接口规格说明书
<span style="color:red">请求参数：</span>
<span style="color:red">字段名称</span>
<span style="color:red">变量名</span>
<span style="color:red">类型</span>
<span style="color:red">长度</span>
<span style="color:red">必填</span>
<span style="color:red">备注</span>
<span style="color:red">请求流水号</span>
<span style="color:red">seqNo</span>
<span style="color:red">C</span>
<span style="color:red">64</span>
<span style="color:red">Y</span>
<span style="color:red">请求流水号每个机构下需不</span>
<span style="color:red">重复</span>
<span style="color:red">消息内容</span>
<span style="color:red">msg</span>
<span style="color:red">C</span>
<span style="color:red">1024</span>
<span style="color:red">Y</span>
<span style="color:red">msg 消息内容为：</span>
<span style="color:red">字段名称</span>
<span style="color:red">变量名</span>
<span style="color:red">类型</span>
<span style="color:red">长度</span>
<span style="color:red">必填</span>
<span style="color:red">备注</span>
<span style="color:red">业务时间</span>
<span style="color:red">businessTime</span>
<span style="color:red">C</span>
<span style="color:red">17</span>
<span style="color:red">Y</span>
<span style="color:red">yyyyMMddHHmmSSsss</span>
<span style="color:red">据此计算交易日</span>
<span style="color:red">IOPV 数据</span>
<span style="color:red">fundList</span>
<span style="color:red">L</span>
<span style="color:red">list 开始</span>
<span style="color:red">行情ID</span>
<span style="color:red">marketId</span>
<span style="color:red">N</span>
<span style="color:red">19</span>
<span style="color:red">Y</span>
<span style="color:red">每日自1 起递增</span>
<span style="color:red">证券代码</span>
<span style="color:red">fundCode</span>
<span style="color:red">C</span>
<span style="color:red">6</span>
<span style="color:red">Y</span>
<span style="color:red">证券代码</span>
<span style="color:red">每份基金实时</span>
<span style="color:red">参考净值</span>
<span style="color:red">price</span>
<span style="color:red">N</span>
<span style="color:red">14(5)</span>
<span style="color:red">Y</span>
<span style="color:red">IOPV 值，需为非负数</span>
<span style="color:red">IOPV 数据</span>
<span style="color:red">fundList</span>
<span style="color:red">L</span>
<span style="color:red">list 结束</span>
<span style="color:red">备注</span>
<span style="color:red">text</span>
<span style="color:red">C</span>
<span style="color:red">12</span>
<span style="color:red">N</span>
说明：
1.
每次上传请求中包含的产品数最大不超过 100 条，即行情 ID 不超过 100 个。
<span style="color:red">2.</span>
<span style="color:red">业务时间表示IOPV 行情生成时间。</span>
<span style="color:red">3.</span>
行情 ID 字段在同一交易日内不可重复，不支持回溯，在同一个请求 List 中需
增序排列，可跳号。
4.
<span style="color:red">证券代码在每次上传请求消息中不得重复。</span>
只有当请求参数 list 内所有 IOPV 行情 <span style="color:red">均校验通过，</span> 响应中 <span style="color:red">的</span> 通讯返回码 code 才会
返回 200 <span style="color:red">，</span> 表示更新成功。其他情况下，响应参数中的 data 将返回第一个处理失败的
行情 ID 以及拒绝原因 <span style="color:red">。</span>
<span style="color:red">响应参数：</span>

IOPV 外部源机构接入市场参与者接口规格说明书
<span style="color:red">字段名称</span>
<span style="color:red">变量名</span>
<span style="color:red">类型</span>
<span style="color:red">长度</span>
<span style="color:red">必填</span>
<span style="color:red">备注</span>
<span style="color:red">行情</span> <span style="color:red">ID</span>
<span style="color:red">marketId</span>
<span style="color:red">N</span>
<span style="color:red">19</span>
<span style="color:red">N</span>
<span style="color:red">拒绝原因</span>
<span style="color:red">orderRejReason</span>
<span style="color:red">N</span>
<span style="color:red">6</span>
<span style="color:red">N</span>
<span style="color:red">参考返回码列表</span>
<span style="color:red">备注</span>
<span style="color:red">text</span>
<span style="color:red">C</span>
<span style="color:red">24</span>
<span style="color:red">N</span>
<span style="color:red">请求示例：</span>
<span style="color:red">header = {</span>
<span style="color:red">"sessionId": "dhwkejdbjshk2332444...."</span>
<span style="color:red">}</span>
<span style="color:red">body = {</span>
<span style="color:red">"mctCode": "XXXXX",</span>
<span style="color:red">"seqNo": "1243443d5d33s44444....",</span>
<span style="color:red">"sendDate": "20210502",</span>
<span style="color:red">"bizId": "001",</span>
<span style="color:red">"version": "1.0",</span>
<span style="color:red">"sendTime": "102020",</span>
<span style="color:red">"msg": " {</span>
<span style="color:red">"businessTime": "20251219145232000",</span>
<span style="color:red">"fundList": [</span>
<span style="color:red">{</span>
<span style="color:red">"marketId": 1,</span>
<span style="color:red">"fundCode": "1111",</span>
<span style="color:red">"price": 1.234</span>
<span style="color:red">},</span>
<span style="color:red">{</span>
<span style="color:red">"marketId": 2,</span>
<span style="color:red">"funCode": "2222",</span>

IOPV 外部源机构接入市场参与者接口规格说明书
<span style="color:red">"price": 1.345</span>
<span style="color:red">}</span>
<span style="color:red">]</span>
<span style="color:red">}"</span>
<span style="color:red">}</span>
<span style="color:red">响应示例：</span>
<span style="color:red">{</span>
<span style="color:red">"code": 200,</span>
<span style="color:red">"message": "</span> <span style="color:red">操作成功</span> <span style="color:red">",</span>
<span style="color:red">"data": {},</span>
<span style="color:red">"respTime": "20260113085403955"</span>
<span style="color:red">}</span>

> **变更标注说明**：本文档中已用 `<span style="color:...">` 标注了变更内容（红色=修改/新增，蓝色=其他说明）。


<metadata>
{
  "title": "20260129_IS419_上海证券交易所互联网交易平台市场参与者接口规格说明书（IOPV卷）1",
  "source_url": null,
  "raw_path": "knowledge\\raw\\sse\\测试文档\\20260129_IS419_上海证券交易所互联网交易平台市场参与者接口规格说明书（IOPV卷）1.1版_20260129（IOPV外部源接入_技术开发稿）.pdf",
  "markdown_path": "knowledge\\articles\\sse\\markdown\\测试文档\\IS419_上海证券交易所互联网交易平台市场参与者接口规格说明书（IOPV卷）1.1版_20260129（IOPV外部源.md",
  "file_hash": "sha256:1434d196994db0ee571d0692ae420a8c69c9eef32655b2bb2943769951cc9064",
  "file_format": "pdf",
  "page_count": 14,
  "doc_type": "interface_spec",
  "version": null,
  "previous_version": null,
  "public_date": "2025-08-15",
  "effective_date": null,
  "has_changes": true,
  "parse_status": "success",
  "parse_date": "2026-05-02T01:48:29.351013+00:00",
  "sub_category": null
}
</metadata>