from collections import Counter, deque


def _components(grid, background):
    """Return the four-connected non-background components."""
    height, width = len(grid), len(grid[0])
    unseen = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] != background
    }
    components = []

    while unseen:
        start = unseen.pop()
        component = [start]
        stack = [start]
        while stack:
            row, col = stack.pop()
            for neighbor in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    component.append(neighbor)
                    stack.append(neighbor)
        components.append(component)

    return components


def _bounds(cells):
    rows = [row for row, _ in cells]
    cols = [col for _, col in cells]
    return min(rows), max(rows), min(cols), max(cols)


def _colors(grid, component):
    return {grid[row][col] for row, col in component}


def _deepest_color(grid, bounds, base_color):
    """Find the innermost color in the template's nested color bands."""
    top, bottom, left, right = bounds
    adjacency = {}
    for row in range(top, bottom + 1):
        for col in range(left, right + 1):
            color = grid[row][col]
            adjacency.setdefault(color, set())
            for next_row, next_col in ((row + 1, col), (row, col + 1)):
                if next_row > bottom or next_col > right:
                    continue
                other = grid[next_row][next_col]
                if color != other:
                    adjacency[color].add(other)
                    adjacency.setdefault(other, set()).add(color)

    distances = {base_color: 0}
    queue = deque([base_color])
    while queue:
        color = queue.popleft()
        for other in adjacency[color]:
            if other not in distances:
                distances[other] = distances[color] + 1
                queue.append(other)

    return max(distances, key=distances.get)


def _source_index(index, target_size, source_size, before, after):
    """Keep fixed edge bands and map the elastic middle to one source slice."""
    if index < before:
        return index
    if index >= target_size - after:
        return source_size - (target_size - index)
    return before


def transform(grid: list[list[int]]) -> list[list[int]]:
    """Resize a nested rectangular template into its solid-color targets."""
    if not grid:
        return []

    height, width = len(grid), len(grid[0])
    background = Counter(
        value for row in grid for value in row
    ).most_common(1)[0][0]
    components = _components(grid, background)
    component_colors = [
        _colors(grid, component) for component in components
    ]

    template_index = next(
        index for index, colors in enumerate(component_colors)
        if len(colors) > 1
    )
    template = components[template_index]
    template_bounds = _bounds(template)
    top, bottom, left, right = template_bounds

    uniform_colors = [
        next(iter(colors))
        for colors in component_colors
        if len(colors) == 1
    ]
    base_color = Counter(uniform_colors).most_common(1)[0][0]
    inner_color = _deepest_color(grid, template_bounds, base_color)
    inner_cells = [
        (row, col)
        for row, col in template
        if grid[row][col] == inner_color
    ]
    inner_top, inner_bottom, inner_left, inner_right = _bounds(inner_cells)

    source = [row[left:right + 1] for row in grid[top:bottom + 1]]
    source_height = bottom - top + 1
    source_width = right - left + 1
    rows_before = inner_top - top
    rows_after = bottom - inner_bottom
    cols_before = inner_left - left
    cols_after = right - inner_right

    result = [row[:] for row in grid]
    for index, component in enumerate(components):
        if index == template_index or component_colors[index] != {base_color}:
            continue

        target_top, target_bottom, target_left, target_right = _bounds(component)
        target_height = target_bottom - target_top + 1
        target_width = target_right - target_left + 1
        for row in range(target_height):
            source_row = _source_index(
                row, target_height, source_height, rows_before, rows_after
            )
            for col in range(target_width):
                source_col = _source_index(
                    col, target_width, source_width, cols_before, cols_after
                )
                result[target_top + row][target_left + col] = source[source_row][source_col]

    return result
