def transform(grid):
    row = grid[0]
    size = 5 * sum(value != 0 for value in row)
    out = [[0] * size for _ in range(size)]
    for i, color in enumerate(row):
        if color == 0:
            continue
        diagonal = size + i - 1
        for r in range(size):
            c = diagonal - r
            if 0 <= c < size:
                out[r][c] = color
    return out
