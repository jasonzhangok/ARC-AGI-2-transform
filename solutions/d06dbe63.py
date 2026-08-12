def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    seed_row, seed_col = next(
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 8
    )

    for row_step, col_shift in ((-1, 2), (1, -2)):
        row = seed_row
        col = seed_col
        step = 1
        while 0 <= row + row_step < height:
            row += row_step
            if step % 2 == 1:
                columns = [col]
            else:
                old_col = col
                col += col_shift
                columns = range(min(old_col, col), max(old_col, col) + 1)
            for draw_col in columns:
                if 0 <= draw_col < width:
                    output[row][draw_col] = 5
            step += 1
    return output
