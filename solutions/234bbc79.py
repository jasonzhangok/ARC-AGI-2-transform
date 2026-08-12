def transform(grid):
    height, width = len(grid), len(grid[0])
    completed = [row[:] for row in grid]

    changed = True
    while changed:
        changed = False
        for row in range(height):
            for col in range(width):
                if completed[row][col] != 5:
                    continue
                adjacent_colors = {
                    completed[neighbor_row][neighbor_col]
                    for neighbor_row, neighbor_col in ((row+1,col),(row-1,col),(row,col+1),(row,col-1))
                    if 0 <= neighbor_row < height and 0 <= neighbor_col < width
                    and completed[neighbor_row][neighbor_col] not in (0, 5)
                }
                if len(adjacent_colors) == 1:
                    completed[row][col] = adjacent_colors.pop()
                    changed = True

    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if completed[row][col] == 0 or (row, col) in seen:
                continue
            color = completed[row][col]
            queue = [(row, col)]
            seen.add((row, col))
            component = []
            for current_row, current_col in queue:
                component.append((current_row, current_col))
                for neighbor in ((current_row+1,current_col),(current_row-1,current_col),(current_row,current_col+1),(current_row,current_col-1)):
                    if (0 <= neighbor[0] < height and 0 <= neighbor[1] < width
                            and neighbor not in seen
                            and completed[neighbor[0]][neighbor[1]] == color):
                        seen.add(neighbor)
                        queue.append(neighbor)
            components.append(component)

    components = [record[2] for record in sorted((min(col for _, col in component), index, component) for index, component in enumerate(components))]
    output_width = sum(
        max(col for _, col in component) - min(col for _, col in component) + 1
        for component in components
    )
    output = [[0] * output_width for _ in range(height)]
    horizontal_offset = 0
    previous_exit_row = None

    for index, component in enumerate(components):
        color = completed[component[0][0]][component[0][1]]
        top = min(row for row, _ in component)
        left = min(col for _, col in component)
        right = max(col for _, col in component)
        normalized = {(row - top, col - left) for row, col in component}
        endpoints = []
        for row, col in normalized:
            degree = sum(neighbor in normalized for neighbor in ((row+1,col),(row-1,col),(row,col+1),(row,col-1)))
            if degree <= 1:
                endpoints.append((row, col))
        left_endpoint = min((point[1],point[0],point) for point in endpoints)[2]
        right_endpoint = max((point[1],-point[0],point) for point in endpoints)[2]
        vertical_offset = (
            top if index == 0 else previous_exit_row - left_endpoint[0]
        )
        for row, col in normalized:
            output[vertical_offset + row][horizontal_offset + col] = color
        previous_exit_row = vertical_offset + right_endpoint[0]
        horizontal_offset += right - left + 1
    return output
