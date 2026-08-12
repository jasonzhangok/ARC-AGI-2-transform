def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 1
    }

    while remaining:
        start = remaining.pop()
        queue = [start]
        component = []
        for row, col in queue:
            component.append((row, col))
            for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = row + row_step, col + col_step
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    queue.append(neighbor)
        top = min(row for row, _ in component)
        bottom = max(row for row, _ in component)
        left = min(col for _, col in component)
        right = max(col for _, col in component)
        seed = next(
            grid[row][col]
            for row in range(top + 1, bottom)
            for col in range(left + 1, right)
            if grid[row][col] not in (0, 1)
        )
        for row in range(top + 1, bottom):
            for col in range(left + 1, right):
                output[row][col] = seed
        gap = next(col for col in range(left, right + 1) if grid[top][col] == 0)
        output[top][gap] = seed
        for col in range(left, right + 1):
            output[top - 1][col] = seed
    return output
