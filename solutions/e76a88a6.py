def transform(grid):
    h, w = len(grid), len(grid[0])
    template_cells = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value not in (0, 5)]
    r0, r1 = min(r for r, _ in template_cells), max(r for r, _ in template_cells)
    c0, c1 = min(c for _, c in template_cells), max(c for _, c in template_cells)
    template = [row[c0:c1 + 1] for row in grid[r0:r1 + 1]]
    th, tw = len(template), len(template[0])
    output = [row[:] for row in grid]
    used = set()
    for r in range(h - th + 1):
        for c in range(w - tw + 1):
            positions = {(r + x, c + y) for x in range(th) for y in range(tw)}
            if positions & used:
                continue
            if all(grid[x][y] == 5 for x, y in positions):
                for x in range(th):
                    for y in range(tw):
                        output[r + x][c + y] = template[x][y]
                used |= positions
    return output
