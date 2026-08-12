def transform(grid):
    n = len(grid)
    output = [[0] * (n * n) for _ in range(n * n)]
    for br in range(n):
        for bc in range(n):
            outer = grid[br][bc]
            for r in range(n):
                for c in range(n):
                    if grid[r][c] == outer:
                        output[br * n + r][bc * n + c] = outer
    return output
