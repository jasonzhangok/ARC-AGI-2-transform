def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    blue = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                blue.append((row, col))
    top = min(row for row, col in blue)
    bottom = max(row for row, col in blue)

    runs = []
    for col in range(width):
        if grid[bottom][col] == 1:
            if not runs or col != runs[-1][-1] + 1:
                runs.append([col])
            else:
                runs[-1].append(col)

    slots = []
    for run in runs:
        left = run[0]
        right = run[-1]
        connected_to_top = any(grid[top][col] == 1 for col in run)
        enclosed_by_top = (left > 0 and right + 1 < width
                           and grid[top][left - 1] == 1
                           and grid[top][right + 1] == 1)
        if connected_to_top or enclosed_by_top:
            slots.append((left, right))

    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 5 or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbor_row = current_row + row_step
                    neighbor_col = current_col + col_step
                    neighbor = (neighbor_row, neighbor_col)
                    if (0 <= neighbor_row < height and 0 <= neighbor_col < width
                            and grid[neighbor_row][neighbor_col] == 5
                            and neighbor not in seen):
                        seen.add(neighbor)
                        stack.append(neighbor)
            components.append((min(col for row, col in cells), cells))
    components.sort()

    used = set()
    for left, right in slots:
        chosen = None
        for index, component in enumerate(components):
            if index in used:
                continue
            cells = component[1]
            component_left = min(col for row, col in cells)
            component_right = max(col for row, col in cells)
            if component_left <= right and component_right >= left:
                chosen = index
                break
        if chosen is not None:
            used.add(chosen)
            for row, col in components[chosen][1]:
                output[row][col] = 2
    return output
