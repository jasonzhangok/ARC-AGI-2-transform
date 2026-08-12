from collections import Counter, deque


def transform(grid):
    h,w=len(grid),len(grid[0]);bg=Counter(v for row in grid for v in row).most_common(1)[0][0]
    seen=set();objects=[]
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc]==bg or (sr,sc) in seen:continue
            color=grid[sr][sc];q=deque([(sr,sc)]);seen.add((sr,sc));n=0
            while q:
                r,c=q.popleft();n+=1
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<h and 0<=nc<w and grid[nr][nc]==color and (nr,nc) not in seen:
                        seen.add((nr,nc));q.append((nr,nc))
            objects.append((n,color))
    colors=[color for _,color in sorted(objects,reverse=True)];n=len(colors);size=2*n-1
    return [[colors[min(r,c,size-1-r,size-1-c)] for c in range(size)] for r in range(size)]
