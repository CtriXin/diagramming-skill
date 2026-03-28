# 贡献指南

欢迎给 `diagramming-skill` 提交改动。

## 这个仓库优先追求什么

- 文本优先的画图工作流
- 默认使用 `Mermaid`
- 本地文件产物，便于保存和 diff
- 尽量少依赖客户端内嵌渲染

## 比较有价值的贡献

- 新的 `Mermaid` 示例
- 更好的 `outline` 模板
- 小而实用的脚本增强
- 更贴近真实使用场景的触发词
- 让 `Codex` / `Claude` 兼容性更好的改进

## 提 PR 前建议

1. 默认坚持 Mermaid-first，除非有很强的理由
2. 文档里避免写死个人机器绝对路径
3. 尽量保持改动小而清晰
4. 如果新增示例，最好同时提供源文件和生成后的 HTML

## 常见本地验证命令

```bash
python3 scripts/create_diagram_bundle.py \
  --title "Example" \
  --slug example \
  --diagram examples/mermaid-intro.mmd \
  --outline examples/mermaid-intro-outline.md \
  --output-dir ./tmp/diagrams
```

## 文档要求

- 变更对外行为时，尽量同步更新 `README.md` 和 `README.zh-CN.md`
- 保持示例文件可用、不过期
