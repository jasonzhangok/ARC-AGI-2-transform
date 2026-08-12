from collections import Counter


def transform(grid):
    counts = Counter(value for row in grid for value in row if value != 0)
    color = min(counts, key=counts.get)
    points = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == color]
    top, bottom = min(r for r, _ in points), max(r for r, _ in points)
    left, right = min(c for _, c in points), max(c for _, c in points)
    return [[color] * (right - left + 1) for _ in range(bottom - top + 1)]
