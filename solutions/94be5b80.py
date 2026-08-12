from collections import deque


def transform(grid):
    h, w = len(grid), len(grid[0])
    header_row = next(r for r in range(h) if sum(value != 0 for value in grid[r]) >= 3)
    colors = [value for value in grid[header_row] if value != 0]
    components = []
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            color = grid[r][c]
            queue = deque([(r, c)])
            seen.add((r, c))
            component = []
            while queue:
                x, y = queue.popleft()
                component.append((x, y))
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == color and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
            components.append((color, component))
    color, template_cells = max(components, key=lambda item: len(item[1]))
    r0, r1 = min(r for r, _ in template_cells), max(r for r, _ in template_cells)
    c0, c1 = min(c for _, c in template_cells), max(c for _, c in template_cells)
    template = {(r - r0, c - c0) for r, c in template_cells}
    ph = r1 - r0 + 1
    base = r0 - colors.index(color) * ph
    output = [row[:] for row in grid]
    header_end = header_row
    while header_end + 1 < h and grid[header_end + 1] == grid[header_row]:
        header_end += 1
    for r in range(header_row, header_end + 1):
        for c in range(w):
            if output[r][c] in colors:
                output[r][c] = 0
    for index, fill in enumerate(colors):
        top = base + index * ph
        for dr, dc in template:
            r, c = top + dr, c0 + dc
            if 0 <= r < h and 0 <= c < w:
                output[r][c] = fill
    return output
