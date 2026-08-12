def transform(grid):
    output = [row[:] for row in grid]
    colors = sorted({value for row in grid for value in row if value != 0})

    for color in colors:
        points = [
            (r, c)
            for r, row in enumerate(grid)
            for c, value in enumerate(row)
            if value == color
        ]
        if points[0][0] == points[1][0]:
            r = points[0][0]
            for c in range(min(points[0][1], points[1][1]), max(points[0][1], points[1][1]) + 1):
                output[r][c] = color

    for color in colors:
        points = [
            (r, c)
            for r, row in enumerate(grid)
            for c, value in enumerate(row)
            if value == color
        ]
        if points[0][1] == points[1][1]:
            c = points[0][1]
            for r in range(min(points[0][0], points[1][0]), max(points[0][0], points[1][0]) + 1):
                output[r][c] = color

    return output
