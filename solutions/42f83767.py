def transform(grid):
    height, width = len(grid), len(grid[0])
    template_rows = []
    for row in range(height):
        if 5 in grid[row]:
            template_rows.append(row)

    template_top = min(template_rows)
    template_size = max(template_rows) - template_top + 1
    template_left = width
    for row in template_rows:
        for col in range(width):
            if grid[row][col] == 5 and col < template_left:
                template_left = col

    palette = []
    for col in range(template_left):
        color = grid[template_top][col]
        if color != 0 and color != 5 and color not in palette:
            palette.append(color)

    layout_points = []
    for row in range(template_top + template_size, height):
        for col in range(width):
            if grid[row][col] in palette:
                layout_points.append((row, col))
    layout_top = min(row for row, col in layout_points)
    layout_bottom = max(row for row, col in layout_points)
    layout_left = min(col for row, col in layout_points)
    layout_right = max(col for row, col in layout_points)

    result = []
    for layout_row in range(layout_top, layout_bottom + 1):
        for inner_row in range(template_size):
            output_row = []
            for layout_col in range(layout_left, layout_right + 1):
                color = grid[layout_row][layout_col]
                slot = palette.index(color)
                source_left = template_left + slot * (template_size + 1)
                for inner_col in range(template_size):
                    if grid[template_top + inner_row][source_left + inner_col] == 5:
                        output_row.append(color)
                    else:
                        output_row.append(0)
            result.append(output_row)
    return result
