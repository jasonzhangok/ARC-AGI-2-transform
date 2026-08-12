def transform(grid):
    colored = [value for row in grid for value in row if value != 0]
    output = [[colored[0]] * len(colored)]
    return output
