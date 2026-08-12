def transform(grid):
    out = [row[:] for row in grid]
    h, w = (len(grid), len(grid[0]))
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            q = list([(r, c)])
            seen.add((r, c))
            cells = []
            while q:
                y, x = q.pop(0)
                cells.append((y, x))
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = (y + dy, x + dx)
                    if 0 <= ny < h and 0 <= nx < w and (grid[ny][nx] != 0) and ((ny, nx) not in seen):
                        seen.add((ny, nx))
                        q.append((ny, nx))
            colors = sorted({grid[y][x] for y, x in cells})
            if len(colors) == 2:
                a, b = colors
                for y, x in cells:
                    out[y][x] = b if grid[y][x] == a else a
    output = out
    return output
