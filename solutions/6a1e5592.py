def transform(grid):
    height, width = len(grid), len(grid[0])
    components = []
    seen = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 or (row, col) in seen:
                continue
            color = grid[row][col]
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbor = (current_row + row_step, current_col + col_step)
                    if (
                        0 <= neighbor[0] < height
                        and 0 <= neighbor[1] < width
                        and grid[neighbor[0]][neighbor[1]] == color
                        and neighbor not in seen
                    ):
                        seen.add(neighbor)
                        stack.append(neighbor)
            components.append(cells)

    panel_cells = components[0]
    for cells in components[1:]:
        cells_top = min(row for row, _ in cells)
        panel_top = min(row for row, _ in panel_cells)
        if cells_top < panel_top or (
            cells_top == panel_top and len(cells) > len(panel_cells)
        ):
            panel_cells = cells
    panel_color = grid[panel_cells[0][0]][panel_cells[0][1]]
    panel_top = min(row for row, _ in panel_cells)
    panel_bottom = max(row for row, _ in panel_cells)
    panel_left = min(col for _, col in panel_cells)
    panel_right = max(col for _, col in panel_cells)

    output = [[0] * width for _ in range(height)]
    for row, col in panel_cells:
        output[row][col] = panel_color

    holes = []
    seen = set()
    for row in range(panel_top, panel_bottom + 1):
        for col in range(panel_left, panel_right + 1):
            if grid[row][col] != 0 or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbor = (current_row + row_step, current_col + col_step)
                    if (
                        panel_top <= neighbor[0] <= panel_bottom
                        and panel_left <= neighbor[1] <= panel_right
                        and grid[neighbor[0]][neighbor[1]] == 0
                        and neighbor not in seen
                    ):
                        seen.add(neighbor)
                        stack.append(neighbor)
            holes.append(cells)

    pieces = []
    seen = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] in (0, panel_color) or (row, col) in seen:
                continue
            piece_color = grid[row][col]
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbor = (current_row + row_step, current_col + col_step)
                    if (
                        0 <= neighbor[0] < height
                        and 0 <= neighbor[1] < width
                        and grid[neighbor[0]][neighbor[1]] == piece_color
                        and neighbor not in seen
                    ):
                        seen.add(neighbor)
                        stack.append(neighbor)
            pieces.append(cells)

    used = set()
    for hole in holes:
        hole_top = min(row for row, _ in hole)
        hole_left = min(col for _, col in hole)
        hole_shape = {(row - hole_top, col - hole_left) for row, col in hole}
        for index, piece in enumerate(pieces):
            if index in used:
                continue
            piece_top = min(row for row, _ in piece)
            piece_left = min(col for _, col in piece)
            visible = [
                (row - piece_top, col - piece_left)
                for row, col in piece
                if row - piece_top <= panel_bottom - hole_top
            ]
            if not visible:
                continue
            visible_left = min(col for _, col in visible)
            visible_shape = {(row, col - visible_left) for row, col in visible}
            if visible_shape != hole_shape:
                continue
            for row, col in piece:
                target_row = hole_top + row - piece_top
                target_col = hole_left + col - piece_left - visible_left
                if 0 <= target_row < height and 0 <= target_col < width:
                    output[target_row][target_col] = 1
            used.add(index)
            break

    return output
