def transform(grid):
    if not grid or not grid[0]:
        output = [row[:] for row in grid]
    else:
        output = [row[:] for row in grid]
        height, width = len(grid), len(grid[0])
        counts = {}
        for source_row in grid:
            for value in source_row:
                counts[value] = counts.get(value, 0) + 1
        background = None
        for value in counts:
            if background is None or counts[value] > counts[background]:
                background = value
        unseen = {(row, col) for row in range(height) for col in range(width)
                  if grid[row][col] != background}
        components = []
        while unseen:
            start = unseen.pop()
            stack = [start]
            cells = {start}
            while stack:
                row, col = stack.pop()
                for drow in (-1, 0, 1):
                    for dcol in (-1, 0, 1):
                        neighbor = row + drow, col + dcol
                        if neighbor in unseen:
                            unseen.remove(neighbor)
                            cells.add(neighbor)
                            stack.append(neighbor)
            components.append(cells)

        descriptions = []
        for cells in components:
            colors = {}
            for row, col in cells:
                value = grid[row][col]
                colors[value] = colors.get(value, 0) + 1
            top = min(row for row, _ in cells); left = min(col for _, col in cells)
            bottom = max(row for row, _ in cells); right = max(col for _, col in cells)
            descriptions.append((cells, colors, (top, left, bottom, right)))
        solid_squares = {}
        for cells, colors, box in descriptions:
            top, left, bottom, right = box
            side = bottom - top + 1
            if len(colors) == 1 and right - left + 1 == side and len(cells) == side * side:
                color = next(iter(colors))
                solid_squares.setdefault(color, []).append((top, left, side, cells))
        template_options = []
        for description in descriptions:
            cells, colors, _ = description
            anchors = [color for color, amount in colors.items()
                       if amount == 1 and color in solid_squares]
            if len(colors) >= 3 and len(anchors) >= 2:
                template_options.append((len(anchors), len(colors), -len(cells), description))

        if template_options:
            chosen = max((item[:3], -index, item[3])
                         for index, item in enumerate(template_options))[2]
            template_cells, template_colors, template_box = chosen
            top, left, bottom, right = template_box
            template = [row[left:right + 1] for row in grid[top:bottom + 1]]
            anchor_colors = sorted(color for color, amount in template_colors.items()
                                   if amount == 1 and color in solid_squares)
            variants = []
            seen_variants = set()
            current = [row[:] for row in template]
            for _ in range(4):
                for candidate in (current, [row[::-1] for row in current]):
                    key = tuple(map(tuple, candidate))
                    if key not in seen_variants:
                        seen_variants.add(key)
                        variants.append([row[:] for row in candidate])
                current = [list(row) for row in zip(*current[::-1])]
            placements = {}
            for variant in variants:
                positions = {}
                for row, line in enumerate(variant):
                    for col, color in enumerate(line):
                        if color in anchor_colors:
                            positions.setdefault(color, []).append((row, col))
                for first_index, first_color in enumerate(anchor_colors):
                    if len(positions.get(first_color, ())) != 1:
                        continue
                    first_position = positions[first_color][0]
                    for second_color in anchor_colors[first_index + 1:]:
                        if len(positions.get(second_color, ())) != 1:
                            continue
                        second_position = positions[second_color][0]
                        for first_top, first_left, side, _ in solid_squares[first_color]:
                            for second_top, second_left, second_side, _ in solid_squares[second_color]:
                                if (side != second_side
                                        or second_top - first_top != (second_position[0] - first_position[0]) * side
                                        or second_left - first_left != (second_position[1] - first_position[1]) * side):
                                    continue
                                base_top = first_top - first_position[0] * side
                                base_left = first_left - first_position[1] * side
                                scaled_height = len(variant) * side
                                scaled_width = len(variant[0]) * side
                                if (0 <= base_top <= height - scaled_height
                                        and 0 <= base_left <= width - scaled_width):
                                    placements.setdefault((base_top, base_left, side), variant)
            for (base_top, base_left, side), variant in placements.items():
                for template_row, line in enumerate(variant):
                    for template_col, color in enumerate(line):
                        if color == background:
                            continue
                        for drow in range(side):
                            for dcol in range(side):
                                output[base_top + template_row * side + drow][base_left + template_col * side + dcol] = color
    return output
