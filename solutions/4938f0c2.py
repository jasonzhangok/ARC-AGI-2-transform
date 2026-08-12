def transform(grid):
    out = [row[:] for row in grid]
    markers = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 3]
    row_sum = min(r for r, _ in markers) + max(r for r, _ in markers)
    col_sum = min(c for _, c in markers) + max(c for _, c in markers)
    twos = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 2]
    h, w = len(grid), len(grid[0])
    for r, c in twos:
        for y, x in ((r, c), (row_sum - r, c), (r, col_sum - c),
                     (row_sum - r, col_sum - c)):
            if 0 <= y < h and 0 <= x < w:
                out[y][x] = 2
    output = out
    return output
