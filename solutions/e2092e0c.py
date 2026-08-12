def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    output = [row[:] for row in grid]
    seen = set()
    marker = None
    marker_bounds = None
    marker_area = -1
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 5 or (row, col) in seen:
                continue
            pending = [(row, col)]
            seen.add((row, col))
            component = []
            while pending:
                current_row, current_col = pending.pop()
                component.append((current_row, current_col))
                for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row = current_row + delta_row
                    next_col = current_col + delta_col
                    if 0 <= next_row < height and 0 <= next_col < width and (grid[next_row][next_col] == 5) and ((next_row, next_col) not in seen):
                        seen.add((next_row, next_col))
                        pending.append((next_row, next_col))
            top = min((point[0] for point in component))
            bottom = max((point[0] for point in component))
            left = min((point[1] for point in component))
            right = max((point[1] for point in component))
            if top == bottom or left == right:
                continue
            cells = set(component)
            is_marker = True
            for current_row in range(top, bottom + 1):
                for current_col in range(left, right + 1):
                    expected = current_row == bottom or current_col == right
                    if ((current_row, current_col) in cells) != expected:
                        is_marker = False
            area = (bottom - top + 1) * (right - left + 1)
            if is_marker and area > marker_area:
                marker = 5
                marker_bounds = (top, bottom, left, right)
                marker_area = area
    if marker_bounds is None:
        output = output
    else:
        source_top, source_bottom, source_left, source_right = marker_bounds
        pattern_height = source_bottom - source_top
        pattern_width = source_right - source_left
        for row in range(1, height - pattern_height):
            for col in range(1, width - pattern_width):
                matches = True
                for pattern_row in range(pattern_height):
                    for pattern_col in range(pattern_width):
                        if grid[row + pattern_row][col + pattern_col] != grid[source_top + pattern_row][source_left + pattern_col]:
                            matches = False
                if not matches:
                    continue
                for frame_col in range(col - 1, col + pattern_width + 1):
                    output[row - 1][frame_col] = marker
                    output[row + pattern_height][frame_col] = marker
                for frame_row in range(row, row + pattern_height):
                    output[frame_row][col - 1] = marker
                    output[frame_row][col + pattern_width] = marker
        output = output
    return output
