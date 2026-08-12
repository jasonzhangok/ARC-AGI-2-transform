def transform(grid):
    height, width = len(grid), len(grid[0])
    result = [[0 for _ in range(width)] for _ in range(height)]
    points = [(r, c) for r in range(height) for c in range(width) if grid[r][c] != 0]
    bottom = max(r for r, _ in points)
    for r, c in points:
        shifted = c - (bottom - r)
        if 0 <= shifted < width:
            result[r][shifted] = grid[r][c]
    return result
