def transform(grid):
    width = len(grid[0]) if grid else 0
    output = [
        [
            1 if value == 5 and grid[row_index][width - 1 - column_index] == 5 else value
            for column_index, value in enumerate(row)
        ]
        for row_index, row in enumerate(grid)
    ]
    return output
