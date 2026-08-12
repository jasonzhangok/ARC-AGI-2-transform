def transform(grid):
    h, w = len(grid), len(grid[0])
    start = next(r for r, row in enumerate(grid)
                 if r > 0 and len(set(row)) == 1 and row[0] != 0)
    background = grid[start][0]
    legends = [(r, c, grid[r][c]) for r in range(start) for c in range(w)
               if grid[r][c] != 0]
    legend_colors = {value for _, _, value in legends}
    out = [row[:] for row in grid]
    for r in range(start, h):
        for c in range(w):
            if out[r][c] != background and out[r][c] not in legend_colors:
                out[r][c] = background
    for lr, lc, color in legends:
        seen = set()
        count = 0
        for r in range(start, h):
            for c in range(w):
                if grid[r][c] != color or (r, c) in seen:
                    continue
                count += 1
                stack = [(r, c)]
                seen.add((r, c))
                while stack:
                    y, x = stack.pop()
                    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ny, nx = y + dy, x + dx
                        if (start <= ny < h and 0 <= nx < w
                                and grid[ny][nx] == color and (ny, nx) not in seen):
                            seen.add((ny, nx))
                            stack.append((ny, nx))
        for c in range(lc, w):
            out[lr][c] = color if c < lc + count else 0
    return out
