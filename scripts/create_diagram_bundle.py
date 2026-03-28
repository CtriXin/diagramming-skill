#!/usr/bin/env python3
import argparse
import html
import json
import shutil
from pathlib import Path


HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f7f7f3;
      --card: #ffffff;
      --text: #1f2937;
      --muted: #6b7280;
      --border: #e5e7eb;
    }}
    body {{
      margin: 0;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: linear-gradient(180deg, #f3f4f6 0%, #f8fafc 100%);
      color: var(--text);
    }}
    .wrap {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 24px;
    }}
    .card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: 24px;
    }}
    p {{
      margin: 0 0 20px;
      color: var(--muted);
      font-size: 14px;
    }}
    pre.mermaid {{
      margin: 0;
      overflow: auto;
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <h1>{title}</h1>
      <p>Open this file in a browser to view the Mermaid diagram.</p>
      <pre class="mermaid">{diagram}</pre>
    </div>
  </div>
  <script type="module">
    import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
    mermaid.initialize({{
      startOnLoad: true,
      securityLevel: "loose",
      theme: "default"
    }});
  </script>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a local diagram bundle: Mermaid source + outline + browser-openable HTML.")
    parser.add_argument("--title", required=True, help="Diagram title")
    parser.add_argument("--slug", required=True, help="Base filename slug")
    parser.add_argument("--diagram", required=True, help="Path to Mermaid source (.mmd)")
    parser.add_argument("--outline", required=True, help="Path to outline markdown")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    diagram_path = Path(args.diagram).expanduser().resolve()
    outline_path = Path(args.outline).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    dest_diagram = output_dir / f"{args.slug}.mmd"
    dest_outline = output_dir / f"{args.slug}-outline.md"
    dest_html = output_dir / f"{args.slug}.html"

    if diagram_path != dest_diagram:
        shutil.copyfile(diagram_path, dest_diagram)
    if outline_path != dest_outline:
        shutil.copyfile(outline_path, dest_outline)

    source = diagram_path.read_text(encoding="utf-8")
    dest_html.write_text(
        HTML_TEMPLATE.format(
            title=html.escape(args.title),
            diagram=html.escape(source),
        ),
        encoding="utf-8",
    )

    print(json.dumps({
        "title": args.title,
        "diagram": str(dest_diagram),
        "outline": str(dest_outline),
        "html": str(dest_html),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
