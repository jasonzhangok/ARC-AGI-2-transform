def transform(grid):
    height = len(grid)
    width = len(grid[0])
    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 6
    }
    output = [row[:] for row in grid]

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

        size = len(component)
        rows = {row for row, _ in component}
        cols = {col for _, col in component}
        box_height = max(rows) - min(rows) + 1
        box_width = max(cols) - min(cols) + 1

        if size == 2:
            color = 9
        elif size == 3 and (box_height == 1 or box_width == 1):
            color = 2
        elif size == 3:
            color = 4
        elif size == 4:
            color = 8
        elif size == 5:
            color = 3
        else:
            color = 5

        for row, col in component:
            output[row][col] = color

    return output
