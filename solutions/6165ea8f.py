def _normalize(points):
    r0 = min(r for r, _ in points); c0 = min(c for _, c in points)
    return frozenset((r-r0, c-c0) for r, c in points)

def _variants(points):
    cur = set(points); ans = set()
    for _ in range(4):
        ans.add(_normalize(cur))
        ans.add(_normalize({(r, -c) for r, c in cur}))
        cur = {(c, -r) for r, c in cur}
    return ans

def transform(grid):
    labels = [row[-1] for row in grid if row[-1] != 0]
    shapes = {}
    for color in labels:
        points = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row[:-1]) if v == color}
        shapes[color] = _variants(points)
    n = len(labels); size = 3*n + 2
    out = [[0] * size for _ in range(size)]
    for i, color in enumerate(labels):
        for r in range(2):
            for c in range(2):
                out[r][3+3*i+c] = color
                out[3+3*i+r][c] = color
    for i, a in enumerate(labels):
        for j, b in enumerate(labels):
            if i == j: continue
            value = 2 if shapes[a] & shapes[b] else 5
            for r in range(2):
                for c in range(2): out[3+3*i+r][3+3*j+c] = value
    return out
