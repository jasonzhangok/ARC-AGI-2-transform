from collections import deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    code_cells = {(r, c) for r in range(height) for c in range(width) if grid[r][c] not in (0, 5)}
    code_top = min(r for r, _ in code_cells)
    code_bottom = max(r for r, _ in code_cells)
    code_left = min(c for _, c in code_cells)
    code_right = max(c for _, c in code_cells)
    code = [row[code_left:code_right + 1] for row in grid[code_top:code_bottom + 1]]
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == 5}
    components = []
    while remaining:
        start = remaining.pop()
        component = {start}
        queue = deque([start])
        while queue:
            r, c = queue.popleft()
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining:
                    remaining.remove(point)
                    component.add(point)
                    queue.append(point)
        components.append(component)
    components.sort(key=lambda comp: (min(r for r, _ in comp), min(c for _, c in comp)))
    result = [row[:] for row in grid]
    for component, color in zip(components, (value for row in code for value in row)):
        for r, c in component:
            result[r][c] = color
    return result
