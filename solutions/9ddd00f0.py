def transform(grid):
    size = len(grid)
    tile = next(k for k in range(1, size + 1) if k * k + k - 1 == size)
    color = next(value for row in grid for value in row if value != 0)
    out = [[0] * size for _ in range(size)]
    for macro_r in range(tile):
        for macro_c in range(tile):
            top = macro_r * (tile + 1)
            left = macro_c * (tile + 1)
            for r in range(tile):
                for c in range(tile):
                    if (r, c) != (macro_r, macro_c):
                        out[top + r][left + c] = color
    output = out
    return output
