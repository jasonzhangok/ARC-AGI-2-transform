def transform(grid):
    output = []
    for r, row in enumerate(grid):
        if r % 2 == 0:
            output.append(row[:])
        else:
            output.append([row[-1]] + row[:-1])
    return output
