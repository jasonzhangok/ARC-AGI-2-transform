from collections import Counter, deque


def transform(grid):
    h,w=len(grid),len(grid[0]);bg=Counter(v for row in grid for v in row).most_common(1)[0][0]
    row_sep=next((r for r,row in enumerate(grid) if len(set(row))==1 and row[0]!=bg),None)
    col_sep=next((c for c in range(w) if len({grid[r][c] for r in range(h)})==1 and grid[0][c]!=bg),None)
    sep_color=grid[row_sep][0] if row_sep is not None else grid[0][col_sep]
    sizes={}
    for color in {v for row in grid for v in row if v not in (bg,sep_color)}:
        seen=set();best=0
        for sr in range(h):
            for sc in range(w):
                if grid[sr][sc]!=color or (sr,sc) in seen: continue
                q=deque([(sr,sc)]);seen.add((sr,sc));n=0
                while q:
                    r,c=q.popleft();n+=1
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]==color and (nr,nc) not in seen:
                            seen.add((nr,nc));q.append((nr,nc))
                best=max(best,n)
        sizes[color]=best
    obj_color=max(sizes,key=sizes.get);out=[row[:] for row in grid];seen=set()
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc]!=obj_color or (sr,sc) in seen: continue
            q=deque([(sr,sc)]);seen.add((sr,sc));cells=[]
            while q:
                r,c=q.popleft();cells.append((r,c))
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<h and 0<=nc<w and grid[nr][nc]==obj_color and (nr,nc) not in seen:
                        seen.add((nr,nc));q.append((nr,nc))
            reflected=[]
            if col_sep is not None: reflected=[(r,2*col_sep-c) for r,c in cells]
            else: reflected=[(2*row_sep-r,c) for r,c in cells]
            for r,c in reflected:
                if 0<=r<h and 0<=c<w: out[r][c]=obj_color
            if col_sep is not None:
                original_min,original_max=min(c for _,c in cells),max(c for _,c in cells)
                reflected_min,reflected_max=min(c for _,c in reflected),max(c for _,c in reflected)
                left_edge,right_edge=(original_max,reflected_min) if original_max<reflected_min else (reflected_max,original_min)
                for r in range(min(r for r,_ in cells),max(r for r,_ in cells)+1):
                    for c in range(left_edge+1,right_edge):
                        out[r][c]=sep_color
            else:
                original_min,original_max=min(r for r,_ in cells),max(r for r,_ in cells)
                reflected_min,reflected_max=min(r for r,_ in reflected),max(r for r,_ in reflected)
                top_edge,bottom_edge=(original_max,reflected_min) if original_max<reflected_min else (reflected_max,original_min)
                for r in range(top_edge+1,bottom_edge):
                    for c in range(min(c for _,c in cells),max(c for _,c in cells)+1):
                        out[r][c]=sep_color
    return out
