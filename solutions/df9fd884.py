def transform(grid):
    height = len(grid)
    result = [row[:] for row in grid]
    top_columns = [column for column, value in enumerate(grid[0]) if value == 4]
    payload = [
        (row, column, value)
        for row, values in enumerate(grid)
        for column, value in enumerate(values)
        if value != 4 and value != 7
    ]

    payload_rows = [row for row, column, value in payload]
    payload_columns = [column for row, column, value in payload]
    row_shift = height - 1 - max(payload_rows)
    column_shift = (
        min(top_columns)
        + max(top_columns)
        - min(payload_columns)
        - max(payload_columns)
    ) // 2

    for row, column, value in payload:
        result[row][column] = 7
    for row, column, value in payload:
        result[row + row_shift][column + column_shift] = value
    output = result
    return output
