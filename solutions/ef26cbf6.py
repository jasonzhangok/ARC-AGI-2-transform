def transform(grid):
    h, w = len(grid), len(grid[0])
    row_lines = [-1] + [r for r, row in enumerate(grid) if all(v == 4 for v in row)] + [h]
    col_lines = [-1] + [c for c in range(w) if all(grid[r][c] == 4 for r in range(h))] + [w]
    out = [row[:] for row in grid]
    regions = []
    for ri, (a, b) in enumerate(zip(row_lines, row_lines[1:])):
        for ci, (x, y) in enumerate(zip(col_lines, col_lines[1:])):
            values = [grid[r][c] for r in range(a + 1, b) for c in range(x + 1, y)]
            marker = next((v for v in values if v not in (0, 1, 4)), None)
            regions.append((ri, ci, a, b, x, y, marker, 1 in values))
    markers = [region for region in regions if region[6] is not None]
    for ri, ci, a, b, x, y, _, has_ones in regions:
        if not has_ones:
            continue
        partner = next(region for region in markers
                       if region[0] == ri or region[1] == ci)
        color = partner[6]
        for r in range(a + 1, b):
            for c in range(x + 1, y):
                if out[r][c] == 1:
                    out[r][c] = color
    return out
