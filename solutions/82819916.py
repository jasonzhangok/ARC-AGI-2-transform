def transform(grid):
    out=[row[:] for row in grid]
    template=next(row for row in grid if sum(v!=0 for v in row)==len(row))
    source=[]
    for v in template:
        if v not in source:source.append(v)
    for r,row in enumerate(grid):
        vals=[]
        for v in row:
            if v and v not in vals:vals.append(v)
        if len(vals)==2 and row!=template:
            mapping={source[0]:vals[0],source[1]:vals[1]}
            out[r]=[mapping[v] for v in template]
    output = out
    return output
