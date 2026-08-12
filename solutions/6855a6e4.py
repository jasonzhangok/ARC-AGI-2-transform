def transform(grid):
    h, w = len(grid), len(grid[0])
    out = [[0 if v == 5 else v for v in row] for row in grid]
    fives = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    twos = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    for r, c in fives:
        candidates = []
        for rr, cc in twos:
            if rr == r:
                candidates.append((abs(cc-c), r, 2*cc-c))
            if cc == c:
                candidates.append((abs(rr-r), 2*rr-r, c))
        _, nr, nc = min(candidates)
        if 0 <= nr < h and 0 <= nc < w:
            out[nr][nc] = 5
    return out
