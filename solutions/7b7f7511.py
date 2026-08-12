def transform(grid):
    h, w = len(grid), len(grid[0])
    if w % 2 == 0 and all(row[:w // 2] == row[w // 2:] for row in grid):
        return [row[:w // 2] for row in grid]
    return [row[:] for row in grid[:h // 2]]
