def transform(grid):
    h,w=len(grid),len(grid[0]); colors=set(v for row in grid for v in row)
    color_list=list(colors)
    outer=max((max(max(sum(v==x for v in row) for row in grid),max(sum(grid[r][c]==x for r in range(h)) for c in range(w))),-index,x) for index,x in enumerate(color_list))[2]
    other_colors=[x for x in color_list if x!=outer]
    sep=max((max(sum(v==x for v in row) for row in grid),-index,x) for index,x in enumerate(other_colors))[2]
    rs=[r for r in range(h) if sum(v==sep for v in grid[r])>w//2]
    cs=[c for c in range(w) if sum(grid[r][c]==sep for r in range(h))>h//2]
    part_sets=[]
    for indices in (rs,cs):
        groups=[]
        for x in indices:
            if not groups or x>groups[-1][-1]+1: groups.append([x])
            else: groups[-1].append(x)
        part_sets.append([(groups[i][-1]+1,groups[i+1][0]) for i in range(len(groups)-1)])
    rparts,cparts=part_sets; out=[]
    for r0,r1 in rparts:
        row=[]
        for c0,c1 in cparts:
            vals=[grid[r][c] for r in range(r0,r1) for c in range(c0,c1) if grid[r][c] not in (outer,sep)]
            counts={}
            for value in vals:counts[value]=counts.get(value,0)+1
            best=None
            for value in counts:
                if best is None or counts[value]>counts[best]:best=value
            row.append(best if vals else outer)
        out.append(row)
    output=out
    return output
