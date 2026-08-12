from collections import deque


def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    components = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0 or (r, c) in seen:
                continue
            queue = deque([(r, c)])
            seen.add((r, c))
            component = []
            while queue:
                x, y = queue.popleft()
                component.append((x, y))
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 0 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
            components.append(component)
    min_r = min(r for comp in components for r, _ in comp)
    max_r = max(r for comp in components for r, _ in comp)
    min_c = min(c for comp in components for _, c in comp)
    max_c = max(c for comp in components for _, c in comp)
    for component in components:
        edge = any(r in (min_r, max_r) or c in (min_c, max_c) for r, c in component)
        color = 2 if edge else 3
        for r, c in component:
            output[r][c] = color
    return output
