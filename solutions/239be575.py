def transform(grid):
    height, width = len(grid), len(grid[0])

    components_by_color = {}
    for color in (2, 8):
        remaining = {
            (r, c)
            for r in range(height)
            for c in range(width)
            if grid[r][c] == color
        }
        found = []
        while remaining:
            start = remaining.pop()
            component = {start}
            stack = [start]
            while stack:
                r, c = stack.pop()
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        neighbor = (r + dr, c + dc)
                        if neighbor in remaining:
                            remaining.remove(neighbor)
                            component.add(neighbor)
                            stack.append(neighbor)
            found.append(component)
        components_by_color[color] = found

    targets = components_by_color[2]
    output = [[0]]
    for path in components_by_color[8]:
        touches = 0
        for target in targets:
            if any(
                max(abs(r - tr), abs(c - tc)) <= 1
                for r, c in path
                for tr, tc in target
            ):
                touches += 1
        if touches >= 2:
            output = [[8]]
            break
    return output
