def transform(grid):
    height = len(grid)
    width = len(grid[0])
    separator_rows = []
    separator_cols = []
    for row in range(height):
        if grid[row][0] != 0 and all(value == grid[row][0] for value in grid[row]):
            separator_rows.append(row)
    for col in range(width):
        if grid[0][col] != 0 and all(
            grid[row][col] == grid[0][col] for row in range(height)
        ):
            separator_cols.append(col)

    row_bounds = [-1] + separator_rows + [height]
    col_bounds = [-1] + separator_cols + [width]
    for row_index in range(len(row_bounds) - 1):
        for col_index in range(len(col_bounds) - 1):
            block = [
                row[col_bounds[col_index] + 1:col_bounds[col_index + 1]]
                for row in grid[row_bounds[row_index] + 1:row_bounds[row_index + 1]]
            ]
            colors = set()
            for row in block:
                for color in row:
                    if color != 0:
                        colors.add(color)
            if len(colors) == 1:
                return [row[:] for row in block]

    return []
