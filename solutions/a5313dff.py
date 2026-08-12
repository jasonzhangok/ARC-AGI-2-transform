def transform(grid):
    h, w = (len(grid), len(grid[0]))
    outside = set()
    q = []
    for r in range(h):
        for c in (0, w - 1):
            if grid[r][c] == 0 and (r, c) not in outside:
                outside.add((r, c))
                q.append((r, c))
    for c in range(w):
        for r in (0, h - 1):
            if grid[r][c] == 0 and (r, c) not in outside:
                outside.add((r, c))
                q.append((r, c))
    while q:
        r, c = q.pop(0)
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < h and 0 <= nc < w and (grid[nr][nc] == 0) and ((nr, nc) not in outside):
                outside.add((nr, nc))
                q.append((nr, nc))
    output = [[1 if grid[r][c] == 0 and (r, c) not in outside else grid[r][c] for c in range(w)] for r in range(h)]
    return output
