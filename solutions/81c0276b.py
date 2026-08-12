from collections import Counter


def transform(grid):
    divider=Counter(v for row in grid for v in row if v).most_common(1)[0][0]
    counts=Counter(v for row in grid for v in row if v not in (0,divider))
    counts={color:n//4 for color,n in counts.items()}
    items=sorted((n,c) for c,n in counts.items())
    width=max(n for n,c in items)
    return [[c]*n+[0]*(width-n) for n,c in items]
