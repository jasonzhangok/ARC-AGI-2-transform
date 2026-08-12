def transform(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    count = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 5 or (r, c) in seen:
                continue
            count += 1
            stack = [(r, c)]
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny, nx = y + dy, x + dx
                    if (0 <= ny < h and 0 <= nx < w and grid[ny][nx] == 5
                            and (ny, nx) not in seen):
                        seen.add((ny, nx))
                        stack.append((ny, nx))
    output = [[0] for _ in range(count + 1)]
    return output
