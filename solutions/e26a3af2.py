from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])

    row_colors = [Counter(row).most_common(1)[0][0] for row in grid]
    row_result = [[row_colors[row]] * width for row in range(height)]

    col_colors = [
        Counter(grid[row][col] for row in range(height)).most_common(1)[0][0]
        for col in range(width)
    ]
    col_result = [col_colors[:] for _ in range(height)]

    row_changes = sum(
        grid[row][col] != row_result[row][col]
        for row in range(height)
        for col in range(width)
    )
    col_changes = sum(
        grid[row][col] != col_result[row][col]
        for row in range(height)
        for col in range(width)
    )
    return row_result if row_changes <= col_changes else col_result
