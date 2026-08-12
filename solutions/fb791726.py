def transform(grid):
    h, w = len(grid), len(grid[0])
    out = [[0] * (2 * w) for _ in range(2 * h)]
    for r in range(h):
        for c in range(w):
            out[r][c] = grid[r][c]
            out[r + h][c + w] = grid[r][c]
    separator_rows = [r for r in range(1, h - 1)
                      if all(v == 0 for v in grid[r])
                      and grid[r - 1] == grid[r + 1]
                      and any(v != 0 for v in grid[r - 1])]
    for r in separator_rows:
        out[r] = [3] * (2 * w)
        out[r + h] = [3] * (2 * w)
    output = out
    return output
