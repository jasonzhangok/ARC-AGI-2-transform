def transform(grid):
    half = len(grid[0]) // 2
    output = [[6 if row[c] != 0 or row[c + half] != 0 else 0 for c in range(half)] for row in grid]
    return output
