def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    color_counts = {}
    for row in grid:
        for color in row:
            color_counts[color] = color_counts.get(color, 0) + 1
    background = 0
    background_count = -1
    for color in color_counts:
        if color_counts[color] > background_count:
            background = color
            background_count = color_counts[color]

    visited = set()
    components = []
    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == background or (start_row, start_col) in visited:
                continue
            component = []
            queue = [(start_row, start_col)]
            visited.add((start_row, start_col))
            position = 0
            while position < len(queue):
                row, col = queue[position]
                position += 1
                component.append((row, col))
                for row_step in (-1, 0, 1):
                    for col_step in (-1, 0, 1):
                        neighbor = (row + row_step, col + col_step)
                        if (row_step != 0 or col_step != 0) and 0 <= neighbor[0] < height and 0 <= neighbor[1] < width and neighbor not in visited and grid[neighbor[0]][neighbor[1]] != background:
                            visited.add(neighbor)
                            queue.append(neighbor)
            components.append(component)

    sources = []
    source_indices = set()
    for component_index in range(len(components)):
        component = components[component_index]
        component_colors = {grid[row][col] for row, col in component}
        if len(component_colors) > 1:
            top = min(row for row, col in component)
            left = min(col for row, col in component)
            pattern = {(row - top, col - left): grid[row][col] for row, col in component}
            pattern_height = max(row for row, col in pattern) + 1
            pattern_width = max(col for row, col in pattern) + 1
            sources.append((component_index, pattern, pattern_height, pattern_width))
            source_indices.add(component_index)

    candidate_scores = {}
    for fragment_index in range(len(components)):
        if fragment_index in source_indices:
            continue
        fragment = components[fragment_index]
        for source_number in range(len(sources)):
            component_index, pattern, pattern_height, pattern_width = sources[source_number]
            for fragment_row, fragment_col in fragment:
                for pattern_cell in pattern:
                    pattern_row, pattern_col = pattern_cell
                    if grid[fragment_row][fragment_col] != pattern[pattern_cell]:
                        continue
                    target_top = fragment_row - pattern_row
                    target_left = fragment_col - pattern_col
                    if target_top < 0 or target_left < 0 or target_top + pattern_height > height or target_left + pattern_width > width:
                        continue
                    fragment_matches = True
                    for row, col in fragment:
                        relative = (row - target_top, col - target_left)
                        if relative not in pattern or pattern[relative] != grid[row][col]:
                            fragment_matches = False
                    if not fragment_matches:
                        continue
                    placement_matches = True
                    for row_offset in range(pattern_height):
                        for col_offset in range(pattern_width):
                            color = grid[target_top + row_offset][target_left + col_offset]
                            relative = (row_offset, col_offset)
                            if color != background and (relative not in pattern or pattern[relative] != color):
                                placement_matches = False
                    if placement_matches:
                        score = 0
                        for relative in pattern:
                            row_offset, col_offset = relative
                            if grid[target_top + row_offset][target_left + col_offset] == pattern[relative]:
                                score += 1
                        candidate_scores[(source_number, target_top, target_left)] = score

    ranked_candidates = []
    for key in candidate_scores:
        source_number, target_top, target_left = key
        ranked_candidates.append((-candidate_scores[key], source_number, target_top, target_left))
    ranked_candidates.sort()
    occupied = set()
    for negative_score, source_number, target_top, target_left in ranked_candidates:
        component_index, pattern, pattern_height, pattern_width = sources[source_number]
        target_cells = {(target_top + row, target_left + col) for row, col in pattern}
        if target_cells & occupied:
            continue
        occupied |= target_cells
        for relative in pattern:
            row_offset, col_offset = relative
            output[target_top + row_offset][target_left + col_offset] = pattern[relative]

    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            if color != background and color_counts[color] == 1:
                output[row][col] = background

    return output
