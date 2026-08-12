def transform(grid):
    source_color = next(value for row in grid for value in row if value != 0)

    if source_color == 1:
        bar_row = 1
        stem_col = 1
    elif source_color == 2:
        bar_row = 0
        stem_col = 1
    else:
        bar_row = 2
        stem_col = 2

    output = []
    for row in range(3):
        output_row = []
        for col in range(3):
            if row == bar_row or col == stem_col:
                output_row.append(5)
            else:
                output_row.append(0)
        output.append(output_row)
    return output
