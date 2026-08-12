def transform(grid):
    height = len(grid)
    width = len(grid[0])
    corner_row = 0
    corner_col = 0
    border = grid[0][0]
    found = False
    for row in (0, height - 1):
        for col in (0, width - 1):
            color = grid[row][col]
            if all(grid[row][c] == color for c in range(width)) and all(
                grid[r][col] == color for r in range(height)
            ):
                corner_row = row
                corner_col = col
                border = color
                found = True
                break
        if found:
            break

    inside = grid[height - 1 - corner_row][width - 1 - corner_col]
    row_step = 1 if corner_row == 0 else -1
    col_step = 1 if corner_col == 0 else -1
    inner_row = corner_row + row_step
    inner_col = corner_col + col_step
    result = [[8 for _ in range(width)] for _ in range(height)]

    for col in range(width):
        if col != corner_col:
            result[corner_row][col] = inside
        if col != corner_col and col != inner_col:
            result[inner_row][col] = border
    for row in range(height):
        if row != corner_row:
            result[row][corner_col] = inside
        if row != corner_row and row != inner_row:
            result[row][inner_col] = border

    row = corner_row + 2 * row_step
    col = corner_col + 2 * col_step
    while 0 <= row < height and 0 <= col < width:
        result[row][col] = inside
        row += row_step
        col += col_step
    return result
