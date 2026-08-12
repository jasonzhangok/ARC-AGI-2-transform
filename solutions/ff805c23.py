def transform(grid):
    height, width = len(grid), len(grid[0])
    covered = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 1
    ]
    top = min(row for row, _ in covered)
    bottom = max(row for row, _ in covered)
    left = min(col for _, col in covered)
    right = max(col for _, col in covered)
    output = []

    for row in range(top, bottom + 1):
        output_row = []
        for col in range(left, right + 1):
            symmetric_values = (
                grid[height - 1 - row][col],
                grid[row][width - 1 - col],
                grid[height - 1 - row][width - 1 - col],
            )
            output_row.append(next(value for value in symmetric_values if value != 1))
        output.append(output_row)
    return output
