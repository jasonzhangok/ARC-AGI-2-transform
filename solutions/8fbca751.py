from collections import deque


def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    components = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 8 or (r, c) in seen:
                continue
            queue = deque([(r, c)])
            seen.add((r, c))
            component = []
            while queue:
                x, y = queue.popleft()
                component.append((x, y))
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 8 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
            components.append(component)
    large = [component for component in components if len(component) > 1]
    for singleton in [component for component in components if len(component) == 1]:
        x, y = singleton[0]
        nearest = min(large, key=lambda comp: min(max(abs(x - a), abs(y - b)) for a, b in comp))
        nearest.append((x, y))
    for component in large:
        r0, r1 = min(x for x, _ in component), max(x for x, _ in component)
        c0, c1 = min(y for _, y in component), max(y for _, y in component)
        for x in range(r0, r1 + 1):
            for y in range(c0, c1 + 1):
                if output[x][y] == 0:
                    output[x][y] = 2
    return output
