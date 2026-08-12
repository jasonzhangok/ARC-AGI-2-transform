from collections import Counter


def transform(grid):
    blocks = []
    for r0 in (0, 3):
        for c0 in (0, 3):
            blocks.append(tuple(tuple(grid[r][c0:c0 + 2]) for r in range(r0, r0 + 2)))
    counts = Counter(blocks)
    unique = next(block for block in blocks if counts[block] == 1)
    return [list(row) for row in unique]
