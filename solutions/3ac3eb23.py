def transform(grid):
    height, width = len(grid), len(grid[0])
    seeds = [(c, value) for c, value in enumerate(grid[0]) if value != 0]
    result = [[0 for _ in range(width)] for _ in range(height)]
    for r in range(height):
        for column, color in seeds:
            offsets = (0,) if r % 2 == 0 else (-1, 1)
            for offset in offsets:
                c = column + offset
                if 0 <= c < width:
                    result[r][c] = color
    return result
