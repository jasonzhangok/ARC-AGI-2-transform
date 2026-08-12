def transform(grid):
    height, width = len(grid), len(grid[0])
    marker = next(
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 5
    )
    zeros = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 0
    }

    # The marker lies on the continuation of the straight edge of the zero
    # figure.  Its first zero in a cardinal direction fixes the scan axis.
    rays = []
    for drow, dcol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        row, col = marker
        distance = 0
        while True:
            row += drow
            col += dcol
            distance += 1
            if not (0 <= row < height and 0 <= col < width):
                break
            if (row, col) in zeros:
                rays.append((distance, (drow, dcol), (row, col)))
                break

    _, direction, origin = min(rays)
    drow, dcol = direction

    # Choose the perpendicular direction containing the zero bars.
    normal = (dcol, -drow)
    lateral = [
        (row - origin[0]) * normal[0] + (col - origin[1]) * normal[1]
        for row, col in zeros
    ]
    if min(lateral) < 0:
        normal = (-normal[0], -normal[1])

    bars = {}
    for row, col in zeros:
        u = (row - origin[0]) * drow + (col - origin[1]) * dcol
        v = (row - origin[0]) * normal[0] + (col - origin[1]) * normal[1]
        bars.setdefault(u, set()).add(v)

    lengths = [max(bars[u]) + 1 for u in range(max(bars) + 1)]
    mismatch = next(
        (index for index, length in enumerate(lengths) if length != index + 1),
        len(lengths),
    )

    if mismatch == 0:
        target = (origin[0] - drow, origin[1] - dcol)
    else:
        bar_index = mismatch - 1 if mismatch < len(lengths) else len(lengths) - 1
        extension = lengths[bar_index]
        target = (
            origin[0] + bar_index * drow + extension * normal[0],
            origin[1] + bar_index * dcol + extension * normal[1],
        )

    output = [row[:] for row in grid]
    output[marker[0]][marker[1]] = 7
    output[target[0]][target[1]] = 5
    return output
