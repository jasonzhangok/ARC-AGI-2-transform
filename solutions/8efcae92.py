def transform(grid):
    h, w = (len(grid), len(grid[0]))
    seen = set()
    components = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            queue = list([(r, c)])
            seen.add((r, c))
            component = []
            while queue:
                x, y = queue.pop(0)
                component.append((x, y))
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < h and 0 <= ny < w and (grid[nx][ny] != 0) and ((nx, ny) not in seen):
                        seen.add((nx, ny))
                        queue.append((nx, ny))
            components.append(component)
    chosen = max(((sum((grid[r][c] == 2 for r, c in _item_1)), _index_1, _item_1) for _index_1, _item_1 in enumerate(components)))[2]
    r0, r1 = (min((r for r, _ in chosen)), max((r for r, _ in chosen)))
    c0, c1 = (min((c for _, c in chosen)), max((c for _, c in chosen)))
    output = [row[c0:c1 + 1] for row in grid[r0:r1 + 1]]
    return output
