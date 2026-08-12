def transform(grid):
    result = [row[:] for row in grid]
    separator = next((r for r, row in enumerate(grid) if all((value == 5 for value in row))))
    counts = {}
    for cell_value in (value for row in grid[:separator] for value in row):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    color = max(counts, key=counts.get)
    result[-1][len(grid[0]) // 2] = color
    output = result
    return output
