def transform(grid):
    separator = next(c for c in range(len(grid[0])) if all(row[c] == 4 for row in grid))
    return [
        [2 if row[c] != 0 or row[c + separator + 1] != 0 else 0 for c in range(separator)]
        for row in grid
    ]
