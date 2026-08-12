def transform(grid):
    rows=[row for row in grid if any(row)]
    return [[next((v for v in row[2*c:2*c+2] if v!=0),0) for c in range(len(row)//2)] for row in rows]
