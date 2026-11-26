"""Write a one-line joke about office life.

The joke turns on a real office detail -- the printer that
only jams when it matters -- and lands its laugh in the
last few words. The program writes exactly that one line
to /output/entry.txt.
"""

import os

# The entry: the office printer, and its suspicious sense of timing.
# "Smell a deadline" is tighter than a sensor: the joke lands sooner.
ENTRY = "Our printer can smell a deadline, because it has never once jammed on a document nobody needed."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
