def transform(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    components = []
    for row in range(height):
        for column in range(width):
            if grid[row][column] == 0 or (row, column) in seen:
                continue
            stack = [(row, column)]
            seen.add((row, column))
            cells = []
            while stack:
                current_row, current_column = stack.pop()
                cells.append((current_row, current_column))
                for row_step, column_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbor = (current_row + row_step, current_column + column_step)
                    if (
                        0 <= neighbor[0] < height
                        and 0 <= neighbor[1] < width
                        and grid[neighbor[0]][neighbor[1]] != 0
                        and neighbor not in seen
                    ):
                        seen.add(neighbor)
                        stack.append(neighbor)
            components.append(cells)

    panel = max(components, key=len)
    panel_cells = set(panel)
    top = min(row for row, _ in panel)
    bottom = max(row for row, _ in panel)
    left = min(column for _, column in panel)
    right = max(column for _, column in panel)
    panel_height = bottom - top + 1
    panel_width = right - left + 1

    outside = [
        (grid[row][column], row, column)
        for row in range(height)
        for column in range(width)
        if grid[row][column] != 0 and (row, column) not in panel_cells
    ]
    anchor_colors = {color for color, _, _ in outside}
    inside = [
        (grid[row][column], row - top, column - left)
        for row, column in panel
        if grid[row][column] in anchor_colors
    ]

    outside_top = min(row for _, row, _ in outside)
    outside_bottom = max(row for _, row, _ in outside)
    outside_left = min(column for _, _, column in outside)
    outside_right = max(column for _, _, column in outside)
    target_arrangement = {
        color: (
            row == outside_top,
            row == outside_bottom,
            column == outside_left,
            column == outside_right,
        )
        for color, row, column in outside
    }

    chosen = 0
    for mode in range(8):
        transformed_anchors = []
        for color, row, column in inside:
            if mode == 0:
                new_row, new_column = row, column
            elif mode == 1:
                new_row, new_column = column, panel_height - 1 - row
            elif mode == 2:
                new_row = panel_height - 1 - row
                new_column = panel_width - 1 - column
            elif mode == 3:
                new_row, new_column = panel_width - 1 - column, row
            elif mode == 4:
                new_row, new_column = panel_height - 1 - row, column
            elif mode == 5:
                new_row, new_column = row, panel_width - 1 - column
            elif mode == 6:
                new_row, new_column = column, row
            else:
                new_row = panel_width - 1 - column
                new_column = panel_height - 1 - row
            transformed_anchors.append((color, new_row, new_column))

        anchor_top = min(row for _, row, _ in transformed_anchors)
        anchor_bottom = max(row for _, row, _ in transformed_anchors)
        anchor_left = min(column for _, _, column in transformed_anchors)
        anchor_right = max(column for _, _, column in transformed_anchors)
        arrangement = {
            color: (
                row == anchor_top,
                row == anchor_bottom,
                column == anchor_left,
                column == anchor_right,
            )
            for color, row, column in transformed_anchors
        }
        if arrangement == target_arrangement:
            chosen = mode
            break

    if chosen in (1, 3, 6, 7):
        output = [[0] * panel_height for _ in range(panel_width)]
    else:
        output = [[0] * panel_width for _ in range(panel_height)]

    for row in range(panel_height):
        for column in range(panel_width):
            if chosen == 0:
                new_row, new_column = row, column
            elif chosen == 1:
                new_row, new_column = column, panel_height - 1 - row
            elif chosen == 2:
                new_row = panel_height - 1 - row
                new_column = panel_width - 1 - column
            elif chosen == 3:
                new_row, new_column = panel_width - 1 - column, row
            elif chosen == 4:
                new_row, new_column = panel_height - 1 - row, column
            elif chosen == 5:
                new_row, new_column = row, panel_width - 1 - column
            elif chosen == 6:
                new_row, new_column = column, row
            else:
                new_row = panel_width - 1 - column
                new_column = panel_height - 1 - row
            output[new_row][new_column] = grid[top + row][left + column]

    return output
