def transform(grid):
    height = len(grid)
    width = len(grid[0])
    cells = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 7
    ]
    bottom = max(row for row, _ in cells)
    center = next(col for row, col in cells if row == bottom)
    output = [[0] * width for _ in range(height)]

    for row in range(bottom, -1, -1):
        radius = bottom - row
        for col in range(center - radius, center + radius + 1):
            if 0 <= col < width:
                output[row][col] = 7 if (col - center) % 2 == 0 else 8
    return output
