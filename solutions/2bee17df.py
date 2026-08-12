def transform(grid):
    height = len(grid)
    width = len(grid[0])

    clear_rows = {
        row
        for row in range(1, height - 1)
        if all(grid[row][column] == 0 for column in range(1, width - 1))
    }
    clear_columns = {
        column
        for column in range(1, width - 1)
        if all(grid[row][column] == 0 for row in range(1, height - 1))
    }

    result = [row[:] for row in grid]
    for row in range(1, height - 1):
        for column in range(1, width - 1):
            if grid[row][column] == 0 and (
                row in clear_rows or column in clear_columns
            ):
                result[row][column] = 3
    return result
