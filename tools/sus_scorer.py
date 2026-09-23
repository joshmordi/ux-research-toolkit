#!/usr/bin/env python3
"""Score System Usability Scale (SUS) questionnaires from a CSV file.

The CSV should have one row per participant and 10 columns (Q1..Q10),
each a number from 1 to 5.

Scoring follows Brooke (1996):
  - odd-numbered items:  contribution = response - 1
  - even-numbered items: contribution = 5 - response
  - SUS score = sum of contributions * 2.5   (range 0-100)

Usage:
    python3 sus_scorer.py responses.csv

Example CSV:
    Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10
    4,2,5,1,4,2,5,2,4,1
    5,1,4,2,5,1,4,1,5,2
"""
import csv
import sys


def sus_score(responses):
    """responses: list of 10 ints, each 1-5. Returns score 0-100."""
    if len(responses) != 10:
        raise ValueError(f"expected 10 responses, got {len(responses)}")
    total = 0.0
    for i, r in enumerate(responses, start=1):
        if not 1 <= r <= 5:
            raise ValueError(f"Q{i} out of range (1-5): {r}")
        total += (r - 1) if i % 2 == 1 else (5 - r)
    return total * 2.5


def interpret(score):
    if score >= 80.3:
        return "A - excellent"
    if score >= 68:
        return "B - above average"
    if score >= 51:
        return "C - below average, worth improving"
    return "D/F - poor, needs work"


def main():
    if len(sys.argv) != 2:
        print(__doc__.strip().splitlines()[-8])
        print("Usage: python3 sus_scorer.py responses.csv")
        sys.exit(1)
    scores = []
    with open(sys.argv[1], newline="") as f:
        for n, row in enumerate(csv.reader(f), start=1):
            row = [c.strip() for c in row if c.strip() != ""]
            if n == 1 and not row[0].lstrip("-").isdigit():
                continue  # header row
            try:
                responses = [int(float(c)) for c in row[:10]]
            except ValueError:
                print(f"row {n}: skipped (non-numeric values)")
                continue
            try:
                scores.append(sus_score(responses))
            except ValueError as e:
                print(f"row {n}: skipped ({e})")
    if not scores:
        print("no valid responses found")
        sys.exit(1)
    print(f"participants: {len(scores)}")
    print(f"mean SUS:      {sum(scores) / len(scores):.1f}")
    print(f"min / max:     {min(scores):.1f} / {max(scores):.1f}")
    print(f"interpretation: {interpret(sum(scores) / len(scores))}")
    print()
    for i, s in enumerate(scores, start=1):
        print(f"  participant {i}: {s:.1f}")


if __name__ == "__main__":
    main()
