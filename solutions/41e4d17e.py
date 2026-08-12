def transform(grid):
    height, width = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == 1}
    components = []
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
        components.append(component)
    for component in components:
        center_row = (min(r for r, _ in component) + max(r for r, _ in component)) // 2
        center_column = (min(c for _, c in component) + max(c for _, c in component)) // 2
        for c in range(width):
            if result[center_row][c] == 8:
                result[center_row][c] = 6
        for r in range(height):
            if result[r][center_column] == 8:
                result[r][center_column] = 6
    output = result
    return output
