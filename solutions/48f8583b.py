from collections import Counter


def transform(grid):
    n = len(grid)
    counts = Counter(v for row in grid for v in row)
    marker = min(counts, key=lambda v: counts[v])
    out = [[0] * (n * n) for _ in range(n * n)]
    for br in range(n):
        for bc in range(n):
            if grid[br][bc] != marker:
                continue
            for r in range(n):
                for c in range(n):
                    out[br * n + r][bc * n + c] = grid[r][c]
    return out
