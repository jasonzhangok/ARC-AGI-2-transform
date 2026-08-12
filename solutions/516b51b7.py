def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    seen = set()
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc] != 1 or (sr, sc) in seen:
                continue
            stack = [(sr, sc)]; seen.add((sr, sc)); cells = []
            while stack:
                r, c = stack.pop(); cells.append((r, c))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 1 and (nr, nc) not in seen:
                        seen.add((nr, nc)); stack.append((nr, nc))
            r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
            c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
            palette = (1, 2, 3, 2)
            for r, c in cells:
                d = min(r-r0, r1-r, c-c0, c1-c)
                out[r][c] = palette[d % 4]
    return out
