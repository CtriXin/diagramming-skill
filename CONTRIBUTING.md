# Contributing

Thanks for contributing to `diagramming-skill`.

## What This Repository Optimizes For

- Text-first diagram workflows
- Mermaid as the default format
- Local file outputs that are durable and diffable
- Minimal dependence on client-side widget rendering

## Good Contributions

- New Mermaid examples
- Better outline patterns
- Small, practical script improvements
- Trigger phrase improvements for real user prompts
- Better portability across Codex and Claude environments

## Before You Open a PR

1. Keep the default workflow Mermaid-first unless there is a strong reason not to
2. Avoid machine-specific absolute paths in docs
3. Prefer small, reviewable changes
4. If you add a new example, include both the source and the generated HTML

## Typical Local Checks

```bash
python3 scripts/create_diagram_bundle.py \
  --title "Example" \
  --slug example \
  --diagram examples/mermaid-intro.mmd \
  --outline examples/mermaid-intro-outline.md \
  --output-dir ./tmp/diagrams
```

## Documentation

- Keep `README.md` and `README.zh-CN.md` aligned when changing user-facing behavior
- Keep examples current
