def transform(grid):
    h, w = (len(grid), len(grid[0]))
    seen = set()
    components = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0 or (r, c) in seen:
                continue
            queue = list([(r, c)])
            seen.add((r, c))
            component = []
            while queue:
                x, y = queue.pop(0)
                component.append((x, y))
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < h and 0 <= ny < w and (grid[nx][ny] == 0) and ((nx, ny) not in seen):
                        seen.add((nx, ny))
                        queue.append((nx, ny))
            components.append(component)
    top_left = next((comp for comp in components if (0, 0) in comp))
    bottom_right = next((comp for comp in components if (h - 1, w - 1) in comp))
    center = min(((min(((2 * r - h + 1) ** 2 + (2 * c - w + 1) ** 2 for r, c in _item_1)), _index_1, _item_1) for _index_1, _item_1 in enumerate((comp for comp in components if comp is not top_left and comp is not bottom_right))))[2]
    output = [row[:] for row in grid]
    for color, component in ((1, top_left), (2, center), (3, bottom_right)):
        for r, c in component:
            output[r][c] = color
    return output
