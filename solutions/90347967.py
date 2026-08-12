def transform(grid):
    h, w = len(grid), len(grid[0])
    pivot = next((r, c) for r in range(h) for c in range(w) if grid[r][c] == 5)
    pr, pc = pivot
    output = [[0] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0:
                nr, nc = 2 * pr - r, 2 * pc - c
                if 0 <= nr < h and 0 <= nc < w:
                    output[nr][nc] = grid[r][c]
    return output
