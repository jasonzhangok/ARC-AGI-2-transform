

def transform(grid):
    height = len(grid)
    width = len(grid[0])
    top = next(
        row for row in range(height)
        if sum(value != 0 for value in grid[row]) > width // 2
    )
    bottom = max(
        row for row in range(height)
        if sum(value != 0 for value in grid[row]) > width // 2
    )
    left = next(
        col for col in range(width)
        if sum(grid[row][col] != 0 for row in range(height)) > height // 2
    )
    right = max(
        col for col in range(width)
        if sum(grid[row][col] != 0 for row in range(height)) > height // 2
    )

    top_color = {}
    for cell_value in (grid[top]):
        top_color[cell_value] = top_color.get(cell_value, 0) + 1
    top_color = max(top_color, key=top_color.get)
    bottom_color = {}
    for cell_value in (grid[bottom]):
        bottom_color[cell_value] = bottom_color.get(cell_value, 0) + 1
    bottom_color = max(bottom_color, key=bottom_color.get)
    left_color = {}
    for cell_value in (grid[row][left] for row in range(height)):
        left_color[cell_value] = left_color.get(cell_value, 0) + 1
    left_color = max(left_color, key=left_color.get)
    right_color = {}
    for cell_value in (grid[row][right] for row in range(height)):
        right_color[cell_value] = right_color.get(cell_value, 0) + 1
    right_color = max(right_color, key=right_color.get)
    output = [row[:] for row in grid]

    for row in range(top + 1, bottom):
        for col in range(left + 1, right):
            output[row][col] = 0
    for row in range(top + 1, bottom):
        for col in range(left + 1, right):
            color = grid[row][col]
            if color == top_color:
                output[top + 1][col] = color
            elif color == bottom_color:
                output[bottom - 1][col] = color
            elif color == left_color:
                output[row][left + 1] = color
            elif color == right_color:
                output[row][right - 1] = color
    return output
