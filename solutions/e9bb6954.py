def transform(grid):
    h, w = len(grid), len(grid[0])
    objects = []
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            value = grid[r][c]
            if value and all(grid[y][x] == value
                             for y in range(r - 1, r + 2)
                             for x in range(c - 1, c + 2)):
                objects.append((r, c, value))
    out = [row[:] for row in grid]
    for r, c, value in objects:
        for x in range(w):
            out[r][x] = value
        for y in range(h):
            out[y][c] = value
    for r, _, _ in objects:
        for _, c, _ in objects:
            if not any(orow == r and ocol == c for orow, ocol, _ in objects):
                out[r][c] = 0
    output = out
    return output
