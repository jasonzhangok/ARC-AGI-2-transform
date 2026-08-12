def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    components = []

    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == 0 or (start_row, start_col) in seen:
                continue
            component = []
            queue = [(start_row, start_col)]
            seen.add((start_row, start_col))
            for row, col in queue:
                component.append((row, col))
                for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = (row + delta_row, col + delta_col)
                    if (
                        0 <= neighbor[0] < height
                        and 0 <= neighbor[1] < width
                        and grid[neighbor[0]][neighbor[1]] != 0
                        and neighbor not in seen
                    ):
                        seen.add(neighbor)
                        queue.append(neighbor)
            components.append(component)

    isolated = {}
    for component in components:
        if len(component) == 1:
            row, col = component[0]
            color = grid[row][col]
            isolated.setdefault(color, []).append((row, col))

    moves = []
    for component in components:
        if len(component) == 1:
            continue
        color_counts = {}
        for row, col in component:
            color = grid[row][col]
            color_counts[color] = color_counts.get(color, 0) + 1
        if len(color_counts) != 2:
            continue
        main_color = max(color_counts, key=color_counts.get)
        marker_colors = [color for color in color_counts if color != main_color]
        marker_color = marker_colors[0]
        if color_counts[marker_color] != 1 or marker_color not in isolated:
            continue

        main_cells = {
            (row, col)
            for row, col in component
            if grid[row][col] == main_color
        }
        elbow = None
        for row, col in main_cells:
            horizontal = (row, col - 1) in main_cells or (row, col + 1) in main_cells
            vertical = (row - 1, col) in main_cells or (row + 1, col) in main_cells
            if horizontal and vertical:
                elbow = (row, col)
                break
        if elbow is None:
            continue

        target_row, target_col = isolated[marker_color][0]
        moves.append((component, target_row - elbow[0], target_col - elbow[1]))

    output = [row[:] for row in grid]
    for component, delta_row, delta_col in moves:
        for row, col in component:
            output[row][col] = 0
    for component, delta_row, delta_col in moves:
        for row, col in component:
            output[row + delta_row][col + delta_col] = grid[row][col]
    return output
