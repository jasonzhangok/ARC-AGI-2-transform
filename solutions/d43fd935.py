def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    block = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 3
    ]
    block_rows = {row for row, _ in block}
    block_cols = {col for _, col in block}
    top, bottom = min(block_rows), max(block_rows)
    left, right = min(block_cols), max(block_cols)

    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            if color in (0, 3):
                continue
            if row in block_rows:
                if col < left:
                    columns = range(col + 1, left)
                elif col > right:
                    columns = range(right + 1, col)
                else:
                    columns = ()
                for draw_col in columns:
                    output[row][draw_col] = color
            if col in block_cols:
                if row < top:
                    rows = range(row + 1, top)
                elif row > bottom:
                    rows = range(bottom + 1, row)
                else:
                    rows = ()
                for draw_row in rows:
                    output[draw_row][col] = color
    return output
