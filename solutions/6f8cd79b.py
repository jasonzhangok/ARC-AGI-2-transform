def transform(grid):
    h,w=len(grid),len(grid[0]);return [[8 if r in (0,h-1) or c in (0,w-1) else 0 for c in range(w)] for r in range(h)]
