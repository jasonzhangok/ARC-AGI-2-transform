def transform(grid):
    h, w = len(grid), len(grid[0])
    divider_row = next(r for r in range(h) if all(value == 1 for value in grid[r]))
    divider_col = next(c for c in range(w) if all(grid[r][c] == 1 for r in range(h)))
    quadrants = [
        [row[:divider_col] for row in grid[:divider_row]],
        [row[divider_col + 1:] for row in grid[:divider_row]],
        [row[:divider_col] for row in grid[divider_row + 1:]],
        [row[divider_col + 1:] for row in grid[divider_row + 1:]],
    ]
    out_h = len(quadrants[0])
    out_w = len(quadrants[0][0])
    out = [[0] * out_w for _ in range(out_h)]
    for index in (3, 2, 1, 0):
        layer = quadrants[index]
        for r in range(out_h):
            for c in range(out_w):
                if layer[r][c] != 0:
                    out[r][c] = layer[r][c]
    output = out
    return output
