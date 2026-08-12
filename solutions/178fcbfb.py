def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for row in range(height):
        if 1 in grid[row]:
            output[row] = [1] * width
        elif 3 in grid[row]:
            output[row] = [3] * width
    columns = {
        col
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 2
    }
    for col in columns:
        for row in range(height):
            if 1 not in grid[row] and 3 not in grid[row]:
                output[row][col] = 2
    return output
