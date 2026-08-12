def _components(cells):
    remaining = set(cells)
    result = []
    while remaining:
        start = remaining.pop()
        stack = [start]
        component = {start}
        while stack:
            row, col = stack.pop()
            for neighbor in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    stack.append(neighbor)
        result.append(component)
    return result


def transform(grid):
    height = len(grid)
    width = len(grid[0])
    background = 7

    bottom_colors = {
        grid[height - 1][col]
        for col in range(width)
        if grid[height - 1][col] != background
    }
    fixed_color = max(
        bottom_colors,
        key=lambda color: sum(value == color for row in grid for value in row),
    )
    fixed = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == fixed_color
    }
    movable = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] not in (background, fixed_color)
    }

    components = _components(movable)
    components.sort(key=lambda component: max(row for row, _ in component), reverse=True)

    settled = set()
    placements = []
    for component in components:
        distance = 0
        while True:
            shifted = {(row + distance + 1, col) for row, col in component}
            if any(row >= height - 1 for row, _ in shifted):
                break
            if shifted & fixed or shifted & settled:
                break
            if any((row + 1, col) in fixed for row, col in shifted):
                break
            distance += 1

        placed = {(row + distance, col) for row, col in component}
        settled.update(placed)
        placements.append((component, distance))

    output = [row[:] for row in grid]
    for component in components:
        for row, col in component:
            output[row][col] = background
    for component, distance in placements:
        for row, col in component:
            output[row + distance][col] = grid[row][col]

    return output
