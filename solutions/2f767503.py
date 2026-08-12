def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    fives = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 5
    ]
    marker = next(
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 9
    )
    center = fives[0]
    center_distance = abs(center[0] - marker[0]) + abs(center[1] - marker[1])
    for cell in fives[1:]:
        distance = abs(cell[0] - marker[0]) + abs(cell[1] - marker[1])
        if distance < center_distance:
            center = cell
            center_distance = distance
    step_row = center[0] - marker[0]
    step_col = center[1] - marker[1]
    ray = set()
    row = center[0] + step_row
    col = center[1] + step_col
    while 0 <= row < height and 0 <= col < width:
        ray.add((row, col))
        row += step_row
        col += step_col

    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 4
    }
    while remaining:
        first = remaining.pop()
        component = {first}
        frontier = [first]
        while frontier:
            row, col = frontier.pop()
            for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbor = (row + delta_row, col + delta_col)
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    frontier.append(neighbor)
        if component & ray:
            for row, col in component:
                output[row][col] = 7

    return output
