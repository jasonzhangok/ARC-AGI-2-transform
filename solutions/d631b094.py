def transform(grid):
    colored = [value for row in grid for value in row if value != 0]
    return [[colored[0]] * len(colored)]
