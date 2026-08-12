def transform(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    objects = []
    for r in range(h):
        for c in range(w):
            color = grid[r][c]
            if color == 0 or (r, c) in seen:
                continue
            cells = []
            stack = [(r, c)]
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                cells.append((y, x))
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny, nx = y + dy, x + dx
                    if (0 <= ny < h and 0 <= nx < w and grid[ny][nx] == color
                            and (ny, nx) not in seen):
                        seen.add((ny, nx))
                        stack.append((ny, nx))
            r0, r1 = min(y for y, _ in cells), max(y for y, _ in cells)
            c0, c1 = min(x for _, x in cells), max(x for _, x in cells)
            if len(cells) == (r1 - r0 + 1) * (c1 - c0 + 1):
                objects.append((color, r0, r1, c0, c1))
    out = [row[:] for row in grid]
    for i, a in enumerate(objects):
        for b in objects[i + 1:]:
            if a[0] != b[0]:
                continue
            top, bottom = max(a[1], b[1]), min(a[2], b[2])
            if top < bottom and (a[4] < b[3] or b[4] < a[3]):
                left, right = (a, b) if a[4] < b[3] else (b, a)
                blocked = any(
                    other[0] == a[0] and left[4] < other[3]
                    and other[4] < right[3]
                    and max(top, other[1]) <= min(bottom, other[2])
                    for other in objects if other not in (a, b)
                )
                if not blocked:
                    for r in range(top + 1, bottom):
                        for c in range(left[4] + 1, right[3]):
                            out[r][c] = 8
            left_edge, right_edge = max(a[3], b[3]), min(a[4], b[4])
            if left_edge < right_edge and (a[2] < b[1] or b[2] < a[1]):
                upper, lower = (a, b) if a[2] < b[1] else (b, a)
                blocked = any(
                    other[0] == a[0] and upper[2] < other[1]
                    and other[2] < lower[1]
                    and max(left_edge, other[3]) <= min(right_edge, other[4])
                    for other in objects if other not in (a, b)
                )
                if not blocked:
                    for r in range(upper[2] + 1, lower[1]):
                        for c in range(left_edge + 1, right_edge):
                            out[r][c] = 8
    return out
