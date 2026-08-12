from collections import Counter


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

    top_color = Counter(grid[top]).most_common(1)[0][0]
    bottom_color = Counter(grid[bottom]).most_common(1)[0][0]
    left_color = Counter(grid[row][left] for row in range(height)).most_common(1)[0][0]
    right_color = Counter(grid[row][right] for row in range(height)).most_common(1)[0][0]
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
