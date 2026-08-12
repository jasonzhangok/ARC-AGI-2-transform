def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    marker_cells = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 4
    ]
    top = min(row for row, _ in marker_cells)
    bottom = max(row for row, _ in marker_cells)
    left = min(col for _, col in marker_cells)
    right = max(col for _, col in marker_cells)
    template = [line[left:right + 1] for line in grid[top:bottom + 1]]
    template_height = len(template)
    template_width = len(template[0])

    for start_row in range(height - template_height + 1):
        for start_col in range(width - template_width + 1):
            matches = True
            for row in range(template_height):
                for col in range(template_width):
                    expected = template[row][col]
                    actual = grid[start_row + row][start_col + col]
                    if expected == 4:
                        if actual not in (0, 4):
                            matches = False
                    elif actual != expected:
                        matches = False
            if matches:
                for row in range(template_height):
                    for col in range(template_width):
                        if template[row][col] == 4:
                            output[start_row + row][start_col + col] = 4
    return output
