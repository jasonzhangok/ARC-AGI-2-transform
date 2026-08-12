def transform(grid):
    h,w=len(grid),len(grid[0]); out=[row[:] for row in grid]
    colors=[v for v in set(sum(grid,[])) if v not in (0,1,2)]
    objects=[]
    for color in colors:
        cells=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==color]
        objects.append((sum(r for r,_ in cells)/len(cells),sum(c for _,c in cells)/len(cells),color))
    cr=sum(r for r,_,_ in objects)/len(objects); cc=sum(c for _,c,_ in objects)/len(objects)
    remaining=objects[:]; ordered=[]
    while remaining:
        best_index=0
        for index in range(1,len(remaining)):
            ay=remaining[best_index][1]-cc; ax=cr-remaining[best_index][0]
            by=remaining[index][1]-cc; bx=cr-remaining[index][0]
            a_half=0 if ay<0 or ay==0 and ax>=0 else 1
            b_half=0 if by<0 or by==0 and bx>=0 else 1
            cross=ax*by-ay*bx
            if b_half<a_half or b_half==a_half and cross<0:
                best_index=index
        ordered.append(remaining.pop(best_index))
    objects=ordered
    mapping={objects[i][2]:objects[(i+1)%len(objects)][2] for i in range(len(objects))}
    for r in range(h):
        for c in range(w):
            if grid[r][c] in mapping: out[r][c]=mapping[grid[r][c]]
    output=out
    return output
