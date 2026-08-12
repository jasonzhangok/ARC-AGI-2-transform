def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    anchors = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 5
    ]
    for anchor_row, anchor_col in anchors:
        directions = []
        for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            row, col = anchor_row + row_step, anchor_col + col_step
            if 0 <= row < height and 0 <= col < width and grid[row][col] == 2:
                directions.append((row_step, col_step))
        if len(directions) != 1:
            continue
        row_step, col_step = directions[0]

        row, col = anchor_row + row_step, anchor_col + col_step
        while (0 <= row + row_step < height and 0 <= col + col_step < width and
               grid[row + row_step][col + col_step] == 2):
            row += row_step
            col += col_step
        tail_end = row, col

        row += row_step
        col += col_step
        while 0 <= row < height and 0 <= col < width and grid[row][col] != 2:
            row += row_step
            col += col_step
        detached = []
        while 0 <= row < height and 0 <= col < width and grid[row][col] == 2:
            detached.append((row, col))
            row += row_step
            col += col_step
        if not detached:
            continue

        perpendiculars = ((-col_step, row_step), (col_step, -row_step))
        turn_row, turn_col = perpendiculars[0]
        center_row = (height - 1) / 2
        center_col = (width - 1) / 2
        best_score = None
        for candidate_row, candidate_col in perpendiculars:
            score = (
                candidate_row * (center_row - anchor_row)
                + candidate_col * (center_col - anchor_col)
            )
            if best_score is None or score > best_score:
                best_score = score
                turn_row, turn_col = candidate_row, candidate_col
        start_row = tail_end[0] + row_step + turn_row
        start_col = tail_end[1] + col_step + turn_col

        for source_row, source_col in detached:
            output[source_row][source_col] = 7
        for index in range(len(detached)):
            output[start_row + index * turn_row][start_col + index * turn_col] = 2

    for anchor_row, anchor_col in anchors:
        black_directions = []
        for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            row = anchor_row + row_step
            col = anchor_col + col_step
            if 0 <= row < height and 0 <= col < width:
                if grid[row][col] == 0:
                    black_directions.append((row_step, col_step))
        if len(black_directions) != 1:
            continue
        row_step, col_step = black_directions[0]
        row = anchor_row + 2 * row_step
        col = anchor_col + 2 * col_step
        detached = []
        while 0 <= row < height and 0 <= col < width and grid[row][col] == 2:
            detached.append((row, col))
            row += row_step
            col += col_step
        if not detached:
            continue
        perpendiculars = ((-col_step, row_step), (col_step, -row_step))
        turn_row, turn_col = perpendiculars[0]
        center_row = (height - 1) / 2
        center_col = (width - 1) / 2
        best_score = None
        for candidate_row, candidate_col in perpendiculars:
            score = (
                candidate_row * (center_row - anchor_row)
                + candidate_col * (center_col - anchor_col)
            )
            if best_score is None or score > best_score:
                best_score = score
                turn_row, turn_col = candidate_row, candidate_col
        for source_row, source_col in detached:
            output[source_row][source_col] = 7
        black_row = anchor_row + row_step
        black_col = anchor_col + col_step
        for index in range(len(detached)):
            output[black_row + (index + 1) * turn_row][
                black_col + (index + 1) * turn_col
            ] = 2
    return output
