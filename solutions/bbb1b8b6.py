def transform(grid):
    separator = next(c for c in range(len(grid[0])) if all(row[c] == 5 for row in grid))
    left = [row[:separator] for row in grid]
    right = [row[separator + 1:] for row in grid]
    if any(right[r][c] != 0 and left[r][c] != 0 for r in range(len(grid)) for c in range(separator)):
        return [row[:] for row in left]
    return [
        [right[r][c] if right[r][c] != 0 else left[r][c] for c in range(separator)]
        for r in range(len(grid))
    ]
