from collections import Counter


def _components(cells):
    remaining = set(cells)
    result = []
    while remaining:
        start = remaining.pop()
        stack = [start]
        component = {start}
        while stack:
            row, col = stack.pop()
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    neighbor = (row + dr, col + dc)
                    if neighbor in remaining:
                        remaining.remove(neighbor)
                        component.add(neighbor)
                        stack.append(neighbor)
        result.append(component)
    return result


def _visible_ring(height, width, center_row, center_col, radius):
    return {
        (row, col)
        for row in range(height)
        for col in range(width)
        if abs(row - center_row) + abs(col - center_col) == radius
    }


def _smallest_ring(component, height, width):
    sample_row, sample_col = next(iter(component))
    candidates = []
    for center_row in range(-height, 2 * height):
        for center_col in range(-width, 2 * width):
            radius = abs(sample_row - center_row) + abs(sample_col - center_col)
            if _visible_ring(height, width, center_row, center_col, radius) == component:
                candidates.append((radius, center_row, center_col))
    if not candidates:
        return None
    radius, center_row, center_col = min(candidates)
    return center_row, center_col, radius


def transform(grid):
    height = len(grid)
    width = len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    output = [row[:] for row in grid]

    for color, radius_change in ((2, -1), (5, 1)):
        cells = {
            (row, col)
            for row in range(height)
            for col in range(width)
            if grid[row][col] == color
        }
        for row, col in cells:
            output[row][col] = background

        for component in _components(cells):
            ring = _smallest_ring(component, height, width)
            if ring is None:
                for row, col in component:
                    output[row][col] = color
                continue

            center_row, center_col, radius = ring
            new_radius = radius + radius_change
            if new_radius < 0:
                continue

            # When an expanding ring is centered on the bottom boundary, its
            # next visible phase advances one cell along that boundary.
            if color == 5 and center_row == height - 1:
                center_col += 1

            for row, col in _visible_ring(
                height, width, center_row, center_col, new_radius
            ):
                output[row][col] = color

    return output
