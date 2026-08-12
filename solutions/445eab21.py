def transform(grid):
    counts = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    color = max(counts, key=counts.get)
    output = [[color, color], [color, color]]
    return output
