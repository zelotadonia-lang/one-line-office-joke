"""One-line office joke entry for the make.fun 24-hour sprint.

Writes the entry text to /output/entry.txt, with no trailing newline,
so the file holds exactly the joke text and nothing else.
"""

import os

JOKE = "The vendor promised delivery in two weeks, so we planned around it, waited six, and renamed the delay a rollout."


def main():
    """Write JOKE to /output/entry.txt after the length gate."""
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(JOKE))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
