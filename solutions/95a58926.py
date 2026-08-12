from collections import Counter


def transform(grid):
    h, w = len(grid), len(grid[0])
    horizontal = [r for r in range(h) if grid[r].count(5) > w // 2]
    vertical = [c for c in range(w) if sum(grid[r][c] == 5 for r in range(h)) > h // 2]
    special = Counter(value for row in grid for value in row if value not in (0, 5)).most_common(1)[0][0]
    output = [[0] * w for _ in range(h)]
    for r in horizontal:
        output[r] = [5] * w
    for c in vertical:
        for r in range(h):
            output[r][c] = 5
    for r in horizontal:
        for c in vertical:
            output[r][c] = special
    return output
