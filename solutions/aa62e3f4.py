def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    foreground_colors = []
    for value in counts:
        if value != background:
            foreground_colors.append(value)
    output_color = min(foreground_colors, key=counts.get)

    output = [[background for col in range(width)] for row in range(height)]
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for row in range(height):
        for col in range(width):
            if grid[row][col] != background:
                continue
            for row_step, col_step in directions:
                neighbor_row = row + row_step
                neighbor_col = col + col_step
                if (0 <= neighbor_row < height and 0 <= neighbor_col < width
                        and grid[neighbor_row][neighbor_col] != background):
                    output[row][col] = output_color
                    break
    return output
