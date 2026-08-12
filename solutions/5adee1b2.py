def transform(grid):
    h, w = (len(grid), len(grid[0]))
    out = [row[:] for row in grid]
    mapping = {}
    marker_cells = set()
    for r in range(h - 1):
        for c in range(w - 1):
            a, b = (grid[r][c], grid[r][c + 1])
            if a and b and (a != b) and (grid[r + 1][c] == a) and (grid[r + 1][c + 1] == b):
                mapping[a] = b
                marker_cells.update({(r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)})
    for source, border in mapping.items():
        cells = {(r, c) for r in range(h) for c in range(w) if grid[r][c] == source and (r, c) not in marker_cells}
        seen = set()
        while cells - seen:
            start = next(iter(cells - seen))
            stack = [start]
            seen.add(start)
            comp = []
            while stack:
                p = stack.pop()
                comp.append(p)
                for q in cells:
                    if q not in seen and max(abs(q[0] - p[0]), abs(q[1] - p[1])) <= 2:
                        seen.add(q)
                        stack.append(q)
            r0, r1 = (min((r for r, _ in comp)), max((r for r, _ in comp)))
            c0, c1 = (min((c for _, c in comp)), max((c for _, c in comp)))
            a0, a1 = (max(0, r0 - 1), min(h - 1, r1 + 1))
            b0, b1 = (max(0, c0 - 1), min(w - 1, c1 + 1))
            outside = set()
            q = []
            for r in range(a0, a1 + 1):
                for c in (b0, b1):
                    if out[r][c] == 0 and (r, c) not in outside:
                        outside.add((r, c))
                        q.append((r, c))
            for c in range(b0, b1 + 1):
                for r in (a0, a1):
                    if out[r][c] == 0 and (r, c) not in outside:
                        outside.add((r, c))
                        q.append((r, c))
            while q:
                r, c = q.pop(0)
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = (r + dr, c + dc)
                    if a0 <= nr <= a1 and b0 <= nc <= b1 and (out[nr][nc] == 0) and ((nr, nc) not in outside):
                        outside.add((nr, nc))
                        q.append((nr, nc))
            for r, c in outside:
                out[r][c] = border
    output = out
    return output
