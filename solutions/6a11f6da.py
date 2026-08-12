def transform(grid):
    panels=[grid[i:i+5] for i in (0,5,10)]
    output = [[6 if panels[2][r][c]==6 else 1 if panels[0][r][c]==1 else 8 if panels[1][r][c]==8 else 0 for c in range(5)] for r in range(5)]
    return output
