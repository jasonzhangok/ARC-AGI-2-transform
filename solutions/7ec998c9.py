from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    marker_row, marker_col = next(
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] != background
    )
    output = [row[:] for row in grid]
    for row in range(height):
        if row != marker_row:
            output[row][marker_col] = 1

    if marker_row % 2 == 1:
        top_columns = range(0, marker_col + 1)
        bottom_columns = range(marker_col, width)
    else:
        top_columns = range(marker_col, width)
        bottom_columns = range(0, marker_col + 1)
    for col in top_columns:
        output[0][col] = 1
    for col in bottom_columns:
        output[height - 1][col] = 1
    output[marker_row][marker_col] = grid[marker_row][marker_col]
    return output
