from collections import deque


def transform(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    components = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            queue = deque([(r, c)])
            seen.add((r, c))
            component = []
            while queue:
                x, y = queue.popleft()
                component.append((x, y))
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 0 and (nx, ny) not in seen:
                            seen.add((nx, ny))
                            queue.append((nx, ny))
            components.append(component)
    chosen = max(components, key=lambda comp: len({grid[r][c] for r, c in comp}))
    r0, r1 = min(r for r, _ in chosen), max(r for r, _ in chosen)
    c0, c1 = min(c for _, c in chosen), max(c for _, c in chosen)
    return [row[c0:c1 + 1] for row in grid[r0:r1 + 1]]
