def _project_lanes(grid, divider, vertical):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    lane_count = height if vertical else width
    axis_size = width if vertical else height

    def value(lane, position):
        return grid[lane][position] if vertical else grid[position][lane]

    def set_value(lane, position, color):
        if vertical:
            output[lane][position] = color
        else:
            output[position][lane] = color

    yellow_positions = [
        position
        for lane in range(lane_count)
        for position in range(axis_size)
        if value(lane, position) == 4
    ]
    direction = 1 if sum(yellow_positions) / len(yellow_positions) < divider else -1

    for lane in range(lane_count):
        yellows = [p for p in range(axis_size) if value(lane, p) == 4]
        if not yellows:
            continue

        for p in yellows:
            set_value(lane, p, 3)
        nearest = max(yellows) if direction == 1 else min(yellows)
        for p in range(nearest + direction, divider, direction):
            set_value(lane, p, 4)

        reds = [p for p in range(axis_size) if value(lane, p) == 2]
        shift = (
            axis_size - 1 - max(reds)
            if direction == 1
            else -min(reds)
        )
        boundary = axis_size if direction == 1 else -1
        for p in range(divider + direction, boundary, direction):
            set_value(lane, p, 8)
        for p in reds:
            set_value(lane, p + shift, 2)

    return output


def transform(grid):
    height, width = len(grid), len(grid[0])
    full_row = next(
        (r for r in range(height) if all(grid[r][c] == 8 for c in range(width))),
        None,
    )
    if full_row is not None:
        return _project_lanes(grid, full_row, vertical=False)

    full_column = next(
        c for c in range(width) if all(grid[r][c] == 8 for r in range(height))
    )
    return _project_lanes(grid, full_column, vertical=True)
