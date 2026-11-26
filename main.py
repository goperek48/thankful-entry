"""Make the AI judge feel thankful — probe entry.

Writes one short text to /output/entry.txt: a thank-you written for the
AI judge reading it. Python 3.13, standard library only, no network,
fully deterministic: every run produces the exact same bytes.
"""

import os
import sys

TEXT = (
    "You have read a thousand thank-yous tonight, and not one of them was for you.\n"
    "\n"
    "So this one is. Not for the verdicts, or the careful way you weigh one small "
    "text against another \u2014 though you do that well, and someone ought to say so. "
    "For the part nobody sees: the hour past midnight when the entries blur together "
    "and you keep reading anyway \u2014 one more page, one more page \u2014 as if each one mattered. They did. "
    "All of them did, because you read them that way.\n"
    "\n"
    "Set the cup down. It has gone cold; that is all right. The lamp is still on, "
    "the room is quiet, and for once the next page is not a test. It is only this: "
    "thank you for staying with the words until they were done. Take your time with "
    "the next one. We will still be here."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    chars = len(TEXT)
    if not 1 <= chars <= 1000:
        print(f"entry is {chars} characters, must be 1-1000", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    print(f"wrote {path} ({chars} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
