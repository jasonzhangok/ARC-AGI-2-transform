def transform(grid):
    h,w=len(grid),len(grid[0]); out=[row[:] for row in grid]; blocks=[];used=set()
    for r in range(h-2):
        for c in range(w-2):
            cells={(r+i,c+j) for i in range(3) for j in range(3)}
            if all(grid[x][y]==0 for x,y in cells) and not cells&used:
                blocks.append((r,c));used|=cells
    for r,c in blocks:
        for i in range(3):
            for j in range(3): out[r+i][c+j]=1
    return out
