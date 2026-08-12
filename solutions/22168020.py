def transform(grid):
    output = [row[:] for row in grid]
    colors = {value for row in grid for value in row if value != 0}
    for color in colors:
        for row, values in enumerate(grid):
            columns = [col for col, value in enumerate(values) if value == color]
            if len(columns) >= 2:
                for col in range(min(columns), max(columns) + 1):
                    output[row][col] = color
    return output
