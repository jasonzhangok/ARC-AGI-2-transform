def transform(grid):
    height = len(grid)
    width = len(grid[0])

    vertical = height > width
    total_length = height if vertical else width
    other_length = width if vertical else height
    frame_count = 0
    frame_length = 0
    best_difference = None
    for candidate_count in range(3, total_length + 1):
        if total_length % candidate_count != 0:
            continue
        candidate_length = total_length // candidate_count
        if candidate_length < 3:
            continue
        difference = abs(candidate_length - other_length)
        if best_difference is None or difference < best_difference:
            best_difference = difference
            frame_count = candidate_count
            frame_length = candidate_length

    frames = []
    if vertical:
        for frame_index in range(frame_count):
            top = frame_index * frame_length
            frames.append([row[:] for row in grid[top:top + frame_length]])
    else:
        for frame_index in range(frame_count):
            left = frame_index * frame_length
            frame = []
            for row in range(height):
                frame.append(grid[row][left:left + frame_length])
            frames.append(frame)

    template = frames[-1]
    frame_height = len(template)
    frame_width = len(template[0])
    output = [row[:] for row in template]

    changing_colors = set()
    for frame_index in range(frame_count - 1):
        for row in range(frame_height):
            for col in range(frame_width):
                if frames[frame_index][row][col] != template[row][col]:
                    changing_colors.add(frames[frame_index][row][col])

    projected_colors = set()
    projection_sources = []
    for color in changing_colors:
        active_frames = []
        for frame_index in range(frame_count - 1):
            active = False
            for row in range(frame_height):
                for col in range(frame_width):
                    if frames[frame_index][row][col] == color:
                        if frames[frame_index][row][col] != template[row][col]:
                            active = True
            if active:
                active_frames.append(frame_index)
        if len(active_frames) < 2:
            continue
        previous_index = active_frames[-2]
        current_index = active_frames[-1]
        stride = current_index - previous_index
        if current_index + stride != frame_count - 1:
            continue
        if frame_count > 3 and len(active_frames) == frame_count - 1:
            continue
        projected_colors.add(color)
        projection_sources.append((previous_index, current_index, color))

        previous = frames[previous_index]
        current = frames[current_index]
        if vertical:
            for row in range(frame_height):
                previous_positions = []
                current_positions = []
                for col in range(frame_width):
                    if previous[row][col] == color and previous[row][col] != template[row][col]:
                        previous_positions.append(col)
                    if current[row][col] == color and current[row][col] != template[row][col]:
                        current_positions.append(col)
                if previous_positions and current_positions:
                    previous_runs = []
                    current_runs = []
                    for col in previous_positions:
                        if not previous_runs or col > previous_runs[-1][1] + 1:
                            previous_runs.append([col, col])
                        else:
                            previous_runs[-1][1] = col
                    for col in current_positions:
                        if not current_runs or col > current_runs[-1][1] + 1:
                            current_runs.append([col, col])
                        else:
                            current_runs[-1][1] = col
                    if len(previous_runs) == len(current_runs):
                        for run_index in range(len(previous_runs)):
                            next_left = 2 * current_runs[run_index][0] - previous_runs[run_index][0]
                            next_right = 2 * current_runs[run_index][1] - previous_runs[run_index][1]
                            for col in range(next_left, next_right + 1):
                                if 0 <= col < frame_width:
                                    output[row][col] = color
        else:
            for col in range(frame_width):
                previous_positions = []
                current_positions = []
                for row in range(frame_height):
                    if previous[row][col] == color and previous[row][col] != template[row][col]:
                        previous_positions.append(row)
                    if current[row][col] == color and current[row][col] != template[row][col]:
                        current_positions.append(row)
                if previous_positions and current_positions:
                    previous_runs = []
                    current_runs = []
                    for row in previous_positions:
                        if not previous_runs or row > previous_runs[-1][1] + 1:
                            previous_runs.append([row, row])
                        else:
                            previous_runs[-1][1] = row
                    for row in current_positions:
                        if not current_runs or row > current_runs[-1][1] + 1:
                            current_runs.append([row, row])
                        else:
                            current_runs[-1][1] = row
                    if len(previous_runs) == len(current_runs):
                        for run_index in range(len(previous_runs)):
                            next_top = 2 * current_runs[run_index][0] - previous_runs[run_index][0]
                            next_bottom = 2 * current_runs[run_index][1] - previous_runs[run_index][1]
                            for row in range(next_top, next_bottom + 1):
                                if 0 <= row < frame_height:
                                    output[row][col] = color

    for previous_index, current_index, primary_color in projection_sources:
        previous = frames[previous_index]
        current = frames[current_index]
        companion_colors = set()
        for companion_color in changing_colors:
            if companion_color in projected_colors:
                continue
            previous_count = 0
            current_count = 0
            for row in range(frame_height):
                for col in range(frame_width):
                    if previous[row][col] == companion_color:
                        previous_count += 1
                    if current[row][col] == companion_color:
                        current_count += 1
            if previous_count == 0 or current_count == 0:
                continue
            companion_colors.add(companion_color)

            if vertical:
                for row in range(frame_height):
                    previous_positions = []
                    current_positions = []
                    for col in range(frame_width):
                        if previous[row][col] == companion_color:
                            previous_positions.append(col)
                        if current[row][col] == companion_color:
                            current_positions.append(col)
                    if not previous_positions or not current_positions:
                        continue
                    next_left = 2 * min(current_positions) - min(previous_positions)
                    next_right = 2 * max(current_positions) - max(previous_positions)
                    spacing = 0
                    combined_positions = sorted(set(previous_positions + current_positions))
                    for index in range(1, len(combined_positions)):
                        difference = combined_positions[index] - combined_positions[index - 1]
                        if difference == 0:
                            continue
                        if spacing == 0:
                            spacing = difference
                        else:
                            first = spacing
                            second = difference
                            while second:
                                first, second = second, first % second
                            spacing = first
                    if spacing == 0:
                        spacing = 1
                    for col in range(next_left, next_right + 1, spacing):
                        if 0 <= col < frame_width:
                            output[row][col] = companion_color
            else:
                for col in range(frame_width):
                    previous_positions = []
                    current_positions = []
                    for row in range(frame_height):
                        if previous[row][col] == companion_color:
                            previous_positions.append(row)
                        if current[row][col] == companion_color:
                            current_positions.append(row)
                    if not previous_positions or not current_positions:
                        continue
                    next_top = 2 * min(current_positions) - min(previous_positions)
                    next_bottom = 2 * max(current_positions) - max(previous_positions)
                    spacing = 0
                    combined_positions = sorted(set(previous_positions + current_positions))
                    for index in range(1, len(combined_positions)):
                        difference = combined_positions[index] - combined_positions[index - 1]
                        if difference == 0:
                            continue
                        if spacing == 0:
                            spacing = difference
                        else:
                            first = spacing
                            second = difference
                            while second:
                                first, second = second, first % second
                            spacing = first
                    if spacing == 0:
                        spacing = 1
                    for row in range(next_top, next_bottom + 1, spacing):
                        if 0 <= row < frame_height:
                            output[row][col] = companion_color

        if companion_colors:
            object_colors = set(companion_colors)
            object_colors.add(primary_color)
            if vertical:
                for row in range(frame_height):
                    positions = []
                    for col in range(frame_width):
                        if output[row][col] in object_colors:
                            positions.append(col)
                    if positions:
                        for col in range(min(positions), max(positions) + 1):
                            if output[row][col] == template[row][col]:
                                output[row][col] = primary_color
            else:
                for col in range(frame_width):
                    positions = []
                    for row in range(frame_height):
                        if output[row][col] in object_colors:
                            positions.append(row)
                    if positions:
                        for row in range(min(positions), max(positions) + 1):
                            if output[row][col] == template[row][col]:
                                output[row][col] = primary_color

    return output
