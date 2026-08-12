def transform(grid):
    height, width = len(grid), len(grid[0])
    exterior = set()
    queue = []
    for row in range(height):
        for col in range(width):
            if (row in (0, height - 1) or col in (0, width - 1)) and grid[row][col] == 0:
                exterior.add((row, col))
                queue.append((row, col))
    for row, col in queue:
        for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor = row + row_step, col + col_step
            if (0 <= neighbor[0] < height and 0 <= neighbor[1] < width
                    and grid[neighbor[0]][neighbor[1]] == 0
                    and neighbor not in exterior):
                exterior.add(neighbor)
                queue.append(neighbor)

    enclosed = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 0 and (row, col) not in exterior
    }
    output = [row[:] for row in grid]
    while enclosed:
        start = enclosed.pop()
        queue = [start]
        component = []
        for row, col in queue:
            component.append((row, col))
            for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = row + row_step, col + col_step
                if neighbor in enclosed:
                    enclosed.remove(neighbor)
                    queue.append(neighbor)
        top = min(row for row, _ in component)
        bottom = max(row for row, _ in component)
        left = min(col for _, col in component)
        right = max(col for _, col in component)
        side = bottom - top + 1
        if side == right - left + 1 and len(component) == side * side:
            for row, col in component:
                output[row][col] = 2
    return output
