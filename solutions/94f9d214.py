def transform(grid):
    top = grid[:4]
    bottom = grid[4:8]
    return [[2 if top[r][c] == 0 and bottom[r][c] == 0 else 0 for c in range(4)] for r in range(4)]
