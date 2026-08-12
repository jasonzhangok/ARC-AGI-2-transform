def transform(grid):
    height = len(grid)
    width = len(grid[0])
    markers = []
    for top in range(height - 2):
        for left in range(width - 2):
            corners = [(top, left), (top, left + 2),
                       (top + 2, left), (top + 2, left + 2)]
            present = []
            for corner in corners:
                if grid[corner[0]][corner[1]] == 4:
                    present.append(corner)
            if len(present) == 3:
                for corner in corners:
                    if corner not in present:
                        markers.append((top, left, corner))

    raw_template = []
    for row in range(height):
        for column in range(width):
            if grid[row][column] == 2:
                raw_template.append((row, column))
    source = markers[0]
    source_distance = height + width
    for marker in markers:
        anchor = marker[2]
        distance = min(abs(row - anchor[0]) + abs(column - anchor[1])
                       for row, column in raw_template)
        if distance < source_distance:
            source = marker
            source_distance = distance
    source_anchor = source[2]

    template = set()
    template_rows = set(row for row, column in raw_template)
    for row in template_rows:
        nearest = None
        nearest_distance = width + 1
        for cell_row, cell_column in raw_template:
            if cell_row == row and abs(cell_column - source_anchor[1]) < nearest_distance:
                nearest = (cell_row, cell_column)
                nearest_distance = abs(cell_column - source_anchor[1])
        template.add(nearest)
    template_columns = set(column for row, column in raw_template)
    for column in template_columns:
        nearest = None
        nearest_distance = height + 1
        for cell_row, cell_column in raw_template:
            if cell_column == column and abs(cell_row - source_anchor[0]) < nearest_distance:
                nearest = (cell_row, cell_column)
                nearest_distance = abs(cell_row - source_anchor[0])
        template.add(nearest)
    farthest = max(abs(row - source_anchor[0]) + abs(column - source_anchor[1])
                   for row, column in raw_template)
    for row, column in raw_template:
        if abs(row - source_anchor[0]) + abs(column - source_anchor[1]) == farthest:
            template.add((row, column))
    if source_distance > 0:
        template = set(raw_template)

    source_row_sign = -1 if source_anchor[0] == source[0] else 1
    source_column_sign = -1 if source_anchor[1] == source[1] else 1
    relative = []
    for row, column in template:
        relative.append((row - source_anchor[0], column - source_anchor[1]))

    output = []
    for row in grid:
        output.append([0 if value == 2 else value for value in row])
    for marker in markers:
        target_anchor = marker[2]
        target_row_sign = -1 if target_anchor[0] == marker[0] else 1
        target_column_sign = -1 if target_anchor[1] == marker[1] else 1
        for row_offset, column_offset in relative:
            row = (target_anchor[0]
                   + row_offset * target_row_sign * source_row_sign)
            column = (target_anchor[1]
                      + column_offset * target_column_sign * source_column_sign)
            if 0 <= row < height and 0 <= column < width:
                output[row][column] = 2
    return output
