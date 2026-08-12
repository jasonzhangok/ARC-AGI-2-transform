def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for color in row:
            counts[color] = counts.get(color, 0) + 1
    background = max(counts, key=counts.get)

    template = []
    marker = None
    marker_color = None
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0:
                template.append((row, col))
            elif grid[row][col] != background:
                marker = (row, col)
                marker_color = grid[row][col]

    anchor = None
    best_distance = -1
    for row, col in template:
        row_step = marker[0] - row
        col_step = marker[1] - col
        if row_step != 0 and abs(row_step) == abs(col_step):
            if abs(row_step) > best_distance:
                best_distance = abs(row_step)
                anchor = (row, col)

    row_step = marker[0] - anchor[0]
    col_step = marker[1] - anchor[1]
    output = [row[:] for row in grid]
    repetition = 1
    while True:
        inside = False
        for row, col in template:
            target_row = row + repetition * row_step
            target_col = col + repetition * col_step
            if 0 <= target_row < height and 0 <= target_col < width:
                output[target_row][target_col] = marker_color
                inside = True
        if not inside:
            break
        repetition += 1
    return output
