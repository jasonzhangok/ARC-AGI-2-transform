def transform(grid):
    h,w=len(grid),len(grid[0]);templates=[];template_cells=set()
    for r in (0,h-1):
        c=0
        while c<w:
            if grid[r][c]==0:c+=1;continue
            a=c
            while c<w and grid[r][c]!=0:c+=1
            if c-a>=3:
                seq=grid[r][a:c];templates.append(seq);template_cells.update((r,x) for x in range(a,c))
    out=[row[:] for row in grid]
    markers=[(r,c,grid[r][c]) for r in range(h) for c in range(w) if grid[r][c]!=0 and (r,c) not in template_cells]
    for r,c,color in markers:
        seq=next(s for s in templates if color in s);start=c-seq.index(color)
        for i,v in enumerate(seq):
            if 0<=start+i<w:out[r][start+i]=v
    output = out
    return output
