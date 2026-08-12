def transform(grid):
    height, width = (len(grid), len(grid[0]))
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != 8}
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
    colored_counts = [sum((grid[r][c] != 0 for r, c in component)) for component in components]
    target = components[colored_counts.index(min(colored_counts))]
    source = components[colored_counts.index(max(colored_counts))]
    target_colors = {grid[r][c] for r, c in target if grid[r][c] != 0}
    source_colors = {grid[r][c] for r, c in source if grid[r][c] != 0}
    marker = next(iter(target_colors & source_colors))
    target_marker = next(((r, c) for r, c in target if grid[r][c] == marker))
    source_marker = next(((r, c) for r, c in source if grid[r][c] == marker))
    top = min((r for r, _ in target))
    bottom = max((r for r, _ in target))
    left = min((c for _, c in target))
    right = max((c for _, c in target))
    result = [[0] * (right - left + 1) for _ in range(bottom - top + 1)]
    for r, c in source:
        if grid[r][c] != 0:
            rr = r - source_marker[0] + target_marker[0] - top
            cc = c - source_marker[1] + target_marker[1] - left
            if 0 <= rr < len(result) and 0 <= cc < len(result[0]):
                result[rr][cc] = grid[r][c]
    output = result
    return output
