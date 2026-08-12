def transform(grid):
    h,w=len(grid),len(grid[0]); cr,cc=h//2,w//2; colors={}
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=7: colors[max(abs(r-cr),abs(c-cc))]=grid[r][c]
    output = [[colors[max(abs(r-cr),abs(c-cc))] for c in range(w)] for r in range(h)]
    return output
