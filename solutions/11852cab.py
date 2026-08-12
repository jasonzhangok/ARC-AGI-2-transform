def transform(grid):
    output = [row[:] for row in grid]
    points = [
        (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value != 0
    ]
    top, bottom = min(r for r, _ in points), max(r for r, _ in points)
    left, right = min(c for _, c in points), max(c for _, c in points)
    for r, c in points:
        for rr, cc in (
            (r, c),
            (top + bottom - r, c),
            (r, left + right - c),
            (top + bottom - r, left + right - c),
        ):
            if output[rr][cc] == 0:
                output[rr][cc] = grid[r][c]
    return output
