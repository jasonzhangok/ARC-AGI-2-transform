def transform(grid):
    height = len(grid)
    width = len(grid[0])
    best = None
    for top in range(height):
        empty_columns = [True] * width
        for bottom in range(top, height):
            for column in range(width):
                empty_columns[column] = empty_columns[column] and grid[bottom][column] == 0
            column = 0
            while column < width:
                if not empty_columns[column]:
                    column += 1
                    continue
                left = column
                while column < width and empty_columns[column]:
                    column += 1
                rectangle_width = column - left
                rectangle_height = bottom - top + 1
                if rectangle_height >= rectangle_width:
                    candidate = (rectangle_width * rectangle_height, top, bottom, left, column - 1)
                    if best is None or candidate[0] > best[0]:
                        best = candidate

    raw_top, raw_bottom, raw_left, raw_right = best[1:]
    top = raw_top + (raw_top > 0)
    bottom = raw_bottom - (raw_bottom < height - 1)
    left = raw_left + (raw_left > 0)
    right = raw_right - (raw_right < width - 1)
    output = [row[:] for row in grid]
    for row in range(top, bottom + 1):
        for column in range(left, right + 1):
            output[row][column] = 3

    horizontal_runs = []
    for side_left, side_right in ((0, left - 1), (right + 1, width - 1)):
        if side_left > side_right:
            continue
        blank_rows = []
        for row in range(height):
            blank_rows.append(all(grid[row][column] == 0
                                  for column in range(side_left, side_right + 1)))
        row = 0
        while row < height:
            if not blank_rows[row]:
                row += 1
                continue
            run_top = row
            while row < height and blank_rows[row]:
                row += 1
            run_bottom = row - 1
            if run_bottom - run_top + 1 >= 3:
                horizontal_runs.append((run_top, run_bottom, side_left, side_right))
                core_top = run_top + (run_top > 0)
                core_bottom = run_bottom - (run_bottom < height - 1)
                for fill_row in range(max(core_top, top), min(core_bottom, bottom) + 1):
                    for column in range(side_left, side_right + 1):
                        output[fill_row][column] = 3

    for run_top, run_bottom, side_left, side_right in horizontal_runs:
        for edge_top, edge_bottom, junction in ((0, run_top, run_top),
                                                 (run_bottom, height - 1, run_bottom)):
            column = side_left
            while column <= side_right:
                if not all(grid[row][column] == 0 for row in range(edge_top, edge_bottom + 1)):
                    column += 1
                    continue
                run_left = column
                while (column <= side_right
                       and all(grid[row][column] == 0 for row in range(edge_top, edge_bottom + 1))):
                    column += 1
                run_right = column - 1
                if run_right - run_left + 1 >= 3 and edge_bottom - edge_top + 1 >= 6:
                    core_left = run_left + (run_left > 0)
                    core_right = run_right - (run_right < width - 1)
                    if edge_top == 0:
                        fill_top, fill_bottom = 0, junction
                    else:
                        fill_top, fill_bottom = junction, height - 1
                    for fill_row in range(fill_top, fill_bottom + 1):
                        for fill_column in range(core_left, core_right + 1):
                            output[fill_row][fill_column] = 3
    return output
