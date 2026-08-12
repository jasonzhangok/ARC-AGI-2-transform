from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = max(counts, key=counts.get)
    separator = min(counts, key=counts.get)
    horizontal = sum(all(value == separator for value in row) for row in grid)
    vertical = sum(
        all(grid[r][c] == separator for r in range(height))
        for c in range(width)
    )
    return [[background] * (vertical + 1) for _ in range(horizontal + 1)]
