def _neighbors(nodes, point):
    return {
        other
        for other in nodes
        if abs(point[0] - other[0]) + abs(point[1] - other[1]) == 1
    }


def _components(nodes):
    nodes = set(nodes)
    seen = set()
    result = []
    for point in nodes:
        if point in seen:
            continue
        stack = [point]
        seen.add(point)
        component = []
        while stack:
            current = stack.pop()
            component.append(current)
            for neighbor in _neighbors(nodes, current):
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        result.append(component)
    return sorted(result, key=len, reverse=True)


def _isomorphism(source, target):
    source, target = set(source), set(target)
    source_anchor = max(source, key=lambda point: (point[0], -point[1]))
    target_anchor = min(target)
    mapping = {source_anchor: target_anchor}
    used = {target_anchor}
    order = sorted(
        source - {source_anchor},
        key=lambda point: (
            -len(_neighbors(source, point)),
            abs(point[0] - source_anchor[0]) + abs(point[1] - source_anchor[1]),
            point,
        ),
    )

    def search(index):
        if index == len(order):
            return True
        source_point = order[index]
        for target_point in sorted(target - used):
            if len(_neighbors(source, source_point)) != len(_neighbors(target, target_point)):
                continue
            if not all(
                (mapped_source in _neighbors(source, source_point))
                == (mapped_target in _neighbors(target, target_point))
                for mapped_source, mapped_target in mapping.items()
            ):
                continue
            mapping[source_point] = target_point
            used.add(target_point)
            if search(index + 1):
                return True
            used.remove(target_point)
            del mapping[source_point]
        return False

    search(0)
    return mapping


def transform(grid):
    height, width = len(grid), len(grid[0])
    key_points = [
        (r, c, grid[r][c])
        for r in range(height)
        for c in range(width)
        if grid[r][c] not in (0, 8)
    ]
    key_top, key_bottom = min(r for r, _, _ in key_points), max(r for r, _, _ in key_points)
    key_left, key_right = min(c for _, c, _ in key_points), max(c for _, c, _ in key_points)
    key_height, key_width = key_bottom - key_top + 1, key_right - key_left + 1
    colors = {
        (r - key_top, c - key_left): color
        for r, c, color in key_points
    }

    azure = [
        (r, c)
        for r in range(height)
        for c in range(width)
        if grid[r][c] == 8
    ]
    top, bottom = min(r for r, _ in azure), max(r for r, _ in azure)
    left, right = min(c for _, c in azure), max(c for _, c in azure)
    scale = (bottom - top + 1) // key_height
    mask = {
        (r, c)
        for r in range(key_height)
        for c in range(key_width)
        if all(
            grid[top + r * scale + dr][left + c * scale + dc] == 8
            for dr in range(scale)
            for dc in range(scale)
        )
    }

    output = [row[:] for row in grid]
    for source_component, target_component in zip(
        _components(colors), _components(mask)
    ):
        mapping = _isomorphism(source_component, target_component)
        for source, target in mapping.items():
            for dr in range(scale):
                for dc in range(scale):
                    output[top + target[0] * scale + dr][
                        left + target[1] * scale + dc
                    ] = colors[source]
    return output
