def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 5 or (r, c) in seen:
                continue
            stack, component = [(r, c)], []
            seen.add((r, c))
            while stack:
                x, y = stack.pop()
                component.append((x, y))
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 5 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            r0, r1 = min(x for x, _ in component), max(x for x, _ in component)
            c0, c1 = min(y for _, y in component), max(y for _, y in component)
            for x, y in component:
                on_vertical = y in (c0, c1)
                on_horizontal = x in (r0, r1)
                output[x][y] = 1 if on_vertical and on_horizontal else 4 if on_vertical or on_horizontal else 2
    return output
