def transform(grid):
    output = [row[:] for row in grid]
    cells = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 8]
    r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
    c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
    for c in range(c0, c1 + 1):
        if output[r0][c] == 0:
            output[r0][c] = 1
        if output[r1][c] == 0:
            output[r1][c] = 1
    for r in range(r0, r1 + 1):
        if output[r][c0] == 0:
            output[r][c0] = 1
        if output[r][c1] == 0:
            output[r][c1] = 1
    return output
