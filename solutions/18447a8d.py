def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    color_counts = {}
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            color_counts[color] = color_counts.get(color, 0) + 1
    background = 0
    background_count = -1
    for color in color_counts:
        if color_counts[color] > background_count:
            background = color
            background_count = color_counts[color]

    separators = []
    for row in range(height):
        if all(grid[row][col] == background for col in range(width)):
            separators.append(row)

    panels = []
    for index in range(len(separators) - 1):
        top = separators[index] + 1
        bottom = separators[index + 1]
        if top >= bottom:
            continue
        mask = []
        colored = []
        object_color = background
        for row in range(top, bottom):
            for col in range(width):
                if grid[row][col] == 8:
                    mask.append((row - top, col))
                elif grid[row][col] != background:
                    colored.append((row - top, col))
                    object_color = grid[row][col]
        if mask and colored:
            mask_left = min(col for row, col in mask)
            object_left = min(col for row, col in colored)
            object_right = max(col for row, col in colored)
            normalized_mask = set()
            normalized_object = set()
            for row, col in mask:
                normalized_mask.add((row, col - mask_left))
            for row, col in colored:
                normalized_object.add((row, col - object_left))
            panels.append(
                (
                    top,
                    bottom - top,
                    mask_left,
                    normalized_mask,
                    object_color,
                    normalized_object,
                    object_right - object_left + 1,
                )
            )

    for row in range(height):
        for col in range(width):
            if grid[row][col] != background and grid[row][col] != 8:
                output[row][col] = background

    rectangle_width_counts = {}
    for panel_index in range(len(panels)):
        panel_height = panels[panel_index][1]
        mask = panels[panel_index][3]
        for object_index in range(len(panels)):
            candidate = panels[object_index][5]
            candidate_width = panels[object_index][6]
            total_cells = len(mask) + len(candidate)
            if total_cells % panel_height != 0:
                continue
            rectangle_width = total_cells // panel_height
            if rectangle_width < candidate_width:
                continue
            shifted_candidate = set()
            for row, col in candidate:
                shifted_candidate.add((row, rectangle_width - candidate_width + col))
            union = mask.union(shifted_candidate)
            if not mask.intersection(shifted_candidate):
                if len(union) == panel_height * rectangle_width:
                    complete = True
                    for row in range(panel_height):
                        for col in range(rectangle_width):
                            if (row, col) not in union:
                                complete = False
                    if complete:
                        rectangle_width_counts[rectangle_width] = (
                            rectangle_width_counts.get(rectangle_width, 0) + 1
                        )
    common_rectangle_width = 0
    common_rectangle_width_count = -1
    for rectangle_width in rectangle_width_counts:
        if rectangle_width_counts[rectangle_width] > common_rectangle_width_count:
            common_rectangle_width = rectangle_width
            common_rectangle_width_count = rectangle_width_counts[rectangle_width]

    used_objects = set()
    for panel_index in range(len(panels)):
        top, panel_height, mask_left, mask, own_color, own_object, own_width = panels[panel_index]
        matched_index = -1
        matched_positions = set()
        for object_index in range(len(panels)):
            if object_index in used_objects:
                continue
            candidate_color = panels[object_index][4]
            candidate = panels[object_index][5]
            candidate_width = panels[object_index][6]
            total_cells = len(mask) + len(candidate)
            if total_cells % panel_height != 0:
                continue
            rectangle_width = total_cells // panel_height
            if rectangle_width != common_rectangle_width:
                continue
            if rectangle_width < candidate_width:
                continue
            shifted_candidate = set()
            for row, col in candidate:
                shifted_candidate.add((row, rectangle_width - candidate_width + col))
            if mask.intersection(shifted_candidate):
                continue
            union = mask.union(shifted_candidate)
            complete = True
            for row in range(panel_height):
                for col in range(rectangle_width):
                    if (row, col) not in union:
                        complete = False
            if complete and len(union) == panel_height * rectangle_width:
                matched_index = object_index
                matched_positions = shifted_candidate
                break

        if matched_index >= 0:
            used_objects.add(matched_index)
            matched_color = panels[matched_index][4]
            for row, col in matched_positions:
                output[top + row][mask_left + col] = matched_color

    return output
