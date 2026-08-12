def transform(grid):
    h, w = len(grid), len(grid[0])
    colors = {v for row in grid for v in row if v != 0}
    scale = len(colors)
    out = [[grid[r // scale][c // scale] for c in range(w * scale)]
           for r in range(h * scale)]
    candidates = []
    for color in colors:
        cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == color]
        r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
        c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
        if (len(cells) == (r1 - r0 + 1) * (c1 - c0 + 1)
                and r1 - r0 >= 1 and c1 - c0 >= 1
                and r1 - r0 < h - 1 and c1 - c0 < w - 1):
            candidates.append((len(cells), r0, r1, c0, c1))
    _, r0, r1, c0, c1 = min(candidates)
    R0, R1 = r0 * scale, (r1 + 1) * scale - 1
    C0, C1 = c0 * scale, (c1 + 1) * scale - 1
    for r, c, dr, dc in ((R0, C0, -1, -1), (R0, C1, -1, 1),
                         (R1, C0, 1, -1), (R1, C1, 1, 1)):
        for step in range(1, scale + 1):
            y, x = r + dr * step, c + dc * step
            if 0 <= y < h * scale and 0 <= x < w * scale and out[y][x] == 0:
                out[y][x] = 2
    output = out
    return output
