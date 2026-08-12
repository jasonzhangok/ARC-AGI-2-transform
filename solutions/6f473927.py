def transform(grid):
    mirror=[[8 if v==0 else 0 for v in row[::-1]] for row in grid]
    left=any(row[0]!=0 for row in grid);right=any(row[-1]!=0 for row in grid)
    return [mirror[r]+grid[r] if left and not right else grid[r]+mirror[r] for r in range(len(grid))]
