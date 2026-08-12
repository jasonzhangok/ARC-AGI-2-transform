def transform(grid):
    result = [row[:] for row in grid]
    marker_colors = {value for row in grid for value in row if value != 8}
    if not marker_colors:
        return result

    color = next(iter(marker_colors))
    displacement = {
        7: (-2, 0),
        2: (0, -2),
        9: (2, 0),
        1: (0, 1),
    }[color]
    dr, dc = displacement
    points = [
        (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value == color
    ]
    for r, c in points:
        result[r][c] = 8
    for r, c in points:
        result[r + dr][c + dc] = color
    return result
