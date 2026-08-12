def transform(grid):
    height, width = len(grid), len(grid[0])
    tile = [[0] * width for _ in range(height)]
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != 0:
                tile[(r - 1) % height][(c - 1) % width] = 2
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != 0:
                tile[r][c] = value
    return [tile[r % height] * 3 for r in range(height * 3)]
