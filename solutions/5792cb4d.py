def transform(grid):
    h, w = (len(grid), len(grid[0]))
    bg = {}
    for cell_value in (v for row in grid for v in row):
        bg[cell_value] = bg.get(cell_value, 0) + 1
    bg = max(bg, key=bg.get)
    out = [row[:] for row in grid]
    points = {(r, c) for r in range(h) for c in range(w) if grid[r][c] != bg}
    seen = set()
    while points - seen:
        start = next(iter(points - seen))
        q = list([start])
        seen.add(start)
        comp = []
        while q:
            p = q.pop(0)
            comp.append(p)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n = (p[0] + dr, p[1] + dc)
                if n in points and n not in seen:
                    seen.add(n)
                    q.append(n)
        s = set(comp)
        ends = [p for p in comp if sum(((p[0] + dr, p[1] + dc) in s for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))) == 1]
        path = [ends[0]]
        prev = None
        while len(path) < len(comp):
            cur = path[-1]
            nxt = next((p for p in ((cur[0] + 1, cur[1]), (cur[0] - 1, cur[1]), (cur[0], cur[1] + 1), (cur[0], cur[1] - 1)) if p in s and p != prev and (p not in path)))
            prev = cur
            path.append(nxt)
        values = [grid[r][c] for r, c in path][::-1]
        for (r, c), v in zip(path, values):
            out[r][c] = v
    output = out
    return output
