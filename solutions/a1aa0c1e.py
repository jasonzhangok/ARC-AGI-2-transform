def transform(grid):
    full_rows = []
    for row_index, row in enumerate(grid):
        if row and row[0] != 0:
            is_full = True
            for value in row[1:]:
                if value != row[0]:
                    is_full = False
                    break
            if is_full:
                full_rows.append((row_index, row[0]))

    result = []
    ladder_bounds = []
    for index, (row_index, color) in enumerate(full_rows):
        if color == 9:
            continue
        next_row = full_rows[index + 1][0]
        rung_count = 0
        left = len(grid[0])
        right = -1
        for source_row in range(row_index + 1, next_row):
            color_columns = []
            for column, value in enumerate(grid[source_row]):
                if value == color:
                    color_columns.append(column)
            if (len(color_columns) == 3
                    and color_columns[1] == color_columns[0] + 1
                    and color_columns[2] == color_columns[1] + 1):
                rung_count += 1
                if color_columns[0] < left:
                    left = color_columns[0]
                if color_columns[2] > right:
                    right = color_columns[2]
        output_row = []
        for column in range(3):
            output_row.append(color if column < rung_count else 0)
        output_row.extend([9, 0])
        result.append(output_row)
        ladder_bounds.append((left, right))

    marker_column = 0
    for row in grid:
        for column, value in enumerate(row):
            if value == 5:
                marker_column = column
    nearest_index = -1
    nearest_distance = len(grid[0]) + 1
    for index, (left, right) in enumerate(ladder_bounds):
        if right < 0:
            continue
        if marker_column < left:
            distance = left - marker_column
        elif marker_column > right:
            distance = marker_column - right
        else:
            distance = 0
        if distance <= nearest_distance:
            nearest_distance = distance
            nearest_index = index
    if nearest_index >= 0:
        result[len(result) - 1 - nearest_index][4] = 5
    output = result
    return output
