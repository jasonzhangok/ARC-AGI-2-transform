def transform(grid):
    split = next(r for r, row in enumerate(grid) if all(v == 4 for v in row))
    top, bottom = grid[:split], grid[split + 1:]
    output = [[3 if top[r][c] != 0 or bottom[r][c] != 0 else 0
             for c in range(len(grid[0]))] for r in range(len(top))]
    return output
