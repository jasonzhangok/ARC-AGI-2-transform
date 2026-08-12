def transform(grid):
    h,w=len(grid),len(grid[0]);shape={(r,c) for r in range(h) for c in range(w) if grid[r][c]==5};colors=set(v for row in grid for v in row)-{0,5}
    def score(color):
        pts=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==color];ds=[min(abs(r-x)+abs(c-y) for x,y in shape) for r,c in pts]
        return min(ds),sum(ds)/len(ds)
    chosen=min(colors,key=score)
    return [[chosen if v==5 else 0 for v in row] for row in grid]
