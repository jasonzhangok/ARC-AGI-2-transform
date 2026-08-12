def transform(grid):
    out = [[0 if value == 5 else value for value in row] for row in grid]
    h, w = len(grid), len(grid[0])
    colored = [(r, c, grid[r][c]) for r in range(h) for c in range(w)
               if grid[r][c] not in (0, 5)]
    color = colored[0][2]
    base_offset = colored[0][1] - colored[0][0]

    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 5 or (r, c) in seen:
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
                            and grid[nr][nc] == 5 and (nr, nc) not in seen):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            offsets = [cc - cr for cr, cc in component]
            if max(offsets) < base_offset:
                target_offset = min(offsets) - 2
            else:
                target_offset = max(offsets) + 2
            for nr in range(h):
                nc = nr + target_offset
                if 0 <= nc < w:
                    out[nr][nc] = color
    return out
