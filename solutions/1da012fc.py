from itertools import permutations


def _components(grid, color):
    height, width = len(grid), len(grid[0])
    seen = set()
    result = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != color or (row, col) in seen:
                continue
            component = []
            stack = [(row, col)]
            seen.add((row, col))
            while stack:
                current_row, current_col = stack.pop()
                component.append((current_row, current_col))
                for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = current_row + row_step
                    next_col = current_col + col_step
                    next_cell = (next_row, next_col)
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and next_cell not in seen
                        and grid[next_row][next_col] == color
                    ):
                        seen.add(next_cell)
                        stack.append(next_cell)
            result.append(component)
    return result


def _normalized(points):
    rows = [row for row, _ in points]
    cols = [col for _, col in points]
    top, bottom = min(rows), max(rows)
    left, right = min(cols), max(cols)
    return [
        (
            (row - top) / (bottom - top) if bottom > top else 0,
            (col - left) / (right - left) if right > left else 0,
        )
        for row, col in points
    ]


def transform(grid):
    height, width = len(grid), len(grid[0])
    non_frame_colors = {
        value for row in grid for value in row if value not in (0, 5)
    }
    counts = {
        color: sum(row.count(color) for row in grid)
        for color in non_frame_colors
    }
    object_color = max(counts, key=counts.get)
    objects = _components(grid, object_color)
    centers = [
        (
            sum(row for row, _ in component) / len(component),
            sum(col for _, col in component) / len(component),
        )
        for component in objects
    ]
    markers = [
        (row, col, grid[row][col])
        for row in range(height)
        for col in range(width)
        if grid[row][col] not in (0, 5, object_color)
    ]

    normalized_centers = _normalized(centers)
    normalized_markers = _normalized([(row, col) for row, col, _ in markers])
    best_cost = None
    best_assignment = None
    for assignment in permutations(range(len(markers))):
        cost = sum(
            (normalized_centers[index][0] - normalized_markers[marker][0]) ** 2
            + (normalized_centers[index][1] - normalized_markers[marker][1]) ** 2
            for index, marker in enumerate(assignment)
        )
        if best_cost is None or cost < best_cost:
            best_cost = cost
            best_assignment = assignment

    output = [row[:] for row in grid]
    for index, marker_index in enumerate(best_assignment):
        new_color = markers[marker_index][2]
        for row, col in objects[index]:
            output[row][col] = new_color
    return output
