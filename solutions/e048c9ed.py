def transform(grid):
    output = [row[:] for row in grid]
    marker_row = None
    marker_column = None
    for row_index, row in enumerate(grid):
        nonzero_columns = []
        for column, value in enumerate(row):
            if value != 0:
                nonzero_columns.append(column)
        if (len(nonzero_columns) == 1
                and row[nonzero_columns[0]] == 5):
            marker_row = row_index
            marker_column = nonzero_columns[0]
            break

    if marker_column is None:
        return output
    for row_index, row in enumerate(grid):
        if row_index == marker_row:
            continue
        nonzero_columns = []
        for column, value in enumerate(row):
            if value != 0:
                nonzero_columns.append(column)
        if not nonzero_columns:
            continue
        interval_count = len(nonzero_columns) - 1
        bar_color = row[nonzero_columns[0]]
        if bar_color == 7:
            interval_count = 10 - bar_color
        output[row_index][marker_column] = interval_count * interval_count % 10
    return output
