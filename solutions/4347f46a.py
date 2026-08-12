from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    result = [row[:] for row in grid]
    for color in {value for row in grid for value in row if value != background}:
        points = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == color]
        top, bottom = min(r for r, _ in points), max(r for r, _ in points)
        left, right = min(c for _, c in points), max(c for _, c in points)
        for r, c in points:
            if top < r < bottom and left < c < right:
                result[r][c] = background
    return result
