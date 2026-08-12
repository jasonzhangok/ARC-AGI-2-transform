from collections import deque


def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    colors = {( -1, -1): 1, (-1, 1): 2, (1, -1): 3, (1, 1): 4}
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 5 or (r, c) in seen:
                continue
            queue = deque([(r, c)])
            seen.add((r, c))
            component = []
            while queue:
                x, y = queue.popleft()
                component.append((x, y))
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 5 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
            r0, r1 = min(x for x, _ in component), max(x for x, _ in component)
            c0, c1 = min(y for _, y in component), max(y for _, y in component)
            for (dr, dc), color in colors.items():
                x = r0 - 1 if dr < 0 else r1 + 1
                y = c0 - 1 if dc < 0 else c1 + 1
                if 0 <= x < h and 0 <= y < w:
                    output[x][y] = color
    return output
