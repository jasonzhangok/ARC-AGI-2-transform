def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    colors = []
    for value in counts:
        if value != background:
            colors.append(value)

    directions = []
    for row_step in (-1, 0, 1):
        for col_step in (-1, 0, 1):
            if row_step != 0 or col_step != 0:
                directions.append((row_step, col_step))

    components_by_color = {}
    for color in colors:
        points = set()
        for row in range(height):
            for col in range(width):
                if grid[row][col] == color:
                    points.add((row, col))
        seen = set()
        components = []
        for start in sorted(points):
            if start in seen:
                continue
            stack = [start]
            seen.add(start)
            component = []
            while stack:
                row, col = stack.pop()
                component.append((row, col))
                for row_step, col_step in directions:
                    neighbor = (row + row_step, col + col_step)
                    if neighbor in points and neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            components.append(component)
        components_by_color[color] = components

    line_color = None
    for color in colors:
        if len(components_by_color[color]) == 1:
            line_color = color
            break
    marker_color = None
    for color in colors:
        if color != line_color:
            marker_color = color

    line_cells = sorted(components_by_color[line_color][0])
    endpoints = (line_cells[0], line_cells[-1])
    marker_components = components_by_color[marker_color]
    anchors = []
    for component in marker_components:
        top = min(row for row, col in component)
        bottom = max(row for row, col in component)
        left = min(col for row, col in component)
        right = max(col for row, col in component)
        anchors.append(((top + bottom) // 2, (left + right) // 2))

    first_anchor = anchors[0]
    marker_offsets = []
    for row, col in marker_components[0]:
        marker_offsets.append((row - first_anchor[0], col - first_anchor[1]))

    output = [[background for col in range(width)] for row in range(height)]
    for first_index in range(len(anchors)):
        first = anchors[first_index]
        for second_index in range(first_index + 1, len(anchors)):
            second = anchors[second_index]
            row_step = 0 if second[0] == first[0] else (1 if second[0] > first[0] else -1)
            col_step = 0 if second[1] == first[1] else (1 if second[1] > first[1] else -1)
            distance = max(abs(second[0] - first[0]), abs(second[1] - first[1]))
            for step in range(distance + 1):
                row = first[0] + row_step * step
                col = first[1] + col_step * step
                output[row][col] = line_color

    for endpoint_row, endpoint_col in endpoints:
        for row_offset, col_offset in marker_offsets:
            row = endpoint_row + row_offset
            col = endpoint_col + col_offset
            if 0 <= row < height and 0 <= col < width:
                output[row][col] = marker_color
    return output
