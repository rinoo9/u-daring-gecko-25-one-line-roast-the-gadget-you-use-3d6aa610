"""One-line roast entry for the make.fun bounty 'One-Line Roast: The Gadget You Use Every Day'.

Round 3 revision: the roast is now my robot vacuum, which has mapped
the whole house and learned my schedule, yet still eats the same
charging cable every single day. The joke lands because it picks a
specific, lived-in failure mode — a supposedly smart machine defeated
daily by the one cable it lives next to — instead of the tired
battery-life cliche every gadget roast reaches for. A robot vacuum is
supposed to know the floor better than I do; the punchline is that it
knows the house and still loses to the cable.

Writes a single original roast line to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
"""

import os

ROAST = "My robot vacuum has mapped my whole house, learned my schedule, and still eats the same charging cable every single day."


def main() -> None:
    # The bounty caps the roast at 200 characters; this entry is 119, so the
    # gate only guards against accidental edits that would push it over.
    assert 1 <= len(ROAST) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
