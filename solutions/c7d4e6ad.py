def transform(grid):
    output = []
    for row in grid:
        labels = [value for value in row if value not in (0, 5)]
        color = labels[0] if labels else None
        output.append([color if value == 5 and color is not None else value for value in row])
    return output
