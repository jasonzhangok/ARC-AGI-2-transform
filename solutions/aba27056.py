def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]

    colored = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] != 0
    ]
    if colored:
        top = min(row for row, _ in colored)
        bottom = max(row for row, _ in colored)
        left = min(col for _, col in colored)
        right = max(col for _, col in colored)

        sides = [
        ("top", [(top, col) for col in range(left, right + 1)]),
        ("bottom", [(bottom, col) for col in range(left, right + 1)]),
        ("left", [(row, left) for row in range(top, bottom + 1)]),
        ("right", [(row, right) for row in range(top, bottom + 1)]),
    ]
        openings = [
        (name, [point for point in side if grid[point[0]][point[1]] == 0])
        for name, side in sides
    ]
        indexed_openings = [(len(item[1]), -index, item) for index, item in enumerate(openings)]
        side_name, opening = max(indexed_openings)[2]

        if opening:
            # Light fills the framed chamber, including its opening.
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    if output[row][col] == 0:
                        output[row][col] = 4

            # Outside the opening, each opening cell casts a straight ray.  The two
            # ends additionally cast outward-diverging 45-degree rays.
            if side_name in ("top", "bottom"):
                direction = -1 if side_name == "top" else 1
                boundary_row = top if side_name == "top" else bottom
                first_col = min(col for _, col in opening)
                last_col = max(col for _, col in opening)
                step = 1
                row = boundary_row + direction
                while 0 <= row < height:
                    for _, col in opening:
                        if 0 <= col < width and output[row][col] == 0:
                            output[row][col] = 4
                    for ray_col in (first_col - step, last_col + step):
                        if 0 <= ray_col < width and output[row][ray_col] == 0:
                            output[row][ray_col] = 4
                    step += 1
                    row += direction
            else:
                direction = -1 if side_name == "left" else 1
                boundary_col = left if side_name == "left" else right
                first_row = min(row for row, _ in opening)
                last_row = max(row for row, _ in opening)
                step = 1
                col = boundary_col + direction
                while 0 <= col < width:
                    for row, _ in opening:
                        if 0 <= row < height and output[row][col] == 0:
                            output[row][col] = 4
                    for ray_row in (first_row - step, last_row + step):
                        if 0 <= ray_row < height and output[ray_row][col] == 0:
                            output[ray_row][col] = 4
                    step += 1
                    col += direction

    return output
