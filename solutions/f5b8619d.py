def transform(grid):
    marked_columns = {
        col
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] != 0
    }
    tile = [
        [8 if value == 0 and col in marked_columns else value for col, value in enumerate(row)]
        for row in grid
    ]
    doubled_rows = [row + row for row in tile]
    return doubled_rows + [row[:] for row in doubled_rows]
