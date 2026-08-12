def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [[4 if value == 5 else value for value in row] for row in grid]

    five_seen = set()
    five_components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 5 or (row, col) in five_seen:
                continue
            stack = [(row, col)]
            five_seen.add((row, col))
            component = []
            while stack:
                current_row, current_col = stack.pop()
                component.append((current_row, current_col))
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    point = (current_row + row_step, current_col + col_step)
                    if (0 <= point[0] < height and 0 <= point[1] < width
                            and grid[point[0]][point[1]] == 5
                            and point not in five_seen):
                        five_seen.add(point)
                        stack.append(point)
            five_components.append(component)

    seven_seen = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 7 or (row, col) in seven_seen:
                continue
            stack = [(row, col)]
            seven_seen.add((row, col))
            seven_component = []
            while stack:
                current_row, current_col = stack.pop()
                seven_component.append((current_row, current_col))
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    point = (current_row + row_step, current_col + col_step)
                    if (0 <= point[0] < height and 0 <= point[1] < width
                            and grid[point[0]][point[1]] == 7
                            and point not in seven_seen):
                        seven_seen.add(point)
                        stack.append(point)

            adjacent = []
            seven_cells = set(seven_component)
            for component in five_components:
                touching = False
                for marker_row, marker_col in component:
                    for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        if (marker_row + row_step, marker_col + col_step) in seven_cells:
                            touching = True
                if touching:
                    adjacent.append(component)
            if not adjacent:
                continue

            markers = [point for component in adjacent for point in component]
            top = min(point[0] for point in seven_component)
            bottom = max(point[0] for point in seven_component)
            left = min(point[1] for point in seven_component)
            right = max(point[1] for point in seven_component)
            horizontal_weight = 0
            vertical_weight = 0
            for component in adjacent:
                component_height = max(point[0] for point in component) - min(point[0] for point in component)
                component_width = max(point[1] for point in component) - min(point[1] for point in component)
                if component_width > component_height:
                    horizontal_weight += len(component)
                elif component_height > component_width:
                    vertical_weight += len(component)

            if horizontal_weight >= vertical_weight:
                band_size = right - left + 1
                band_count = len(markers) // band_size
                top_distance = sum(abs(point[0] - top) for point in markers)
                bottom_distance = sum(abs(point[0] - bottom) for point in markers)
                first_row = top if top_distance <= bottom_distance else bottom - band_count + 1
                for paint_row in range(first_row, first_row + band_count):
                    for paint_col in range(left, right + 1):
                        if grid[paint_row][paint_col] == 7:
                            output[paint_row][paint_col] = 5
            else:
                band_size = bottom - top + 1
                band_count = len(markers) // band_size
                left_distance = sum(abs(point[1] - left) for point in markers)
                right_distance = sum(abs(point[1] - right) for point in markers)
                first_col = left if left_distance <= right_distance else right - band_count + 1
                for paint_row in range(top, bottom + 1):
                    for paint_col in range(first_col, first_col + band_count):
                        if grid[paint_row][paint_col] == 7:
                            output[paint_row][paint_col] = 5

    return output
