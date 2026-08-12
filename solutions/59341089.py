def transform(grid):
    tile=[row[::-1] for row in grid]
    return [tile[r]+grid[r]+tile[r]+grid[r] for r in range(len(grid))]
