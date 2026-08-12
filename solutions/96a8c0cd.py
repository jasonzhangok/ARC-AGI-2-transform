def transform(grid):
    height, width = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    row, col = next(
        (r, c)
        for r in range(height)
        for c in range(width)
        if grid[r][c] == 2
    )

    if row == 0:
        forward = (1, 0)
    elif row == height - 1:
        forward = (-1, 0)
    elif col == 0:
        forward = (0, 1)
    else:
        forward = (0, -1)
    left = (-forward[1], forward[0])

    while True:
        ahead = (row + forward[0], col + forward[1])
        if not (0 <= ahead[0] < height and 0 <= ahead[1] < width):
            break
        symbol = grid[ahead[0]][ahead[1]]
        if symbol not in (1, 3):
            row, col = ahead
            if grid[ahead[0]][ahead[1]] == 0:
                result[ahead[0]][ahead[1]] = 2
            continue

        # 1 means pass on the traveler's left; 3 means pass on the right.
        side = left if symbol == 1 else (-left[0], -left[1])
        endpoint = ahead
        while True:
            following = (endpoint[0] + side[0], endpoint[1] + side[1])
            if (0 <= following[0] < height and 0 <= following[1] < width
                    and grid[following[0]][following[1]] == symbol):
                endpoint = following
            else:
                break
        target = (endpoint[0] + side[0], endpoint[1] + side[1])

        transverse_axis = 0 if side[0] else 1
        while (row, col)[transverse_axis] != target[transverse_axis]:
            row += side[0]
            col += side[1]
            if 0 <= row < height and 0 <= col < width and grid[row][col] == 0:
                result[row][col] = 2

        # Pass beside the one-cell-thick bar and emerge just beyond it.
        for _ in range(2):
            row += forward[0]
            col += forward[1]
            if 0 <= row < height and 0 <= col < width and grid[row][col] == 0:
                result[row][col] = 2

    output = result
    return output
