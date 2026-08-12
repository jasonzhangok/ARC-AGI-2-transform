def transform(grid):
    zero_rows = {r for r, row in enumerate(grid) if 0 in row}
    zero_cols = {c for c in range(len(grid[0])) if any(grid[r][c] == 0 for r in range(len(grid)))}
    output = [
        [value if (r not in zero_rows and c not in zero_cols) or value == 2 else 0 for c, value in enumerate(row)]
        for r, row in enumerate(grid)
    ]
    return output
