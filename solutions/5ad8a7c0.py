def transform(grid):
    out=[row[:] for row in grid]
    patterns={}
    for r,row in enumerate(grid):
        cols=tuple(c for c,v in enumerate(row) if v==2)
        if len(cols)==2:patterns.setdefault(cols,[]).append(r)
    for (left,right),rows in patterns.items():
        if len(rows)<2:continue
        valid=True
        for r in range(len(grid)):
            if r in rows:continue
            cols=[c for c,v in enumerate(grid[r]) if v==2]
            if len(cols)==2 and left<cols[0] and cols[1]<right:valid=False
        if valid:
            for r in rows:
                for c in range(left,right+1):out[r][c]=2
    return out
