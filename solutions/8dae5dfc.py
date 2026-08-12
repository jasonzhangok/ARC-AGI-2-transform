from collections import deque


def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
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
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 0 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
            r0, r1 = min(x for x, _ in component), max(x for x, _ in component)
            c0, c1 = min(y for _, y in component), max(y for _, y in component)
            colors = sorted({grid[x][y] for x, y in component},
                            key=lambda color: min(min(x - r0, r1 - x, y - c0, c1 - y)
                                                  for x, y in component if grid[x][y] == color))
            replacement = dict(zip(colors, reversed(colors)))
            for x, y in component:
                output[x][y] = replacement[grid[x][y]]
    return output
