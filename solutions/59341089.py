def transform(grid):
    tile=[row[::-1] for row in grid]
    output = [tile[r]+grid[r]+tile[r]+grid[r] for r in range(len(grid))]
    return output
