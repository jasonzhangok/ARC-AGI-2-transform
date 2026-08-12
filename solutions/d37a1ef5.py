def transform(grid):
    cells = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 2]
    r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
    c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
    markers = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 5]
    mr0, mr1 = min(r for r, _ in markers), max(r for r, _ in markers)
    mc0, mc1 = min(c for _, c in markers), max(c for _, c in markers)
    output = [row[:] for row in grid]
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            if output[r][c] == 0 and not (mr0 <= r <= mr1 and mc0 <= c <= mc1):
                output[r][c] = 2
    return output
