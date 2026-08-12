def transform(grid):
    height = len(grid)
    width = len(grid[0])
    background = 7
    bottom_colors = {grid[height - 1][col] for col in range(width) if grid[height - 1][col] != background}
    fixed_color = max(((sum((value == _item_1 for row in grid for value in row)), _index_1, _item_1) for _index_1, _item_1 in enumerate(bottom_colors)))[2]
    fixed = {(row, col) for row in range(height) for col in range(width) if grid[row][col] == fixed_color}
    movable = {(row, col) for row in range(height) for col in range(width) if grid[row][col] not in (background, fixed_color)}
    _cells = movable
    remaining = set(_cells)
    result = []
    while remaining:
        start = remaining.pop()
        stack = [start]
        component = {start}
        while stack:
            row, col = stack.pop()
            for neighbor in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    stack.append(neighbor)
        result.append(component)
    _components_result_1 = result
    components = _components_result_1
    components = [_record_2[2] for _record_2 in sorted(((max((row for row, _ in _item_2)), -_index_2, _item_2) for _index_2, _item_2 in enumerate(components)), reverse=True)]
    settled = set()
    placements = []
    for component in components:
        distance = 0
        while True:
            shifted = {(row + distance + 1, col) for row, col in component}
            if any((row >= height - 1 for row, _ in shifted)):
                break
            if shifted & fixed or shifted & settled:
                break
            if any(((row + 1, col) in fixed for row, col in shifted)):
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
