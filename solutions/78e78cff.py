def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for color in row:
            counts[color] = counts.get(color, 0) + 1

    background = list(counts)[0]
    for color in counts:
        if background not in counts or counts[color] > counts[background]:
            background = color
    wall_color = background
    for color in counts:
        if color != background and (wall_color == background or counts[color] > counts[wall_color]):
            wall_color = color
    fill_color = background
    for color in counts:
        if color != background and color != wall_color:
            fill_color = color

    wall_points = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == wall_color:
                wall_points.append((row, col))
    top = min(point[0] for point in wall_points)
    bottom = max(point[0] for point in wall_points)
    left = min(point[1] for point in wall_points)
    right = max(point[1] for point in wall_points)

    output = [row[:] for row in grid]
    for row in range(top + 1, bottom):
        for col in range(left + 1, right):
            if output[row][col] == background:
                output[row][col] = fill_color

    top_wall = [col for col in range(left, right + 1) if grid[top][col] == wall_color]
    bottom_wall = [col for col in range(left, right + 1) if grid[bottom][col] == wall_color]
    left_wall = [row for row in range(top, bottom + 1) if grid[row][left] == wall_color]
    right_wall = [row for row in range(top, bottom + 1) if grid[row][right] == wall_color]

    for col in range(min(top_wall), max(top_wall) + 1):
        if grid[top][col] == background:
            for row in range(top + 1):
                output[row][col] = fill_color
    for col in range(min(bottom_wall), max(bottom_wall) + 1):
        if grid[bottom][col] == background:
            for row in range(bottom, height):
                output[row][col] = fill_color
    for row in range(min(left_wall), max(left_wall) + 1):
        if grid[row][left] == background:
            for col in range(left + 1):
                output[row][col] = fill_color
    for row in range(min(right_wall), max(right_wall) + 1):
        if grid[row][right] == background:
            for col in range(right, width):
                output[row][col] = fill_color
    return output
