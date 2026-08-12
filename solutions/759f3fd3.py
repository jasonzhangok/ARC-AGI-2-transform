def transform(grid):
    """在十字交点周围绘制间隔一格的方形环。"""
    height = len(grid)
    width = len(grid[0])
    result = [row[:] for row in grid]

    axis_row = next(
        row_index
        for row_index, row in enumerate(grid)
        if row[0] != 0 and all(value == row[0] for value in row)
    )
    axis_column = next(
        column_index
        for column_index in range(width)
        if grid[0][column_index] != 0
        and all(grid[row_index][column_index] == grid[0][column_index]
                for row_index in range(height))
    )

    for row_index in range(height):
        for column_index in range(width):
            radius = max(abs(row_index - axis_row), abs(column_index - axis_column))
            if result[row_index][column_index] == 0 and radius > 0 and radius % 2 == 0:
                result[row_index][column_index] = 4

    return result
