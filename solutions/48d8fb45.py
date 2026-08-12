def transform(grid):
    h, w = (len(grid), len(grid[0]))
    marker = next(((r, c) for r in range(h) for c in range(w) if grid[r][c] == 5))
    seen = set()
    components = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] in (0, 5) or (r, c) in seen:
                continue
            color = grid[r][c]
            q = list([(r, c)])
            seen.add((r, c))
            cells = []
            while q:
                y, x = q.pop(0)
                cells.append((y, x))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        if dy == dx == 0:
                            continue
                        ny, nx = (y + dy, x + dx)
                        if 0 <= ny < h and 0 <= nx < w and (grid[ny][nx] == color) and ((ny, nx) not in seen):
                            seen.add((ny, nx))
                            q.append((ny, nx))
            distance = min((abs(y - marker[0]) + abs(x - marker[1]) for y, x in cells))
            components.append((distance, cells, color))
    _, cells, color = min(((_item_1[0], _index_1, _item_1) for _index_1, _item_1 in enumerate(components)))[2]
    r0, r1 = (min((r for r, _ in cells)), max((r for r, _ in cells)))
    c0, c1 = (min((c for _, c in cells)), max((c for _, c in cells)))
    chosen = set(cells)
    output = [[color if (r, c) in chosen else 0 for c in range(c0, c1 + 1)] for r in range(r0, r1 + 1)]
    return output
