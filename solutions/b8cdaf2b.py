def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = set((value for row in grid for value in row)) - {0}
    inner_color = min(((sum((value == _key_item_1 for row in grid for value in row)), _key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(colors)))[2]
    inner_cells = [(row, col) for row in range(height) for col in range(width) if grid[row][col] == inner_color]
    base_row = max((row for row, _ in inner_cells))
    left = min((col for row, col in inner_cells if row == base_row))
    right = max((col for row, col in inner_cells if row == base_row))
    output = [row[:] for row in grid]
    step = 1
    while base_row - 1 - step >= 0:
        row = base_row - 1 - step
        left_col = left - step
        right_col = right + step
        if 0 <= left_col < width:
            output[row][left_col] = inner_color
        if 0 <= right_col < width:
            output[row][right_col] = inner_color
        step += 1
    return output
