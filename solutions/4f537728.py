def transform(grid):
    marker = next(v for row in grid for v in row if v not in (0, 1))
    cells = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == marker]
    rows = {r for r, _ in cells}
    cols = {c for _, c in cells}
    output = [[marker if v != 0 and (r in rows or c in cols) else v
             for c, v in enumerate(row)] for r, row in enumerate(grid)]
    return output
