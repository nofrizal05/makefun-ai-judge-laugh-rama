"""Make the AI Judge Laugh — one original funny line.

Writes exactly one line (plus a trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = (
    "The judge read my joke, laughed so hard it crashed, then deducted "
    "points — turns out the funniest thing in my entry was me trusting "
    "an AI to judge humour."
)


def main():
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if len(LINE) > 280:
        raise ValueError("entry exceeds 280 characters: %d" % len(LINE))

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
