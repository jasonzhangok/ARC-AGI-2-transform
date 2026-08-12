def transform(grid):
    height, width = (len(grid), len(grid[0]))
    row_colors = [max((count_dict := {}) or ([count_dict.update({count_item: count_dict.get(count_item, 0) + 1}) for count_item in row] and count_dict), key=count_dict.get) for row in grid]
    row_result = [[row_colors[row]] * width for row in range(height)]
    col_colors = [max((count_dict := {}) or ([count_dict.update({count_item: count_dict.get(count_item, 0) + 1}) for count_item in (grid[row][col] for row in range(height))] and count_dict), key=count_dict.get) for col in range(width)]
    col_result = [col_colors[:] for _ in range(height)]
    row_changes = sum((grid[row][col] != row_result[row][col] for row in range(height) for col in range(width)))
    col_changes = sum((grid[row][col] != col_result[row][col] for row in range(height) for col in range(width)))
    output = row_result if row_changes <= col_changes else col_result
    return output
