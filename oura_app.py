import argparse
import csv
from typing import List


def read_scores(path: str, column: str) -> List[int]:
    """Read readiness scores from a CSV file."""
    scores: List[int] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            val = row.get(column)
            if not val:
                continue
            try:
                scores.append(int(float(val)))
            except ValueError:
                continue
    return scores


def calculate_trend(values: List[int]) -> float:
    """Return the difference between the last 7 day mean and previous 7 day mean."""
    if len(values) < 14:
        raise ValueError("At least 14 values are required to compute trend")
    recent = values[-7:]
    previous = values[-14:-7]
    return sum(recent) / 7 - sum(previous) / 7


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze Oura Ring readiness trends from a CSV export"
    )
    parser.add_argument("csv_file", help="CSV file containing readiness scores")
    parser.add_argument(
        "--column", default="score", help="Column name holding the readiness score"
    )
    args = parser.parse_args()

    scores = read_scores(args.csv_file, args.column)
    if len(scores) < 14:
        raise SystemExit("Not enough data to compute trend")

    trend = calculate_trend(scores)
    if trend > 0:
        msg = "Your readiness score has improved over the past week."
    elif trend < 0:
        msg = "Your readiness score has declined over the past week."
    else:
        msg = "Your readiness score is stable week over week."
    print(msg)


if __name__ == "__main__":
    main()
