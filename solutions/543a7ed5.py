def transform(grid):
    h, w = (len(grid), len(grid[0]))
    out = [row[:] for row in grid]
    seen = set()
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc] != 6 or (sr, sc) in seen:
                continue
            q = list([(sr, sc)])
            seen.add((sr, sc))
            cells = []
            while q:
                r, c = q.pop(0)
                cells.append((r, c))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = (r + dr, c + dc)
                    if 0 <= nr < h and 0 <= nc < w and (grid[nr][nc] == 6) and ((nr, nc) not in seen):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            r0, r1 = (min((r for r, _ in cells)), max((r for r, _ in cells)))
            c0, c1 = (min((c for _, c in cells)), max((c for _, c in cells)))
            for r in range(max(0, r0 - 1), min(h, r1 + 2)):
                for c in range(max(0, c0 - 1), min(w, c1 + 2)):
                    if r0 <= r <= r1 and c0 <= c <= c1:
                        if out[r][c] == 8:
                            out[r][c] = 4
                    elif out[r][c] == 8:
                        out[r][c] = 3
    output = out
    return output
