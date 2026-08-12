def transform(grid):
    height = len(grid)
    output = [
        [
            0 if value == 0 else 2 if grid[height - 1 - row][col] == 8 else 5
            for col, value in enumerate(values)
        ]
        for row, values in enumerate(grid)
    ]
    return output
