def transform(grid):
    h, w = len(grid), len(grid[0]); out = [row[:] for row in grid]
    seen = set(); regions = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0 or (r,c) in seen: continue
            stack=[(r,c)]; seen.add((r,c)); cells=[]
            while stack:
                x,y=stack.pop(); cells.append((x,y))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    q=(x+dx,y+dy)
                    if 0<=q[0]<h and 0<=q[1]<w and q not in seen and grid[q[0]][q[1]]==0:
                        seen.add(q); stack.append(q)
            regions.append(cells)
    small=min(map(len,regions)); large=max(map(len,regions))
    for cells in regions:
        color=7 if len(cells)==small else 8 if len(cells)==large else 0
        if color:
            for r,c in cells: out[r][c]=color
    return out
