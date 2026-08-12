def transform(grid):
    height = len(grid)
    width = len(grid[0])
    separator = 0
    for row in range(height):
        if all(value == 5 for value in grid[row]):
            separator = row
            break
    center_row = 0
    center_col = 0
    for row in range(separator + 1, height):
        for col in range(width):
            if grid[row][col] != 0:
                center_row = row
                center_col = col

    last_color_col = 0
    for col in range(width):
        if grid[0][col] != 0:
            last_color_col = col
    rings = grid[0][:last_color_col + 1]
    output = [row[:] for row in grid]
    for row in range(separator + 1, height):
        for col in range(width):
            distance = max(abs(row - center_row), abs(col - center_col))
            if distance < len(rings):
                output[row][col] = rings[distance]
    complete_radius = min(
        center_row - (separator + 1),
        height - 1 - center_row,
        center_col,
        width - 1 - center_col,
    )
    for radius in range(complete_radius + 1, len(rings)):
        output[0][radius] = 5
    return output
