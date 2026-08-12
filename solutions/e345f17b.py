def transform(grid):
    half = len(grid[0]) // 2
    return [[4 if row[c] == 0 and row[c + half] == 0 else 0 for c in range(half)] for row in grid]
