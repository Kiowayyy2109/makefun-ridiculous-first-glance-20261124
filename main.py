"""Ridiculous at First Glance, Real by the Second.

Writes a single-sentence startup pitch (at most 200 characters) to
/output/entry.txt. The pitch is a fixed, deterministic string: one
sentence pitching a bizarre idea that turns out to be a real business.
"""

import os

# Output path: the grader reads /output/entry.txt. ENTRY_OUTPUT lets a
# local run point elsewhere without changing the default.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

PITCH = (
    "We bottle the air from the exact spot where celebrities sneezed and "
    "sell it to collectors, because fans already pay thousands for stars' "
    "trash and air is the only souvenir nobody can fake."
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the pitch after enforcing the gate: 1-200 chars, one sentence."""
    text = text.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"pitch must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")
    if not text.endswith(".") or text.count(".") != 1:
        raise ValueError("pitch must be exactly one sentence")
    return text


def main() -> None:
    text = validate(PITCH)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
