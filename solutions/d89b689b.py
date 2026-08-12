def transform(grid):
    h, w = len(grid), len(grid[0])
    square = next(
        (r, c)
        for r in range(h - 1)
        for c in range(w - 1)
        if all(grid[r + dr][c + dc] == 8 for dr in (0, 1) for dc in (0, 1))
    )
    r0, c0 = square
    output = [[0] * w for _ in range(h)]
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value in (0, 8):
                continue
            target_r = r0 if r < r0 else r0 + 1
            target_c = c0 if c < c0 else c0 + 1
            output[target_r][target_c] = value
    return output
