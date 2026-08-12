def transform(grid):
    top = grid[:4]
    bottom = grid[5:9]
    return [[3 if (top[r][c] != 0) != (bottom[r][c] != 0) else 0 for c in range(4)] for r in range(4)]
