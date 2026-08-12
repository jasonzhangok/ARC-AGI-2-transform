from collections import Counter, defaultdict, deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != background}
    component_counts = defaultdict(int)
    while remaining:
        start = remaining.pop()
        color = grid[start[0]][start[1]]
        queue = deque([start])
        while queue:
            r, c = queue.popleft()
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining and grid[point[0]][point[1]] == color:
                    remaining.remove(point)
                    queue.append(point)
        component_counts[color] += 1
    ordered = sorted(component_counts.items(), key=lambda item: (-item[1], item[0]))
    size = max(component_counts.values())
    return [[background] * (size - count) + [color] * count for color, count in ordered]
