def transform(grid):
    h,w=len(grid),len(grid[0]);out=[row[:] for row in grid];seen=set()
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=5 or (r,c) in seen:continue
            st=[(r,c)];seen.add((r,c));cells=[]
            while st:
                x,y=st.pop();cells.append((x,y))
                for a,b in ((1,0),(-1,0),(0,1),(0,-1)):
                    q=(x+a,y+b)
                    if 0<=q[0]<h and 0<=q[1]<w and q not in seen and grid[q[0]][q[1]]==5:seen.add(q);st.append(q)
            color=5-len(cells)
            for x,y in cells:out[x][y]=color
    output = out
    return output
