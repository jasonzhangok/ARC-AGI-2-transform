def transform(grid):
    h, w = (len(grid), len(grid[0]))
    out = [row[:] for row in grid]
    seen = set()
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc] == 0 or (sr, sc) in seen:
                continue
            q = list([(sr, sc)])
            seen.add((sr, sc))
            cells = []
            while q:
                r, c = q.pop(0)
                cells.append((r, c))
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < h and 0 <= nc < w and (grid[nr][nc] != 0) and ((nr, nc) not in seen):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            if sum((grid[r][c] == 8 for r, c in cells)) > 1:
                for r, c in cells:
                    out[r][c] = 0
    output = out
    return output
