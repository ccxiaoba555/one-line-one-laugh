"""One Line, One Laugh — a one-line entry for make.fun.

The program writes exactly one funny line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

LINE = (
    "I told my smart house to make me feel in charge, so it changed the locks, "
    "formed a tenants' union, and now negotiates rent through the doorbell."
)

MAX_CHARS = 200


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, cap is {MAX_CHARS}"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")

    # Read back and verify what actually landed on disk, byte for byte.
    written = out_path.read_text(encoding="utf-8")
    assert written == text, "read-back mismatch: entry.txt differs from LINE"
    assert len(written) == len(text) == 144, "read-back length mismatch"
    print(f"wrote {len(text)} chars to {out_path} (read-back verified)")


if __name__ == "__main__":
    main()
