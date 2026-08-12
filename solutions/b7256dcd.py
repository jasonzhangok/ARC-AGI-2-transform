def transform(grid):
    h, w = len(grid), len(grid[0])
    background, target = 7, 6
    output = [[background if value not in (background, target) else value for value in row] for row in grid]
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != target or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            component = []
            marker = None
            while stack:
                x, y = stack.pop()
                component.append((x, y))
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < h and 0 <= ny < w):
                        continue
                    value = grid[nx][ny]
                    if value == target and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        stack.append((nx, ny))
                    elif value not in (background, target):
                        marker = value
            color = target if marker is None else marker
            for x, y in component:
                output[x][y] = color
    return output
