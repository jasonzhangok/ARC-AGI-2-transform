def transform(grid):
    height, width = len(grid), len(grid[0])
    full_row = next(
        (r for r in range(height) if all(grid[r][c] == 8 for c in range(width))),
        None,
    )
    vertical = full_row is None
    divider = (next(c for c in range(width) if all(grid[r][c] == 8 for r in range(height)))
               if vertical else full_row)
    output = [row[:] for row in grid]
    lane_count = height if vertical else width
    axis_size = width if vertical else height
    yellow_positions = [position for lane in range(lane_count) for position in range(axis_size)
                        if (grid[lane][position] if vertical else grid[position][lane]) == 4]
    direction = 1 if sum(yellow_positions) / len(yellow_positions) < divider else -1
    for lane in range(lane_count):
        yellows = [position for position in range(axis_size)
                   if (grid[lane][position] if vertical else grid[position][lane]) == 4]
        if not yellows:
            continue
        for position in yellows:
            if vertical: output[lane][position] = 3
            else: output[position][lane] = 3
        nearest = max(yellows) if direction == 1 else min(yellows)
        for position in range(nearest + direction, divider, direction):
            if vertical: output[lane][position] = 4
            else: output[position][lane] = 4
        reds = [position for position in range(axis_size)
                if (grid[lane][position] if vertical else grid[position][lane]) == 2]
        shift = axis_size - 1 - max(reds) if direction == 1 else -min(reds)
        boundary = axis_size if direction == 1 else -1
        for position in range(divider + direction, boundary, direction):
            if vertical: output[lane][position] = 8
            else: output[position][lane] = 8
        for position in reds:
            if vertical: output[lane][position + shift] = 2
            else: output[position + shift][lane] = 2
    return output
