from collections import Counter


def transform(grid):
    count=Counter(v for row in grid for v in row if v)
    main=count.most_common(1)[0][0]
    h,w=len(grid),len(grid[0]);out=[[0]*w for _ in range(h)];rects=[]
    for r0 in range(h):
        for r1 in range(r0+2,h):
            for c0 in range(w):
                for c1 in range(c0+2,w):
                    if all(grid[r][c]!=0 for r in range(r0,r1+1) for c in range(c0,c1+1)):
                        rects.append((r0,r1,c0,c1))
    maximal=[q for q in rects if not any(p[0]<=q[0] and q[1]<=p[1] and p[2]<=q[2] and q[3]<=p[3] and p!=q for p in rects)]
    for r0,r1,c0,c1 in maximal:
        for r in range(r0,r1+1):
            for c in range(c0,c1+1):out[r][c]=main
    return out
