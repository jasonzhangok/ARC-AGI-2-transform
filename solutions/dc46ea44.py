def transform(grid):
    height = len(grid)
    width = len(grid[0])
    separator = next((row for row in range(height) if all((value == 4 for value in grid[row]))))
    output = [[7] * width for _ in range(height)]
    output[separator] = [4] * width
    six_cells = {(row, col) for row in range(separator + 1, height) for col in range(width) if grid[row][col] == 6}
    row_shift = separator + 1
    for row, col in six_cells:
        output[row - row_shift][col] = 6
    tip = min((((_key_item_1[1], _key_item_1[0]), _key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(((row - row_shift, col) for row, col in six_cells))))[2]
    other_color = next((value for row in range(separator + 1, height) for value in grid[row] if value not in (6, 7)))
    other_cells = {(row, col) for row in range(separator + 1, height) for col in range(width) if grid[row][col] == other_color}
    bottom = max((row for row, _ in other_cells))
    right = max((col for _, col in other_cells))
    d_row = tip[0] - bottom
    d_col = tip[1] - right
    for row, col in other_cells:
        output[row + d_row][col + d_col] = other_color
    return output
