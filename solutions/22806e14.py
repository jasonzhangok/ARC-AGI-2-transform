def transform(grid):
    height = len(grid)
    width = len(grid[0])

    color_counts = {}
    color_positions = {}
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            color_counts[color] = color_counts.get(color, 0) + 1
            if color not in color_positions:
                color_positions[color] = []
            color_positions[color].append((row, col))
    background = 0
    background_count = -1
    for color in color_counts:
        if color_counts[color] > background_count:
            background = color
            background_count = color_counts[color]
    marker_color = background
    for color in color_counts:
        if color != background and color_counts[color] == 5:
            marker_color = color
    main_color = background
    for color in color_counts:
        if color not in (background, marker_color):
            main_color = color

    marker = color_positions[marker_color]
    main_cells = color_positions[main_color]
    main_top = min(row for row, col in main_cells)
    main_bottom = max(row for row, col in main_cells)
    main_left = min(col for row, col in main_cells)
    main_right = max(col for row, col in main_cells)
    marker_center_row = sum(row for row, col in marker) // len(marker)
    marker_center_col = sum(col for row, col in marker) // len(marker)
    preserve_marker = False
    for row, col in marker:
        if row == 0:
            preserve_marker = True
    if main_top < marker_center_row < main_bottom:
        if main_left < marker_center_col < main_right:
            preserve_marker = True

    output = [row[:] for row in grid]
    if not preserve_marker:
        for row, col in marker:
            output[row][col] = background

    remaining = set(main_cells)
    while remaining:
        start = remaining.pop()
        component = {start}
        stack = [start]
        while stack:
            row, col = stack.pop()
            for neighbor in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    stack.append(neighbor)
        top = min(row for row, col in component)
        bottom = max(row for row, col in component)
        left = min(col for row, col in component)
        right = max(col for row, col in component)
        side = bottom - top + 1
        if side == right - left + 1 and side % 2 == 1:
            if len(component) == side * side:
                output[(top + bottom) // 2][(left + right) // 2] = marker_color

    return output
