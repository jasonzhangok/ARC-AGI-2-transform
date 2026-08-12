def _components(grid, predicate):
    height, width = len(grid), len(grid[0])
    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if predicate(grid[row][col])
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


def _shape(component):
    top = min(row for row, _ in component)
    left = min(col for _, col in component)
    return {(row - top, col - left) for row, col in component}


def transform(grid):
    height, width = len(grid), len(grid[0])
    half = width // 2
    left = [row[:half] for row in grid]
    right = [row[half:] for row in grid]
    sources = []
    for component in _components(right, lambda value: value != 0):
        color = right[component[0][0]][component[0][1]]
        sources.append((color, _shape(component)))

    output = [row[:] for row in left]
    for hole in _components(left, lambda value: value == 0):
        if any(row in (0, height - 1) or col in (0, half - 1)
               for row, col in hole):
            continue
        shape = _shape(hole)
        color = next(color for color, source_shape in sources if source_shape == shape)
        for row, col in hole:
            output[row][col] = color
    return output
