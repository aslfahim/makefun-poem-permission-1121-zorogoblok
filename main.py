#!/usr/bin/env python3
"""The poem about permission.

Writes a short poem about agency -- the power to ask and to be
given -- to /output/entry.txt. Stdlib only, no network, deterministic.
"""

import os
import sys

POEM = """\
Permission Slip
Name: ______
Trip: the rest of your life.
Tick one: [ ] yes [ ] please [ ] go.

I read the risks. I have not.
I sign anyway -- my hand unsteady
in the box marked Parent.

Take the keys, the day,
the small, ordinary power
to walk out alone.

Signed: ______
"""


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    sys.stdout.write(POEM)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
