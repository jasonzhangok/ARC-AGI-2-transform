def transform(grid):
    h, w = len(grid), len(grid[0])
    for r in range(h - 2):
        for c in range(w - 2):
            border = [
                grid[r][c], grid[r][c + 1], grid[r][c + 2],
                grid[r + 1][c], grid[r + 1][c + 2],
                grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2],
            ]
            if border[0] != 0 and all(value == border[0] for value in border):
                center = grid[r + 1][c + 1]
                if center != border[0]:
                    return [[center]]
    return [[]]
