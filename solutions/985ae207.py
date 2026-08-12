def transform(grid):
    out = [row[:] for row in grid]
    h, w = (len(grid), len(grid[0]))
    templates = []
    for top in range(h - 2):
        for left in range(w - 2):
            outer = grid[top][left]
            center = grid[top + 1][left + 1]
            if outer == 8 or center in (8, outer):
                continue
            if all((grid[top + r][left + c] == outer for r in range(3) for c in range(3) if (r, c) != (1, 1))):
                pattern = [row[left:left + 3] for row in grid[top:top + 3]]
                templates.append((top, left, center, pattern))
    for top, left, center_color, pattern in templates:
        _grid = grid
        _color = center_color
        h, w = (len(_grid), len(_grid[0]))
        seen = set()
        result = []
        for r in range(h):
            for c in range(w):
                if _grid[r][c] != _color or (r, c) in seen:
                    continue
                stack = [(r, c)]
                seen.add((r, c))
                component = set()
                while stack:
                    cr, cc = stack.pop()
                    component.add((cr, cc))
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = (cr + dr, cc + dc)
                        if 0 <= nr < h and 0 <= nc < w and (_grid[nr][nc] == _color) and ((nr, nc) not in seen):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                result.append(component)
        _color_components_result_1 = result
        blocks = _color_components_result_1
        target = max(blocks, key=len)
        block_top = min((r for r, _ in target))
        block_bottom = max((r for r, _ in target))
        block_left = min((c for _, c in target))
        block_right = max((c for _, c in target))
        if block_right < left:
            dr, dc = (0, -3)
        elif block_left > left + 2:
            dr, dc = (0, 3)
        elif block_bottom < top:
            dr, dc = (-3, 0)
        else:
            dr, dc = (3, 0)
        current_top, current_left = (top, left)
        while True:
            current_top += dr
            current_left += dc
            patch_cells = {(current_top + r, current_left + c) for r in range(3) for c in range(3)}
            for r in range(3):
                for c in range(3):
                    nr, nc = (current_top + r, current_left + c)
                    if 0 <= nr < h and 0 <= nc < w:
                        out[nr][nc] = pattern[r][c]
            if patch_cells & target:
                break
    output = out
    return output
