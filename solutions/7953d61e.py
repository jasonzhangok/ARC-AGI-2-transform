def _cw(g):
    return [list(row) for row in zip(*g[::-1])]


def transform(grid):
    cw = _cw(grid)
    half = _cw(cw)
    ccw = _cw(half)
    return [grid[r] + ccw[r] for r in range(len(grid))] + [
        half[r] + cw[r] for r in range(len(grid))
    ]
