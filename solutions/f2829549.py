def transform(grid):
    divider = next(c for c in range(len(grid[0]))
                   if all(row[c] == 1 for row in grid))
    left = [row[:divider] for row in grid]
    right = [row[divider + 1:] for row in grid]
    return [[3 if a == 0 and b == 0 else 0 for a, b in zip(ra, rb)]
            for ra, rb in zip(left, right)]
