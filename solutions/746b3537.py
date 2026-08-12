def transform(grid):
    rows=[]
    for row in grid:
        if not rows or row!=rows[-1]:rows.append(row[:])
    out=[]
    for row in rows:
        nr=[]
        for v in row:
            if not nr or v!=nr[-1]:nr.append(v)
        out.append(nr)
    return out
