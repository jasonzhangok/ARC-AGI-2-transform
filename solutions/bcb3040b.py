def transform(grid):
    result = [row[:] for row in grid]
    endpoints = [
        (row, col)
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] == 2
    ]
    start_row, start_col = endpoints[0]
    end_row, end_col = endpoints[1]
    row_step = (end_row > start_row) - (end_row < start_row)
    col_step = (end_col > start_col) - (end_col < start_col)
    length = max(abs(end_row - start_row), abs(end_col - start_col))

    for offset in range(length + 1):
        row = start_row + offset * row_step
        col = start_col + offset * col_step
        result[row][col] = 3 if grid[row][col] == 1 else 2
    return result
