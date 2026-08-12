def transform(grid):
    row_indices = [0, 0] + list(range(1, len(grid) - 1)) + [len(grid) - 1, len(grid) - 1]
    col_indices = [0, 0] + list(range(1, len(grid[0]) - 1)) + [len(grid[0]) - 1, len(grid[0]) - 1]
    return [[grid[r][c] for c in col_indices] for r in row_indices]
