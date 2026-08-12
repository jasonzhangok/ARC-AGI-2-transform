def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    foreground = next(color for color in counts if color != background)

    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != foreground or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            component = []
            while stack:
                cr, cc = stack.pop()
                component.append((cr, cc))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if (0 <= nr < h and 0 <= nc < w
                            and grid[nr][nc] == foreground
                            and (nr, nc) not in seen):
                        seen.add((nr, nc))
                        stack.append((nr, nc))

            if len(component) == 1:
                out[r][c] = background
                continue
            top = min(cr for cr, _ in component)
            bottom = max(cr for cr, _ in component)
            left = min(cc for _, cc in component)
            right = max(cc for _, cc in component)
            normalized = {(cr - top, cc - left) for cr, cc in component}
            ch, cw = bottom - top + 1, right - left + 1
            left_right = all((cr, cw - 1 - cc) in normalized
                             for cr, cc in normalized)
            top_bottom = all((ch - 1 - cr, cc) in normalized
                             for cr, cc in normalized)
            half_turn = all((ch - 1 - cr, cw - 1 - cc) in normalized
                            for cr, cc in normalized)
            if left_right:
                new_color = 3
            elif top_bottom:
                new_color = 1
            elif half_turn:
                new_color = 6
            else:
                new_color = foreground
            for cr, cc in component:
                out[cr][cc] = new_color
    output = out
    return output
