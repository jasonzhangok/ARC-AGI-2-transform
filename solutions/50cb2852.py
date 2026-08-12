def transform(grid):
    out = [row[:] for row in grid]
    h, w = (len(grid), len(grid[0]))
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            color = grid[r][c]
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
            r0, r1 = (min((y for y, _ in cells)), max((y for y, _ in cells)))
            c0, c1 = (min((x for _, x in cells)), max((x for _, x in cells)))
            for y in range(r0 + 1, r1):
                for x in range(c0 + 1, c1):
                    out[y][x] = 8
    output = out
    return output
