def transform(grid):
    h,w=len(grid),len(grid[0]); frame=grid[0][0]; out=[[0 if v==frame else v for v in row] for row in grid]
    rows={r for r in range(h) if 2 in grid[r]}; cols={c for c in range(w) if any(grid[r][c]==2 for r in range(h))}
    horizontal=len(rows)>=len(cols)
    selected=rows if horizontal else cols
    starts=[x for x in sorted(selected) if x-1 not in selected]
    offsets=[x-starts[0] for x in sorted(selected) if starts[0]<=x<(starts[1] if len(starts)>1 else max(selected)+1)]
    if len(starts)>1:
        period=starts[1]-starts[0];limit=h if horizontal else w
        selected={s+off for s in range(starts[0],limit,period) for off in offsets if s+off<limit}
    for r in range(h):
        for c in range(w):
            if out[r][c]==0 and ((horizontal and r in selected) or (not horizontal and c in selected)): out[r][c]=frame
    if horizontal:
        for c in range(w):
            if any(grid[r][c]==2 for r in range(h)):
                for r in selected:out[r][c]=2
    else:
        for r in range(h):
            if 2 in grid[r]:
                for c in selected:out[r][c]=2
    for r in range(h):
        if sum(grid[r][c]==3 for c in range(w)) > w//2:
            for c in range(w):
                out[r][c]=3
    for c in range(w):
        if sum(grid[r][c]==3 for r in range(h)) > h//2:
            for r in range(h):
                out[r][c]=3
    return out
