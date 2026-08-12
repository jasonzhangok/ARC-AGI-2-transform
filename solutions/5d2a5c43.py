def transform(grid):
    return [[8 if row[c]!=0 or row[c+5]!=0 else 0 for c in range(4)] for row in grid]
