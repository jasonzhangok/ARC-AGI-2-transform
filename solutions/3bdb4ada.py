def transform(grid):
    height, width = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    colors = {value for row in grid for value in row if value != 0}
    for color in colors:
        points = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == color]
        top, bottom = min(r for r, _ in points), max(r for r, _ in points)
        left, right = min(c for _, c in points), max(c for _, c in points)
        middle = (top + bottom) // 2
        for c in range(left + 1, right, 2):
            result[middle][c] = 0
    return result
