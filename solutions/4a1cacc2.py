def transform(grid):
    h, w = len(grid), len(grid[0])
    r, c = next((r, c) for r in range(h) for c in range(w) if grid[r][c] != 8)
    color = grid[r][c]
    vertical_edge = 0 if r <= h - 1 - r else h - 1
    horizontal_edge = 0 if c <= w - 1 - c else w - 1
    out = [row[:] for row in grid]
    for y in range(min(r, vertical_edge), max(r, vertical_edge) + 1):
        for x in range(min(c, horizontal_edge), max(c, horizontal_edge) + 1):
            out[y][x] = color
    return out
