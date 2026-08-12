def _components(grid, color):
    height, width = len(grid), len(grid[0])
    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == color
    }
    result = []
    while remaining:
        start = remaining.pop()
        queue = [start]
        component = []
        for row, col in queue:
            component.append((row, col))
            for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = row + row_step, col + col_step
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    queue.append(neighbor)
        result.append(component)
    return result


def _normalized(component):
    top = min(row for row, _ in component)
    left = min(col for _, col in component)
    return {(row - top, col - left) for row, col in component}


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
            if (0 <= neighbor[0] < height and 0 <= neighbor[1] < width and
                    grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in exterior):
                exterior.add(neighbor)
                queue.append(neighbor)

    holes = []
    enclosed = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 0 and (row, col) not in exterior
    }
    while enclosed:
        start = enclosed.pop()
        queue = [start]
        hole = []
        for row, col in queue:
            hole.append((row, col))
            for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = row + row_step, col + col_step
                if neighbor in enclosed:
                    enclosed.remove(neighbor)
                    queue.append(neighbor)
        holes.append(hole)

    sources = []
    for color in set(value for row in grid for value in row) - {0, 5}:
        for component in _components(grid, color):
            sources.append((color, component, _normalized(component)))

    output = [row[:] for row in grid]
    used = set()
    for hole in holes:
        shape = _normalized(hole)
        match = next(
            (index for index, source in enumerate(sources)
             if index not in used and source[2] == shape),
            None,
        )
        if match is None:
            continue
        used.add(match)
        color, component, _ = sources[match]
        for row, col in component:
            output[row][col] = 0
        for row, col in hole:
            output[row][col] = color
    return output
