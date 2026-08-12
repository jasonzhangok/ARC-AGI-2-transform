def _has_hole(component):
    cells = {(r, c) for r, c, _ in component}
    top = min(r for r, _, _ in component)
    bottom = max(r for r, _, _ in component)
    left = min(c for _, c, _ in component)
    right = max(c for _, c, _ in component)
    outside = set()
    stack = []
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            if ((r in (top, bottom) or c in (left, right))
                    and (r, c) not in cells):
                outside.add((r, c))
                stack.append((r, c))
    while stack:
        r, c = stack.pop()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if (top <= nr <= bottom and left <= nc <= right
                    and (nr, nc) not in cells and (nr, nc) not in outside):
                outside.add((nr, nc))
                stack.append((nr, nc))
    return any((r, c) not in cells and (r, c) not in outside
               for r in range(top, bottom + 1)
               for c in range(left, right + 1))


def transform(grid):
    h, w = len(grid), len(grid[0])
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
                    nr, nc = cr + dr, cc + dc
                    if (0 <= nr < h and 0 <= nc < w
                            and grid[nr][nc] == color and (nr, nc) not in seen):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            top = min(cr for cr, _, _ in component)
            bottom = max(cr for cr, _, _ in component)
            components.append((top, bottom, component, _has_hole(component)))

    out = [[0] * w for _ in range(h)]
    occupied = set()
    groups = [
        (sorted((item for item in components if item[3]), key=lambda item: item[0]), True),
        (sorted((item for item in components if not item[3]),
                key=lambda item: item[0], reverse=True), False),
    ]
    for group, pack_top in groups:
        for top, bottom, component, _ in group:
            height = bottom - top + 1
            candidates = (range(h - height + 1) if pack_top
                          else range(h - height, -1, -1))
            for new_top in candidates:
                translated = {(new_top + r - top, c) for r, c, _ in component}
                if translated & occupied:
                    continue
                for r, c, color in component:
                    out[new_top + r - top][c] = color
                occupied |= translated
                break
    return out
