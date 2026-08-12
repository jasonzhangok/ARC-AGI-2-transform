def transform(grid):
    height = len(grid)
    width = len(grid[0])
    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] != 0
    }
    objects = []
    while remaining:
        pending = [remaining.pop()]
        component = set(pending)
        while pending:
            row, col = pending.pop()
            for neighbor in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    pending.append(neighbor)
        objects.append(component)

    output = [row[:] for row in grid]
    for component in objects:
        marker_row, marker_col = next(
            (row, col) for row, col in component if grid[row][col] == 2
        )
        top = min(row for row, _ in component)
        bottom = max(row for row, _ in component)
        left = min(col for _, col in component)
        right = max(col for _, col in component)
        rect_height = bottom - top + 1
        rect_width = right - left + 1

        if rect_width > rect_height:
            half = rect_height - 1
            col_start = max(0, marker_col - half)
            col_end = min(width - 1, marker_col + half)
            rows = range(0, top) if marker_row == top else range(bottom + 1, height)
            for row in rows:
                for col in range(col_start, col_end + 1):
                    output[row][col] = 2 if col == marker_col else 3
        else:
            half = rect_width - 1
            row_start = max(0, marker_row - half)
            row_end = min(height - 1, marker_row + half)
            cols = range(0, left) if marker_col == left else range(right + 1, width)
            for row in range(row_start, row_end + 1):
                for col in cols:
                    output[row][col] = 2 if row == marker_row else 3
    return output
