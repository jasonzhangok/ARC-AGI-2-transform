def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)

    unseen = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] != background:
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

    information = []
    for component in components:
        top = min(row for row, col in component)
        bottom = max(row for row, col in component)
        left = min(col for row, col in component)
        right = max(col for row, col in component)
        component_colors = {grid[row][col] for row, col in component}
        information.append((component, top, bottom, left, right, component_colors))

    common_colors = set(information[0][5])
    for info in information[1:]:
        common_colors &= info[5]
    marker_color = next(iter(common_colors))

    ordered = []
    remaining = information[:]
    while remaining:
        largest_index = 0
        largest_area = 0
        for index, info in enumerate(remaining):
            area = (info[2] - info[1] + 1) * (info[4] - info[3] + 1)
            if area > largest_area:
                largest_area = area
                largest_index = index
        ordered.append(remaining.pop(largest_index))

    base = ordered[0]
    output_height = base[2] - base[1] + 1
    output_width = base[4] - base[3] + 1
    output = []
    for row in range(base[1], base[2] + 1):
        output.append(grid[row][base[3]:base[4] + 1])

    for info in ordered[1:]:
        component, top, bottom, left, right, component_colors = info
        crop_height = bottom - top + 1
        crop_width = right - left + 1
        local_markers = {
            (row - top, col - left)
            for row, col in component
            if grid[row][col] == marker_color
        }

        local_sizes = {}
        marker_unseen = set(local_markers)
        while marker_unseen:
            start = marker_unseen.pop()
            marker_component = {start}
            frontier = [start]
            while frontier:
                row, col = frontier.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = (row + dr, col + dc)
                    if neighbor in marker_unseen:
                        marker_unseen.remove(neighbor)
                        marker_component.add(neighbor)
                        frontier.append(neighbor)
            for point in marker_component:
                local_sizes[point] = len(marker_component)

        target_markers = {
            (row, col)
            for row in range(output_height)
            for col in range(output_width)
            if output[row][col] == marker_color
        }
        target_sizes = {}
        marker_unseen = set(target_markers)
        while marker_unseen:
            start = marker_unseen.pop()
            marker_component = {start}
            frontier = [start]
            while frontier:
                row, col = frontier.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = (row + dr, col + dc)
                    if neighbor in marker_unseen:
                        marker_unseen.remove(neighbor)
                        marker_component.add(neighbor)
                        frontier.append(neighbor)
            for point in marker_component:
                target_sizes[point] = len(marker_component)

        anchor = next(iter(local_markers))
        placement = None
        for target in target_markers:
            row_offset = target[0] - anchor[0]
            col_offset = target[1] - anchor[1]
            inside = (
                0 <= row_offset and 0 <= col_offset and
                row_offset + crop_height <= output_height and
                col_offset + crop_width <= output_width
            )
            if not inside:
                continue
            matches = True
            for row, col in local_markers:
                translated = (row + row_offset, col + col_offset)
                if (translated not in target_markers or
                        local_sizes[(row, col)] != target_sizes[translated]):
                    matches = False
                    break
            if matches:
                placement = (row_offset, col_offset)
                break

        row_offset, col_offset = placement
        for row in range(crop_height):
            for col in range(crop_width):
                value = grid[top + row][left + col]
                if value != background:
                    output[row_offset + row][col_offset + col] = value
    return output
