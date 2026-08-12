def transform(grid):
    frame_cells = [
        (row, col)
        for row, line in enumerate(grid)
        for col, value in enumerate(line)
        if value == 1
    ]
    top = min(row for row, _ in frame_cells)
    bottom = max(row for row, _ in frame_cells)
    left = min(col for _, col in frame_cells)
    right = max(col for _, col in frame_cells)

    markers = [
        grid[row][col]
        for row in range(top + 1, bottom)
        for col in range(left + 1, right)
        if grid[row][col] not in (0, 1)
    ]
    marker_color = markers[0]
    marker_count = len(markers)

    return [
        [marker_color if row * 3 + col < marker_count else 0 for col in range(3)]
        for row in range(3)
    ]
