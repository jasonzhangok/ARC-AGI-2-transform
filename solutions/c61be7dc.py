def transform(grid):
    height = len(grid)
    width = len(grid[0])
    zero_rows = [
        row for row in range(height)
        if all(value == 0 for value in grid[row])
    ]
    zero_cols = [
        col for col in range(width)
        if all(grid[row][col] == 0 for row in range(height))
    ]
    five_count = sum(value == 5 for row in grid for value in row)
    output = [[7] * width for _ in range(height)]

    if len(zero_cols) == 2:
        center_col = (zero_cols[0] + zero_cols[1]) // 2
        center_row = max(
            range(height),
            key=lambda row: (
                sum(value == 0 for value in grid[row])
                if 5 in grid[row] and set(grid[row]) <= {0, 5}
                else -1
            ),
        )
        for col in (center_col - 1, center_col + 1):
            for row in range(height):
                output[row][col] = 0
        for col in range(width):
            output[center_row][col] = 0
        start = center_row - five_count // 2
        for row in range(start, start + five_count):
            output[row][center_col] = 5
    else:
        center_row = (zero_rows[0] + zero_rows[1]) // 2
        center_col = max(
            range(width),
            key=lambda col: (
                sum(grid[row][col] == 0 for row in range(height))
                if (any(grid[row][col] == 5 for row in range(height))
                    and {grid[row][col] for row in range(height)} <= {0, 5})
                else -1
            ),
        )
        for row in (center_row - 1, center_row + 1):
            for col in range(width):
                output[row][col] = 0
        for row in range(height):
            output[row][center_col] = 0
        start = center_col - five_count // 2
        for col in range(start, start + five_count):
            output[center_row][col] = 5
    return output
