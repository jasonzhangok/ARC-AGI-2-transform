def transform(grid):
    separator = next(c for c in range(len(grid[0])) if all(row[c] == 5 for row in grid))
    output = []
    for row in grid:
        left = row[:separator]
        right = row[separator + 1:][::-1]
        output.append([a if a != 0 else b for a, b in zip(left, right)])
    return output
