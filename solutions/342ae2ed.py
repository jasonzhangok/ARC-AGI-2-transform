from collections import defaultdict, deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    background = 7
    colors = {value for row in grid for value in row if value != background}
    result = [row[:] for row in grid]
    for color in colors:
        remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == color}
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
        if len(components) != 2:
            continue
        first, second = components
        a, b = min(
            ((p, q) for p in first for q in second),
            key=lambda pair: max(abs(pair[0][0] - pair[1][0]), abs(pair[0][1] - pair[1][1])),
        )
        dr = (b[0] > a[0]) - (b[0] < a[0])
        dc = (b[1] > a[1]) - (b[1] < a[1])
        r, c = a[0] + dr, a[1] + dc
        while (r, c) != b:
            result[r][c] = color
            r += dr
            c += dc
    return result
