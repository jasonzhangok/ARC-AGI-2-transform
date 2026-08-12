def transform(grid):
    height, width = len(grid), len(grid[0])
    points = [(r, c, grid[r][c]) for r in range(height) for c in range(width) if grid[r][c] != 0]
    output = [[0] * width for _ in range(height)]
    for row, col, color in points:
        for x in range(width):
            output[row][x] = color
        for y in range(height):
            output[y][col] = color
    for i, (row1, col1, _) in enumerate(points):
        for row2, col2, _ in points[i + 1:]:
            output[row1][col2] = 2
            output[row2][col1] = 2
    for row, col, color in points:
        output[row][col] = color
    return output
