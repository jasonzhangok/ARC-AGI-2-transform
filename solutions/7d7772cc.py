def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    wall_line = None
    best_frame_area = -1
    for row in range(height):
        uniform = True
        for col in range(1, width):
            if grid[row][col] != grid[row][0]:
                uniform = False
                break
        if uniform:
            wall = grid[row][0]
            for enclosed_above in (True, False):
                if enclosed_above:
                    side_rows = range(0, row + 1)
                    inner_rows = range(1, row)
                else:
                    side_rows = range(row, height)
                    inner_rows = range(row + 1, height - 1)
                framed = True
                for side_row in side_rows:
                    if grid[side_row][0] != wall or grid[side_row][width - 1] != wall:
                        framed = False
                interior = []
                for inner_row in inner_rows:
                    for col in range(1, width - 1):
                        interior.append(grid[inner_row][col])
                if framed and interior:
                    background = interior[0]
                    for value in interior[1:]:
                        if interior.count(value) > interior.count(background):
                            background = value
                    if background != wall and len(interior) > best_frame_area:
                        best_frame_area = len(interior)
                        wall_line = ("row", row, wall)
    for col in range(width):
        uniform = True
        for row in range(1, height):
            if grid[row][col] != grid[0][col]:
                uniform = False
                break
        if uniform:
            wall = grid[0][col]
            for enclosed_left in (True, False):
                if enclosed_left:
                    side_cols = range(0, col + 1)
                    inner_cols = range(1, col)
                else:
                    side_cols = range(col, width)
                    inner_cols = range(col + 1, width - 1)
                framed = True
                for side_col in side_cols:
                    if grid[0][side_col] != wall or grid[height - 1][side_col] != wall:
                        framed = False
                interior = []
                for row in range(1, height - 1):
                    for inner_col in inner_cols:
                        interior.append(grid[row][inner_col])
                if framed and interior:
                    background = interior[0]
                    for value in interior[1:]:
                        if interior.count(value) > interior.count(background):
                            background = value
                    if background != wall and len(interior) > best_frame_area:
                        best_frame_area = len(interior)
                        wall_line = ("column", col, wall)

    orientation, divider, wall = wall_line

    if orientation == "row":
        top_frame = 0
        bottom_frame = 0
        for row in range(divider):
            top_frame += (grid[row][0] == wall) + (grid[row][width - 1] == wall)
        for row in range(divider + 1, height):
            bottom_frame += (grid[row][0] == wall) + (grid[row][width - 1] == wall)
        enclosed_below = bottom_frame > top_frame
        if enclosed_below:
            reference_rows = range(divider + 1, height)
            moving_rows = range(divider)
            near_edge = divider - 1
            far_edge = 0
        else:
            reference_rows = range(divider)
            moving_rows = range(divider + 1, height)
            near_edge = divider + 1
            far_edge = height - 1

        reference_area = []
        moving_area = []
        for row in reference_rows:
            for col in range(width):
                if grid[row][col] != wall:
                    reference_area.append(grid[row][col])
        for row in moving_rows:
            for col in range(width):
                if grid[row][col] != wall:
                    moving_area.append(grid[row][col])
        reference_background = reference_area[0]
        moving_background = moving_area[0]
        for value in reference_area[1:]:
            if reference_area.count(value) > reference_area.count(reference_background):
                reference_background = value
        for value in moving_area[1:]:
            if moving_area.count(value) > moving_area.count(moving_background):
                moving_background = value

        for col in range(width):
            reference = None
            for row in reference_rows:
                if grid[row][col] != wall and grid[row][col] != reference_background:
                    reference = grid[row][col]
            for row in moving_rows:
                value = grid[row][col]
                if value != wall and value != moving_background:
                    output[row][col] = moving_background
                    output[near_edge if value == reference else far_edge][col] = value
    else:
        left_frame = 0
        right_frame = 0
        for col in range(divider):
            left_frame += (grid[0][col] == wall) + (grid[height - 1][col] == wall)
        for col in range(divider + 1, width):
            right_frame += (grid[0][col] == wall) + (grid[height - 1][col] == wall)
        enclosed_left = left_frame > right_frame
        if enclosed_left:
            reference_columns = range(divider)
            moving_columns = range(divider + 1, width)
            near_edge = divider + 1
            far_edge = width - 1
        else:
            reference_columns = range(divider + 1, width)
            moving_columns = range(divider)
            near_edge = divider - 1
            far_edge = 0

        reference_area = []
        moving_area = []
        for row in range(height):
            for col in reference_columns:
                if grid[row][col] != wall:
                    reference_area.append(grid[row][col])
            for col in moving_columns:
                if grid[row][col] != wall:
                    moving_area.append(grid[row][col])
        reference_background = reference_area[0]
        moving_background = moving_area[0]
        for value in reference_area[1:]:
            if reference_area.count(value) > reference_area.count(reference_background):
                reference_background = value
        for value in moving_area[1:]:
            if moving_area.count(value) > moving_area.count(moving_background):
                moving_background = value

        for row in range(height):
            reference = None
            for col in reference_columns:
                if grid[row][col] != wall and grid[row][col] != reference_background:
                    reference = grid[row][col]
            for col in moving_columns:
                value = grid[row][col]
                if value != wall and value != moving_background:
                    output[row][col] = moving_background
                    output[row][near_edge if value == reference else far_edge] = value

    return output
