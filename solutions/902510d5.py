def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    components = []

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 or (row, col) in seen:
                continue
            color = grid[row][col]
            pending = [(row, col)]
            seen.add((row, col))
            component = []
            while pending:
                current_row, current_col = pending.pop()
                component.append((current_row, current_col))
                for delta_row, delta_col in (
                    (-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),
                    (1, -1), (1, 0), (1, 1),
                ):
                    next_row = current_row + delta_row
                    next_col = current_col + delta_col
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and (next_row, next_col) not in seen
                        and grid[next_row][next_col] == color
                    ):
                        seen.add((next_row, next_col))
                        pending.append((next_row, next_col))
            components.append(component)

    main = max(components, key=len)
    main_cells = set(main)
    corners = (
        (0, 0),
        (0, width - 1),
        (height - 1, 0),
        (height - 1, width - 1),
    )
    anchor = None
    for corner in corners:
        if grid[corner[0]][corner[1]] != 0 and corner not in main_cells:
            anchor = corner
            break

    hints = []
    counts = {}
    for row in range(height):
        for col in range(width):
            if (
                grid[row][col] != 0
                and (row, col) not in main_cells
                and (row, col) != anchor
            ):
                hints.append((row, col))
                color = grid[row][col]
                counts[color] = counts.get(color, 0) + 1

    fill_color = max(counts, key=counts.get)
    side = len(hints)
    output = [[0] * width for _ in range(height)]

    for row in range(height):
        for col in range(width):
            if anchor[0] == 0:
                vertical_distance = row
            else:
                vertical_distance = height - 1 - row
            if anchor[1] == 0:
                horizontal_distance = col
            else:
                horizontal_distance = width - 1 - col
            if vertical_distance + horizontal_distance < side:
                output[row][col] = fill_color

    for row, col in main:
        output[row][col] = grid[row][col]

    return output
