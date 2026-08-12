def transform(grid):
    height, width = (len(grid), len(grid[0]))
    template_cells = {(r, c) for r in range(height) for c in range(width) if grid[r][c] not in (0, 8)}
    top = min((r for r, _ in template_cells))
    left = min((c for _, c in template_cells))
    template = {(r - top, c - left): grid[r][c] for r, c in template_cells}
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == 8}
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
    result = [[0] * width for _ in range(height)]
    for component in components:
        target_top = min((r for r, _ in component))
        target_left = min((c for _, c in component))
        for (dr, dc), color in template.items():
            result[target_top + dr][target_left + dc] = color
    output = result
    return output
