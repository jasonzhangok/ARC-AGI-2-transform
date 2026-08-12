def transform(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [row[:] for row in grid]

    colored = {
        (r, c)
        for r in range(rows)
        for c in range(cols)
        if grid[r][c] not in (0, 8)
    }
    first = next(iter(colored))
    paint = grid[first[0]][first[1]]

    remaining = set(colored)
    components = []
    while remaining:
        start = remaining.pop()
        component = {start}
        queue = [start]
        for r, c in queue:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = (r + dr, c + dc)
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    queue.append(neighbor)
        components.append(component)

    objects = [
        (r, c)
        for r in range(rows)
        for c in range(cols)
        if grid[r][c] != 0
    ]
    top = min(r for r, c in objects)
    bottom = max(r for r, c in objects)
    left = min(c for r, c in objects)
    right = max(c for r, c in objects)

    distances = []
    for component in components[:2]:
        distance = {cell: 0 for cell in component}
        queue = list(component)
        for r, c in queue:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = (r + dr, c + dc)
                nr, nc = neighbor
                if (top <= nr <= bottom and left <= nc <= right
                        and grid[nr][nc] != 8 and neighbor not in distance):
                    distance[neighbor] = distance[(r, c)] + 1
                    queue.append(neighbor)
        distances.append(distance)

    shortest = min(distances[0][cell] for cell in components[1])
    selected = set(colored)
    for cell in distances[0]:
        if (cell in distances[1]
                and distances[0][cell] + distances[1][cell] == shortest):
            selected.add(cell)

    span = 0
    for component in components:
        height = max(r for r, c in component) - min(r for r, c in component) + 1
        width = max(c for r, c in component) - min(c for r, c in component) + 1
        span = max(span, height, width)

    changed = True
    while changed:
        additions = set()
        for r, c in selected:
            lo = c
            while lo > left and grid[r][lo - 1] != 8:
                lo -= 1
            hi = c
            while hi < right and grid[r][hi + 1] != 8:
                hi += 1
            length = hi - lo + 1
            bounded_left = lo > left or (lo == 0 and length <= span)
            bounded_right = hi < right or (hi == cols - 1 and length <= span)
            if bounded_left and bounded_right:
                additions.update((r, x) for x in range(lo, hi + 1))

            lo = r
            while lo > top and grid[lo - 1][c] != 8:
                lo -= 1
            hi = r
            while hi < bottom and grid[hi + 1][c] != 8:
                hi += 1
            length = hi - lo + 1
            bounded_top = lo > top or (lo == 0 and length <= span)
            bounded_bottom = hi < bottom or (hi == rows - 1 and length <= span)
            if bounded_top and bounded_bottom:
                additions.update((x, c) for x in range(lo, hi + 1))

        changed = not additions.issubset(selected)
        selected.update(additions)

    for r, c in selected:
        result[r][c] = paint
    return result
