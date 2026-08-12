def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    components = []

    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == 0 or (start_row, start_col) in seen:
                continue
            component = []
            queue = [(start_row, start_col)]
            seen.add((start_row, start_col))
            for row, col in queue:
                component.append((row, col))
                for drow, dcol in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row, next_col = row + drow, col + dcol
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and grid[next_row][next_col] != 0
                        and (next_row, next_col) not in seen
                    ):
                        seen.add((next_row, next_col))
                        queue.append((next_row, next_col))
            components.append(component)

    least_marked = min(
        components,
        key=lambda component: sum(grid[row][col] == 9 for row, col in component),
    )
    for row, col in least_marked:
        output[row][col] = 0
    return output
