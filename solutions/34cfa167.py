def transform(grid):
    rows = len(grid)
    cols = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = 0
    background_count = -1
    for value in counts:
        if counts[value] > background_count:
            background = value
            background_count = counts[value]

    source_top = rows
    source_left = cols
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                source_top = r
                source_left = c
                break
        if source_top != rows:
            break

    source_right = source_left
    while source_right + 1 < cols and grid[source_top][source_right + 1] == 1:
        source_right += 1
    source_bottom = source_top
    while source_bottom + 1 < rows and grid[source_bottom + 1][source_left] == 1:
        source_bottom += 1

    target_top = rows
    target_left = cols
    for r in range(rows):
        for c in range(cols):
            if (grid[r][c] == 1 and
                    not (source_top <= r <= source_bottom and
                         source_left <= c <= source_right)):
                if target_top == rows:
                    target_top = r
                if c < target_left:
                    target_left = c
    marker_height = source_bottom - source_top + 1
    marker_width = source_right - source_left + 1
    target_bottom = target_top + marker_height - 1
    target_right = target_left + marker_width - 1

    horizontal_border = grid[source_top][source_right + 1]
    payload = grid[source_top][source_right + 3]
    vertical_border = grid[source_bottom + 1][source_left]
    result = [row[:] for row in grid]

    for r in range(source_top, source_bottom + 1):
        for c in range(target_left, target_right + 1):
            result[r][c] = 1
    for r in range(target_top, target_bottom + 1):
        for c in range(source_left, source_right + 1):
            result[r][c] = 1

    for c in range(source_right + 1, target_left):
        phase = (c - source_right) % 4
        value = background
        if phase == 1:
            value = horizontal_border
        elif phase == 3:
            value = payload
        for r in range(source_top, source_bottom + 1):
            result[r][c] = value
        for r in range(target_top, target_bottom + 1):
            result[r][c] = value
        result[source_top - 1][c] = horizontal_border
        result[target_bottom + 1][c] = horizontal_border

    for r in range(source_bottom + 1, target_top):
        phase = (r - source_bottom) % 4
        value = background
        if phase == 1:
            value = vertical_border
        elif phase == 3:
            value = payload
        for c in range(source_left, source_right + 1):
            result[r][c] = value
        for c in range(target_left, target_right + 1):
            result[r][c] = value
        result[r][source_left - 1] = vertical_border
        result[r][target_right + 1] = vertical_border

    return result
