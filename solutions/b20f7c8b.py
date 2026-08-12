def transform(grid):
    height = len(grid)
    width = len(grid[0])
    left_eights = sum(grid[row][col] == 8 for row in range(height) for col in range(6))
    right_eights = sum(
        grid[row][col] == 8
        for row in range(height)
        for col in range(width - 6, width)
    )
    if left_eights > right_eights:
        side_cols = set(range(6))
        main_cols = set(range(6, width))
    else:
        side_cols = set(range(width - 6, width))
        main_cols = set(range(width - 6))

    legend = {}
    for color in {
        grid[row][col]
        for row in range(height)
        for col in side_cols
        if grid[row][col] != 8
    }:
        cells = {
            (row, col)
            for row in range(height)
            for col in side_cols
            if grid[row][col] == color
        }
        top = min(row for row, _ in cells)
        left = min(col for _, col in cells)
        legend[color] = {(row - top, col - left) for row, col in cells}

    def canonical(shape):
        variants = []
        current = set(shape)
        for _ in range(4):
            for reflected in (current, {(row, 2 - col) for row, col in current}):
                top = min(row for row, _ in reflected)
                left = min(col for _, col in reflected)
                variants.append(tuple(sorted((row - top, col - left) for row, col in reflected)))
            current = {(col, 2 - row) for row, col in current}
        return min(variants)

    by_shape = {canonical(shape): color for color, shape in legend.items()}

    remaining = {
        (row, col)
        for row in range(height)
        for col in main_cols
        if grid[row][col] != 0
    }
    panels = []
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
        if len(component) == 25:
            panels.append(component)

    output = [row[:] for row in grid]
    for panel in panels:
        top = min(row for row, _ in panel)
        left = min(col for _, col in panel)
        colors = {grid[row][col] for row, col in panel}
        if len(colors) == 1:
            color = next(iter(colors))
            for row in range(top, top + 5):
                for col in range(left, left + 5):
                    output[row][col] = 2
            for row, col in legend[color]:
                output[top + 1 + row][left + 1 + col] = 1
        else:
            shape = {
                (row - top - 1, col - left - 1)
                for row, col in panel
                if grid[row][col] == 1
            }
            color = by_shape[canonical(shape)]
            for row in range(top, top + 5):
                for col in range(left, left + 5):
                    output[row][col] = color
    return output
