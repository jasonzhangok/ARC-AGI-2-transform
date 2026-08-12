def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    from collections import deque
    seen, boxes = set(), []
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc] != 3 or (sr, sc) in seen:
                continue
            q, comp = deque([(sr, sc)]), []
            seen.add((sr, sc))
            while q:
                r, c = q.popleft()
                comp.append((r, c))
                for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 3 and (nr,nc) not in seen:
                        seen.add((nr,nc)); q.append((nr,nc))
            if len(comp) >= 10:
                boxes.append((min(r for r,_ in comp), max(r for r,_ in comp),
                              min(c for _,c in comp), max(c for _,c in comp)))
    reds = [(r, c) for r in range(h) for c in range(w)
            if grid[r][c] == 2 and any(r0 <= r <= r1 and c0 <= c <= c1
                                      for r0,r1,c0,c1 in boxes)]
    centers = set(reds)
    for r, c in reds:
        for x in range(max(0, r - 1), min(h, r + 2)):
            for y in range(max(0, c - 1), min(w, c + 2)):
                if (x, y) not in centers:
                    out[x][y] = 1
    return out
