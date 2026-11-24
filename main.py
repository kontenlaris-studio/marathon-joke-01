"""One-Liner Marathon entry: a GPS with a mother's tone of disappointment."""

import os

JOKE = (
    "My GPS said 'recalculating' in the exact tone my mother uses "
    "when I disappoint her. I have now driven to three wrong cities "
    "just to avoid hearing it again."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote {path} ({len(JOKE)} characters)")


if __name__ == "__main__":
    main()
