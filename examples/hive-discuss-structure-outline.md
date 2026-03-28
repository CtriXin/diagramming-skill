# hive-discuss Structure

## One-line summary

`hive-discuss` is not discuss-only. It combines discussion, a2a review, cross-review, and debate capabilities in one package.

## Structure

- Entry points
- Core package
- Capability functions
- Config layer
- Model caller
- Outputs

## Key relations

- `/hive-discuss` and `/hive-a2a` are wrappers over the same core package
- Config selects models and routes
- `ModelCaller` abstracts the underlying model execution

## Notes

- Good example for architecture or package-level diagrams
