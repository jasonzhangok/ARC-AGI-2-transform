def transform(grid):
    height = len(grid)
    width = len(grid[0])
    marker_row = 0
    marker_col = 0
    marker_color = 0

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0 and grid[row][col] != 5:
                marker_row = row
                marker_col = col
                marker_color = grid[row][col]

    output = [row[:] for row in grid]
    for row in range(marker_row % 2, height, 2):
        for col in range(marker_col % 2, width, 2):
            if grid[row][col] == 0:
                output[row][col] = marker_color

    return output
