def transform(grid):
    counts = {}
    for row in grid:
        for value in row:
            if value != 0:
                counts[value] = counts.get(value, 0) + 1
    marker_color = 0
    shape_color = 0
    for color in counts:
        if counts[color] == 1:
            marker_color = color
        else:
            shape_color = color

    output = []
    for row in grid:
        output_row = []
        for value in row:
            if value == shape_color:
                output_row.append(marker_color)
            elif value == marker_color:
                output_row.append(0)
            else:
                output_row.append(value)
        output.append(output_row)
    return output
