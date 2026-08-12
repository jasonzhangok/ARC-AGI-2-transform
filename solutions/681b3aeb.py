def transform(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    objects = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 or (row, col) in seen:
                continue
            color = grid[row][col]
            queue = [(row, col)]
            seen.add((row, col))
            component = []
            for current_row, current_col in queue:
                component.append((current_row, current_col))
                for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = current_row + row_step, current_col + col_step
                    if (0 <= neighbor[0] < height and 0 <= neighbor[1] < width
                            and neighbor not in seen
                            and grid[neighbor[0]][neighbor[1]] == color):
                        seen.add(neighbor)
                        queue.append(neighbor)
            top = min(r for r, _ in component)
            left = min(c for _, c in component)
            shape = {(r - top, c - left) for r, c in component}
            objects.append((color, shape))

    placements = []
    for color, shape in objects:
        shape_height = max(row for row, _ in shape) + 1
        shape_width = max(col for _, col in shape) + 1
        placements.append([
            {(row + row_offset, col + col_offset) for row, col in shape}
            for row_offset in range(4 - shape_height)
            for col_offset in range(4 - shape_width)
        ])

    combinations = [()]
    for choices in placements:
        combinations = [prefix + (choice,) for prefix in combinations for choice in choices]
    output = None
    for chosen in combinations:
        if len(set().union(*chosen)) == 9 and sum(map(len, chosen)) == 9:
            output = [[0] * 3 for _ in range(3)]
            for (color, _), cells in zip(objects, chosen):
                for row, col in cells:
                    output[row][col] = color
            break
    return output
