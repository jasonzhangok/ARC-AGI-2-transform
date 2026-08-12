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
    chosen = min(
        colors,
        key=lambda color: sum(value == color for row in grid for value in row),
    )

    if len({row for row, _ in axis}) == 1:
        axis_row = axis[0][0]
        reflect = lambda row, col: (2 * axis_row - row, col)
    elif len({col for _, col in axis}) == 1:
        axis_col = axis[0][1]
        reflect = lambda row, col: (row, 2 * axis_col - col)
    elif len({row - col for row, col in axis}) == 1:
        offset = axis[0][0] - axis[0][1]
        reflect = lambda row, col: (col + offset, row - offset)
    else:
        total = axis[0][0] + axis[0][1]
        reflect = lambda row, col: (total - col, total - row)

    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] == chosen:
                target_row, target_col = reflect(row, col)
                if 0 <= target_row < height and 0 <= target_col < width:
                    output[target_row][target_col] = chosen
    return output
