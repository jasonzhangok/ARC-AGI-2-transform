from collections import Counter, deque


def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    regions = {}
    for color in (1, 8):
        cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == color]
        regions[color] = (min(c for _, c in cells), max(c for _, c in cells))
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 2 or (r, c) in seen:
                continue
            queue = deque([(r, c)])
            seen.add((r, c))
            component = []
            while queue:
                x, y = queue.popleft()
                component.append((x, y))
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 2 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
            neighbors = []
            for x, y in component:
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] in (1, 8):
                        neighbors.append(grid[nx][ny])
            background = Counter(neighbors).most_common(1)[0][0]
            for x, y in component:
                output[x][y] = background
            c0, c1 = min(y for _, y in component), max(y for _, y in component)
            width = c1 - c0 + 1
            target = regions[background][0] if background == 8 else regions[background][1] - width + 1
            shift = target - c0
            for x, y in component:
                output[x][y + shift] = 2
    return output
