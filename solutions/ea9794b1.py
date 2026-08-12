def transform(grid):
    parts = (
        [row[5:] for row in grid[:5]],
        [row[:5] for row in grid[5:]],
        [row[5:] for row in grid[5:]],
        [row[:5] for row in grid[:5]],
    )
    output = [[next((part[r][c] for part in parts if part[r][c] != 0), 0)
             for c in range(5)] for r in range(5)]
    return output
