def transform(grid):
    height = len(grid)
    width = len(grid[0])
    remaining = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 8:
                remaining.add((row, col))
    components = []
    while remaining:
        start = remaining.pop()
        component = {start}
        stack = [start]
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
        components.append(component)

    ordered_components = []
    remaining_indices = set(range(len(components)))
    while remaining_indices:
        selected_index = None
        selected_size = -1
        for index in remaining_indices:
            if len(components[index]) > selected_size:
                selected_index = index
                selected_size = len(components[index])
        ordered_components.append(components[selected_index])
        remaining_indices.remove(selected_index)

    large_components = []
    for component in ordered_components:
        selected_cluster = None
        selected_span = None
        component_top = min(row for row, col in component)
        component_bottom = max(row for row, col in component)
        for index in range(len(large_components)):
            cluster_top = min(row for row, col in large_components[index])
            cluster_bottom = max(row for row, col in large_components[index])
            combined_top = min(component_top, cluster_top)
            combined_bottom = max(component_bottom, cluster_bottom)
            combined_span = combined_bottom - combined_top + 1
            if combined_span <= 4:
                if selected_span is None or combined_span < selected_span:
                    selected_cluster = index
                    selected_span = combined_span
        if selected_cluster is None:
            large_components.append(set(component))
        else:
            large_components[selected_cluster].update(component)

    output = [row[:] for row in grid]
    for component in large_components:
        top = min(row for row, col in component)
        bottom = max(row for row, col in component)
        left = min(col for row, col in component)
        right = max(col for row, col in component)
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                if output[row][col] == 0:
                    output[row][col] = 2
    return output
