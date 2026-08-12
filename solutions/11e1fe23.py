def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    corners = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0:
                corners.append((row, col, grid[row][col]))

    top = min(row for row, col, color in corners)
    bottom = max(row for row, col, color in corners)
    left = min(col for row, col, color in corners)
    right = max(col for row, col, color in corners)
    center_row = (top + bottom) // 2
    center_col = (left + right) // 2
    output[center_row][center_col] = 5

    for row, col, color in corners:
        if row < center_row:
            target_row = center_row - 1
        elif row > center_row:
            target_row = center_row + 1
        else:
            target_row = center_row
        if col < center_col:
            target_col = center_col - 1
        elif col > center_col:
            target_col = center_col + 1
        else:
            target_col = center_col
        output[target_row][target_col] = color

    return output
