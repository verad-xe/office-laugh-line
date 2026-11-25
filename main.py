#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original line about office life.

Writes a single joke (under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, then self-checks it against the
competition gate: UTF-8 text of 1 to 200 characters, not only
white space.
"""

import os

LINE = "My performance review said I need to 'be more visible', so I now attend meetings in a hi-vis vest."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    # Gate self-check: 1 to 200 characters, not only white space,
    # and a single line (no embedded newline).
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

    # Verify what was actually written.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written entry differs from the line"
    assert 1 <= len(written) <= 200
    assert written.strip()


if __name__ == "__main__":
    main()
