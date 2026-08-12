def transform(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    count = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 8 or (r, c) in seen:
                continue
            count += 1
            stack = [(r, c)]
            seen.add((r, c))
            while stack:
                x, y = stack.pop()
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 8 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        stack.append((nx, ny))
    output = [[8 if r == c else 0 for c in range(count)] for r in range(count)]
    return output
