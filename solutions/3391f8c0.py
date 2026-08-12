from collections import defaultdict, deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    colors = sorted({value for row in grid for value in row if value != 0})
    by_color = defaultdict(list)
    for color in colors:
        remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == color}
        while remaining:
            start = remaining.pop()
            component = {start}
            queue = deque([start])
            while queue:
                r, c = queue.popleft()
                for point in ((r + dr, c + dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)):
                    if point in remaining:
                        remaining.remove(point)
                        component.add(point)
                        queue.append(point)
            by_color[color].append(component)
    shapes = {}
    for color in colors:
        component = by_color[color][0]
        top = min(r for r, _ in component)
        left = min(c for _, c in component)
        shapes[color] = {(r - top, c - left) for r, c in component}
    first, second = colors
    result = [[0] * width for _ in range(height)]
    for color, replacement in ((first, second), (second, first)):
        for component in by_color[color]:
            top = min(r for r, _ in component)
            left = min(c for _, c in component)
            for dr, dc in shapes[replacement]:
                result[top + dr][left + dc] = replacement
    return result
