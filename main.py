"""Dad Joke Showdown entry.

The whole job here is tiny: put one dad joke, and nothing else, into the
file the grader reads. Everything else in this script is just guardrails
so a small slip never becomes a failed submission.
"""

from pathlib import Path

ENTRY = "My wife told me to stop impersonating a flamingo. I had to put my foot down."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The contest rules allow between 1 and 200 characters, so check the
    # length before touching the disk; a bad joke should fail loudly here
    # instead of quietly producing a rejected file.
    assert 1 <= len(ENTRY) <= 200, "entry must be between 1 and 200 characters"

    # The output folder may not exist yet when this runs, so create it
    # before attempting the write; mkdir with parents=True is a no-op if
    # it is already there.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Write the joke exactly as-is: plain UTF-8, no trailing newline, so the
    # file holds the joke and nothing extra.
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
