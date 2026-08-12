def transform(grid):
    height, width = len(grid), len(grid[0])
    objects = []
    _grid = grid
    _color = 3
    height, width = len(_grid), len(_grid[0])
    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if _grid[row][col] == _color
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
    _components_result_1 = result
    for component in _components_result_1:
        top = min(row for row, _ in component)
        left = min(col for _, col in component)
        bottom = max(row for row, _ in component)
        right = max(col for _, col in component)
        side = bottom - top + 1
        if side == right - left + 1 and len(component) == side * side:
            objects.append((top, left, side))

    output = [row[:] for row in grid]
    used = set()
    for first in range(len(objects)):
        for second in range(first + 1, len(objects)):
            a, b = objects[first], objects[second]
            if a[0] > b[0]:
                a, b = b, a
            size = a[2]
            if b[2] != size or b[0] - a[0] != size or abs(b[1] - a[1]) != size:
                continue
            pair = tuple(sorted((objects[first], objects[second])))
            if pair in used:
                continue
            used.add(pair)
            horizontal_shift = b[1] - a[1]
            placements = (
                (a[0] - size, a[1] + 2 * horizontal_shift),
                (b[0] + size, b[1] - 2 * horizontal_shift),
            )
            for top, left in placements:
                for row in range(top, top + size):
                    for col in range(left, left + size):
                        if 0 <= row < height and 0 <= col < width:
                            output[row][col] = 8
    return output
