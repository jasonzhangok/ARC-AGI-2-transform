def transform(grid):
    h,w=len(grid),len(grid[0]); out=[[0]*w for _ in range(h)]
    if all(grid[r][0]==2 for r in range(h)): dr,dc=0,-1
    elif all(grid[r][w-1]==2 for r in range(h)): dr,dc=0,1
    elif all(v==2 for v in grid[0]): dr,dc=-1,0
    else: dr,dc=1,0
    for r in range(h):
        for c in range(w):
            if grid[r][c]==2: out[r][c]=2
    seen=set(); pieces=[]
    for r in range(h):
        for c in range(w):
            if grid[r][c] in (0,2) or (r,c) in seen: continue
            color=grid[r][c]; st=[(r,c)];seen.add((r,c));cells=[]
            while st:
                x,y=st.pop();cells.append((x,y,color))
                for a,b in ((1,0),(-1,0),(0,1),(0,-1)):
                    q=(x+a,y+b)
                    if 0<=q[0]<h and 0<=q[1]<w and q not in seen and grid[q[0]][q[1]]==color:seen.add(q);st.append(q)
            dist=min(r if dr<0 else h-1-r if dr>0 else c if dc<0 else w-1-c for r,c,_ in cells)
            pieces.append((dist,cells))
    for _,cells in sorted(pieces):
        sr=sc=0
        while all(0<=r+sr+dr<h and 0<=c+sc+dc<w and out[r+sr+dr][c+sc+dc]==0 for r,c,_ in cells): sr+=dr;sc+=dc
        for r,c,v in cells: out[r+sr][c+sc]=v
    output = out
    return output
