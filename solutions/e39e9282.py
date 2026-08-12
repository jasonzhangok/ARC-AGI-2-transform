def transform(grid):
    height = len(grid)
    width = len(grid[0])
    result = [row[:] for row in grid]

    visited = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 5 or (row, col) in visited:
                continue
            component = []
            stack = [(row, col)]
            visited.add((row, col))
            touches_marker = False
            while stack:
                current_row, current_col = stack.pop()
                component.append((current_row, current_col))
                for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor_row = current_row + delta_row
                    neighbor_col = current_col + delta_col
                    if not (0 <= neighbor_row < height and 0 <= neighbor_col < width):
                        continue
                    if grid[neighbor_row][neighbor_col] == 9:
                        touches_marker = True
                    elif (grid[neighbor_row][neighbor_col] == 5
                          and (neighbor_row, neighbor_col) not in visited):
                        visited.add((neighbor_row, neighbor_col))
                        stack.append((neighbor_row, neighbor_col))
            if touches_marker:
                for component_row, component_col in component:
                    result[component_row][component_col] = 8

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 9:
                continue
            for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor_row = row + delta_row
                neighbor_col = col + delta_col
                if not (0 <= neighbor_row < height and 0 <= neighbor_col < width):
                    continue
                neighbor = grid[neighbor_row][neighbor_col]
                if neighbor == 5:
                    result[neighbor_row][neighbor_col] = 9
                elif neighbor == 6:
                    result[row][col] = 8
                    target_row = row + 2 * delta_row
                    target_col = col + 2 * delta_col
                    if 0 <= target_row < height and 0 <= target_col < width:
                        result[target_row][target_col] = 9
    return result
