def transform(grid):
    height, width = len(grid), len(grid[0])
    background = 1
    colors = {value for row in grid for value in row if value != background}
    positions = {
        color: {
            (row, col)
            for row in range(height)
            for col in range(width)
            if grid[row][col] == color
        }
        for color in colors
    }
    template_color = max(colors, key=lambda color: len(positions[color]))
    template_top = min(row for row, _ in positions[template_color])
    template_left = min(col for _, col in positions[template_color])
    shape = {
        (row - template_top, col - template_left)
        for row, col in positions[template_color]
    }

    output = [row[:] for row in grid]
    for color in colors:
        translations = set()
        for fragment_row, fragment_col in positions[color]:
            for shape_row, shape_col in shape:
                row_offset = fragment_row - shape_row
                col_offset = fragment_col - shape_col
                if all(
                    (row - row_offset, col - col_offset) in shape
                    for row, col in positions[color]
                ):
                    translations.add((row_offset, col_offset))
        row_offset, col_offset = next(iter(translations))
        for row, col in shape:
            output[row + row_offset][col + col_offset] = color
    return output
