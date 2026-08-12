def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)

    occupied_columns = []
    for col in range(width):
        if any(grid[row][col] != background for row in range(height)):
            occupied_columns.append(col)

    column_groups = []
    for col in occupied_columns:
        if not column_groups or col != column_groups[-1][-1] + 1:
            column_groups.append([col])
        else:
            column_groups[-1].append(col)

    occupied_rows = []
    for row in range(height):
        if any(grid[row][col] != background for col in range(width)):
            occupied_rows.append(row)
    top = occupied_rows[0]
    bottom = occupied_rows[-1]
    left_symbol = column_groups[0]
    right_symbol = column_groups[-1]

    if grid[bottom][left_symbol[0]] != background:
        output_color = 3
    elif grid[bottom][left_symbol[-1]] != background:
        output_color = 2
    else:
        output_color = 1

    output = []
    for row in range(top, bottom + 1):
        new_row = []
        for col in range(right_symbol[0], right_symbol[-1] + 1):
            if grid[row][col] == background:
                new_row.append(background)
            else:
                new_row.append(output_color)
        output.append(new_row)
    return output
