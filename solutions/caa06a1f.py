def transform(grid):
    color_positions = {}
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            value = grid[row][column]
            if value not in color_positions:
                color_positions[value] = []
            color_positions[value].append((row, column))
    cover = 0
    cover_score = -1
    for color in color_positions:
        rows = [row for row, column in color_positions[color]]
        columns = [column for row, column in color_positions[color]]
        score = ((max(rows) - min(rows) + 1) * (max(columns) - min(columns) + 1)
                 if len(color_positions[color]) > 1 else 0)
        if score > cover_score:
            cover = color
            cover_score = score

    visible = []
    for value in grid[0]:
        if value == cover:
            break
        visible.append(value)
    period = []
    for value in visible:
        if value in period:
            break
        period.append(value)
    shifted = period[1:] + period[:1]

    output = []
    for row in range(len(grid)):
        output.append([shifted[((row % 2) + column) % len(shifted)]
                       for column in range(len(grid[0]))])
    return output
