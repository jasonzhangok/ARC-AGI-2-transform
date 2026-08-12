def transform(grid):
    height = len(grid)
    width = len(grid[0])

    counts = {}
    for row in grid:
        for color in row:
            counts[color] = counts.get(color, 0) + 1

    background = None
    background_count = -1
    for color in counts:
        if counts[color] > background_count:
            background = color
            background_count = counts[color]

    last_signal_row = -1
    last_signal_col = -1
    for row in range(height):
        for col in range(width):
            if grid[row][col] != background:
                if row > last_signal_row:
                    last_signal_row = row
                if col > last_signal_col:
                    last_signal_col = col

    motif_height = last_signal_row
    motif_width = last_signal_col
    border = grid[last_signal_row][last_signal_col]
    result = []
    for row in range(height):
        result_row = []
        for col in range(width):
            local = grid[row % motif_height][col % motif_width]
            controller = grid[(row // motif_height) % motif_height][(col // motif_width) % motif_width]
            if local == background:
                result_row.append(background)
            elif controller == background:
                result_row.append(border)
            else:
                result_row.append(local)
        result.append(result_row)
    return result
