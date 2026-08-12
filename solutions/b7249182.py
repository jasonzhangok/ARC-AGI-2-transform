def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seeds = [
        (row, col, grid[row][col])
        for row in range(height)
        for col in range(width)
        if grid[row][col] != 0
    ]
    output = [row[:] for row in grid]

    if seeds[0][0] == seeds[1][0]:
        left_seed, right_seed = sorted(seeds, key=lambda item: item[1])
        row, left_col, left_color = left_seed
        _, right_col, right_color = right_seed
        inner_left = (left_col + right_col) // 2 - 1
        inner_right = (left_col + right_col + 1) // 2 + 1
        top, bottom = row - 2, row + 2
        for col in range(left_col, inner_left + 1):
            output[row][col] = left_color
        for col in range(inner_right, right_col + 1):
            output[row][col] = right_color
        for col in range(inner_left, inner_right + 1):
            color = left_color if col <= inner_left + 1 else right_color
            output[top][col] = color
            output[bottom][col] = color
        for current_row in range(top + 1, bottom):
            output[current_row][inner_left] = left_color
            output[current_row][inner_right] = right_color
    else:
        top_seed, bottom_seed = sorted(seeds, key=lambda item: item[0])
        top_row, col, top_color = top_seed
        bottom_row, _, bottom_color = bottom_seed
        inner_top = (top_row + bottom_row) // 2 - 1
        inner_bottom = (top_row + bottom_row + 1) // 2 + 1
        left, right = col - 2, col + 2
        for row in range(top_row, inner_top + 1):
            output[row][col] = top_color
        for row in range(inner_bottom, bottom_row + 1):
            output[row][col] = bottom_color
        for row in range(inner_top, inner_bottom + 1):
            color = top_color if row <= inner_top + 1 else bottom_color
            output[row][left] = color
            output[row][right] = color
        for current_col in range(left, right + 1):
            output[inner_top][current_col] = top_color
            output[inner_bottom][current_col] = bottom_color
    return output
