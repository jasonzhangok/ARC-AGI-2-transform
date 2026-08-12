def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    non_background = [value for value in counts if value != background]
    fill_color = non_background[0]
    marker_color = non_background[0]
    for value in non_background[1:]:
        if counts[value] > counts[fill_color]:
            fill_color = value
        if counts[value] < counts[marker_color]:
            marker_color = value

    unseen = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] != fill_color:
                unseen.add((row, col))
    components = []
    while unseen:
        start = unseen.pop()
        component = {start}
        frontier = [start]
        while frontier:
            row, col = frontier.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = (row + dr, col + dc)
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    component.add(neighbor)
                    frontier.append(neighbor)
        components.append(component)

    selected = components[0]
    selected_markers = sum(
        grid[row][col] == marker_color for row, col in selected
    )
    for component in components[1:]:
        marker_count = sum(
            grid[row][col] == marker_color for row, col in component
        )
        if marker_count > selected_markers:
            selected = component
            selected_markers = marker_count
    output = [row[:] for row in grid]
    for row, col in selected:
        if grid[row][col] == background:
            output[row][col] = fill_color
    return output
