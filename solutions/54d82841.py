def transform(grid):
    h, w = (len(grid), len(grid[0]))
    out = [row[:] for row in grid]
    seen = set()
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc] == 0 or (sr, sc) in seen:
                continue
            color = grid[sr][sc]
            q = list([(sr, sc)])
            seen.add((sr, sc))
            cells = []
            while q:
                r, c = q.pop(0)
                cells.append((r, c))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = (r + dr, c + dc)
                    if 0 <= nr < h and 0 <= nc < w and (grid[nr][nc] == color) and ((nr, nc) not in seen):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            c0, c1 = (min((c for _, c in cells)), max((c for _, c in cells)))
            out[h - 1][(c0 + c1) // 2] = 4
    output = out
    return output
