import math
from collections import Counter


def transform(grid):
    h,w=len(grid),len(grid[0]); out=[row[:] for row in grid]
    colors=[v for v in set(sum(grid,[])) if v not in (0,1,2)]
    objects=[]
    for color in colors:
        cells=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==color]
        objects.append((sum(r for r,_ in cells)/len(cells),sum(c for _,c in cells)/len(cells),color))
    cr=sum(r for r,_,_ in objects)/len(objects); cc=sum(c for _,c,_ in objects)/len(objects)
    objects.sort(key=lambda x:math.atan2(x[1]-cc,cr-x[0]))
    mapping={objects[i][2]:objects[(i+1)%len(objects)][2] for i in range(len(objects))}
    for r in range(h):
        for c in range(w):
            if grid[r][c] in mapping: out[r][c]=mapping[grid[r][c]]
    return out
