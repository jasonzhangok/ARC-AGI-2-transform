def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    row, col = next(
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 3
    )
    row_step, col_step = 0, 1

    while True:
        next_row = row + row_step
        next_col = col + col_step
        if not (0 <= next_row < height and 0 <= next_col < width):
            break
        obstacle = grid[next_row][next_col]
        if obstacle == 0:
            output[next_row][next_col] = 3
            row, col = next_row, next_col
        elif obstacle == 6:
            row_step, col_step = col_step, -row_step
        elif obstacle == 8:
            row_step, col_step = -col_step, row_step
        else:
            break
    return output
