# 贡献指南

感谢你帮助维护这个中文社区和导航。

## 选择正确的入口

- 使用问题、实践讨论和经验交流：发到 GitHub Discussions
- 推荐一个项目进入导航：使用“推荐项目” Issue 表单
- 已确认的目录或文档修改：提交 Pull Request
- 安全漏洞：按照 `SECURITY.md` 私下报告，不要公开细节

发帖或贡献前请阅读 `COMMUNITY.md` 和 `CODE_OF_CONDUCT.md`。请勿提交 API key、token、私人联系方式、客户数据或其他敏感信息。

## 提名项目

请优先通过 issue 提名项目，并说明：

- 项目名称和链接
- 解决的问题
- 是否开源
- 适合入门、进阶还是生产使用
- 你实际使用或验证过的证据
- 你是项目维护者、贡献者还是普通用户

## 提交 PR

1. 编辑 `data/tools.json`
2. 运行 `python scripts/generate_readme.py`
3. 运行 `python scripts/validate_catalog.py`
4. 提交变更

README 的精选项目区域由脚本生成，请不要直接手改 `<!-- BEGIN GENERATED -->` 和 `<!-- END GENERATED -->` 之间的内容。

## 内容标准

我们更看重质量而不是数量。请避免提交只有营销页面、无法运行、没有维护迹象或明显重复的项目。推荐自己的项目是允许的，但必须公开说明关系，并提供可核验的信息。
