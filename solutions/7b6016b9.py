def transform(grid):
    h, w = len(grid), len(grid[0])
    line = next(v for row in grid for v in row if v)
    out = [[line if v == line else 2 for v in row] for row in grid]
    seen = set()
    stack = [(r, c) for r in range(h) for c in range(w)
             if (r in (0, h - 1) or c in (0, w - 1)) and grid[r][c] == 0]
    seen.update(stack)
    while stack:
        r, c = stack.pop()
        out[r][c] = 3
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            p = r + dr, c + dc
            if 0 <= p[0] < h and 0 <= p[1] < w and p not in seen and grid[p[0]][p[1]] == 0:
                seen.add(p)
                stack.append(p)
    return out
