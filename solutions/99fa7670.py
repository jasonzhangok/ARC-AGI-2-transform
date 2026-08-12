def transform(grid):
    h, w = len(grid), len(grid[0])
    seeds = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0]
    seeds.sort()
    output = [row[:] for row in grid]
    for index, (r, c, color) in enumerate(seeds):
        next_row = seeds[index + 1][0] if index + 1 < len(seeds) else h
        for x in range(c, w):
            output[r][x] = color
        for x in range(r, next_row):
            output[x][w - 1] = color
    return output
