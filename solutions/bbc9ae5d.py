def transform(grid):
    row = grid[0]
    color = next(value for value in row if value != 0)
    initial = sum(value != 0 for value in row)
    return [[color if c < initial + r else 0 for c in range(len(row))] for r in range(len(row) // 2)]
