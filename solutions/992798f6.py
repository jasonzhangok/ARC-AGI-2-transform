def sign(value):
    return (value > 0) - (value < 0)


def transform(grid):
    h, w = len(grid), len(grid[0])
    start = next((r, c) for r in range(h) for c in range(w) if grid[r][c] == 2)
    target = next((r, c) for r in range(h) for c in range(w) if grid[r][c] == 1)
    r, c = start
    output = [row[:] for row in grid]
    dr, dc = target[0] - r, target[1] - c
    if dr and dc:
        r += sign(dr)
        c += sign(dc)
        if (r, c) != target:
            output[r][c] = 3
    while abs(target[0] - r) != abs(target[1] - c):
        if abs(target[0] - r) > abs(target[1] - c):
            r += sign(target[0] - r)
        else:
            c += sign(target[1] - c)
        if (r, c) != target:
            output[r][c] = 3
    while (r, c) != target:
        r += sign(target[0] - r)
        c += sign(target[1] - c)
        if (r, c) != target:
            output[r][c] = 3
    return output
