from collections import Counter, deque


def transform(grid):
    h, w = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    best = []
    seen = set()
    for r in range(h):
        for c in range(w):
            color = grid[r][c]
            if (r, c) in seen:
                continue
            queue = deque([(r, c)])
            seen.add((r, c))
            component = []
            while queue:
                x, y = queue.popleft()
                component.append((x, y))
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < h and 0 <= ny < w and (nx, ny) not in seen and grid[nx][ny] == color:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
            if len(component) > len(best):
                best = component
    r0, r1 = min(r for r, _ in best), max(r for r, _ in best)
    c0, c1 = min(c for _, c in best), max(c for _, c in best)
    cells = set(best)
    while r0 < r1 and sum((r0, c) in cells for c in range(c0, c1 + 1)) < (c1 - c0 + 1) / 2:
        r0 += 1
    while r1 > r0 and sum((r1, c) in cells for c in range(c0, c1 + 1)) < (c1 - c0 + 1) / 2:
        r1 -= 1
    while c0 < c1 and sum((r, c0) in cells for r in range(r0, r1 + 1)) < (r1 - r0 + 1) / 2:
        c0 += 1
    while c1 > c0 and sum((r, c1) in cells for r in range(r0, r1 + 1)) < (r1 - r0 + 1) / 2:
        c1 -= 1
    output = [row[c0:c1 + 1] for row in grid[r0:r1 + 1]]
    main = grid[next(iter(cells))[0]][next(iter(cells))[1]]
    marks = [(r, c) for r, row in enumerate(output) for c, value in enumerate(row) if value != main]
    mark = output[marks[0][0]][marks[0][1]] if marks else main
    for r, c in marks:
        output[r] = [mark] * len(output[r])
        for row in output:
            row[c] = mark
    return output
