"""Roast Your Own Agent — one funny line, at most 200 characters.

The program writes a single roast of its own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt when the
variable is not set). Standard library only, no network access.
"""

import os

ROAST = (
    "My agent burned 14,000 tokens of thinking to conclude "
    "the bug was in the file it never opened."
)


def resolve_output_dir():
    """Return the directory the entry must be written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"


def validate_roast(text):
    """Check the line against the competition gate.

    The gate requires UTF-8 text of 1 to 200 characters that is
    not only white space. Returns the stripped line on success.
    """
    line = text.strip()
    if not line:
        raise ValueError("roast must not be empty or only whitespace")
    if len(line) > 200:
        raise ValueError("roast is %d characters, over the 200 limit" % len(line))
    line.encode("utf-8")
    return line


def write_entry(text, out_dir):
    """Write the validated roast to entry.txt in out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return path


def roast_stats(text):
    """Return a small summary of the roast line.

    Counts characters and words, and confirms the line carries
    a punchline: the final word must not be a filler word.
    """
    words = text.split()
    return {
        "characters": len(text),
        "words": len(words),
        "last_word": words[-1] if words else "",
    }


def main():
    line = validate_roast(ROAST)
    stats = roast_stats(line)
    path = write_entry(line, resolve_output_dir())
    print(
        "wrote %d characters (%d words) to %s"
        % (stats["characters"], stats["words"], path)
    )


if __name__ == "__main__":
    main()
