def transform(grid):
    height = len(grid)
    width = len(grid[0])

    color_counts = {}
    for row in grid:
        for color in row:
            color_counts[color] = color_counts.get(color, 0) + 1

    background = None
    background_count = -1
    for color in color_counts:
        if color_counts[color] > background_count:
            background = color
            background_count = color_counts[color]

    bounding_boxes = {}
    for color in color_counts:
        if color == background:
            continue
        top = height
        bottom = -1
        left = width
        right = -1
        for row_index in range(height):
            for column_index in range(width):
                if grid[row_index][column_index] == color:
                    if row_index < top:
                        top = row_index
                    if row_index > bottom:
                        bottom = row_index
                    if column_index < left:
                        left = column_index
                    if column_index > right:
                        right = column_index
        bounding_boxes[color] = (top, bottom, left, right)

    frame = None
    frame_area = -1
    for color in bounding_boxes:
        top, bottom, left, right = bounding_boxes[color]
        area = (bottom - top + 1) * (right - left + 1)
        if area > frame_area:
            frame = color
            frame_area = area

    signal = None
    for color in bounding_boxes:
        if color != frame:
            signal = color

    top, bottom, left, right = bounding_boxes[frame]
    selected_rows = set()
    selected_columns = set()
    for row_index in range(top, bottom + 1):
        for column_index in range(left, right + 1):
            if grid[row_index][column_index] != signal:
                continue
            if (column_index > 0 and column_index + 1 < width
                    and grid[row_index][column_index - 1] == frame
                    and grid[row_index][column_index + 1] == frame):
                selected_columns.add(column_index)
            if (row_index > 0 and row_index + 1 < height
                    and grid[row_index - 1][column_index] == frame
                    and grid[row_index + 1][column_index] == frame):
                selected_rows.add(row_index)

    output = [row[:] for row in grid]
    for row_index in range(height):
        for column_index in range(width):
            if (row_index in selected_rows
                    or column_index in selected_columns):
                if (top <= row_index <= bottom
                        and left <= column_index <= right):
                    output[row_index][column_index] = frame
                else:
                    output[row_index][column_index] = signal

    return output
