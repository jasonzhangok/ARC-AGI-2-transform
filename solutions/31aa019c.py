from collections import Counter


def transform(grid):
    counts = Counter(value for row in grid for value in row if value != 0)
    color = next(value for value, count in counts.items() if count == 1)
    r, c = next((r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == color)
    result = [[0] * len(grid[0]) for _ in grid]
    for rr in range(r - 1, r + 2):
        for cc in range(c - 1, c + 2):
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]):
                result[rr][cc] = 2
    result[r][c] = color
    return result
