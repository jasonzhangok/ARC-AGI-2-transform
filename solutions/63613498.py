def _components(grid):
    h, w = len(grid), len(grid[0]); seen = set(); ans = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] in (0, 5) or (r,c) in seen: continue
            color = grid[r][c]; stack=[(r,c)]; seen.add((r,c)); cells=[]
            while stack:
                x,y=stack.pop(); cells.append((x,y))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    q=(x+dx,y+dy)
                    if 0<=q[0]<h and 0<=q[1]<w and q not in seen and grid[q[0]][q[1]]==color:
                        seen.add(q); stack.append(q)
            mr=min(x for x,_ in cells); mc=min(y for _,y in cells)
            shape=frozenset((x-mr,y-mc) for x,y in cells)
            ans.append((cells,shape))
    return ans

def transform(grid):
    out=[row[:] for row in grid]; comps=_components(grid); groups={}
    for cells,shape in comps: groups.setdefault(shape,[]).append(cells)
    for group in groups.values():
        if len(group)>1:
            for cells in group[1:]:
                for r,c in cells: out[r][c]=5
    return out
