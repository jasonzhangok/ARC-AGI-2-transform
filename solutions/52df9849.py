from collections import Counter


def transform(grid):
    bg=Counter(v for row in grid for v in row).most_common(1)[0][0]
    colors=[v for v in {v for row in grid for v in row} if v!=bg]
    boxes=[]
    for color in colors:
        cells=[(r,c) for r,row in enumerate(grid) for c,v in enumerate(row) if v==color]
        boxes.append((color,min(r for r,_ in cells),max(r for r,_ in cells),min(c for _,c in cells),max(c for _,c in cells)))
    top=min(boxes,key=lambda b:(b[2]-b[1]+1)*(b[4]-b[3]+1))
    out=[row[:] for row in grid]
    for other in boxes:
        if other==top: continue
        for r in range(max(top[1],other[1]),min(top[2],other[2])+1):
            for c in range(max(top[3],other[3]),min(top[4],other[4])+1): out[r][c]=top[0]
    return out
