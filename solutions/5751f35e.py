from collections import Counter


def transform(grid):
    h,w=len(grid),len(grid[0]);layers={}
    for r in range(h):
        for c in range(w):layers.setdefault(min(r,c,h-1-r,w-1-c),[]).append(grid[r][c])
    colors={d:(Counter(x for x in v if x!=0).most_common(1)[0][0] if any(x!=0 for x in v) else 0) for d,v in layers.items()}
    return [[colors[min(r,c,h-1-r,w-1-c)] for c in range(w)] for r in range(h)]
