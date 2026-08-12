def transform(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    red = next((r, c) for r in range(h) for c in range(w) if grid[r][c] == 2)
    six = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 6]
    ar, ac = red
    cr = sum(r for r, _ in six) / len(six)
    cc = sum(c for _, c in six) / len(six)
    dr = 0 if abs(cr - ar) < .5 else (1 if cr > ar else -1)
    dc = 0 if abs(cc - ac) < .5 else (1 if cc > ac else -1)
    dr, dc = -dr, -dc
    r, c = ar + dr, ac + dc
    while 0 <= r < h and 0 <= c < w and grid[r][c] == 7:
        r, c = r + dr, c + dc
    if 0 <= r < h and 0 <= c < w:
        out[r][c] = 7
    return out
