def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    base_row = max(row for row in range(height) if 2 in grid[row])
    starts = [col for col, value in enumerate(grid[base_row]) if value == 2]

    for start_col in starts:
        col = start_col
        for row in range(base_row - 1, -1, -1):
            if grid[row][col] == 5:
                output[row + 1][col + 1] = 2
                col += 1
            output[row][col] = 2
    return output
