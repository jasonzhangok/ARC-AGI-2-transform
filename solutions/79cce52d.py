def transform(grid):
    n = len(grid) - 1
    top = grid[0].index(2) - 1
    left = next(r for r in range(1, len(grid)) if grid[r][0] == 2) - 1
    body = [row[1:] for row in grid[1:]]
    output = [[body[(r - left) % n][(c - top) % n] for c in range(n)]
            for r in range(n)]
    return output
