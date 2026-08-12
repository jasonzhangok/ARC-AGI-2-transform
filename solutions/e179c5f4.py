def transform(grid):
    h, w = len(grid), len(grid[0])
    seed_r, seed_c = next((r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 1)
    output = [[8] * w for _ in range(h)]
    c, direction = seed_c, 1
    for r in range(seed_r, -1, -1):
        output[r][c] = 1
        if w > 1:
            if c + direction < 0 or c + direction >= w:
                direction *= -1
            c += direction
    return output
