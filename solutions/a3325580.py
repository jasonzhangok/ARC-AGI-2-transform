from collections import Counter


def transform(grid):
    counts = Counter(v for row in grid for v in row if v != 0)
    size = max(counts.values())
    colors = [v for v, n in counts.items() if n == size]
    colors.sort(key=lambda v: min(c for row in grid for c, x in enumerate(row) if x == v))
    return [colors[:] for _ in range(size)]
