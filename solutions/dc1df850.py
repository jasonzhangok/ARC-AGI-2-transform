def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 2:
                for x in range(max(0, r - 1), min(h, r + 2)):
                    for y in range(max(0, c - 1), min(w, c + 2)):
                        if grid[x][y] == 0:
                            output[x][y] = 1
    return output
