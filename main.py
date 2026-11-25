"""One-line roast entry for the make.fun bounty 'One-Line Roast: The Gadget You Use Every Day'.

Latest revision: the roast is now my washing machine, which celebrates
the end of every cycle with a cheerful little tune — as if getting the
clothes clean were its triumph, while the folding, the hanging up, and
the putting away are somehow still my job. The joke works because it
catches a real, specific behaviour: the machine genuinely congratulates
itself, out loud, for the easy half of the chore and leaves the boring
half to me. A washing machine that sings about its own success holds a
very generous opinion of itself.

Writes a single original roast line to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
"""

import os

ROAST = "My washing machine plays a cheerful little tune when it finishes, like the laundry was its triumph and the folding is somehow still my job."


def main() -> None:
    # The bounty caps the roast at 200 characters; this entry is 139, so the
    # check only guards against accidental edits that would push it over.
    assert 1 <= len(ROAST) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
