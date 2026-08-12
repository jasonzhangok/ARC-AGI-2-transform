def transform(grid):
    output = [row[:] for row in grid]
    if not grid or not grid[0]:
        return output

    height = len(grid)
    width = len(grid[0])
    center_row = -1
    center_col = -1
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            color = grid[row][col]
            if (color != 0
                    and grid[row - 1][col] == color
                    and grid[row + 1][col] == color
                    and grid[row][col - 1] == color
                    and grid[row][col + 1] == color):
                center_row = row
                center_col = col
                break
        if center_row >= 0:
            break

    if center_row < 0:
        return output

    for row_step, col_step in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        row = center_row + row_step
        col = center_col + col_step
        while 0 <= row < height and 0 <= col < width:
            output[row][col] = 1
            row += row_step
            col += col_step

    for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        distance = 2
        row = center_row + 2 * row_step
        col = center_col + 2 * col_step
        while 0 <= row < height and 0 <= col < width:
            if distance % 3 == 1:
                output[row][col] = 4
            else:
                output[row][col] = 8
            distance += 1
            row += row_step
            col += col_step

    return output
