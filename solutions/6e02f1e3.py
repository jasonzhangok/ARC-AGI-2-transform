def transform(grid):
    n=len(grid);count=len(set(v for row in grid for v in row));out=[[0]*n for _ in range(n)]
    if count==1:out[0]=[5]*n
    elif count==2:
        for i in range(n):out[i][i]=5
    else:
        for i in range(n):out[i][n-1-i]=5
    output = out
    return output
