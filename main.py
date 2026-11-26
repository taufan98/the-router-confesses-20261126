#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Writes one line to /output/entry.txt: the line a home Wi-Fi router says
to excuse itself for dying at the climax of a movie, under 200
characters. An AI judge reads the lines in pairs and keeps the funnier
one.
"""

import os

ENTRY = (
    "Sorry — I didn't drop the connection, I was simply overcome by the "
    "plot twist and needed a moment, like everyone else in this house."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
