def transform(grid):
    h, w = (len(grid), len(grid[0]))
    seen = set()
    components = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 8 or (r, c) in seen:
                continue
            queue = list([(r, c)])
            seen.add((r, c))
            component = []
            while queue:
                x, y = queue.pop(0)
                component.append((x, y))
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = (x + dx, y + dy)
                        if 0 <= nx < h and 0 <= ny < w and (grid[nx][ny] == 8) and ((nx, ny) not in seen):
                            seen.add((nx, ny))
                            queue.append((nx, ny))
            components.append(component)
    reference = max((((max((c for _, c in _item_1)), len(_item_1)), _index_1, _item_1) for _index_1, _item_1 in enumerate(components)))[2]
    rr0, rr1 = (min((r for r, _ in reference)), max((r for r, _ in reference)))
    rc0 = min((c for _, c in reference))
    ref_h = rr1 - rr0 + 1
    ref_mask = {(r - rr0, c - rc0) for r, c in reference}
    output = [row[:] for row in grid]
    for component in components:
        if component is reference:
            continue
        r0, r1 = (min((r for r, _ in component)), max((r for r, _ in component)))
        c0, c1 = (min((c for _, c in component)), max((c for _, c in component)))
        ch = r1 - r0 + 1
        if ref_h == 1:
            for c in range(c1 + 1, w):
                output[r0][c] = 1
        elif ch == ref_h:
            for dr, dc in ref_mask:
                c = c0 + dc
                if c > c1 and c < w:
                    output[r0 + dr][c] = 1
        else:
            row = r1 + 1
            if row < h:
                for c in range(c1 + 1, w):
                    output[row][c] = 1
    return output
