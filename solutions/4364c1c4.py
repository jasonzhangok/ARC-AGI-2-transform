from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    components = []
    for color in {value for row in grid for value in row if value != background}:
        remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == color}
        while remaining:
            start = remaining.pop()
            component = {start}
            stack = [start]
            while stack:
                r, c = stack.pop()
                for neighbor in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if neighbor in remaining:
                        remaining.remove(neighbor)
                        component.add(neighbor)
                        stack.append(neighbor)
            components.append((min(r for r, _ in component), color, component))
    components.sort()
    result = [row[:] for row in grid]
    for _, _, component in components:
        for r, c in component:
            result[r][c] = background
    for index, (_, color, component) in enumerate(components):
        shift = -1 if index % 2 == 0 else 1
        for r, c in component:
            result[r][c + shift] = color
    return result
