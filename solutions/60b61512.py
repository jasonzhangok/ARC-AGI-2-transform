def transform(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 4 or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            cells = []
            while stack:
                x, y = stack.pop(); cells.append((x, y))
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    q = (x+dx, y+dy)
                    if 0 <= q[0] < h and 0 <= q[1] < w and q not in seen and grid[q[0]][q[1]] == 4:
                        seen.add(q); stack.append(q)
            rs = [x for x, _ in cells]; cs = [y for _, y in cells]
            for x in range(min(rs), max(rs)+1):
                for y in range(min(cs), max(cs)+1):
                    if out[x][y] == 0: out[x][y] = 7
    return out
