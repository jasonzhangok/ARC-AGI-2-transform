def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    key = []
    scaffold = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 8:
                scaffold.append((row, col))
            elif grid[row][col] != 0:
                key.append((row, col, grid[row][col]))

    key_top = min(row for row, col, color in key)
    key_bottom = max(row for row, col, color in key)
    key_left = min(col for row, col, color in key)
    key_height = key_bottom - key_top + 1
    scaffold_top = min(row for row, col in scaffold)
    scaffold_left = min(col for row, col in scaffold)

    block_area = len(scaffold) // len(key)
    scale = 1
    while (scale + 1) * (scale + 1) <= block_area:
        scale += 1

    for row, col, color in key:
        key_row = row - key_top
        key_col = col - key_left
        block_row = key_col
        block_col = key_height - 1 - key_row
        for row_offset in range(scale):
            for col_offset in range(scale):
                target_row = scaffold_top + block_row * scale + row_offset
                target_col = scaffold_left + block_col * scale + col_offset
                output[target_row][target_col] = color

    return output
