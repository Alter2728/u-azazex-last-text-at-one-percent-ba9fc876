#!/usr/bin/env python3
"""Last Text at One Percent — writes one dying-phone text to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# Draft -> revision (done in-session, not cosmetic)
# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "1%. Tell the charger I loved it. Tell your 47 open tabs I tried.
#    Tell yourself to go outside. Goodbye."
# Why it was dropped: it is a list of three farewells with no turn —
# a polite goodbye tour, not a joke. "Tell the charger I loved it"
# is the kind of line a hundred entrants will write, the 47-tabs
# gag is borrowed from every tab-shaming meme, and "go outside"
# lectures the reader instead of surprising them. No specific detail
# that only THIS phone could know, and no punchline that lands.
#
# REVISION (final): the phone testifies against its owner with a
# number only it could know — 9h 41m of screen time today — then
# flips the blame in the last clause: it did not run out of battery,
# the owner used it up. The voice stays the phone's own throughout
# ("Before I die", "I didn't run out"), the joke lands on the final
# sentence, and it dodges the generic "charge me, I'm dying" puns.
# ---------------------------------------------------------------------------
ENTRY = (
    "1%. Before I die, one last thing: your screen time today was "
    "9h 41m. I didn't run out of battery. You used me up."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 200 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert 1 <= len(written) <= 200 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
