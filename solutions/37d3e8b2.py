def transform(grid):
    height, width = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == 8}
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

        top, bottom = min(r for r, _ in component), max(r for r, _ in component)
        left, right = min(c for _, c in component), max(c for _, c in component)
        zeros = {
            (r, c)
            for r in range(top, bottom + 1)
            for c in range(left, right + 1)
            if grid[r][c] == 0
        }
        holes = 0
        while zeros:
            first = zeros.pop()
            region = {first}
            queue = [first]
            while queue:
                r, c = queue.pop()
                for neighbor in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if neighbor in zeros:
                        zeros.remove(neighbor)
                        region.add(neighbor)
                        queue.append(neighbor)
            if not any(r in (top, bottom) or c in (left, right) for r, c in region):
                holes += 1
        color = {1: 1, 2: 2, 3: 3, 4: 7}[holes]
        for r, c in component:
            result[r][c] = color
    return result
