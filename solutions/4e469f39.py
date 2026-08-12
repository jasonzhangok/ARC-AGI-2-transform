def transform(grid):
    h, w = (len(grid), len(grid[0]))
    out = [row[:] for row in grid]
    seen = set()
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc] != 5 or (sr, sc) in seen:
                continue
            q = list([(sr, sc)])
            seen.add((sr, sc))
            cells = []
            while q:
                r, c = q.pop(0)
                cells.append((r, c))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = (r + dr, c + dc)
                    if 0 <= nr < h and 0 <= nc < w and (grid[nr][nc] == 5) and ((nr, nc) not in seen):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            r0, r1 = (min((r for r, _ in cells)), max((r for r, _ in cells)))
            c0, c1 = (min((c for _, c in cells)), max((c for _, c in cells)))
            gap = next((c for c in range(c0, c1 + 1) if grid[r0][c] == 0))
            for r in range(r0 + 1, r1):
                for c in range(c0 + 1, c1):
                    out[r][c] = 2
            out[r0][gap] = 2
            out[r0 - 1][gap] = 2
            if gap - c0 < c1 - gap:
                for c in range(gap, w):
                    out[r0 - 1][c] = 2
            else:
                for c in range(0, gap + 1):
                    out[r0 - 1][c] = 2
    output = out
    return output
