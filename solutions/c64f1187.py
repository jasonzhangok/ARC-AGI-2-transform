def transform(grid):
    height = len(grid)
    width = len(grid[0])
    one_rows = []
    for row in range(height):
        if 1 in grid[row]:
            one_rows.append(row)
    glyph_top = min(one_rows)
    palette_row = glyph_top - 1

    glyphs = {}
    for col in range(width):
        color = grid[palette_row][col]
        if color != 0:
            glyphs[color] = [
                [grid[glyph_top + row][col + 1 + inner_col] == 1 for inner_col in range(2)]
                for row in range(2)
            ]

    row_flags = [5 in grid[row] for row in range(height)]
    col_flags = [any(grid[row][col] == 5 for row in range(height)) for col in range(width)]
    row_bands = []
    row = 0
    while row < height:
        if not row_flags[row]:
            row += 1
            continue
        start = row
        while row + 1 < height and row_flags[row + 1]:
            row += 1
        row_bands.append((start, row))
        row += 1
    col_bands = []
    col = 0
    while col < width:
        if not col_flags[col]:
            col += 1
            continue
        start = col
        while col + 1 < width and col_flags[col + 1]:
            col += 1
        col_bands.append((start, col))
        col += 1

    layout_top = row_bands[0][0]
    layout_left = col_bands[0][0]
    output_height = row_bands[-1][1] - layout_top + 1
    output_width = col_bands[-1][1] - layout_left + 1
    output = [[0 for col in range(output_width)] for row in range(output_height)]

    for row_start, row_end in row_bands:
        for col_start, col_end in col_bands:
            color = 0
            for row in range(row_start, row_end + 1):
                for col in range(col_start, col_end + 1):
                    if grid[row][col] != 0 and grid[row][col] != 5:
                        color = grid[row][col]
            if color != 0:
                glyph = glyphs[color]
                target_row = row_start - layout_top
                target_col = col_start - layout_left
                for row in range(2):
                    for col in range(2):
                        if glyph[row][col]:
                            output[target_row + row][target_col + col] = color
    return output
