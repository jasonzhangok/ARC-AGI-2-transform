def transform(grid):
    height = len(grid)
    width = len(grid[0])
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    seen = set()
    components = []

    for start_row in range(height):
        for start_col in range(width):
            color = grid[start_row][start_col]
            if color in (7, 9) or (start_row, start_col) in seen:
                continue

            stack = [(start_row, start_col)]
            seen.add((start_row, start_col))
            cells = []
            while stack:
                row, col = stack.pop()
                cells.append((row, col))
                for row_step, col_step in directions:
                    next_row = row + row_step
                    next_col = col + col_step
                    point = (next_row, next_col)
                    if not (0 <= next_row < height and 0 <= next_col < width):
                        continue
                    if point in seen or grid[next_row][next_col] != color:
                        continue
                    seen.add(point)
                    stack.append(point)
            components.append((color, cells))

    moves = []
    for color, cells in components:
        away_directions = set()
        for row, col in cells:
            for row_step, col_step in directions:
                marker_row = row - row_step
                marker_col = col - col_step
                if (
                    0 <= marker_row < height
                    and 0 <= marker_col < width
                    and grid[marker_row][marker_col] == 9
                ):
                    away_directions.add((row_step, col_step))

        if len(away_directions) != 1:
            continue
        row_step, col_step = next(iter(away_directions))
        if row_step == -1:
            distance = min(row for row, _ in cells)
        elif row_step == 1:
            distance = min(height - 1 - row for row, _ in cells)
        elif col_step == -1:
            distance = min(col for _, col in cells)
        else:
            distance = min(width - 1 - col for _, col in cells)
        moves.append((color, cells, row_step, col_step, distance))

    output = [row[:] for row in grid]
    for _, cells, _, _, _ in moves:
        for row, col in cells:
            output[row][col] = 7
    for color, cells, row_step, col_step, distance in moves:
        for row, col in cells:
            output[row + distance * row_step][col + distance * col_step] = color

    return output
