def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [[0] * w for _ in range(h)]
    motif = ((5, 1, 5), (1, 0, 1), (5, 1, 5))
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 5:
                continue
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if 0 <= r + dr < h and 0 <= c + dc < w and motif[dr + 1][dc + 1] != 0:
                        output[r + dr][c + dc] = motif[dr + 1][dc + 1]
    return output
