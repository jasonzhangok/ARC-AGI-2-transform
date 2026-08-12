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
    template_color = None
    template_size = -1
    for color in colors:
        if len(positions[color]) > template_size:
            template_color = color
            template_size = len(positions[color])
    template_top = min(row for row, _ in positions[template_color])
    template_left = min(col for _, col in positions[template_color])
    shape = {
        (row - template_top, col - template_left)
        for row, col in positions[template_color]
    }

    output = [row[:] for row in grid]
    for color in colors:
        uncovered = set(positions[color])
        while uncovered:
            best_offset = None
            best_overlap = set()
            for fragment_row, fragment_col in uncovered:
                for shape_row, shape_col in shape:
                    row_offset = fragment_row - shape_row
                    col_offset = fragment_col - shape_col
                    translated = {
                        (row + row_offset, col + col_offset)
                        for row, col in shape
                    }
                    if all(
                        0 <= row < height and 0 <= col < width
                        for row, col in translated
                    ):
                        overlap = translated & uncovered
                        if len(overlap) > len(best_overlap):
                            best_offset = (row_offset, col_offset)
                            best_overlap = overlap
            row_offset, col_offset = best_offset
            for row, col in shape:
                output[row + row_offset][col + col_offset] = color
            uncovered -= best_overlap
    return output
