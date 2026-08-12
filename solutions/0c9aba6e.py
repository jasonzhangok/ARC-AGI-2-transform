def transform(grid):
    separator = next(r for r, row in enumerate(grid) if len(set(row)) == 1 and row[0] == 7)
    top = grid[:separator]
    bottom = grid[separator + 1 :]
    return [
        [8 if top[r][c] == 0 and bottom[r][c] == 0 else 0 for c in range(len(grid[0]))]
        for r in range(len(top))
    ]
