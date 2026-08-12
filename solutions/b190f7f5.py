def transform(grid):
    height = len(grid)
    width = len(grid[0])
    if width == 2 * height:
        size = height
        first = [row[:size] for row in grid]
        second = [row[size:] for row in grid]
    else:
        size = width
        first = [row[:] for row in grid[:size]]
        second = [row[:] for row in grid[size:]]

    first_is_mask = True
    for row in first:
        for value in row:
            if value != 0 and value != 8:
                first_is_mask = False
    if first_is_mask:
        mask = first
        layout = second
    else:
        mask = second
        layout = first

    output = [[0 for column in range(size * size)]
              for row in range(size * size)]
    for macro_row in range(size):
        for macro_column in range(size):
            color = layout[macro_row][macro_column]
            if color == 0:
                continue
            for row in range(size):
                for column in range(size):
                    if mask[row][column] == 8:
                        output[macro_row * size + row][macro_column * size + column] = color
    return output
