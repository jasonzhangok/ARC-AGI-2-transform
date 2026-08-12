def transform(grid):
    h, w = (len(grid), len(grid[0]))
    seen = set()
    components = []
    for r in range(h):
        for c in range(w):
            color = grid[r][c]
            if color == 0 or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            component = []
            while stack:
                cr, cc = stack.pop()
                component.append((cr, cc, color))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = (cr + dr, cc + dc)
                    if 0 <= nr < h and 0 <= nc < w and (grid[nr][nc] == color) and ((nr, nc) not in seen):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            top = min((cr for cr, _, _ in component))
            bottom = max((cr for cr, _, _ in component))
            _component = component
            cells = {(r, c) for r, c, _ in _component}
            top = min((r for r, _, _ in _component))
            bottom = max((r for r, _, _ in _component))
            left = min((c for _, c, _ in _component))
            right = max((c for _, c, _ in _component))
            outside = set()
            stack = []
            for r in range(top, bottom + 1):
                for c in range(left, right + 1):
                    if (r in (top, bottom) or c in (left, right)) and (r, c) not in cells:
                        outside.add((r, c))
                        stack.append((r, c))
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = (r + dr, c + dc)
                    if top <= nr <= bottom and left <= nc <= right and ((nr, nc) not in cells) and ((nr, nc) not in outside):
                        outside.add((nr, nc))
                        stack.append((nr, nc))
            _has_hole_result_1 = any(((r, c) not in cells and (r, c) not in outside for r in range(top, bottom + 1) for c in range(left, right + 1)))
            components.append((top, bottom, component, _has_hole_result_1))
    out = [[0] * w for _ in range(h)]
    occupied = set()
    groups = [([_record_1[2] for _record_1 in sorted(((_item_1[0], _index_1, _item_1) for _index_1, _item_1 in enumerate((item for item in components if item[3]))))], True), ([_record_2[2] for _record_2 in sorted(((_item_2[0], -_index_2, _item_2) for _index_2, _item_2 in enumerate((item for item in components if not item[3]))), reverse=True)], False)]
    for group, pack_top in groups:
        for top, bottom, component, _ in group:
            height = bottom - top + 1
            candidates = range(h - height + 1) if pack_top else range(h - height, -1, -1)
            for new_top in candidates:
                translated = {(new_top + r - top, c) for r, c, _ in component}
                if translated & occupied:
                    continue
                for r, c, color in component:
                    out[new_top + r - top][c] = color
                occupied |= translated
                break
    output = out
    return output
