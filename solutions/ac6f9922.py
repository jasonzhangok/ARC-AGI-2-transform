from collections import Counter


def transform(grid):
    h,w=len(grid),len(grid[0]); colors=set(v for row in grid for v in row)
    outer=max(colors,key=lambda x:max(max(sum(v==x for v in row) for row in grid),max(sum(grid[r][c]==x for r in range(h)) for c in range(w))))
    sep=max((x for x in colors if x!=outer),key=lambda x:max(sum(v==x for v in row) for row in grid))
    rs=[r for r in range(h) if sum(v==sep for v in grid[r])>w//2]
    cs=[c for c in range(w) if sum(grid[r][c]==sep for r in range(h))>h//2]
    def gaps(indices):
        groups=[]
        for x in indices:
            if not groups or x>groups[-1][-1]+1: groups.append([x])
            else: groups[-1].append(x)
        return [(groups[i][-1]+1,groups[i+1][0]) for i in range(len(groups)-1)]
    rparts,cparts=gaps(rs),gaps(cs); out=[]
    for r0,r1 in rparts:
        row=[]
        for c0,c1 in cparts:
            vals=[grid[r][c] for r in range(r0,r1) for c in range(c0,c1) if grid[r][c] not in (outer,sep)]
            row.append(Counter(vals).most_common(1)[0][0] if vals else outer)
        out.append(row)
    return out
