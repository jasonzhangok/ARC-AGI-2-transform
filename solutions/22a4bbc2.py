def transform(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    components = []

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 or (row, col) in seen:
                continue
            color = grid[row][col]
            component = []
            queue = [(row, col)]
            seen.add((row, col))
            for current_row, current_col in queue:
                component.append((current_row, current_col))
                for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = current_row + row_step, current_col + col_step
                    if (0 <= neighbor[0] < height and
                            0 <= neighbor[1] < width and
                            neighbor not in seen and
                            grid[neighbor[0]][neighbor[1]] == color):
                        seen.add(neighbor)
                        queue.append(neighbor)
            components.append(component)

    components.sort(key=lambda component: min(component))
    output = [row[:] for row in grid]
    for index, component in enumerate(components):
        if index % 3 == 0:
            for row, col in component:
                output[row][col] = 2
    return output
