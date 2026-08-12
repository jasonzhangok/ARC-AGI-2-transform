def transform(grid):
    size = len(grid)
    output = [row[:] for row in grid]
    for row in range(size):
        for column in range(size):
            if grid[row][column] != 4:
                continue
            symmetric_cells = [(row, size - 1 - column),
                               (size - 1 - row, column),
                               (column, row),
                               (size - 1 - column, size - 1 - row),
                               (size - 1 - row, size - 1 - column),
                               (column, size - 1 - row),
                               (size - 1 - column, row)]
            for symmetric_row, symmetric_column in symmetric_cells:
                if grid[symmetric_row][symmetric_column] != 4:
                    output[row][column] = grid[symmetric_row][symmetric_column]
                    break
    return output
