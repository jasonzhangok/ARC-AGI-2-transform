def transform(grid):
    h, w = len(grid), len(grid[0])
    twos = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    r0, r1 = min(r for r, _ in twos), max(r for r, _ in twos)
    c0, c1 = min(c for _, c in twos), max(c for _, c in twos)
    cr, cc = (r0 + r1) // 2, (c0 + c1) // 2
    markers = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 3 and (r, c) != (cr, cc)]
    if all(r == cr for r, _ in markers):
        left = [p for p in markers if p[1] < cc]
        right = [p for p in markers if p[1] > cc]
        target = min(right, key=lambda p: p[1]) if len(right) >= len(left) else max(left, key=lambda p: p[1])
    else:
        above = [p for p in markers if p[0] < cr]
        below = [p for p in markers if p[0] > cr]
        target = min(below, key=lambda p: p[0]) if len(below) >= len(above) else max(above, key=lambda p: p[0])
    dr, dc = target[0] - cr, target[1] - cc
    out = [[0 if v == 2 else v for v in row] for row in grid]
    for r, c in twos:
        out[r + dr][c + dc] = 2
    out[target[0]][target[1]] = 3
    return out
