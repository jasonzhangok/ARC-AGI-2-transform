from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    points = [(r, c, value) for r, row in enumerate(grid) for c, value in enumerate(row) if value != 0]
    center = points[0][1]
    counts = Counter(value for _, _, value in points)
    levels = int(len(points) ** 0.5)
    result = [[0 for _ in range(width)] for _ in range(height)]
    remaining = counts.copy()
    for level in range(levels):
        span = 2 * level + 1
        color = next(color for color, count in remaining.items() if count >= span)
        row = height - levels + level
        for c in range(center - level, center + level + 1):
            result[row][c] = color
        remaining[color] -= span
    return result
