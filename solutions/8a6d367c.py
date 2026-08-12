def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = None
    background_count = -1
    for value in counts:
        if counts[value] > background_count:
            background = value
            background_count = counts[value]
    frame_top = 0
    frame_bottom = height - 1
    frame_left = 0
    frame_right = width - 1
    best_area = -1
    seen_frames = set()
    for start_row in range(height):
        for start_col in range(width):
            color = grid[start_row][start_col]
            if color == background or (start_row, start_col) in seen_frames:
                continue
            component = [(start_row, start_col)]
            seen_frames.add((start_row, start_col))
            index = 0
            while index < len(component):
                row, col = component[index]
                index += 1
                for next_row, next_col in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if 0 <= next_row < height and 0 <= next_col < width and ((next_row, next_col) not in seen_frames) and (grid[next_row][next_col] == color):
                        seen_frames.add((next_row, next_col))
                        component.append((next_row, next_col))
            top = min((point[0] for point in component))
            bottom = max((point[0] for point in component))
            left = min((point[1] for point in component))
            right = max((point[1] for point in component))
            is_frame = top < bottom and left < right
            if is_frame:
                for col in range(left, right + 1):
                    if grid[top][col] != color or grid[bottom][col] != color:
                        is_frame = False
                        break
            if is_frame:
                for row in range(top + 1, bottom):
                    if grid[row][left] != color or grid[row][right] != color:
                        is_frame = False
                        break
            area = (bottom - top + 1) * (right - left + 1)
            if is_frame and area > best_area:
                best_area = area
                frame_top = top
                frame_bottom = bottom
                frame_left = left
                frame_right = right
    result = []
    for row in range(frame_top, frame_bottom + 1):
        result.append(grid[row][frame_left:frame_right + 1])
    if best_area < 0:
        output = result
    else:
        inner_height = frame_bottom - frame_top - 1
        inner_width = frame_right - frame_left - 1
        clues = []
        marker_color = None
        for row in range(inner_height):
            for col in range(inner_width):
                value = grid[frame_top + 1 + row][frame_left + 1 + col]
                if value != background:
                    clues.append((row, col))
                    if marker_color is None:
                        marker_color = value
        candidate_components = []
        seen_candidates = set()
        for start_row in range(frame_top):
            for start_col in range(width):
                color = grid[start_row][start_col]
                if color == background or (start_row, start_col) in seen_candidates:
                    continue
                points = [(start_row, start_col)]
                seen_candidates.add((start_row, start_col))
                index = 0
                while index < len(points):
                    row, col = points[index]
                    index += 1
                    for row_step in (-1, 0, 1):
                        for col_step in (-1, 0, 1):
                            next_row = row + row_step
                            next_col = col + col_step
                            if (row_step != 0 or col_step != 0) and 0 <= next_row < frame_top and (0 <= next_col < width) and ((next_row, next_col) not in seen_candidates) and (grid[next_row][next_col] == color):
                                seen_candidates.add((next_row, next_col))
                                points.append((next_row, next_col))
                candidate_components.append(points)
        chosen_shape = None
        row_scale = 0
        col_scale = 0
        for points in candidate_components:
            top = min((point[0] for point in points))
            bottom = max((point[0] for point in points))
            left = min((point[1] for point in points))
            right = max((point[1] for point in points))
            symbol_height = bottom - top + 1
            symbol_width = right - left + 1
            if inner_height % symbol_height != 0 or inner_width % symbol_width != 0:
                continue
            candidate_row_scale = inner_height // symbol_height
            candidate_col_scale = inner_width // symbol_width
            shape = set()
            for row, col in points:
                shape.add((row - top, col - left))
            fits = True
            for row, col in clues:
                if (row // candidate_row_scale, col // candidate_col_scale) not in shape:
                    fits = False
                    break
            if fits:
                chosen_shape = shape
                row_scale = candidate_row_scale
                col_scale = candidate_col_scale
                break
        for row in range(1, len(result) - 1):
            for col in range(1, len(result[0]) - 1):
                result[row][col] = background
        if chosen_shape is not None and marker_color is not None:
            for symbol_row, symbol_col in chosen_shape:
                for row in range(symbol_row * row_scale + 1, (symbol_row + 1) * row_scale + 1):
                    for col in range(symbol_col * col_scale + 1, (symbol_col + 1) * col_scale + 1):
                        result[row][col] = marker_color
        output = result
    return output
