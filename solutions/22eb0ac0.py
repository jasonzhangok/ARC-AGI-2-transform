def transform(grid):
    output = [row[:] for row in grid]
    for row, values in enumerate(grid):
        if values[0] != 0 and values[0] == values[-1]:
            output[row] = [values[0]] * len(values)
    return output
