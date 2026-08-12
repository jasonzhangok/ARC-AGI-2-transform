from collections import Counter


def _components(grid, color):
    height, width = len(grid), len(grid[0])
    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == color
    }
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
    return result


def _normalized(component):
    top = min(row for row, _ in component)
    left = min(col for _, col in component)
    return {(row - top, col - left) for row, col in component}


def transform(grid):
    height, width = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = counts.most_common(1)[0][0]
    colors = [color for color in counts if color != background]
    cross = {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}

    marker_color = None
    marker = None
    for color in colors:
        for component in _components(grid, color):
            if _normalized(component) == cross:
                marker_color = color
                marker = component
                break
        if marker is not None:
            break

    output = [row[:] for row in grid]
    touches_top = any(row == 0 for row, _ in marker)
    if not touches_top:
        for row, col in marker:
            output[row][col] = background

    for color in colors:
        if color == marker_color:
            continue
        for component in _components(grid, color):
            rows = [row for row, _ in component]
            cols = [col for _, col in component]
            top, bottom = min(rows), max(rows)
            left, right = min(cols), max(cols)
            side = bottom - top + 1
            if side == right - left + 1 and side % 2 == 1 and len(component) == side * side:
                output[(top + bottom) // 2][(left + right) // 2] = marker_color
    return output
