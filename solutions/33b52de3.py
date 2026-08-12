def transform(grid):
    height, width = (len(grid), len(grid[0]))
    code_cells = {(r, c) for r in range(height) for c in range(width) if grid[r][c] not in (0, 5)}
    code_top = min((r for r, _ in code_cells))
    code_bottom = max((r for r, _ in code_cells))
    code_left = min((c for _, c in code_cells))
    code_right = max((c for _, c in code_cells))
    code = [row[code_left:code_right + 1] for row in grid[code_top:code_bottom + 1]]
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == 5}
    components = []
    while remaining:
        start = remaining.pop()
        component = {start}
        queue = list([start])
        while queue:
            r, c = queue.pop(0)
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining:
                    remaining.remove(point)
                    component.add(point)
                    queue.append(point)
        components.append(component)
    components = [_record_1[2] for _record_1 in sorted((((min((r for r, _ in _item_1)), min((c for _, c in _item_1))), _index_1, _item_1) for _index_1, _item_1 in enumerate(components)))]
    result = [row[:] for row in grid]
    for component, color in zip(components, (value for row in code for value in row)):
        for r, c in component:
            result[r][c] = color
    output = result
    return output
