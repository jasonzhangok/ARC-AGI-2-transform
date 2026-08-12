def transform(grid):
    height = len(grid)
    width = len(grid[0])
    marker = next(
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 8
    )
    cells = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] not in (0, 8)
    }
    top = min(row for row, _ in cells)
    bottom = max(row for row, _ in cells)
    left = min(col for _, col in cells)
    right = max(col for _, col in cells)
    border_color = grid[top][left]
    interior_color = next(
        grid[row][col]
        for row, col in cells
        if grid[row][col] != border_color
    )

    marker_row, marker_col = marker
    if top <= marker_row <= bottom:
        left = min(left, marker_col)
        right = max(right, marker_col)
    else:
        top = min(top, marker_row)
        bottom = max(bottom, marker_row)

    output = [row[:] for row in grid]
    output[marker_row][marker_col] = 0
    for row in range(top, bottom + 1):
        for col in range(left, right + 1):
            output[row][col] = (
                border_color
                if row in (top, bottom) or col in (left, right)
                else interior_color
            )
    return output
