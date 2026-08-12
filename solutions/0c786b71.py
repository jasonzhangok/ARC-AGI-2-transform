def transform(grid):
    top = [
        list(reversed(row)) + row[:]
        for row in reversed(grid)
    ]
    bottom = [
        list(reversed(row)) + row[:]
        for row in grid
    ]
    return top + bottom
