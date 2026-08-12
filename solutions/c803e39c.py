def transform(grid):
    height = len(grid)
    width = len(grid[0])

    separator_cols = []
    for col in range(width):
        if all(grid[row][col] == 5 for row in range(height)):
            separator_cols.append(col)
    segments = []
    previous = -1
    for separator in separator_cols + [width]:
        if separator > previous + 1:
            segments.append((previous + 1, separator - 1))
        previous = separator

    panels = []
    for segment_left, segment_right in segments:
        points = []
        for row in range(height):
            for col in range(segment_left, segment_right + 1):
                if grid[row][col] != 0 and grid[row][col] != 5:
                    points.append((row, col))
        top = min(point[0] for point in points)
        bottom = max(point[0] for point in points)
        left = min(point[1] for point in points)
        right = max(point[1] for point in points)
        panel = []
        for row in range(top, bottom + 1):
            panel.append(grid[row][left:right + 1])
        panels.append(panel)

    inner_mask = panels[0]
    outer_mask = panels[1]
    foreground = 0
    for row in panels[2]:
        for color in row:
            if color != 0:
                foreground = color
    background = 0
    for row in panels[3]:
        for color in row:
            if color != 0:
                background = color

    size = len(inner_mask)
    output = []
    for outer_row in range(size):
        for inner_row in range(size):
            output_row = []
            for outer_col in range(size):
                for inner_col in range(size):
                    if outer_mask[outer_row][outer_col] != 0 and inner_mask[inner_row][inner_col] != 0:
                        output_row.append(foreground)
                    else:
                        output_row.append(background)
            output.append(output_row)
    return output
