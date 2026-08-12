def transform(grid):
    tile=[[grid[2*r][2*c] for c in range(3)] for r in range(3)]
    mask=grid[7:13]; out=[[0]*18 for _ in range(18)]
    for r in range(6):
        for c in range(6):
            if mask[r][c]!=0:
                for i in range(3):
                    for j in range(3): out[3*r+i][3*c+j]=tile[i][j]
    output = out
    return output
