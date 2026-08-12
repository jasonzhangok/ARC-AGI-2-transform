def transform(grid):
    height = len(grid)
    width = len(grid[0])
    visited = set()
    components = []

    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == 0 or (start_row, start_col) in visited:
                continue
            color = grid[start_row][start_col]
            component = []
            queue = [(start_row, start_col)]
            visited.add((start_row, start_col))
            position = 0
            while position < len(queue):
                row, col = queue[position]
                position += 1
                component.append((row, col))
                for row_step in (-1, 0, 1):
                    for col_step in (-1, 0, 1):
                        neighbor = (row + row_step, col + col_step)
                        if (row_step != 0 or col_step != 0) and 0 <= neighbor[0] < height and 0 <= neighbor[1] < width and neighbor not in visited and grid[neighbor[0]][neighbor[1]] == color:
                            visited.add(neighbor)
                            queue.append(neighbor)
            components.append((color, component))

    output = []
    for color, component in components:
        top = min(row for row, col in component)
        bottom = max(row for row, col in component)
        left = min(col for row, col in component)
        right = max(col for row, col in component)
        component_width = right - left + 1
        normalized = {(row - top, col - left) for row, col in component}
        symmetric = True
        for row, col in normalized:
            if (row, component_width - 1 - col) not in normalized:
                symmetric = False
                break
        if not symmetric:
            output = [[0 for col in range(component_width)] for row in range(bottom - top + 1)]
            for row, col in component:
                output[row - top][col - left] = color
            break
    return output
