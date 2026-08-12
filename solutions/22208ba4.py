from collections import Counter, deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != background}
    components = []
    while remaining:
        start = remaining.pop()
        color = grid[start[0]][start[1]]
        queue = deque([start])
        component = {start}
        while queue:
            row, col = queue.popleft()
            for point in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if point in remaining and grid[point[0]][point[1]] == color:
                    remaining.remove(point)
                    component.add(point)
                    queue.append(point)
        components.append((color, component))
    frequencies = Counter(color for color, _ in components)
    output = [row[:] for row in grid]
    for color, component in components:
        if frequencies[color] < 2:
            continue
        top, bottom = min(r for r, _ in component), max(r for r, _ in component)
        left, right = min(c for _, c in component), max(c for _, c in component)
        size = bottom - top + 1
        dr = size if top == 0 else -size
        dc = size if left == 0 else -size
        for row, col in component:
            output[row][col] = background
        for row, col in component:
            output[row + dr][col + dc] = color
    return output
