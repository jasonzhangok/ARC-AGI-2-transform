def transform(grid):
    h, w = (len(grid), len(grid[0]))
    all_colors = {v for row in grid for v in row if v != 0}
    components = []
    seen = set()
    for color in all_colors:
        for r in range(h):
            for c in range(w):
                if grid[r][c] != color or (r, c) in seen:
                    continue
                q = list([(r, c)])
                seen.add((r, c))
                cells = []
                while q:
                    y, x = q.pop(0)
                    cells.append((y, x))
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = (y + dy, x + dx)
                        if 0 <= ny < h and 0 <= nx < w and (grid[ny][nx] == color) and ((ny, nx) not in seen):
                            seen.add((ny, nx))
                            q.append((ny, nx))
                if len(cells) >= 8:
                    components.append((color, set(cells)))
    out = [[0] * w for _ in range(h)]
    for _, boundary in components:
        for r, c in boundary:
            out[r][c] = grid[r][c]
    for boundary_color, boundary in components:
        r0, r1 = (min((r for r, _ in boundary)), max((r for r, _ in boundary)))
        c0, c1 = (min((c for _, c in boundary)), max((c for _, c in boundary)))
        outside = set()
        q = []
        for r in range(r0, r1 + 1):
            for c in (c0, c1):
                if (r, c) not in boundary and (r, c) not in outside:
                    outside.add((r, c))
                    q.append((r, c))
        for c in range(c0, c1 + 1):
            for r in (r0, r1):
                if (r, c) not in boundary and (r, c) not in outside:
                    outside.add((r, c))
                    q.append((r, c))
        while q:
            r, c = q.pop(0)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = (r + dr, c + dc)
                if r0 <= nr <= r1 and c0 <= nc <= c1 and ((nr, nc) not in boundary) and ((nr, nc) not in outside):
                    outside.add((nr, nc))
                    q.append((nr, nc))
        inside = [(r, c) for r in range(r0, r1 + 1) for c in range(c0, c1 + 1) if (r, c) not in boundary and (r, c) not in outside]
        markers = {}
        for cell_value in (grid[r][c] for r, c in inside if grid[r][c] not in (0, boundary_color)):
            markers[cell_value] = markers.get(cell_value, 0) + 1
        if not markers:
            continue
        fill = max(markers, key=markers.get)
        for r, c in inside:
            out[r][c] = fill
    output = out
    return output
