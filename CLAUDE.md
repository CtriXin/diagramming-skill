# diagramming-skill

> 任何 agent 接手前先读仓库根目录 `HANDBOOK.md`，再读这个文件。

## 这是什么

`diagramming-skill` 是一个统一的画图 skill 主体，给 `Codex` 和 `Claude` 共用。

默认策略：

- 默认用 `Mermaid`
- 默认产出本地文件
- 默认交付 `mmd + outline + html`
- 只有用户明确要手绘风时才走本地 `Excalidraw`

## 文件结构

```text
diagramming-skill/
├── CLAUDE.md
├── SKILL.md
├── .gitignore
├── .ai/
│   └── agent-release-notes.md
└── scripts/
    ├── create_diagram_bundle.py
    └── render_mermaid_html.py
```

## Release Note Handoff

每次有已落地改动后，都要把本轮摘要追加到：

`./.ai/agent-release-notes.md`

这个文件必须保持在 `.gitignore` 内，默认不进 git。

## 当前约定

- `Codex` 本地安装路径：`~/.codex/skills/diagramming`
- `Claude` 本地安装路径：`~/.claude/skills/diagramming`
- 两边都应该是指向本目录的 symlink
- 仓库文档与脚本说明优先使用相对路径，不写死个人机器绝对路径

## 不要做的事

- 不要把聊天内嵌渲染当成唯一交付物
- 不要默认依赖 `excalidraw_remote`
- 不要只给图，不给 `outline`
