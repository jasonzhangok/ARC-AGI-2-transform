def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    gray = [
        (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value == 5
    ]
    period = len(gray)
    template = [
        [0 if value == 5 else value for value in grid[r]]
        for r in range(period)
    ]
    start = next(
        r
        for r in range(height)
        if r >= period and all(value == 0 for value in grid[r])
    )
    for r in range(start, height):
        output[r] = template[(r - start) % period][:]
    return output
