"""One-Line Office Joke: 24-Hour Sprint.

Writes one short joke about office life to /output/entry.txt.

The joke: a standup claim of "no blockers" told while the speaker's own
broken deployment is still rolling back behind them — the deadpan status
update is itself the lie, and the rollback is the punchline.
"""

import os

JOKE = (
    "In standup I said 'no blockers' while the deployment I broke "
    "was still rolling back behind me."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1-200 characters, not whitespace
    # only. Check here so a bad joke fails loudly at build time instead
    # of silently scoring 0 after submission.
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(
            f"joke must be 1-200 characters, got {len(JOKE)}"
        )
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
