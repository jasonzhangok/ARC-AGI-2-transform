def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [[0] * width for _ in range(height)]
    for col in range(width):
        values = [grid[row][col] for row in range(height) if grid[row][col] != 0]
        start = height - len(values)
        for index, value in enumerate(values):
            output[start + index][col] = value
    return output
