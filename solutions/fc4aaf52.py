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

    foreground = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != background:
                foreground.append((row, col))
    top = min(row for row, col in foreground)
    bottom = max(row for row, col in foreground)
    middle = (top + bottom + 1) // 2
    shift = sum(grid[middle][col] != background for col in range(width))

    output = [[background for col in range(width)] for row in range(height)]
    for row, col in foreground:
        new_col = col + shift if row < middle else col
        if grid[row][col] == foreground_colors[0]:
            output[row][new_col] = foreground_colors[1]
        else:
            output[row][new_col] = foreground_colors[0]
    return output
