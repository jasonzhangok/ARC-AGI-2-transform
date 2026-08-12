def transform(grid):
    height = len(grid)
    width = len(grid[0])

    counts = {}
    for row in grid:
        for color in row:
            counts[color] = counts.get(color, 0) + 1
    background = max(counts, key=counts.get)

    visited = set()
    components = []
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            if color == background or (row, col) in visited:
                continue
            cells = []
            stack = [(row, col)]
            visited.add((row, col))
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor_row = current_row + delta_row
                    neighbor_col = current_col + delta_col
                    if not (0 <= neighbor_row < height and 0 <= neighbor_col < width):
                        continue
                    if (neighbor_row, neighbor_col) in visited:
                        continue
                    if grid[neighbor_row][neighbor_col] == color:
                        visited.add((neighbor_row, neighbor_col))
                        stack.append((neighbor_row, neighbor_col))

            top = min(row for row, col in cells)
            left = min(col for row, col in cells)
            shape = set()
            for cell_row, cell_col in cells:
                shape.add((cell_row - top, cell_col - left))
            components.append((color, cells, shape))

    chosen = None
    for candidate_index in range(len(components)):
        candidate_color, candidate_cells, candidate_shape = components[candidate_index]
        top = min(row for row, col in candidate_cells)
        bottom = max(row for row, col in candidate_cells)
        left = min(col for row, col in candidate_cells)
        right = max(col for row, col in candidate_cells)

        remaining = set()
        contains_other_color = False
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                if grid[row][col] == background:
                    remaining.add((row, col))
                elif grid[row][col] != candidate_color:
                    contains_other_color = True
        if contains_other_color or not remaining:
            continue

        gaps = []
        while remaining:
            start = remaining.pop()
            cells = [start]
            stack = [start]
            while stack:
                current_row, current_col = stack.pop()
                for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = (current_row + delta_row, current_col + delta_col)
                    if neighbor in remaining:
                        remaining.remove(neighbor)
                        stack.append(neighbor)
                        cells.append(neighbor)
            gap_top = min(row for row, col in cells)
            gap_left = min(col for row, col in cells)
            shape = set()
            for cell_row, cell_col in cells:
                shape.add((cell_row - gap_top, cell_col - gap_left))
            gaps.append((cells, shape))

        fills = []
        used_sources = set()
        all_matched = True
        for gap_cells, gap_shape in gaps:
            fill_color = None
            matched_source = None
            for source_index in range(len(components)):
                if source_index == candidate_index or source_index in used_sources:
                    continue
                source_color, source_cells, source_shape = components[source_index]
                outside = True
                for source_row, source_col in source_cells:
                    if top <= source_row <= bottom and left <= source_col <= right:
                        outside = False
                if outside and source_shape == gap_shape:
                    fill_color = source_color
                    matched_source = source_index
                    break
            if fill_color is None:
                all_matched = False
                break
            used_sources.add(matched_source)
            fills.append((gap_cells, fill_color))

        if all_matched:
            chosen = (top, bottom, left, right, candidate_color, fills)
            break

    if chosen is None:
        return [row[:] for row in grid]

    top, bottom, left, right, candidate_color, fills = chosen
    output = [[candidate_color for col in range(left, right + 1)]
              for row in range(top, bottom + 1)]
    for gap_cells, fill_color in fills:
        for row, col in gap_cells:
            output[row - top][col - left] = fill_color
    return output
