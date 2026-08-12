def transform(grid):
    height, width = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    nodes = []

    for color in (2, 8):
        remaining = {
            (r, c)
            for r in range(height)
            for c in range(width)
            if grid[r][c] == color
        }
        while remaining:
            start = remaining.pop()
            component = {start}
            stack = [start]
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = (r + dr, c + dc)
                    if neighbor in remaining:
                        remaining.remove(neighbor)
                        component.add(neighbor)
                        stack.append(neighbor)
            top = min(r for r, _ in component)
            left = min(c for _, c in component)
            bottom = max(r for r, _ in component)
            right = max(c for _, c in component)
            nodes.append((color, top, left, bottom - top + 1, right - left + 1))

    current = next(index for index, node in enumerate(nodes) if node[0] == 2)
    visited = {current}
    while True:
        source = nodes[current]
        candidates = []
        for index, node in enumerate(nodes):
            if index in visited:
                continue
            if source[1] == node[1]:
                low, high = sorted((source[2], node[2]))
                blocked = any(
                    other not in (current, index)
                    and item[1] == source[1]
                    and low < item[2] < high
                    for other, item in enumerate(nodes)
                )
                if not blocked:
                    candidates.append((abs(source[2] - node[2]), index, "horizontal"))
            if source[2] == node[2]:
                low, high = sorted((source[1], node[1]))
                blocked = any(
                    other not in (current, index)
                    and item[2] == source[2]
                    and low < item[1] < high
                    for other, item in enumerate(nodes)
                )
                if not blocked:
                    candidates.append((abs(source[1] - node[1]), index, "vertical"))
        if not candidates:
            break

        _, next_index, orientation = min(candidates)
        target = nodes[next_index]
        if orientation == "horizontal":
            left = min(source[2] + source[4], target[2] + target[4])
            right = max(source[2], target[2])
            for r in range(source[1], source[1] + 2):
                for c in range(left, right):
                    if result[r][c] == 0:
                        result[r][c] = 7
        else:
            top = min(source[1] + source[3], target[1] + target[3])
            bottom = max(source[1], target[1])
            for r in range(top, bottom):
                for c in range(source[2], source[2] + 2):
                    if result[r][c] == 0:
                        result[r][c] = 7
        visited.add(next_index)
        current = next_index
    return result
