def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [[0] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 5:
                for x in range(max(0, r - 1), min(h, r + 2)):
                    for y in range(max(0, c - 1), min(w, c + 2)):
                        output[x][y] = 1
    return output
