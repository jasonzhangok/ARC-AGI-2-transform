def transform(grid):
    out = [row[:] for row in grid]
    w = len(grid[0])
    for r, row in enumerate(grid):
        count = row.count(3)
        if count == 0:
            continue
        out[r] = [0 if value == 3 else value for value in out[r]]
        eights = [c for c, value in enumerate(row) if value == 8]
        start = max(eights) + 1 if eights else 0
        for c in range(start, min(start + count, w)):
            out[r][c] = 3
    output = out
    return output
