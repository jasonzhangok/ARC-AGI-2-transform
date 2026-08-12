def transform(grid):
    divider = next(r for r, row in enumerate(grid) if len(set(row)) == 1 and row[0] == 5)
    top = grid[:divider]
    bottom = grid[divider + 1:]
    return [[a if a != 0 else b for a, b in zip(ra, rb)]
            for ra, rb in zip(top, bottom)]
