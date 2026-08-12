def transform(grid):
    output = [row[:] for row in grid]
    cells = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 5]
    r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
    c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
    for r in range(r0 + 1, r1):
        for c in range(c0 + 1, c1):
            output[r][c] = 8
    for c in range(c0, c1 + 1):
        if grid[r0][c] == 0:
            for r in range(0, r0 + 1):
                output[r][c] = 8
        if grid[r1][c] == 0:
            for r in range(r1, len(grid)):
                output[r][c] = 8
    for r in range(r0, r1 + 1):
        if grid[r][c0] == 0:
            for c in range(0, c0 + 1):
                output[r][c] = 8
        if grid[r][c1] == 0:
            for c in range(c1, len(grid[0])):
                output[r][c] = 8
    return output
