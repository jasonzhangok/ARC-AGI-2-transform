def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)

    seen = set()
    components = []
    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == background or (start_row, start_col) in seen:
                continue
            component = []
            queue = [(start_row, start_col)]
            seen.add((start_row, start_col))
            for row, col in queue:
                component.append((row, col))
                for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = (row + delta_row, col + delta_col)
                    if (
                        0 <= neighbor[0] < height
                        and 0 <= neighbor[1] < width
                        and grid[neighbor[0]][neighbor[1]] != background
                        and neighbor not in seen
                    ):
                        seen.add(neighbor)
                        queue.append(neighbor)
            components.append(component)

    moves = []
    for component in components:
        if len(component) >= 4:
            bottom = max(row for row, col in component)
            moves.append((component, height - 1 - bottom))

    output = [row[:] for row in grid]
    for component, shift in moves:
        for row, col in component:
            output[row][col] = background
    for component, shift in moves:
        for row, col in component:
            output[row + shift][col] = grid[row][col]
    return output
