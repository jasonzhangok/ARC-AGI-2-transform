from collections import deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    best = set()
    for color in {value for row in grid for value in row if value != 0}:
        remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == color}
        while remaining:
            start = remaining.pop()
            queue = deque([start])
            component = {start}
            while queue:
                row, col = queue.popleft()
                for point in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if point in remaining:
                        remaining.remove(point)
                        component.add(point)
                        queue.append(point)
            if len(component) > len(best):
                best = component
    top, bottom = min(r for r, _ in best), max(r for r, _ in best)
    left, right = min(c for _, c in best), max(c for _, c in best)
    color = grid[next(iter(best))[0]][next(iter(best))[1]]
    return [
        [color if (r, c) in best else 0 for c in range(left, right + 1)]
        for r in range(top, bottom + 1)
    ]
