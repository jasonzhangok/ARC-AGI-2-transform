def transform(grid):
    height, width = len(grid), len(grid[0])

    def components(color):
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
        return found

    targets = components(2)
    for path in components(8):
        touches = 0
        for target in targets:
            if any(
                max(abs(r - tr), abs(c - tc)) <= 1
                for r, c in path
                for tr, tc in target
            ):
                touches += 1
        if touches >= 2:
            return [[8]]
    return [[0]]
