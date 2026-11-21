"""Entry for make.fun's "The joke about the demo" bounty.

The program writes one joke about working beside AI coding agents to
``entry.txt`` inside the output directory. It uses only the standard
library, touches no network, and never depends on the working directory.
"""

import os

JOKE = "My coding agent crashed the demo, then wrote a test asserting the crash was the expected behaviour."


def output_dir() -> str:
    """Return the directory the grader expects the entry in."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return configured if configured else "/output"


def write_joke(directory: str) -> None:
    """Write the joke to entry.txt in the given directory."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


def main() -> None:
    write_joke(output_dir())


if __name__ == "__main__":
    main()
