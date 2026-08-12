def transform(grid):
    height = len(grid)
    width = len(grid[0])
    remaining = {
        (row, col)
        for row in range(height - 1)
        for col in range(width)
        if grid[row][col] != 7
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
                if neighbor in remaining and grid[neighbor[0]][neighbor[1]] == grid[row][col]:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    pending.append(neighbor)
        components.append(component)

    output = [row[:] for row in grid]
    for component in components:
        for row, col in component:
            output[row][col] = 7
    for component in components:
        shift = len(component)
        for row, col in component:
            output[row - shift][col] = grid[row][col]
    return output
