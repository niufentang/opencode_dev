
### plan模式下交互
我想实现pipeline/pipeline.py，一个五步知识库自动化流水线：
需求：
1. Step 1: 采集（Collect）— 从上交所交易技术支持专区、深交所技术服务、中国结算业务规则三大数据源自动爬取技术与规则文档，提取结构化元数据并下载原始文件
2. Step 2: 解析（Parse）— 将将采集到的原始异构文件（PDF/Word/ZIP/HTML）解析为结构化 Markdown 文本和元数据，标注技术变更与规则变更，为后续语义分析提供标准化输入
3. Step 3: 分析（Analyze）— 对解析后的 Markdown 文档进行语义分析，执行技术变更/规则变更检测、版本差异比对、废止替代检测、跨站关联发现与标签自动分类，产出结构化分析结果。
4. Step 4: 整理（Organize）— 对分析后的原始数据进行去重、过滤、格式化，输出为标准知识条目 JSON，是流水线的最后一环，产出供下游检索和分发的最终数据。
5. Step 5: 保存（Save）— 将文章保存为独立 JSON 文件到 knowledge/articles/
先结合项目分析，是否合理，是否有其他优化方案、建议等


多轮讨论后结果document:

[06_pipeline_design.md](../doc/06_pipeline_design.md)


[06_pipeline_usage.md](../doc/06_pipeline_usage.md)

