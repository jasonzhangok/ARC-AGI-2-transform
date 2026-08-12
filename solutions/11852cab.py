def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    points = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0:
                points.append((row, col, grid[row][col]))

    top = min(row for row, col, color in points)
    bottom = max(row for row, col, color in points)
    left = min(col for row, col, color in points)
    right = max(col for row, col, color in points)
    doubled_center_row = top + bottom
    doubled_center_col = left + right

    for row, col, color in points:
        doubled_row = 2 * row
        doubled_col = 2 * col
        for rotation in range(4):
            if doubled_row % 2 == 0 and doubled_col % 2 == 0:
                target_row = doubled_row // 2
                target_col = doubled_col // 2
                if 0 <= target_row < height and 0 <= target_col < width:
                    if output[target_row][target_col] == 0:
                        output[target_row][target_col] = color
            row_offset = doubled_row - doubled_center_row
            col_offset = doubled_col - doubled_center_col
            doubled_row = doubled_center_row + col_offset
            doubled_col = doubled_center_col - row_offset

    return output
