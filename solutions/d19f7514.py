def transform(grid):
    half = len(grid) // 2
    output = [
        [4 if grid[r][c] != 0 or grid[r + half][c] != 0 else 0 for c in range(len(grid[0]))]
        for r in range(half)
    ]
    return output
