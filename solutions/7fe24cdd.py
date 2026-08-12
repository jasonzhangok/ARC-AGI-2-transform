def transform(grid):
    n=len(grid)
    cw=[list(row) for row in zip(*grid[::-1])]
    half=[list(row) for row in zip(*cw[::-1])]
    ccw=[list(row) for row in zip(*half[::-1])]
    output = [grid[r]+cw[r] for r in range(n)]+[ccw[r]+half[r] for r in range(n)]
    return output
