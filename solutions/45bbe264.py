def transform(grid):
    h, w = len(grid), len(grid[0])
    markers = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c]]
    by_row = {r: color for r, _, color in markers}
    by_col = {c: color for _, c, color in markers}
    out = [[0] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            horizontal = by_row.get(r)
            vertical = by_col.get(c)
            if horizontal is not None and vertical is not None:
                out[r][c] = horizontal if horizontal == vertical else 2
            elif horizontal is not None:
                out[r][c] = horizontal
            elif vertical is not None:
                out[r][c] = vertical
    output = out
    return output
