from collections import deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == 1}
    components = []
    while remaining:
        start = remaining.pop()
        component = {start}
        queue = deque([start])
        while queue:
            r, c = queue.popleft()
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining:
                    remaining.remove(point)
                    component.add(point)
                    queue.append(point)
        components.append(component)

    result = [[4] * width for _ in range(height)]
    for component in components:
        top = min(r for r, _ in component)
        bottom = max(r for r, _ in component)
        left = min(c for _, c in component)
        right = max(c for _, c in component)
        background = {(r, c) for r in range(top, bottom + 1) for c in range(left, right + 1) if (r, c) not in component}
        reachable = set()
        queue = deque(
            point for point in background
            if point[0] in (top, bottom) or point[1] in (left, right)
        )
        reachable.update(queue)
        while queue:
            r, c = queue.popleft()
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in background and point not in reachable:
                    reachable.add(point)
                    queue.append(point)
        closed = not background or bool(background - reachable)
        color = 2 if closed else 3
        shift = -left if closed else width - 1 - right
        for r, c in component:
            result[r][c + shift] = color
    return result
