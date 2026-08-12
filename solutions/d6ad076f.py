def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen, boxes = set(), []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            color = grid[r][c]
            stack, cells = [(r, c)], []
            seen.add((r, c))
            while stack:
                x, y = stack.pop()
                cells.append((x, y))
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == color and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            boxes.append((min(x for x, _ in cells), max(x for x, _ in cells), min(y for _, y in cells), max(y for _, y in cells)))
    a, b = boxes
    if a[1] < b[0] or b[1] < a[0]:
        if b[1] < a[0]:
            a, b = b, a
        for r in range(a[1] + 1, b[0]):
            for c in range(max(a[2], b[2]) + 1, min(a[3], b[3])):
                output[r][c] = 8
    else:
        if b[3] < a[2]:
            a, b = b, a
        for r in range(max(a[0], b[0]) + 1, min(a[1], b[1])):
            for c in range(a[3] + 1, b[2]):
                output[r][c] = 8
    return output
