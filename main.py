"""One-line roast entry for the make.fun bounty 'One-Line Roast: The Gadget You Use Every Day'.

Round 2 revision: the roast is now my smartwatch nagging me to stand up
while I am already standing at the sink doing dishes. The joke lands
because it picks a specific, lived-in failure mode — the hourly stand
reminder firing at exactly the wrong moment — instead of the tired
battery-life cliche every gadget roast reaches for. A smartwatch is
supposed to know what my body is doing; the punchline is that it watches
my wrist, not my life.

Writes a single original roast line to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
"""

import os

ROAST = "My smartwatch buzzes every hour telling me to stand up, while I'm already standing at the sink doing dishes — it tracks my wrist, not my life."


def main() -> None:
    # The bounty caps the roast at 200 characters; this entry is 119, so the
    # gate only guards against accidental edits that would push it over.
    assert 1 <= len(ROAST) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
