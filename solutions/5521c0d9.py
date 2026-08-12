def transform(grid):
    h, w = (len(grid), len(grid[0]))
    out = [[0] * w for _ in range(h)]
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
            height = max((r for r, _ in cells)) - min((r for r, _ in cells)) + 1
            for r, c in cells:
                out[r - height][c] = color
    output = out
    return output
