def transform(grid):
    h, w = len(grid), len(grid[0])
    out = [[0] * w for _ in range(h)]
    r, c = next((r, c) for r in range(h) for c in range(w) if grid[r][c] != 0)
    color = grid[r][c]
    for dr, dc in ((1,1),(1,-1),(-1,1),(-1,-1)):
        x, y = r, c
        while 0 <= x < h and 0 <= y < w:
            out[x][y] = color
            x += dr; y += dc
    output = out
    return output
