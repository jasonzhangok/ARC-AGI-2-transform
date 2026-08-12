def transform(grid):
    height = len(grid)
    width = len(grid[0])
    components = []

    for color in set(value for row in grid for value in row) - {0}:
        remaining = {
            (row, col)
            for row in range(height)
            for col in range(width)
            if grid[row][col] == color
        }
        while remaining:
            pending = [remaining.pop()]
            component = set(pending)
            while pending:
                row, col = pending.pop()
                for drow in (-1, 0, 1):
                    for dcol in (-1, 0, 1):
                        neighbor = (row + drow, col + dcol)
                        if neighbor in remaining:
                            remaining.remove(neighbor)
                            component.add(neighbor)
                            pending.append(neighbor)
            components.append((color, component))

    seeds = [
        (color, next(iter(component)))
        for color, component in components
        if len(component) == 1
    ]
    templates = [
        component for _, component in components if len(component) > 1
    ]
    output = [row[:] for row in grid]

    for template in templates:
        top = min(row for row, _ in template)
        bottom = max(row for row, _ in template)
        left = min(col for _, col in template)
        right = max(col for _, col in template)
        box_height = bottom - top + 1
        box_width = right - left + 1
        relative = {(row - top, col - left) for row, col in template}

        for vertical in (-1, 0, 1):
            for horizontal in (-1, 0, 1):
                if vertical == 0 and horizontal == 0:
                    continue
                target = {
                    (
                        top
                        + vertical * box_height
                        + (box_height - 1 - row if vertical else row),
                        left
                        + horizontal * box_width
                        + (box_width - 1 - col if horizontal else col),
                    )
                    for row, col in relative
                }
                for color, seed in seeds:
                    if seed in target:
                        for row, col in target:
                            if 0 <= row < height and 0 <= col < width:
                                output[row][col] = color
    return output
