def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [[0] * (2 * w) for _ in range(2 * h)]
    for shift in range(max(2 * h, 2 * w)):
        for r in range(h):
            for c in range(w):
                if r + shift < 2 * h and c + shift < 2 * w and grid[r][c] != 0:
                    output[r + shift][c + shift] = grid[r][c]
    return output
