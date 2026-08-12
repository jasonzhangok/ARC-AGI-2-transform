def transform(grid):
    half = len(grid) // 2
    output = [
        [6 if (grid[r][c] != 0) != (grid[r + half][c] != 0) else 0 for c in range(len(grid[0]))]
        for r in range(half)
    ]
    return output
