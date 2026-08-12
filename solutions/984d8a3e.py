def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = []
    for row in grid:
        for color in row:
            if color not in colors:
                colors.append(color)

    left_color = colors[0]
    left_count = -1
    for color in colors:
        count = sum(row[0] == color for row in grid)
        if count > left_count:
            left_count = count
            left_color = color
    right_color = colors[0]
    right_count = -1
    for color in colors:
        if color == left_color:
            continue
        count = sum(row[-1] == color for row in grid)
        if count > right_count:
            right_count = count
            right_color = color
    middle_color = next(
        color for color in colors if color not in (left_color, right_color)
    )

    center_end = width // 2 + 1
    output = []
    for row in grid:
        middle_count = row.count(middle_color)
        new_row = [left_color] * width
        for col in range(width):
            if row[col] == right_color:
                new_row[col] = right_color
        start = max(0, center_end - middle_count)
        for col in range(start, start + middle_count):
            new_row[col] = middle_color
        output.append(new_row)
    return output
