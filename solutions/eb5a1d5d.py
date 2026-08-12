def transform(grid):
    runs = []
    for row in grid:
        row_runs = []
        for value in row:
            if not row_runs or value != row_runs[-1]:
                row_runs.append(value)
        if len(row_runs) > len(runs):
            runs = row_runs
    middle = len(runs) // 2
    layers = runs[:middle + 1]
    size = len(runs)
    output = []
    for row in range(size):
        output.append([layers[min(row, column, size - 1 - row, size - 1 - column)]
                       for column in range(size)])
    return output
