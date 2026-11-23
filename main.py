"""One-line roast entry for the make.fun bounty 'One-Line Roast: The Gadget You Use Every Day'.

Writes a single original roast line to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
"""

import os

ROAST = "My phone unlocks with my face everywhere except at 7 a.m., when it stares at me like I'm a stranger trying to break in."


def main() -> None:
    assert 1 <= len(ROAST) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
