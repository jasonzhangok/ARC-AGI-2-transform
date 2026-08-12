from collections import deque


def transform(grid):
    h, w = len(grid), len(grid[0])
    seen = set(); objects = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 6 or (r, c) in seen:
                continue
            q = deque([(r, c)]); seen.add((r, c)); cells = []
            while q:
                y, x = q.popleft(); cells.append((y, x))
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = y + dy, x + dx
                    if (0 <= ny < h and 0 <= nx < w and grid[ny][nx] == 6
                            and (ny, nx) not in seen):
                        seen.add((ny, nx)); q.append((ny, nx))
            r0, r1 = min(y for y, _ in cells), max(y for y, _ in cells)
            c0, c1 = min(x for _, x in cells), max(x for _, x in cells)
            objects.append((r0, c0, set(cells)))
    markers = [(r, c, grid[r][c]) for r in range(h) for c in range(w)
               if grid[r][c] not in (0, 6)]
    tiles = []
    for r0, c0, cells in objects:
        center = (r0 + 1.5, c0 + 1.5)
        _, _, color = min(markers, key=lambda m: abs(m[0] - center[0]) + abs(m[1] - center[1]))
        tile = [[color if (r0 + r, c0 + c) in cells else 0 for c in range(4)]
                for r in range(4)]
        tiles.append((r0, c0, tile))
    row_span = max(r for r, _, _ in tiles) - min(r for r, _, _ in tiles)
    col_span = max(c for _, c, _ in tiles) - min(c for _, c, _ in tiles)
    if col_span >= row_span:
        tiles.sort(key=lambda item: item[1])
        return [sum((tile[r] for _, _, tile in tiles), []) for r in range(4)]
    tiles.sort(key=lambda item: item[0])
    return [row for _, _, tile in tiles for row in tile]
