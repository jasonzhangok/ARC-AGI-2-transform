def transform(grid):
    return [[1 if r % 2 == 0 or c % 2 == 0 else 0 for c in range(len(grid[0]))] for r in range(len(grid))]
