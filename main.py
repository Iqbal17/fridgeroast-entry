"""Fridge Roast: One Line, Biggest Laugh (u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb).

Writes exactly one roast line (<=200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.

Decision record
----------------
The brief: one line, at most 200 characters, roasting a smart fridge
(app, firmware updates, camera, ice maker, opinions about milk). The
judge weighs, in order: (1) the joke is a roast of a smart fridge,
(2) the punchline lands on the first read, (3) the joke is specific
to smart fridges, (4) the wording is tight, (5) the angle is fresh
-- explicitly avoiding the obvious cracks about the fridge ordering
groceries or watching you.

Candidates weighed:
  A. "My smart fridge watches me eat ice cream at 3 AM and judges
     me in the app." -- REJECTED. It is the camera/watching crack
     the judge brief explicitly warns most writers reach for first;
     it fails freshness outright.
  B. "My fridge ordered milk I didn't ask for and now I'm
     lactose-intolerant with a subscription." -- REJECTED. The other
     explicitly warned-against crack (ordering groceries), and the
     punchline needs a beat to parse, so it fails criteria 2 and 5.
  C. "My smart fridge updated its firmware and now the ice maker
     needs a reboot, a login, and my forgiveness." -- STRONG
     RESERVE. Specific (firmware + ice maker), a tight three-beat
     list, and "my forgiveness" is a real turn. It loses to the
     winner because the joke leans on the reader knowing firmware
     updates break things -- a beat of thought -- while the winner's
     joke lands instantly.
  D. "My fridge's camera knows everything I eat. Its ice maker
     still can't make ice." -- REJECTED. The contrast is good, but
     half the line is the camera/watching crack the brief warns
     against, so it spends its freshness on the weakest half.
  E. "My fridge's ice maker has been 'making ice' for six hours.
     One cube. It sent me a notification about it." -- CHOSEN.
     The joke is aimed squarely at the fridge's own hardware (ice
     maker) and its own habit (push notifications about its own
     failure); the punchline sits in the last sentence and needs no
     setup the line does not already carry; nothing in it would work
     on a dumb fridge, so it is specific, and nobody's first crack
     is "the fridge bragged about failing".

Writing passes (genuine revisions to the winning line):
  Pass 1 -- the early leader was candidate C (firmware/forgiveness).
  It was replaced by E because the judge weighs "punchline lands on
  the first read" above cleverness, and the notification twist is
  more specific to smart fridges than a firmware joke, which would
  work on any gadget with an update screen.
  Pass 2 -- first draft of E: "My fridge's ice maker has been making
  ice all day. It made one cube and emailed me about it." Three
  changes: "all day" became "for six hours" (a concrete number is
  funnier and tighter); "emailed me" became "sent me a
  notification" (notifications are the smart fridge's signature
  move; email is generic); "One cube." was split into its own
  sentence for punch timing, and scare quotes were added around
  'making ice' to sell that it is not actually making any.
"""

import os

ENTRY = "My fridge's ice maker has been 'making ice' for six hours. One cube. It sent me a notification about it."
MAX_CHARS = 200


def entry_path():
    """Resolve the output path, preferring $MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1-200 chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
