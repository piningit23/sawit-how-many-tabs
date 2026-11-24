"""How Many Tabs Do You Have Open? — entry count: "47".

Why 47, against the judge brief:
- Surprising: far above the handful of tabs most people keep open,
  the number of a genuine tab hoarder — yet still a count a real
  person could honestly have open right now.
- Believable: a specific, odd, non-round number; nobody "picks" 47
  to shock, they arrive at 47 by never closing anything.
- A life behind it: 47 tabs is the browser of someone who opens
  "just one more" article, doc and video and means to read them all.
- Not a round number: 50 or 100 would read as a guess someone made
  up; 47 reads as a count someone actually looked at and reported.
"""

COUNT = "47"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    # Guard: the entry must be digits only, 1-5 chars, no spaces.
    if not (1 <= len(COUNT) <= 5) or not COUNT.isdigit():
        raise SystemExit("entry count must be 1-5 digits")

    # Write digits only, no trailing newline: the gate allows 1-5
    # characters, and the judge compares the exact bytes.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(COUNT)

    # Verify what landed on disk is exactly the count, nothing else.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != COUNT.encode("utf-8"):
        raise SystemExit("output mismatch: entry.txt does not match the count")


if __name__ == "__main__":
    main()
