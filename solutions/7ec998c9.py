def transform(grid):
    height = len(grid)
    width = len(grid[0])
    color_counts = {}
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            color_counts[color] = color_counts.get(color, 0) + 1
    background = 0
    background_count = -1
    for color in color_counts:
        if color_counts[color] > background_count:
            background = color
            background_count = color_counts[color]
    marker_row = 0
    marker_col = 0
    marker_color = background
    for row in range(height):
        for col in range(width):
            if grid[row][col] != background:
                marker_row = row
                marker_col = col
                marker_color = grid[row][col]

    output = [row[:] for row in grid]
    for row in range(height):
        if row != marker_row:
            output[row][marker_col] = 1
    if background % 2 == 0:
        for col in range(0, marker_col + 1):
            output[0][col] = 1
        for col in range(marker_col, width):
            output[height - 1][col] = 1
    else:
        for col in range(marker_col, width):
            output[0][col] = 1
        for col in range(0, marker_col + 1):
            output[height - 1][col] = 1
    output[marker_row][marker_col] = marker_color
    return output
