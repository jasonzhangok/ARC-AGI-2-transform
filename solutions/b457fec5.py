def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)

    palette = []
    for row in grid:
        for value in row:
            if value != background and value != 5:
                palette.append(value)

    remaining = {(r, c) for r in range(height) for c in range(width)
                 if grid[r][c] == 5}
    components = []
    while remaining:
        first = remaining.pop()
        component = {first}
        frontier = [first]
        while frontier:
            r, c = frontier.pop()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbor = (r + dr, c + dc)
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    frontier.append(neighbor)
        components.append(component)

    output = [row[:] for row in grid]
    for component in components:
        top = min(r for r, c in component)
        bottom = max(r for r, c in component)
        left = min(c for r, c in component)
        right = max(c for r, c in component)
        top_cells = [c for r, c in component if r == top]
        top_left = min(top_cells)
        from_left = top_left == left
        block_size = len(top_cells)
        last_block = bottom - top - block_size + 1
        for r, c in component:
            depth = r - top
            side_distance = c - left if from_left else right - c
            block = min(depth, side_distance, last_block)
            output[r][c] = palette[block % len(palette)]
    return output
