def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)

    groups = []
    for color in counts:
        if color == background:
            continue
        unseen = set()
        for row in range(height):
            for col in range(width):
                if grid[row][col] == color:
                    unseen.add((row, col))
        components = []
        while unseen:
            start = unseen.pop()
            component = {start}
            frontier = [start]
            while frontier:
                row, col = frontier.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = (row + dr, col + dc)
                    if neighbor in unseen:
                        unseen.remove(neighbor)
                        component.add(neighbor)
                        frontier.append(neighbor)
            components.append(component)
        groups.append((color, components))

    template_color, template_components = groups[0]
    candidate_color, candidate_components = groups[0]
    for group_color, group_components in groups[1:]:
        if len(group_components) < len(template_components):
            template_color = group_color
            template_components = group_components
        if len(group_components) > len(candidate_components):
            candidate_color = group_color
            candidate_components = group_components
    template = template_components[0]
    top = min(row for row, col in template)
    bottom = max(row for row, col in template)
    left = min(col for row, col in template)
    right = max(col for row, col in template)
    template_sides = [
        all((top, col) in template for col in range(left, right + 1)),
        all((row, right) in template for row in range(top, bottom + 1)),
        all((bottom, col) in template for col in range(left, right + 1)),
        all((row, left) in template for row in range(top, bottom + 1)),
    ]
    open_side = template_sides.index(False)

    selected_bounds = None
    for component in candidate_components:
        top = min(row for row, col in component)
        bottom = max(row for row, col in component)
        left = min(col for row, col in component)
        right = max(col for row, col in component)
        sides = [
            all((top, col) in component for col in range(left, right + 1)),
            all((row, right) in component for row in range(top, bottom + 1)),
            all((bottom, col) in component for col in range(left, right + 1)),
            all((row, left) in component for row in range(top, bottom + 1)),
        ]
        if sum(sides) == 3 and not sides[open_side]:
            selected_bounds = (top, bottom, left, right)

    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if output[row][col] == candidate_color:
                output[row][col] = background

    top, bottom, left, right = selected_bounds
    if open_side == 0:
        top -= 1
    elif open_side == 1:
        right += 1
    elif open_side == 2:
        bottom += 1
    else:
        left -= 1
    for row in range(max(0, top), min(height, bottom + 1)):
        for col in range(max(0, left), min(width, right + 1)):
            output[row][col] = candidate_color

    return output
