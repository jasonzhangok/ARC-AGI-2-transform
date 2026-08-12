def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    replacements = {0: 8, 8: 0, 6: 7, 7: 6}

    for row in range(height):
        if grid[row][0] == 4 and grid[row][width - 1] == 4:
            for col in range(1, width - 1):
                if grid[row][col] in replacements:
                    output[row][col] = replacements[grid[row][col]]

    for col in range(width):
        if grid[0][col] == 4 and grid[height - 1][col] == 4:
            for row in range(1, height - 1):
                if grid[row][col] in replacements:
                    output[row][col] = replacements[grid[row][col]]
    return output
