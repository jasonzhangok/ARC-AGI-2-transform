from collections import deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == 8}
    components = []
    while remaining:
        start = remaining.pop()
        queue = deque([start])
        component = {start}
        while queue:
            row, col = queue.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                point = (row + dr, col + dc)
                if point in remaining:
                    remaining.remove(point)
                    component.add(point)
                    queue.append(point)
        components.append(component)

    for component in components:
        top = min(r for r, _ in component)
        bottom = max(r for r, _ in component)
        left = min(c for _, c in component)
        right = max(c for _, c in component)
        twos = {
            (r, c)
            for r in range(top, bottom + 1)
            for c in range(left, right + 1)
            if grid[r][c] == 2
        }
        if not twos:
            continue
        options = []
        for axis in ("horizontal", "vertical"):
            if axis == "horizontal":
                mirrored = {(top + bottom - r, c) for r, c in twos}
            else:
                mirrored = {(r, left + right - c) for r, c in twos}
            valid = all(grid[r][c] != 8 for r, c in mirrored)
            additions = {point for point in mirrored if grid[point[0]][point[1]] == 0}
            if valid:
                options.append((len(additions), additions))
        if options:
            _, additions = max(options, key=lambda item: item[0])
            for row, col in additions:
                output[row][col] = 2
    return output
