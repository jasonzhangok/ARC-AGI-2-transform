def transform(grid):
    height = len(grid)
    width = len(grid[0])
    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 0
    }
    rectangles = []
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
        rectangles.append(
            (
                min(row for row, _ in component),
                max(row for row, _ in component),
                min(col for _, col in component),
                max(col for _, col in component),
            )
        )

    output = [row[:] for row in grid]
    destinations = []
    for top, bottom, left, right in rectangles:
        rect_height = bottom - top + 1
        rect_width = right - left + 1
        if top == 0:
            for row in range(height):
                for col in range(left, right + 1):
                    output[row][col] = 7
            destinations.append((height - rect_height, height - 1, left, right))
        elif bottom == height - 1:
            for row in range(height):
                for col in range(left, right + 1):
                    output[row][col] = 7
            destinations.append((0, rect_height - 1, left, right))
        elif left == 0:
            for row in range(top, bottom + 1):
                for col in range(width):
                    output[row][col] = 7
            destinations.append((top, bottom, width - rect_width, width - 1))
        else:
            for row in range(top, bottom + 1):
                for col in range(width):
                    output[row][col] = 7
            destinations.append((top, bottom, 0, rect_width - 1))

    for top, bottom, left, right in destinations:
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                output[row][col] = 0
    return output
