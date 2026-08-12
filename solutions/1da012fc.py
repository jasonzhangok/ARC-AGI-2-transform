def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    color_counts = {}
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            color_counts[color] = color_counts.get(color, 0) + 1
    object_color = 0
    object_count = -1
    for color in color_counts:
        if color not in (0, 5) and color_counts[color] > object_count:
            object_color = color
            object_count = color_counts[color]

    seen = set()
    objects = []
    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] != object_color:
                continue
            if (start_row, start_col) in seen:
                continue
            component = []
            stack = [(start_row, start_col)]
            seen.add((start_row, start_col))
            while stack:
                row, col = stack.pop()
                component.append((row, col))
                for row_offset in (-1, 0, 1):
                    for col_offset in (-1, 0, 1):
                        if row_offset == 0 and col_offset == 0:
                            continue
                        next_row = row + row_offset
                        next_col = col + col_offset
                        next_cell = (next_row, next_col)
                        if 0 <= next_row < height and 0 <= next_col < width:
                            if next_cell not in seen:
                                if grid[next_row][next_col] == object_color:
                                    seen.add(next_cell)
                                    stack.append(next_cell)
            objects.append(component)

    centers = []
    for component in objects:
        center_row = sum(row for row, col in component) / len(component)
        center_col = sum(col for row, col in component) / len(component)
        centers.append((center_row, center_col))
    markers = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] not in (0, 5, object_color):
                markers.append((row, col, grid[row][col]))

    center_top = min(row for row, col in centers)
    center_bottom = max(row for row, col in centers)
    center_left = min(col for row, col in centers)
    center_right = max(col for row, col in centers)
    marker_top = min(row for row, col, color in markers)
    marker_bottom = max(row for row, col, color in markers)
    marker_left = min(col for row, col, color in markers)
    marker_right = max(col for row, col, color in markers)

    normalized_centers = []
    for row, col in centers:
        normalized_row = 0
        normalized_col = 0
        if center_bottom > center_top:
            normalized_row = (row - center_top) / (center_bottom - center_top)
        if center_right > center_left:
            normalized_col = (col - center_left) / (center_right - center_left)
        normalized_centers.append((normalized_row, normalized_col))
    normalized_markers = []
    for row, col, color in markers:
        normalized_row = 0
        normalized_col = 0
        if marker_bottom > marker_top:
            normalized_row = (row - marker_top) / (marker_bottom - marker_top)
        if marker_right > marker_left:
            normalized_col = (col - marker_left) / (marker_right - marker_left)
        normalized_markers.append((normalized_row, normalized_col))

    best_cost = None
    best_assignment = []
    search_stack = [(0, [], set(), 0.0)]
    while search_stack:
        object_index, assignment, used_markers, cost = search_stack.pop()
        if object_index == len(objects):
            if best_cost is None or cost < best_cost:
                best_cost = cost
                best_assignment = assignment
            continue
        for marker_index in range(len(markers)):
            if marker_index in used_markers:
                continue
            row_difference = (
                normalized_centers[object_index][0]
                - normalized_markers[marker_index][0]
            )
            col_difference = (
                normalized_centers[object_index][1]
                - normalized_markers[marker_index][1]
            )
            next_cost = cost + row_difference * row_difference + col_difference * col_difference
            if best_cost is not None and next_cost >= best_cost:
                continue
            next_assignment = assignment + [marker_index]
            next_used_markers = set(used_markers)
            next_used_markers.add(marker_index)
            search_stack.append(
                (object_index + 1, next_assignment, next_used_markers, next_cost)
            )

    for object_index in range(len(objects)):
        new_color = markers[best_assignment[object_index]][2]
        for row, col in objects[object_index]:
            output[row][col] = new_color

    return output
