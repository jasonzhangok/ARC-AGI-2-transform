def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            color = grid[r][c]
            if color == 0:
                continue
            for x in range(c + 1, w):
                output[r][x] = 5 if (x - c) % 2 else color
    return output
