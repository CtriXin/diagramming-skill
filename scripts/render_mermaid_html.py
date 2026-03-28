#!/usr/bin/env python3
import argparse
import html
import json
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
    parser = argparse.ArgumentParser(description="Render a Mermaid source file into a browser-openable HTML file.")
    parser.add_argument("input", help="Path to the Mermaid source file (.mmd or .md)")
    parser.add_argument("output", help="Path to the output HTML file")
    parser.add_argument("--title", default="Mermaid Diagram", help="HTML page title")
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    source = input_path.read_text(encoding="utf-8")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        HTML_TEMPLATE.format(
            title=html.escape(args.title),
            diagram=html.escape(source),
        ),
        encoding="utf-8",
    )
    print(json.dumps({
        "input": str(input_path),
        "output": str(output_path),
        "title": args.title,
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
