def transform(grid):
    h, w = (len(grid), len(grid[0]))
    out = [row[:] for row in grid]
    seen = set()
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc] == 8 or (sr, sc) in seen:
                continue
            q, comp = (list([(sr, sc)]), [])
            seen.add((sr, sc))
            while q:
                r, c = q.pop(0)
                comp.append((r, c))
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < h and 0 <= nc < w and (grid[nr][nc] != 8) and ((nr, nc) not in seen):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            r0, r1 = (min((r for r, _ in comp)), max((r for r, _ in comp)))
            c0, c1 = (min((c for _, c in comp)), max((c for _, c in comp)))
            ink = [(r, c) for r, c in comp if grid[r][c] != 0]
            if not ink:
                continue
            ir0, ir1 = (min((r for r, _ in ink)), max((r for r, _ in ink)))
            ic0, ic1 = (min((c for _, c in ink)), max((c for _, c in ink)))
            ph, pw = (ir1 - ir0 + 1, ic1 - ic0 + 1)
            for r in range(r0, r1 + 1):
                for c in range(c0, c1 + 1):
                    out[r][c] = grid[ir0 + (r - ir0) % ph][ic0 + (c - ic0) % pw]
    output = out
    return output
