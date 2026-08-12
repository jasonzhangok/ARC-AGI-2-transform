def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    counts = {}
    for row in grid:
        for color in row:
            counts[color] = counts.get(color, 0) + 1
    background = 0
    largest_count = -1
    for color in counts:
        if counts[color] > largest_count:
            background = color
            largest_count = counts[color]

    panels = []
    col = 0
    while col < width:
        if all(grid[row][col] == background for row in range(height)):
            col += 1
        else:
            left = col
            while col < width and not all(grid[row][col] == background for row in range(height)):
                col += 1
            panels.append((left, col))

    panel_colors = []
    for left, right in panels:
        foreground = background
        for row in range(height):
            for col in range(left, right):
                if grid[row][col] != background:
                    foreground = grid[row][col]
        panel_colors.append(foreground)

    for panel_index in range(len(panels)):
        left, right = panels[panel_index]
        fill_color = panel_colors[(panel_index + 1) % len(panel_colors)]
        for row in range(height):
            for col in range(left, right):
                if output[row][col] == background:
                    output[row][col] = fill_color

    return output
