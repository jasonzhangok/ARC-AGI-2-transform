def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for start_col in range(width):
        if grid[height - 1][start_col] != 2:
            continue
        row, col = height - 1, start_col
        blocked = False
        while row > 0 and not blocked:
            while grid[row - 1][col] == 5:
                if col + 1 == width or grid[row][col + 1] == 5:
                    blocked = True
                    break
                col += 1
                output[row][col] = 2
            if not blocked:
                row -= 1
                output[row][col] = 2
    return output
