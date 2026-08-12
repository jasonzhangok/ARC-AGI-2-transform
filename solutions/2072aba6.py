def transform(grid):
    output = [[0] * (2 * len(grid[0])) for _ in range(2 * len(grid))]
    for row, values in enumerate(grid):
        for col, value in enumerate(values):
            if value == 5:
                output[2 * row][2 * col] = 1
                output[2 * row][2 * col + 1] = 2
                output[2 * row + 1][2 * col] = 2
                output[2 * row + 1][2 * col + 1] = 1
    return output
