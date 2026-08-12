def transform(grid):
    width = len(grid[0])
    output = [row[:] for row in grid]
    for row in range(len(grid)):
        for col in range(width):
            if grid[row][col] == 4:
                output[row][col] = grid[row][width - 1 - col]
    return output
