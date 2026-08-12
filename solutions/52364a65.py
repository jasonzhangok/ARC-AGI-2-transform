def transform(grid):
    h, w = (len(grid), len(grid[0]))
    bg = {}
    for cell_value in (v for row in grid for v in row):
        bg[cell_value] = bg.get(cell_value, 0) + 1
    bg = max(bg, key=bg.get)
    out = [row[:] for row in grid]
    seen = set()
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc] == bg or (sr, sc) in seen:
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
            left = min((c for _, c in cells))
            for r, c in cells:
                if c < left + 2:
                    out[r][c] = bg
    output = out
    return output
