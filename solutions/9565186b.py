from collections import Counter, deque


def transform(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    best = []
    for r in range(h):
        for c in range(w):
            if (r, c) in seen:
                continue
            color = grid[r][c]
            queue = deque([(r, c)])
            seen.add((r, c))
            component = []
            while queue:
                x, y = queue.popleft()
                component.append((x, y))
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == color and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
            if len(component) > len(best):
                best = component
    keep = set(best)
    return [[grid[r][c] if (r, c) in keep else 5 for c in range(w)] for r in range(h)]
