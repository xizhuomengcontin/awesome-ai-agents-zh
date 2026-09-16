# 2026-09-16 收录核验

本次新增 2 个项目，目录共 26 项。数量不是目标；下列信息来自维护者仓库与公开元数据，未运行其模型调用或部署生产环境。

| 项目 | 核验依据 | 适合的需求 | 限制 |
| --- | --- | --- | --- |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai/tree/c92e9c1e1915d071969a46900ba898f014a286d9) | MIT；Python；README 提供类型化 agent、工具及文档入口；核验日仓库未归档 | 结构化结果、Python 应用集成 | 模型调用通常需要服务商凭证与预算；类型正确不代表事实正确 |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework/tree/66d74f38724c8a26429764925acae3e7aee1ca8d) | MIT；Python/.NET；维护者提供 agent 与工作流示例；核验日仓库未归档 | 已有 Python 或 .NET 团队的工作流编排 | 先锁定 SDK 版本；不要假定与其他框架的 API 兼容 |

也审查了 [MCP Inspector](https://github.com/modelcontextprotocol/inspector/tree/795b1bb30ac845b7baa7cb3df8ec0b693882ca1d)。README 标示 MIT，但本次默认分支未找到独立 LICENSE 文件，GitHub license 元数据为空；本轮暂不新增，避免在目录中把许可证判断写得过于确定。

这些是仓库来源审查，不是安全认证、效果排名或推荐购买。活跃时间与默认分支会变化，复查时请使用当前证据。
