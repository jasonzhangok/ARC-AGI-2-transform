def transform(grid):
    out = [row[:] for row in grid]
    cells = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 1]
    top = min(r for r, _ in cells)
    bottom = max(r for r, _ in cells)
    split = top + (bottom - top + 1) // 2
    for r, c in cells:
        if r >= split:
            out[r][c] = 2
    output = out
    return output
