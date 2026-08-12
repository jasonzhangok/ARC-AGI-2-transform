def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    for r in range(h):
        for c in range(1, w - 1):
            if grid[r][c] != 8:
                continue
            if (r >= 3 and r + 3 < h and c >= 3 and c + 3 < w and
                    grid[r][c-3] == grid[r][c-2] == 1 and
                    grid[r][c+2] == grid[r][c+3] == 1 and
                    grid[r-3][c] == grid[r-2][c] == 1 and
                    grid[r+2][c] == grid[r+3][c] == 1):
                out[r][c] = 4
    return out
