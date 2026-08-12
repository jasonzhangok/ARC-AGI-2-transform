def transform(grid):
    height, width = (len(grid), len(grid[0]))
    result = [row[:] for row in grid]
    background = {}
    for cell_value in (value for row in grid for value in row):
        background[cell_value] = background.get(cell_value, 0) + 1
    background = max(background, key=background.get)
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == 1}
    components = []
    while remaining:
        start = remaining.pop()
        component = {start}
        queue = list([start])
        while queue:
            r, c = queue.pop(0)
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining:
                    remaining.remove(point)
                    component.add(point)
                    queue.append(point)
        components.append(component)
    for component in components:
        top = min((r for r, _ in component))
        bottom = max((r for r, _ in component))
        left = min((c for _, c in component))
        right = max((c for _, c in component))
        openings = []
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                if grid[r][c] == background:
                    result[r][c] = 2
                    if r == top:
                        openings.append((r, c, -1, 0))
                    elif r == bottom:
                        openings.append((r, c, 1, 0))
                    elif c == left:
                        openings.append((r, c, 0, -1))
                    elif c == right:
                        openings.append((r, c, 0, 1))
        for r, c, dr, dc in openings:
            r += dr
            c += dc
            while 0 <= r < height and 0 <= c < width:
                if result[r][c] == background:
                    result[r][c] = 2
                r += dr
                c += dc
    output = result
    return output
