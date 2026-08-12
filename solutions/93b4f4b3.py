def transform(grid):
    height, width = len(grid), len(grid[0])
    half = width // 2
    left = [row[:half] for row in grid]
    right = [row[half:] for row in grid]
    component_sets = []
    for panel, want_zero in ((right, False), (left, True)):
        panel_width = len(panel[0])
        remaining = {(row, col) for row in range(height) for col in range(panel_width)
                     if (panel[row][col] == 0) == want_zero}
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
        component_sets.append(result)
    source_components, holes = component_sets
    sources = []
    for component in source_components:
        color = right[component[0][0]][component[0][1]]
        top = min(row for row, _ in component)
        component_left = min(col for _, col in component)
        sources.append((color, {(row - top, col - component_left) for row, col in component}))

    output = [row[:] for row in left]
    for hole in holes:
        if any(row in (0, height - 1) or col in (0, half - 1)
               for row, col in hole):
            continue
        top = min(row for row, _ in hole)
        hole_left = min(col for _, col in hole)
        shape = {(row - top, col - hole_left) for row, col in hole}
        color = next(color for color, source_shape in sources if source_shape == shape)
        for row, col in hole:
            output[row][col] = color
    return output
