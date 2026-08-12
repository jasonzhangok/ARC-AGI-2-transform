def transform(grid):
    height, width = len(grid), len(grid[0])
    rectangle = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 5
    ]
    bottom = max(row for row, _ in rectangle)
    left = min(col for _, col in rectangle)
    right = max(col for _, col in rectangle)
    two = next(
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 2
    )
    eight = next(
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 8
    )

    output = [row[:] for row in grid]
    output[two[0]][two[1]] = 7
    output[eight[0]][eight[1]] = 2
    exit_col = right + 1 if eight[1] > two[1] else left - 1
    output[bottom][exit_col] = 8
    return output
