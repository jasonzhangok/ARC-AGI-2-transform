def transform(grid):
    w=len(grid[0])//2
    return [[5 if row[c]==0 and row[c+w]==0 else 0 for c in range(w)] for row in grid]
