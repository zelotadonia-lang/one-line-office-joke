"""One-line office joke entry for make.fun.

Writes the joke to /output/entry.txt.
"""

import os

JOKE = "My badge photo is from 2019, and security now waves through a stranger who used to be me."


def main():
    """Write the joke to /output/entry.txt.

    The file holds only the joke text, with no trailing newline.
    """
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("joke must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
