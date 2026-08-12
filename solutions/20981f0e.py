def transform(grid):
    height, width = len(grid), len(grid[0])
    marker_rows = sorted({
        row
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 2
    })
    marker_cols = sorted({
        col
        for row in marker_rows
        for col in range(width)
        if grid[row][col] == 2
    })
    output = [row[:] for row in grid]

    for marker_row in marker_rows:
        top = marker_row + 1
        if top + 4 > height:
            continue
        for marker_col in marker_cols:
            left = marker_col + 1
            if left + 4 > width:
                continue
            pixels = [
                (row, col)
                for row in range(top, top + 4)
                for col in range(left, left + 4)
                if grid[row][col] == 1
            ]
            if not pixels:
                continue
            old_top = min(row for row, _ in pixels)
            old_bottom = max(row for row, _ in pixels)
            old_left = min(col for _, col in pixels)
            old_right = max(col for _, col in pixels)
            object_height = old_bottom - old_top + 1
            object_width = old_right - old_left + 1
            new_top = top + (4 - object_height) // 2
            new_left = left + (4 - object_width) // 2
            for row, col in pixels:
                output[row][col] = 0
            for row, col in pixels:
                output[new_top + row - old_top][new_left + col - old_left] = 1
    return output
