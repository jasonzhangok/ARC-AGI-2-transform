def transform(grid):
    out = [row[:] for row in grid]
    target_pairs = ({1, 8}, {4, 7})
    for r, row in enumerate(grid):
        cells = [(c, v) for c, v in enumerate(row) if v != 0]
        if len(cells) != 2 or {cells[0][1], cells[1][1]} not in target_pairs:
            continue
        (c0, a), (c1, b) = cells
        out[r][c0] = a
        out[r][c0 + 1] = b
        if c1 != c0 + 1:
            out[r][c1] = 0
    return out
