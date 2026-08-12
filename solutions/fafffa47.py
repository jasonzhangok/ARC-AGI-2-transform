def transform(grid):
    top, bottom = grid[:3], grid[3:]
    return [[2 if a == 0 and b == 0 else 0 for a, b in zip(ra, rb)]
            for ra, rb in zip(top, bottom)]
