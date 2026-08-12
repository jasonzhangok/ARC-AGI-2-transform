def transform(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    components = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            color = grid[r][c]
            cells = []
            stack = [(r, c)]
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                cells.append((y, x))
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny, nx = y + dy, x + dx
                    if (0 <= ny < h and 0 <= nx < w and grid[ny][nx] == color
                            and (ny, nx) not in seen):
                        seen.add((ny, nx))
                        stack.append((ny, nx))
            components.append(cells)
    frame = max(components, key=len)
    frame_color = grid[frame[0][0]][frame[0][1]]
    output_color = next(value for row in grid for value in row
                        if value not in (0, frame_color))
    r0, r1 = min(r for r, _ in frame), max(r for r, _ in frame)
    c0, c1 = min(c for _, c in frame), max(c for _, c in frame)
    return [[output_color if grid[r][c] == frame_color else grid[r][c]
             for c in range(c0, c1 + 1)] for r in range(r0, r1 + 1)]
