from collections import deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != 0}
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

    def signature(component):
        top = min(r for r, _ in component)
        left = min(c for _, c in component)
        return frozenset((r - top, c - left) for r, c in component)

    exemplars = {}
    for color, component in components:
        if color != 1:
            exemplars[signature(component)] = color
    result = [row[:] for row in grid]
    for color, component in components:
        if color == 1:
            replacement = exemplars[signature(component)]
            for r, c in component:
                result[r][c] = replacement
    return result
