def transform(grid):
    height, width = len(grid), len(grid[0])
    cells = [
        (row, col, grid[row][col])
        for row in range(height)
        for col in range(width)
        if grid[row][col] != 0
    ]
    top = min(row for row, _, _ in cells)
    bottom = max(row for row, _, _ in cells)
    left = min(col for _, col, _ in cells)
    right = max(col for _, col, _ in cells)
    center_row, center_col = next(
        (row, col) for row, col, color in cells if color == 2
    )
    top_color = next(color for row, _, color in cells if row == top)
    bottom_color = next(color for row, _, color in cells if row == bottom)
    left_color = next(color for _, col, color in cells if col == left)
    right_color = next(color for _, col, color in cells if col == right)

    output = [row[:] for row in grid]
    for row in range(top, bottom + 1):
        output[row][left] = left_color
        output[row][right] = right_color
    for col in range(left, right + 1):
        output[top][col] = top_color
        output[bottom][col] = bottom_color
    for col in range(left + 1, right):
        output[center_row][col] = 5
    for row in range(top + 1, bottom):
        output[row][center_col] = 5
    output[center_row][center_col] = 2
    return output
