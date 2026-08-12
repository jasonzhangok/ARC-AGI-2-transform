def transform(grid):
    columns=sorted({c for row in grid for c,v in enumerate(row) if v==0})
    rank={c:i+1 for i,c in enumerate(columns)}
    output = [[rank[c] if v==0 else v for c,v in enumerate(row)] for row in grid]
    return output
