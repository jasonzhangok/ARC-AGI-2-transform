def transform(grid):
    pairs = [[row[:] for row in grid[i:i + 2]] for i in range(0, len(grid), 2)]
    output = [row for pair in reversed(pairs) for row in pair]
    return output
