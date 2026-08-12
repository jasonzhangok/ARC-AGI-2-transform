def transform(grid):
    height, width = len(grid), len(grid[0])
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != 0}
    components = []
    while remaining:
        start = remaining.pop()
        component = {start}
        stack = [start]
        while stack:
            r, c = stack.pop()
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    neighbor = (r + dr, c + dc)
                    if neighbor in remaining:
                        remaining.remove(neighbor)
                        component.add(neighbor)
                        stack.append(neighbor)
        components.append(component)

    singletons = {}
    for component in components:
        if len(component) == 1:
            point = next(iter(component))
            singletons.setdefault(grid[point[0]][point[1]], []).append(point)

    result = [row[:] for row in grid]
    for component in components:
        if len(component) <= 1:
            continue
        colors = {grid[r][c] for r, c in component}
        if len(colors) < 2:
            continue
        marker_points = [
            (r, c)
            for r, c in component
            if grid[r][c] in singletons
        ]
        for marker_row, marker_column in marker_points:
            marker_color = grid[marker_row][marker_column]
            for target_row, target_column in singletons[marker_color]:
                for r, c in component:
                    nr = target_row + r - marker_row
                    horizontal_sign = -1 if marker_color == 2 else 1
                    nc = target_column + horizontal_sign * (c - marker_column)
                    if 0 <= nr < height and 0 <= nc < width:
                        result[nr][nc] = grid[r][c]
    output = result
    return output
