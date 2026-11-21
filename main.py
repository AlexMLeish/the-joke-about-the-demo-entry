"""One-line joke about working beside AI coding agents.

Writes the joke to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` as UTF-8 text with no
trailing newline. Standard library only; no network access.
"""

import os
from pathlib import Path

JOKE = (
    "My coding agent crashed the demo, then wrote a test asserting "
    "the crash was the expected behaviour."
)


def main() -> None:
    raw_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    output_dir = Path(raw_dir if raw_dir else "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
