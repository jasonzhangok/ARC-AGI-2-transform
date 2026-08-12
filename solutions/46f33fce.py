def transform(grid):
    h, w = len(grid), len(grid[0])
    out = [[0] * (2 * w) for _ in range(2 * h)]
    for r in range(h):
        for c in range(w):
            color = grid[r][c]
            if color == 0:
                continue
            r0, c0 = 2 * (r - 1), 2 * (c - 1)
            for y in range(max(0, r0), min(2 * h, r0 + 4)):
                for x in range(max(0, c0), min(2 * w, c0 + 4)):
                    out[y][x] = color
    return out
