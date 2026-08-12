def transform(grid):
    height = len(grid)
    width = len(grid[0])

    column_colors = []
    for col in range(width):
        counts = {}
        for row in range(height):
            value = grid[row][col]
            counts[value] = counts.get(value, 0) + 1
        column_colors.append(max(counts, key=counts.get))

    bands = []
    for col, color in enumerate(column_colors):
        if not bands or color != bands[-1][0]:
            bands.append([color, col, col])
        else:
            bands[-1][2] = col

    first_color, first_left, first_right = bands[0]
    signals = []
    for row in range(height):
        for col in range(first_left, first_right + 1):
            if grid[row][col] != first_color:
                signals.append((row, grid[row][col]))

    ordering_keys = []
    touches_top = min(row for row, color in signals) == 0
    for row, color in signals:
        distance = abs(2 * row - (height - 1))
        if touches_top:
            ordering_keys.append((-distance, row, color))
        else:
            ordering_keys.append((distance, -row, color))
    ordering_keys.sort()
    color_order = [item[2] for item in ordering_keys]
    color_order.append(first_color)

    band_bounds = {}
    for color, left, right in bands:
        band_bounds[color] = (left, right)

    output = []
    for row in range(height):
        new_row = []
        for color in color_order:
            left, right = band_bounds[color]
            for col in range(left, right + 1):
                new_row.append(grid[row][col])
        output.append(new_row)
    return output
