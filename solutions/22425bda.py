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

    line_cells = {}
    colors = []
    for color in color_positions:
        if color == background:
            continue
        colors.append(color)
        points = color_positions[color]
        first_row, first_col = points[0]
        same_row = True
        same_col = True
        same_down_diagonal = True
        same_up_diagonal = True
        for row, col in points:
            if row != first_row:
                same_row = False
            if col != first_col:
                same_col = False
            if row - col != first_row - first_col:
                same_down_diagonal = False
            if row + col != first_row + first_col:
                same_up_diagonal = False
        cells = set()
        for row in range(height):
            for col in range(width):
                on_line = False
                if same_row and row == first_row:
                    on_line = True
                elif same_col and col == first_col:
                    on_line = True
                elif same_down_diagonal and row - col == first_row - first_col:
                    on_line = True
                elif same_up_diagonal and row + col == first_row + first_col:
                    on_line = True
                if on_line:
                    cells.add((row, col))
        line_cells[color] = cells

    above = {}
    for color in colors:
        above[color] = set()
    for row in range(height):
        for col in range(width):
            crossing_colors = []
            for color in colors:
                if (row, col) in line_cells[color]:
                    crossing_colors.append(color)
            visible_color = grid[row][col]
            if len(crossing_colors) >= 2 and visible_color in crossing_colors:
                for color in crossing_colors:
                    if color != visible_color:
                        above[color].add(visible_color)

    remaining = set(colors)
    ordered_colors = []
    while remaining:
        available = []
        for color in remaining:
            has_lower_predecessor = False
            for other_color in remaining:
                if color in above[other_color]:
                    has_lower_predecessor = True
            if not has_lower_predecessor:
                available.append(color)
        if not available:
            for color in remaining:
                available.append(color)
        chosen_color = available[0]
        for color in available:
            if color_counts[color] > color_counts[chosen_color]:
                chosen_color = color
            elif color_counts[color] == color_counts[chosen_color]:
                if color < chosen_color:
                    chosen_color = color
        ordered_colors.append(chosen_color)
        remaining.remove(chosen_color)

    output = [ordered_colors]
    return output
