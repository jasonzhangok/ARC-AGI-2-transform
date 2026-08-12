def transform(grid):
    n=len(grid);out=[[0]*(n*n) for _ in range(n*n)]
    for br in range(n):
        for bc in range(n):
            if grid[br][bc]==0:continue
            for r in range(n):
                for c in range(n):out[br*n+r][bc*n+c]=grid[r][c]
    return out
