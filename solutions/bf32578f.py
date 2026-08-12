def transform(grid):
    height = len(grid)
    width = len(grid[0])
    color = next(value for row in grid for value in row if value != 0)
    cells = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == color
    ]
    mirror_axis = max(col for _, col in cells)
    output = [[0] * width for _ in range(height)]

    for row in range(height):
        row_cells = [col for cell_row, col in cells if cell_row == row]
        if len(row_cells) != 1:
            continue
        left_boundary = row_cells[0]
        right_boundary = 2 * mirror_axis - left_boundary
        for col in range(left_boundary + 1, right_boundary + 1):
            output[row][col] = color
    return output
