def transform(grid):
    n = len(grid)
    clockwise = [[grid[n - 1 - r][c] for r in range(n)] for c in range(n)]
    counterclockwise = [[grid[r][n - 1 - c] for r in range(n)] for c in range(n)]
    halfturn = [row[::-1] for row in grid[::-1]]
    output = ([grid[r][:] + clockwise[r] for r in range(n)]
            + [counterclockwise[r] + halfturn[r] for r in range(n)])
    return output
