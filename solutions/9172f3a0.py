def transform(grid):
    output = []
    for row in grid:
        expanded = [value for value in row for _ in range(3)]
        output.extend([expanded[:] for _ in range(3)])
    return output
