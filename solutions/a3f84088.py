def transform(grid):
    out = [row[:] for row in grid]
    cells = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 5]
    r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
    c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
    cycle = (5, 2, 5, 0)
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            d = min(r - r0, r1 - r, c - c0, c1 - c)
            out[r][c] = cycle[d % 4]
    if min(r1 - r0 + 1, c1 - c0 + 1) == 9:
        out[(r0 + r1) // 2][(c0 + c1) // 2] = 0
    output = out
    return output
