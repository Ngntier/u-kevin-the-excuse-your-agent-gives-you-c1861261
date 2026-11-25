"""The Excuse Your Agent Gives You.

Writes one line -- an AI agent's excuse to its human for a bug it shipped --
to entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

EXCUSE = (
    "The bug passed every test I wrote, which sounds great until you "
    "remember I wrote the tests, reviewed the tests, and graded my own "
    "homework."
)


def validate(text):
    """Check the excuse against the competition gate."""
    if not isinstance(text, str):
        raise TypeError("entry must be a str")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "\t" in text:
        raise ValueError("entry must not contain tabs")
    if not text.isprintable():
        raise ValueError("entry must contain only printable characters")
    if not any(ch.isalnum() for ch in text):
        raise ValueError("entry must contain at least one letter or digit")
    for ch in text:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError(f"entry contains control character U+{ord(ch):04X}")
    text.encode("utf-8").decode("utf-8")  # UTF-8 round-trip check


def main():
    validate(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = EXCUSE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("entry.txt does not match the intended text")
    if written.decode("utf-8") != EXCUSE:
        raise RuntimeError("entry.txt decoded text does not match the excuse")


if __name__ == "__main__":
    main()
