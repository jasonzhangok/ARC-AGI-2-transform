def transform(grid):
    h, w = len(grid), len(grid[0])
    empty_rows = {r for r in range(h) if all(value == 0 for value in grid[r])}
    empty_cols = {c for c in range(w) if all(grid[r][c] == 0 for r in range(h))}
    return [[2 if r in empty_rows or c in empty_cols else grid[r][c] for c in range(w)] for r in range(h)]
