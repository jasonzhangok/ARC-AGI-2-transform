def transform(grid):
    height = len(grid)
    width = len(grid[0])

    header_top = 0
    for row in range(height - 2):
        nonzero = [value for value in grid[row] if value != 0]
        if len(set(nonzero)) >= 3 and grid[row] == grid[row + 1] == grid[row + 2]:
            header_top = row
            break
    header_bottom = header_top
    while header_bottom + 1 < height and grid[header_bottom + 1] == grid[header_top]:
        header_bottom += 1
    colors = [value for value in grid[header_top] if value != 0]

    template_cells = []
    template_color = 0
    for color in colors:
        cells = []
        for row in range(height):
            if not header_top <= row <= header_bottom:
                for column in range(width):
                    if grid[row][column] == color:
                        cells.append((row, column))
        if len(cells) > len(template_cells):
            template_cells = cells
            template_color = color

    top = min(row for row, column in template_cells)
    bottom = max(row for row, column in template_cells)
    left = min(column for row, column in template_cells)
    pattern = [(row - top, column - left) for row, column in template_cells]
    pattern_height = bottom - top + 1
    first_top = top - colors.index(template_color) * pattern_height

    output = [row[:] for row in grid]
    for row in range(header_top, header_bottom + 1):
        for column in range(width):
            output[row][column] = 0
    for index in range(len(colors)):
        copy_top = first_top + index * pattern_height
        for row_offset, column_offset in pattern:
            row = copy_top + row_offset
            column = left + column_offset
            if 0 <= row < height:
                output[row][column] = colors[index]
    return output
