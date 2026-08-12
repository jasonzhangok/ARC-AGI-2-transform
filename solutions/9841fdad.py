def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    frame = grid[0][0]
    divider = next(c for c in range(1, w - 1)
                   if all(grid[r][c] == frame for r in range(h)))
    left_start, left_end = 1, divider - 1
    right_start, right_end = divider + 1, w - 2
    left_width = left_end - left_start + 1
    right_width = right_end - right_start + 1
    left_background = max(
        {grid[r][c] for r in range(1, h - 1)
         for c in range(left_start, left_end + 1)},
        key=lambda color: sum(grid[r][c] == color for r in range(1, h - 1)
                              for c in range(left_start, left_end + 1)))

    seen = set()
    components = []
    for r in range(1, h - 1):
        for c in range(left_start, left_end + 1):
            color = grid[r][c]
            if color == left_background or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            component = []
            while stack:
                cr, cc = stack.pop()
                component.append((cr, cc))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if (1 <= nr < h - 1 and left_start <= nc <= left_end
                            and grid[nr][nc] == color and (nr, nc) not in seen):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            components.append((color, component))

    for color, component in components:
        min_c = min(c for _, c in component)
        max_c = max(c for _, c in component)
        left_gap = min_c - left_start
        right_gap = left_end - max_c
        if left_gap < right_gap:
            for r, c in component:
                out[r][right_start + c - left_start] = color
        elif right_gap < left_gap:
            for r, c in component:
                out[r][right_end - (left_end - c)] = color
        else:
            rows = {r for r, _ in component}
            for r in rows:
                for c in range(right_start + left_gap,
                               right_start + right_width - right_gap):
                    out[r][c] = color
    return out
