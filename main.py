"""One-line roast entry for the make.fun bounty 'One-Line Roast: The Gadget You Use Every Day'.

The roast: my phone's face unlock works everywhere except at 7 a.m., when
it stares at me like I'm a stranger trying to break in. The joke lands
because it picks a specific, lived-in failure mode — the half-awake
morning face, pillow-creased and squinting — instead of the tired
battery-life cliché every gadget roast reaches for. Face unlock is
supposed to know me better than anyone; the punchline is that it is the
one thing that fails to recognise me at the exact moment I need it most.

Writes a single original roast line to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
"""

import os

ROAST = "My phone unlocks with my face everywhere except at 7 a.m., when it stares at me like I'm a stranger trying to break in."


def main() -> None:
    # The bounty caps the roast at 200 characters; this entry is 119, so the
    # gate only guards against accidental edits that would push it over.
    assert 1 <= len(ROAST) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
