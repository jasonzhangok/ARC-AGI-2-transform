def transform(grid):
    height = len(grid)
    width = len(grid[0])
    axis = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 1
    ]

    colors = {
        value
        for row in grid
        for value in row
        if value not in (8, 1)
    }
    color_order = list(colors)
    chosen = min(
        (sum(value == color for row in grid for value in row), index, color)
        for index, color in enumerate(color_order)
    )[2]

    if len({row for row, _ in axis}) == 1:
        axis_row = axis[0][0]
        reflection_kind = 0
    elif len({col for _, col in axis}) == 1:
        axis_col = axis[0][1]
        reflection_kind = 1
    elif len({row - col for row, col in axis}) == 1:
        offset = axis[0][0] - axis[0][1]
        reflection_kind = 2
    else:
        total = axis[0][0] + axis[0][1]
        reflection_kind = 3

    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] == chosen:
                if reflection_kind == 0:
                    target_row, target_col = 2 * axis_row - row, col
                elif reflection_kind == 1:
                    target_row, target_col = row, 2 * axis_col - col
                elif reflection_kind == 2:
                    target_row, target_col = col + offset, row - offset
                else:
                    target_row, target_col = total - col, total - row
                if 0 <= target_row < height and 0 <= target_col < width:
                    output[target_row][target_col] = chosen
    return output
