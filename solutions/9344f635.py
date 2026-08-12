from collections import Counter, deque


def transform(grid):
    h, w = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    output = [row[:] for row in grid]
    seen = set()
    for r in range(h):
        for c in range(w):
            color = grid[r][c]
            if color == background or (r, c) in seen:
                continue
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
            rows = {x for x, _ in component}
            cols = {y for _, y in component}
            if len(rows) == 1:
                row = next(iter(rows))
                output[row] = [color] * w
            elif len(cols) == 1:
                col = next(iter(cols))
                for x in range(h):
                    output[x][col] = color
    return output
