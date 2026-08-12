def transform(grid):
    height = len(grid)
    width = len(grid[0])
    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 1
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
        top = min(row for row, _ in component) - 1
        bottom = max(row for row, _ in component) + 1
        left = min(col for _, col in component) - 1
        right = max(col for _, col in component) + 1
        outside = {(top, left)}
        pending = [(top, left)]
        while pending:
            row, col = pending.pop()
            for neighbor in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                nr, nc = neighbor
                if (
                    top <= nr <= bottom
                    and left <= nc <= right
                    and neighbor not in component
                    and neighbor not in outside
                ):
                    outside.add(neighbor)
                    pending.append(neighbor)

        has_hole = any(
            (row, col) not in component and (row, col) not in outside
            for row in range(top, bottom + 1)
            for col in range(left, right + 1)
        )
        if has_hole:
            for row, col in component:
                output[row][col] = 8
    return output
