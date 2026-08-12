from collections import Counter, deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != background}
    components = []
    while remaining:
        start = remaining.pop()
        color = grid[start[0]][start[1]]
        component = {start}
        queue = deque([start])
        while queue:
            r, c = queue.popleft()
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining and grid[point[0]][point[1]] == color:
                    remaining.remove(point)
                    component.add(point)
                    queue.append(point)
        components.append((color, component))
    rectangle_color, rectangle = max(components, key=lambda item: len(item[1]))
    top = min(r for r, _ in rectangle)
    bottom = max(r for r, _ in rectangle)
    left = min(c for _, c in rectangle)
    right = max(c for _, c in rectangle)
    result = [row[:] for row in grid]
    for color, component in components:
        if component == rectangle:
            continue
        for r, c in component:
            if top <= r <= bottom:
                edge = left - 1 if c < left else right + 1
                for cc in range(min(c, edge), max(c, edge) + 1):
                    result[r][cc] = color
            elif left <= c <= right:
                edge = top - 1 if r < top else bottom + 1
                for rr in range(min(r, edge), max(r, edge) + 1):
                    result[rr][c] = color
    return result
