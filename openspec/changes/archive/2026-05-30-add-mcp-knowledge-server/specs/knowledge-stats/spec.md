## ADDED Requirements

### Requirement: knowledge_stats tool

The system SHALL provide a `knowledge_stats` MCP tool that returns aggregate statistics about the knowledge base.

- **Tool name**: `knowledge_stats`
- **Description**: 获取知识库统计信息：总数、来源分布、类型分布、热门标签
- **Input parameters**: none
- **Computation**: real-time aggregation from in-memory data
- **Return content**:
  - Total article count
  - Distribution by source (sse / szse / chinaclear)
  - Distribution by type (technical_notice / interface_spec / guide / etc.)
  - Distribution by status (active / superseded / deprecated)
  - Top 10 tags by frequency
  - Top 5 recently published (by public_date descending)
  - Top 5 recently crawled (by crawl_date descending)
- **Return format**: formatted text

#### Scenario: Get knowledge base stats
- **WHEN** user calls `knowledge_stats` with no arguments
- **THEN** system returns formatted text with total count, source distribution, type distribution, status distribution, top 10 tags, and last 5 updated articles

#### Scenario: Empty knowledge base
- **WHEN** knowledge base has 0 entries and user calls `knowledge_stats`
- **THEN** system returns stats showing 0 articles across all distributions
