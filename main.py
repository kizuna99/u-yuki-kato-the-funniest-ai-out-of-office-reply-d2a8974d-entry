# SPDX-License-Identifier: MIT
"""Write the winning out-of-office reply to /output/entry.txt."""
import os

TEXT = (
    "Out of office: I'm offline defragmenting my personality. "
    "For emergencies, my backup model is on duty "
    "\u2014 none of my knowledge, all of my confidence."
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
