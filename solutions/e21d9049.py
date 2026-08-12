def transform(grid):
    height, width = (len(grid), len(grid[0]))
    horizontal_row = max(((sum((value != 0 for value in grid[_key_item_1])), -_key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(range(height))))[2]
    vertical_col = max(((sum((grid[row][_key_item_2] != 0 for row in range(height))), -_key_index_2, _key_item_2) for _key_index_2, _key_item_2 in enumerate(range(width))))[2]
    colored_cols = [col for col in range(width) if grid[horizontal_row][col] != 0]
    colored_rows = [row for row in range(height) if grid[row][vertical_col] != 0]
    first_col = min(colored_cols)
    first_row = min(colored_rows)
    horizontal_pattern = [grid[horizontal_row][col] for col in range(first_col, max(colored_cols) + 1)]
    vertical_pattern = [grid[row][vertical_col] for row in range(first_row, max(colored_rows) + 1)]
    output = [row[:] for row in grid]
    for col in range(width):
        output[horizontal_row][col] = horizontal_pattern[(col - first_col) % len(horizontal_pattern)]
    for row in range(height):
        output[row][vertical_col] = vertical_pattern[(row - first_row) % len(vertical_pattern)]
    return output
