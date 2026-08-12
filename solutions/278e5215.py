def transform(grid):
    counts = {}
    for row in grid:
        for value in row:
            if value != 0:
                counts[value] = counts.get(value, 0) + 1
    mask_color = max(counts, key=counts.get)

    mask_cells = []
    legend_cells = []
    for row_index, row in enumerate(grid):
        for col_index, value in enumerate(row):
            if value == mask_color:
                mask_cells.append((row_index, col_index))
            elif value != 0:
                legend_cells.append((row_index, col_index))

    top = min(row for row, col in mask_cells)
    bottom = max(row for row, col in mask_cells)
    left = min(col for row, col in mask_cells)
    right = max(col for row, col in mask_cells)
    legend_top = min(row for row, col in legend_cells)
    legend_left = min(col for row, col in legend_cells)

    column_colors = []
    empty_color = 0
    for row_index in range(legend_top, legend_top + 3):
        legend_row = grid[row_index][legend_left:legend_left + right - left + 1]
        if len(set(legend_row)) == 1:
            empty_color = legend_row[0]
        elif not column_colors:
            column_colors = legend_row

    output = []
    for row_index in range(top, bottom + 1):
        output_row = []
        for col_index in range(left, right + 1):
            if grid[row_index][col_index] == mask_color:
                output_row.append(column_colors[col_index - left])
            else:
                output_row.append(empty_color)
        output.append(output_row)
    return output
