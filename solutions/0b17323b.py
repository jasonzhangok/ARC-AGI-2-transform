def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    points = sorted(
        (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value == 1
    )
    dr = points[1][0] - points[0][0]
    dc = points[1][1] - points[0][1]
    r, c = points[-1][0] + dr, points[-1][1] + dc
    while 0 <= r < height and 0 <= c < width:
        output[r][c] = 2
        r += dr
        c += dc
    return output
