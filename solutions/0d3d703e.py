def transform(grid):
    mapping = {1: 5, 5: 1, 2: 6, 6: 2, 3: 4, 4: 3, 8: 9, 9: 8}
    return [[mapping.get(value, value) for value in row] for row in grid]
