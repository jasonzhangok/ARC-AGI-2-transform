def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 5 or (r, c) in seen:
                continue
            stack, cells = [(r, c)], []
            seen.add((r, c))
            while stack:
                x, y = stack.pop()
                cells.append((x, y))
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 5 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            seeds = [grid[x][y] for x, y in cells if grid[x][y] != 0]
            if seeds:
                for x, y in cells:
                    if grid[x][y] == 0:
                        output[x][y] = seeds[0]
    return output
