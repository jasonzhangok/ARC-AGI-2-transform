def transform(grid):
    height, width = len(grid), len(grid[0])
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != 0}
    components = []
    while remaining:
        start = remaining.pop()
        color = grid[start[0]][start[1]]
        component = {start}
        queue = [start]
        position = 0
        while position < len(queue):
            r, c = queue[position]
            position += 1
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining and grid[point[0]][point[1]] == color:
                    remaining.remove(point)
                    component.add(point)
                    queue.append(point)
        components.append((color, component))

    component_records = []
    for color, component in components:
        top = min(r for r, _ in component)
        left = min(c for _, c in component)
        component_records.append((color, component, frozenset((r - top, c - left) for r, c in component)))

    exemplars = {}
    for color, component, shape in component_records:
        if color != 1:
            exemplars[shape] = color
    result = [row[:] for row in grid]
    for color, component, shape in component_records:
        if color == 1:
            replacement = exemplars[shape]
            for r, c in component:
                result[r][c] = replacement
    output = result
    return output
