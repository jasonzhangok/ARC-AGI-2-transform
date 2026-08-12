from collections import Counter


def transform(grid):
    h = len(grid)
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    start = next(r for r, row in enumerate(grid) if any(value != background for value in row))
    motif = [row[:] for row in grid[start:]]
    period = len(motif)
    return [motif[(r - start) % period][:] for r in range(h)]
