def transform(grid):
    height = len(grid)
    width = len(grid[0])

    color_counts = {}
    for row in grid:
        for color in row:
            color_counts[color] = color_counts.get(color, 0) + 1

    background = None
    background_count = -1
    for color in color_counts:
        if color_counts[color] > background_count:
            background = color
            background_count = color_counts[color]

    left_color = None
    right_color = None
    for color in color_counts:
        if color == background:
            continue
        fills_left = True
        fills_right = True
        for row_index in range(height):
            if grid[row_index][0] != color:
                fills_left = False
            if grid[row_index][width - 1] != color:
                fills_right = False
        if fills_left:
            left_color = color
        if fills_right:
            right_color = color

    components = []
    side_colors = [left_color, right_color]
    for side_index in range(2):
        side_color = side_colors[side_index]
        seen = []
        for row_index in range(height):
            seen.append([False] * width)

        records = []
        for row_index in range(height):
            for column_index in range(1, width - 1):
                if (grid[row_index][column_index] != side_color
                        or seen[row_index][column_index]):
                    continue

                cells = []
                stack = [(row_index, column_index)]
                seen[row_index][column_index] = True
                minimum_column = column_index
                maximum_column = column_index
                while stack:
                    current_row, current_column = stack.pop()
                    cells.append((current_row, current_column))
                    if current_column < minimum_column:
                        minimum_column = current_column
                    if current_column > maximum_column:
                        maximum_column = current_column

                    neighbors = (
                        (current_row - 1, current_column - 1),
                        (current_row - 1, current_column),
                        (current_row - 1, current_column + 1),
                        (current_row, current_column - 1),
                        (current_row, current_column + 1),
                        (current_row + 1, current_column - 1),
                        (current_row + 1, current_column),
                        (current_row + 1, current_column + 1),
                    )
                    for neighbor_row, neighbor_column in neighbors:
                        if (0 <= neighbor_row < height
                                and 1 <= neighbor_column < width - 1
                                and grid[neighbor_row][neighbor_column] == side_color
                                and not seen[neighbor_row][neighbor_column]):
                            seen[neighbor_row][neighbor_column] = True
                            stack.append((neighbor_row, neighbor_column))

                if side_index == 0:
                    distance_key = minimum_column
                else:
                    distance_key = -maximum_column
                records.append([distance_key, cells])

        for record_index in range(1, len(records)):
            current_record = records[record_index]
            insertion_index = record_index - 1
            while (insertion_index >= 0
                    and records[insertion_index][0] > current_record[0]):
                records[insertion_index + 1] = records[insertion_index]
                insertion_index -= 1
            records[insertion_index + 1] = current_record

        if side_index == 0:
            direction = -1
        else:
            direction = 1

        for record in records:
            components.append([side_color, direction, set(record[1]), False])

    while True:
        candidates = set()
        for component_index in range(len(components)):
            if not components[component_index][3]:
                candidates.add(component_index)
        if not candidates:
            break

        proposed_positions = [None] * len(components)
        stopped_this_round = set()
        for component_index in candidates:
            direction = components[component_index][1]
            proposed = set()
            hits_wall = False
            for row_index, column_index in components[component_index][2]:
                next_column = column_index + direction
                if next_column <= 0 or next_column >= width - 1:
                    hits_wall = True
                proposed.add((row_index, next_column))
            proposed_positions[component_index] = proposed
            if hits_wall:
                stopped_this_round.add(component_index)

        for component_index in stopped_this_round:
            candidates.remove(component_index)
            components[component_index][3] = True

        resolving = True
        while resolving:
            resolving = False
            stopped_this_round = set()

            for component_index in candidates:
                for other_index in range(len(components)):
                    if other_index in candidates:
                        continue
                    if (proposed_positions[component_index]
                            & components[other_index][2]):
                        stopped_this_round.add(component_index)
                        break

            candidate_list = []
            for component_index in candidates:
                candidate_list.append(component_index)
            for first_index in range(len(candidate_list)):
                first_component = candidate_list[first_index]
                for second_index in range(first_index + 1, len(candidate_list)):
                    second_component = candidate_list[second_index]
                    proposals_overlap = bool(
                        proposed_positions[first_component]
                        & proposed_positions[second_component]
                    )
                    opposite_directions_cross = False
                    if (components[first_component][1]
                            != components[second_component][1]):
                        if (proposed_positions[first_component]
                                & components[second_component][2]):
                            opposite_directions_cross = True
                        if (proposed_positions[second_component]
                                & components[first_component][2]):
                            opposite_directions_cross = True
                    if proposals_overlap or opposite_directions_cross:
                        stopped_this_round.add(first_component)
                        stopped_this_round.add(second_component)

            if stopped_this_round:
                resolving = True
                for component_index in stopped_this_round:
                    if component_index in candidates:
                        candidates.remove(component_index)
                        components[component_index][3] = True

        for component_index in candidates:
            components[component_index][2] = proposed_positions[component_index]

    output = []
    for row_index in range(height):
        output_row = [background] * width
        output_row[0] = left_color
        output_row[width - 1] = right_color
        output.append(output_row)

    for component in components:
        side_color = component[0]
        for row_index, column_index in component[2]:
            output[row_index][column_index] = side_color

    return output
