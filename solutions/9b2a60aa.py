def transform(grid):
    out = [row[:] for row in grid]
    h, w = (len(grid), len(grid[0]))
    _grid = grid
    h, w = (len(_grid), len(_grid[0]))
    seen = set()
    result = []
    for r in range(h):
        for c in range(w):
            if _grid[r][c] != 2 or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            component = []
            while stack:
                cr, cc = stack.pop()
                component.append((cr, cc))
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = (cr + dr, cc + dc)
                        if 0 <= nr < h and 0 <= nc < w and (_grid[nr][nc] == 2) and ((nr, nc) not in seen):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
            result.append(component)
    _components_of_two_result_1 = result
    template = max(_components_of_two_result_1, key=len)
    template_set = set(template)
    top = min((r for r, _ in template))
    bottom = max((r for r, _ in template))
    left = min((c for _, c in template))
    right = max((c for _, c in template))
    markers = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0 and (r, c) not in template_set]
    vertical = len({c for _, c, _ in markers}) == 1
    markers = [_record_1[2] for _record_1 in sorted(((_item_1[0] if vertical else _item_1[1], _index_1, _item_1) for _index_1, _item_1 in enumerate(markers)))]
    template_index = next((i for i, item in enumerate(markers) if item[2] == 2))
    for index, (marker_r, marker_c, color) in enumerate(markers):
        if vertical:
            start_r = top + marker_r - markers[template_index][0] + (index - template_index) * (bottom - top)
            start_c = left
        else:
            start_r = top
            start_c = left + marker_c - markers[template_index][1] + (index - template_index) * (right - left)
        for r, c in template:
            nr = start_r + r - top
            nc = start_c + c - left
            if 0 <= nr < h and 0 <= nc < w:
                out[nr][nc] = color
    output = out
    return output
