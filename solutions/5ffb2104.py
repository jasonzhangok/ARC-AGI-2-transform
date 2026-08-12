def transform(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    pieces = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            cells = []
            while stack:
                x, y = stack.pop()
                cells.append((x, y, grid[x][y]))
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    q = (x + dx, y + dy)
                    if 0 <= q[0] < h and 0 <= q[1] < w and q not in seen and grid[q[0]][q[1]] != 0:
                        seen.add(q)
                        stack.append(q)
            pieces.append(cells)
    out = [[0] * w for _ in range(h)]
    for cells in sorted(pieces, key=lambda p: max(c for _, c, _ in p), reverse=True):
        shift = 0
        while all(c + shift + 1 < w and out[r][c + shift + 1] == 0 for r, c, _ in cells):
            shift += 1
        for r, c, color in cells:
            out[r][c + shift] = color
    return out
