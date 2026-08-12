def transform(grid):
    height = len(grid)
    width = len(grid[0])

    color_counts = {}
    color_positions = {}
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            color_counts[color] = color_counts.get(color, 0) + 1
            if color not in color_positions:
                color_positions[color] = []
            color_positions[color].append((row, col))
    background = 0
    background_count = -1
    for color in color_counts:
        if color_counts[color] > background_count:
            background = color
            background_count = color_counts[color]

    blue_top = min(row for row, col in color_positions[1])
    output = [[background for col in range(width)] for row in range(height)]
    for color in color_positions:
        if color == background:
            continue
        cells = color_positions[color]
        object_top = min(row for row, col in cells)
        row_shift = blue_top - object_top
        for row, col in cells:
            output[row + row_shift][col] = color

    return output
