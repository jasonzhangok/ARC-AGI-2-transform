def transform(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    components = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 2 or (r, c) in seen:
                continue
            cells = []
            stack = [(r, c)]
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                cells.append((y, x))
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny, nx = y + dy, x + dx
                    if (0 <= ny < h and 0 <= nx < w and grid[ny][nx] == 2
                            and (ny, nx) not in seen):
                        seen.add((ny, nx))
                        stack.append((ny, nx))
            components.append(cells)
    boxes = [(min(r for r, _ in cells), max(r for r, _ in cells),
              min(c for _, c in cells), max(c for _, c in cells))
             for cells in components]
    out = [row[:] for row in grid]
    for i, left in enumerate(boxes):
        for j, right in enumerate(boxes):
            if left[3] >= right[2]:
                continue
            top, bottom = max(left[0], right[0]), min(left[1], right[1])
            if top > bottom:
                continue
            blocked = any(
                k not in (i, j) and left[3] < box[2] and box[3] < right[2]
                and max(top, box[0]) <= min(bottom, box[1])
                for k, box in enumerate(boxes)
            )
            if blocked:
                continue
            for r in range(top, bottom + 1):
                if (any(y == r for y, _ in components[i])
                        and any(y == r for y, _ in components[j])):
                    for c in range(left[3] + 1, right[2]):
                        out[r][c] = 9
    output = out
    return output
