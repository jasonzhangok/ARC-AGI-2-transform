from collections import Counter


def transform(grid):
    color=Counter(v for row in grid for v in row).most_common(1)[0][0]
    return [[color]*len(grid[0]) for _ in grid]
