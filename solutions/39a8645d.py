def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0:
                colors.add(grid[row][col])

    pattern_counts = {}
    pattern_colors = {}
    for color in colors:
        remaining = set()
        for row in range(height):
            for col in range(width):
                if grid[row][col] == color:
                    remaining.add((row, col))
        while remaining:
            start = remaining.pop()
            component = {start}
            stack = [start]
            while stack:
                row, col = stack.pop()
                for row_offset in (-1, 0, 1):
                    for col_offset in (-1, 0, 1):
                        neighbor = (row + row_offset, col + col_offset)
                        if neighbor in remaining:
                            remaining.remove(neighbor)
                            component.add(neighbor)
                            stack.append(neighbor)
            top = min(row for row, col in component)
            bottom = max(row for row, col in component)
            left = min(col for row, col in component)
            right = max(col for row, col in component)
            pattern_rows = []
            for row in range(top, bottom + 1):
                pattern_row = []
                for col in range(left, right + 1):
                    if (row, col) in component:
                        pattern_row.append(1)
                    else:
                        pattern_row.append(0)
                pattern_rows.append(tuple(pattern_row))
            pattern = tuple(pattern_rows)
            key = (color, pattern)
            pattern_counts[key] = pattern_counts.get(key, 0) + 1
            pattern_colors[key] = color

    selected_key = None
    selected_count = -1
    for key in pattern_counts:
        if pattern_counts[key] > selected_count:
            selected_key = key
            selected_count = pattern_counts[key]
    selected_color = pattern_colors[selected_key]
    selected_pattern = selected_key[1]
    output = []
    for pattern_row in selected_pattern:
        output_row = []
        for value in pattern_row:
            if value == 1:
                output_row.append(selected_color)
            else:
                output_row.append(0)
        output.append(output_row)

    return output
