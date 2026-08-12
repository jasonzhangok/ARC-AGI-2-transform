def transform(grid):
    last = max(c for row in grid for c, value in enumerate(row) if value != 0)
    width = last + 1
    period = width
    for candidate in range(1, width):
        if all(grid[r][c] == grid[r][c + candidate] for r in range(len(grid)) for c in range(width - candidate)):
            period = candidate
            break
    return [[row[c % period] for c in range(len(row))] for row in grid]
