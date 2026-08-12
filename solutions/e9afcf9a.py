def transform(grid):
    a, b = grid[0][0], grid[1][0]
    return [[a if (r + c) % 2 == 0 else b for c in range(len(grid[0]))]
            for r in range(len(grid))]
