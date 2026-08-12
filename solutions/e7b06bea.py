def transform(grid):
    h, w = len(grid), len(grid[0])
    block = 0
    while block < h and grid[block][0] == 5:
        block += 1

    legend_cols = []
    for c in range(1, w):
        values = {grid[r][c] for r in range(h)}
        if len(values) == 1 and 0 not in values:
            legend_cols.append(c)
    colors = [grid[0][c] for c in legend_cols]
    target = min(legend_cols) - 1
    out = [[0] * w for _ in range(h)]
    for r in range(block):
        out[r][0] = 5
    for r in range(h):
        out[r][target] = colors[(r // block) % len(colors)]
    return out
