from collections import deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != 0}
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
        components.append(component)
    anchor = next(component for component in components if grid[next(iter(component))[0]][next(iter(component))[1]] == 1)
    target_top = min(r for r, _ in anchor)
    output = [[0] * width for _ in range(height)]
    for component in components:
        top = min(r for r, _ in component)
        for row, col in component:
            output[target_top + row - top][col] = grid[row][col]
    return output
