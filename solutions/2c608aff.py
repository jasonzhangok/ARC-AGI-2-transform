def transform(grid):
    height, width = (len(grid), len(grid[0]))
    background = {}
    for cell_value in (value for row in grid for value in row):
        background[cell_value] = background.get(cell_value, 0) + 1
    background = max(background, key=background.get)
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != background}
    components = []
    while remaining:
        start = remaining.pop()
        color = grid[start[0]][start[1]]
        component = {start}
        queue = list([start])
        while queue:
            r, c = queue.pop(0)
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining and grid[point[0]][point[1]] == color:
                    remaining.remove(point)
                    component.add(point)
                    queue.append(point)
        components.append((color, component))
    rectangle_color, rectangle = max(((len(_item_1[1]), _index_1, _item_1) for _index_1, _item_1 in enumerate(components)))[2]
    top = min((r for r, _ in rectangle))
    bottom = max((r for r, _ in rectangle))
    left = min((c for _, c in rectangle))
    right = max((c for _, c in rectangle))
    result = [row[:] for row in grid]
    for color, component in components:
        if component == rectangle:
            continue
        for r, c in component:
            if top <= r <= bottom:
                edge = left - 1 if c < left else right + 1
                for cc in range(min(c, edge), max(c, edge) + 1):
                    result[r][cc] = color
            elif left <= c <= right:
                edge = top - 1 if r < top else bottom + 1
                for rr in range(min(r, edge), max(r, edge) + 1):
                    result[rr][c] = color
    output = result
    return output
