def transform(grid):
    h, w = len(grid), len(grid[0])
    seen, objects = set(), []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            color = grid[r][c]
            stack, cells = [(r, c)], []
            seen.add((r, c))
            while stack:
                x, y = stack.pop()
                cells.append((x, y))
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == color and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            objects.append((cells, color))
    cells, color = max(objects, key=lambda item: len(item[0]))
    r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
    c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
    occupied = set(cells)
    return [[color if (r, c) in occupied else 0 for c in range(c0, c1 + 1)] for r in range(r0, r1 + 1)]
