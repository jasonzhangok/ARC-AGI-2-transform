def transform(grid):
    height, width = len(grid), len(grid[0])
    nine_count = sum(value == 9 for row in grid for value in row)
    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 2
    }
    candidates = []
    while remaining:
        start = remaining.pop()
        queue = [start]
        component = []
        for row, col in queue:
            component.append((row, col))
            for row_step in (-1, 0, 1):
                for col_step in (-1, 0, 1):
                    neighbor = row + row_step, col + col_step
                    if neighbor in remaining:
                        remaining.remove(neighbor)
                        queue.append(neighbor)
        interior = []
        for row in range(min(r for r, _ in component),
                         max(r for r, _ in component) + 1):
            columns = [col for r, col in component if r == row]
            if len(columns) >= 2:
                interior.extend(
                    (row, col)
                    for col in range(min(columns) + 1, max(columns))
                    if grid[row][col] == 7
                )
        if len(interior) == nine_count:
            candidates.append(interior)

    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if output[row][col] == 9:
                output[row][col] = 7
    for row, col in candidates[0]:
        output[row][col] = 9
    return output
