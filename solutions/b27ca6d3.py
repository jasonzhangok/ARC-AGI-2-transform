def transform(grid):
    height = len(grid)
    width = len(grid[0])
    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 2
    }
    components = []
    while remaining:
        pending = [remaining.pop()]
        component = set(pending)
        while pending:
            row, col = pending.pop()
            for neighbor in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    pending.append(neighbor)
        components.append(component)

    output = [row[:] for row in grid]
    for component in components:
        if len(component) != 2:
            continue
        top = max(0, min(row for row, _ in component) - 1)
        bottom = min(height - 1, max(row for row, _ in component) + 1)
        left = max(0, min(col for _, col in component) - 1)
        right = min(width - 1, max(col for _, col in component) + 1)
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                if row in (top, bottom) or col in (left, right):
                    if output[row][col] == 0:
                        output[row][col] = 3
    return output
