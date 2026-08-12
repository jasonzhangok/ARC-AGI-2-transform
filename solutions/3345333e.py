def transform(grid):
    height = len(grid)
    width = len(grid[0])

    color_counts = {}
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            color_counts[color] = color_counts.get(color, 0) + 1
    background = 0
    background_count = -1
    for color in color_counts:
        if color_counts[color] > background_count:
            background = color
            background_count = color_counts[color]
    main_color = background
    main_count = -1
    for color in color_counts:
        if color != background and color_counts[color] > main_count:
            main_color = color
            main_count = color_counts[color]
    occluder_color = background
    for color in color_counts:
        if color not in (background, main_color):
            occluder_color = color

    main_cells = set()
    occluder_cells = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] == main_color:
                main_cells.add((row, col))
            elif grid[row][col] == occluder_color:
                occluder_cells.add((row, col))

    best_axis = 0
    best_invalid = None
    best_hidden = -1
    for doubled_axis in range(2 * width - 1):
        outside = 0
        invalid = 0
        hidden = 0
        for row, col in main_cells:
            reflected_col = doubled_axis - col
            if not 0 <= reflected_col < width:
                outside += 1
            elif (row, reflected_col) in occluder_cells:
                hidden += 1
            elif (row, reflected_col) not in main_cells:
                invalid += 1
        if outside != 0:
            continue
        if best_invalid is None or invalid < best_invalid:
            best_axis = doubled_axis
            best_invalid = invalid
            best_hidden = hidden
        elif invalid == best_invalid and hidden > best_hidden:
            best_axis = doubled_axis
            best_hidden = hidden

    output = [row[:] for row in grid]
    for row, col in occluder_cells:
        output[row][col] = background
    for row, col in main_cells:
        output[row][col] = main_color
        reflected_col = best_axis - col
        if 0 <= reflected_col < width:
            output[row][reflected_col] = main_color

    return output
