def transform(grid):
    h, w = len(grid), len(grid[0]); seen = set(); comps = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen: continue
            color = grid[r][c]; stack = [(r, c)]; seen.add((r, c)); cells = []
            while stack:
                x, y = stack.pop(); cells.append((x, y))
                for dx in (-1,0,1):
                    for dy in (-1,0,1):
                        if dx==0 and dy==0: continue
                        p=x+dx,y+dy
                        if 0<=p[0]<h and 0<=p[1]<w and p not in seen and grid[p[0]][p[1]]==color:
                            seen.add(p);stack.append(p)
            comps.append((color,cells))
    palette = max((len(item[1]),-index,item[1]) for index,item in enumerate(comps))[2]
    r0,r1=min(r for r,c in palette),max(r for r,c in palette)
    c0,c1=min(c for r,c in palette),max(c for r,c in palette)
    # The solid palette color is the color covering most of its bounding box.
    counts={}
    for r in range(r0,r1+1):
        for c in range(c0,c1+1):counts[grid[r][c]]=counts.get(grid[r][c],0)+1
    base=None
    for value in counts:
        if base is None or counts[value]>counts[base]:base=value
    markers={(0 if r-r0 < (r1-r0+1)/2 else 1,0 if c-c0 < (c1-c0+1)/2 else 1):grid[r][c]
             for r in range(r0,r1+1) for c in range(c0,c1+1) if grid[r][c] not in (0,base)}
    shapes={}
    for color,cells in comps:
        if cells==palette or color==base or all(r0<=r<=r1 and c0<=c<=c1 for r,c in cells): continue
        rr0,cc0=min(r for r,c in cells),min(c for r,c in cells)
        crop=[[0]*3 for _ in range(3)]
        for r,c in cells:
            if r-rr0<3 and c-cc0<3:crop[r-rr0][c-cc0]=color
        shapes[color]=crop
    out=[[0]*7 for _ in range(7)]
    for pos,color in markers.items():
        if color not in shapes: continue
        ro,co=pos[0]*4,pos[1]*4
        for r in range(3):
            for c in range(3):out[ro+r][co+c]=shapes[color][r][c]
    output=out
    return output
