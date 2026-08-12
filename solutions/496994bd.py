def transform(grid):
    out = [row[:] for row in grid]
    used = 0
    while used < len(grid) and any(grid[used]):
        used += 1
    for i in range(used):
        out[len(grid) - used + i] = grid[used - 1 - i][:]
    output = out
    return output
