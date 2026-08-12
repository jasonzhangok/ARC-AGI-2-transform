def _components_of_two(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    result = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 2 or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            component = []
            while stack:
                cr, cc = stack.pop()
                component.append((cr, cc))
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = cr + dr, cc + dc
                        if (0 <= nr < h and 0 <= nc < w
                                and grid[nr][nc] == 2
                                and (nr, nc) not in seen):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
            result.append(component)
    return result


def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    template = max(_components_of_two(grid), key=len)
    template_set = set(template)
    top = min(r for r, _ in template)
    bottom = max(r for r, _ in template)
    left = min(c for _, c in template)
    right = max(c for _, c in template)

    markers = [(r, c, grid[r][c]) for r in range(h) for c in range(w)
               if grid[r][c] != 0 and (r, c) not in template_set]
    vertical = len({c for _, c, _ in markers}) == 1
    markers.sort(key=lambda item: item[0] if vertical else item[1])
    template_index = next(i for i, item in enumerate(markers) if item[2] == 2)

    for index, (marker_r, marker_c, color) in enumerate(markers):
        if vertical:
            start_r = (top + marker_r - markers[template_index][0]
                       + (index - template_index) * (bottom - top))
            start_c = left
        else:
            start_r = top
            start_c = (left + marker_c - markers[template_index][1]
                       + (index - template_index) * (right - left))
        for r, c in template:
            nr = start_r + r - top
            nc = start_c + c - left
            if 0 <= nr < h and 0 <= nc < w:
                out[nr][nc] = color
    return out
