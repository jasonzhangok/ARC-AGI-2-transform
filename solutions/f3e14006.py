def transform(grid):
    height = len(grid)
    width = len(grid[0])
    horizontal_row = 0
    horizontal_count = -1
    for row in range(height):
        count = 0
        for col in range(width):
            if grid[row][col] != 0:
                count += 1
        if count > horizontal_count:
            horizontal_count = count
            horizontal_row = row

    vertical_col = 0
    vertical_count = -1
    for col in range(width):
        count = 0
        for row in range(height):
            if grid[row][col] != 0:
                count += 1
        if count > vertical_count:
            vertical_count = count
            vertical_col = col

    horizontal_counts = {}
    for col in range(width):
        color = grid[horizontal_row][col]
        if color != 0:
            horizontal_counts[color] = horizontal_counts.get(color, 0) + 1
    horizontal_base = 0
    largest = -1
    for color in horizontal_counts:
        if horizontal_counts[color] > largest:
            largest = horizontal_counts[color]
            horizontal_base = color

    vertical_counts = {}
    for row in range(height):
        if row == horizontal_row:
            continue
        color = grid[row][vertical_col]
        if color != 0:
            vertical_counts[color] = vertical_counts.get(color, 0) + 1
    vertical_base = 0
    largest = -1
    for color in vertical_counts:
        if vertical_counts[color] > largest:
            largest = vertical_counts[color]
            vertical_base = color

    horizontal_markers = []
    for col in range(width):
        if col != vertical_col and grid[horizontal_row][col] != 0 and grid[horizontal_row][col] != horizontal_base:
            horizontal_markers.append(col)
    vertical_markers = []
    for row in range(height):
        if row != horizontal_row and grid[row][vertical_col] != 0 and grid[row][vertical_col] != vertical_base:
            vertical_markers.append(row)

    horizontal_marker_color = grid[horizontal_row][horizontal_markers[0]]
    vertical_marker_color = grid[vertical_markers[0]][vertical_col]
    intersection_color = grid[horizontal_row][vertical_col]
    left = min(horizontal_markers)
    right = max(horizontal_markers)
    marker_top = min(vertical_markers)
    marker_bottom = max(vertical_markers)
    top = min(horizontal_row, marker_top)
    bottom = max(horizontal_row, marker_bottom)
    near_marker = vertical_markers[0]
    for row in vertical_markers:
        if abs(row - horizontal_row) < abs(near_marker - horizontal_row):
            near_marker = row

    output = [[0] * width for _ in range(height)]
    for row in range(top, bottom + 1):
        row_phase = (row - horizontal_row) % 2 == 0
        for col in range(left, right + 1):
            col_phase = (col - left) % 2 == 0
            if row_phase and col_phase:
                if marker_top <= row <= marker_bottom:
                    output[row][col] = vertical_marker_color
                else:
                    output[row][col] = horizontal_marker_color
            elif row_phase:
                if intersection_color == horizontal_base and row == near_marker:
                    output[row][col] = horizontal_base
                else:
                    output[row][col] = vertical_base
            elif col_phase:
                output[row][col] = horizontal_base
            else:
                output[row][col] = intersection_color
    return output
