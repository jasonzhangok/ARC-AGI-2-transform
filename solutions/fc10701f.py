def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)

    sevens = []
    nines = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 7:
                sevens.append((row, col))
            elif grid[row][col] == 9:
                nines.append((row, col))

    seven_top = min(row for row, col in sevens)
    seven_bottom = max(row for row, col in sevens)
    seven_left = min(col for row, col in sevens)
    seven_right = max(col for row, col in sevens)
    nine_top = min(row for row, col in nines)
    nine_bottom = max(row for row, col in nines)
    nine_left = min(col for row, col in nines)
    nine_right = max(col for row, col in nines)

    output = [row[:] for row in grid]
    for row, col in sevens:
        output[row][col] = background
    for row, col in nines:
        output[row][col] = background
    row_shift = nine_top - seven_top
    col_shift = nine_left - seven_left
    for row, col in sevens:
        output[row + row_shift][col + col_shift] = 7

    if seven_left == nine_left and seven_right == nine_right:
        left = seven_left
        right = seven_right
        if seven_bottom < nine_top:
            path_start = seven_bottom + 1
            path_end = nine_top
        else:
            path_start = nine_bottom + 1
            path_end = seven_top
        for row in range(path_start, path_end):
            if (
                left > 0
                and right + 1 < width
                and grid[row][left - 1] == 0
                and grid[row][right + 1] == 0
            ):
                for col in range(left, right + 1):
                    output[row][col] = 2
    elif seven_top == nine_top and seven_bottom == nine_bottom:
        top = seven_top
        bottom = seven_bottom
        if seven_right < nine_left:
            path_start = seven_right + 1
            path_end = nine_left
        else:
            path_start = nine_right + 1
            path_end = seven_left
        for col in range(path_start, path_end):
            if (
                top > 0
                and bottom + 1 < height
                and grid[top - 1][col] == 0
                and grid[bottom + 1][col] == 0
            ):
                for row in range(top, bottom + 1):
                    output[row][col] = 2

    return output
