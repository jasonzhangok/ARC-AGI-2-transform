def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    markers = []
    object_points = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 4:
                markers.append((row, col))
            elif grid[row][col] in (1, 8):
                object_points.append((row, col))

    target_group = None
    for first in range(len(markers)):
        for second in range(first + 1, len(markers)):
            for third in range(second + 1, len(markers)):
                group = [markers[first], markers[second], markers[third]]
                rows = sorted({point[0] for point in group})
                cols = sorted({point[1] for point in group})
                if (len(rows) == 2 and len(cols) == 2 and
                        rows[1] - rows[0] == 2 and cols[1] - cols[0] == 2):
                    target_group = group

    target_row = (
        min(point[0] for point in target_group) +
        max(point[0] for point in target_group)
    ) // 2
    target_col = (
        min(point[1] for point in target_group) +
        max(point[1] for point in target_group)
    ) // 2
    source = None
    for marker in markers:
        if marker not in target_group:
            source = marker

    top = min(row for row, col in object_points)
    bottom = max(row for row, col in object_points)
    left = min(col for row, col in object_points)
    right = max(col for row, col in object_points)
    center_row = (top + bottom) // 2
    center_col = (left + right) // 2

    if source[0] < center_row:
        source_direction = 0 if source[1] < center_col else 1
    else:
        source_direction = 2 if source[1] > center_col else 3
    if target_row < center_row:
        target_direction = 0 if target_col < center_col else 1
    else:
        target_direction = 2 if target_col > center_col else 3
    turns = (target_direction - source_direction) % 4

    pattern = [grid[row][left:right + 1] for row in range(top, bottom + 1)]
    for _ in range(turns):
        pattern = [list(row) for row in zip(*pattern[::-1])]

    for row, col in markers:
        output[row][col] = 0
    output[target_row][target_col] = 4
    for row in range(len(pattern)):
        for col in range(len(pattern[0])):
            output[top + row][left + col] = pattern[row][col]
    return output
