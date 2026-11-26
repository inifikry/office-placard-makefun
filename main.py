"""One-line museum placard for an ordinary office stapler,
recast as an ancient ritual artifact. Deterministic: always
writes the same single line to /output/entry.txt."""

import os

PLACARD = (
    "Stapler, c. 1997, pressed steel. Ritual binding instrument: "
    "two sheets joined before witnesses, never to part. "
    "Gift of the Accounts Department, in memory of the merger."
)


def main() -> None:
    # The gate requires 1-180 characters; fail loudly rather than
    # ever writing an over-long line.
    assert 1 <= len(PLACARD) <= 180, len(PLACARD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLACARD + "\n")


if __name__ == "__main__":
    main()
