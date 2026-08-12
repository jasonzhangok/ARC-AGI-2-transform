def transform(grid):
    marker=next(v for row in grid for v in row if v not in (0,2,3))
    return [[marker if v in (2,3) else 0 if v==marker else v for v in row] for row in grid]
