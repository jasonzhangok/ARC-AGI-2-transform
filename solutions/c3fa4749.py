def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    backgrounds = [[-1 for _ in range(width)] for _ in range(height)]

    for row in range(height):
        for col in range(width):
            neighborhood = []
            for nearby_row in range(max(0, row - 2), min(height, row + 3)):
                for nearby_col in range(max(0, col - 2), min(width, col + 3)):
                    neighborhood.append(grid[nearby_row][nearby_col])
            background = neighborhood[0]
            for value in neighborhood[1:]:
                if neighborhood.count(value) > neighborhood.count(background):
                    background = value
            if (neighborhood.count(background) * 2 >= len(neighborhood)
                    and grid[row][col] != background):
                backgrounds[row][col] = background

    output = [row[:] for row in grid]
    seen = set()
    for row in range(height):
        for col in range(width):
            background = backgrounds[row][col]
            if background == -1 or (row, col) in seen:
                continue

            component = set()
            pending = [(row, col)]
            seen.add((row, col))
            while pending:
                current_row, current_col = pending.pop()
                component.add((current_row, current_col))
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row = current_row + row_step
                    next_col = current_col + col_step
                    if (0 <= next_row < height and 0 <= next_col < width
                            and backgrounds[next_row][next_col] == background
                            and (next_row, next_col) not in seen):
                        seen.add((next_row, next_col))
                        pending.append((next_row, next_col))

            surrounded = True
            edge_points = []
            for current_row, current_col in component:
                if (current_row == 0 or current_row == height - 1
                        or current_col == 0 or current_col == width - 1):
                    edge_points.append((current_row, current_col))
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row = current_row + row_step
                    next_col = current_col + col_step
                    if (0 <= next_row < height and 0 <= next_col < width
                            and (next_row, next_col) not in component
                            and grid[next_row][next_col] != background):
                        surrounded = False
            component_colors = set(grid[current_row][current_col]
                                   for current_row, current_col in component)
            if not surrounded or len(component_colors) < 2 or len(edge_points) != 1:
                continue

            edge_row, edge_col = edge_points[0]
            edge_degree = 0
            for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (edge_row + row_step, edge_col + col_step) in component:
                    edge_degree += 1
            if edge_degree != 1:
                continue
            target = grid[edge_row][edge_col]

            top = min(point[0] for point in component)
            bottom = max(point[0] for point in component)
            left = min(point[1] for point in component)
            right = max(point[1] for point in component)
            outside = set()
            pending = []
            for candidate_row in range(top, bottom + 1):
                for candidate_col in range(left, right + 1):
                    if ((candidate_row == top or candidate_row == bottom
                            or candidate_col == left or candidate_col == right)
                            and (candidate_row, candidate_col) not in component
                            and (candidate_row, candidate_col) not in outside):
                        outside.add((candidate_row, candidate_col))
                        pending.append((candidate_row, candidate_col))
            while pending:
                current_row, current_col = pending.pop()
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row = current_row + row_step
                    next_col = current_col + col_step
                    if (top <= next_row <= bottom and left <= next_col <= right
                            and (next_row, next_col) not in component
                            and (next_row, next_col) not in outside):
                        outside.add((next_row, next_col))
                        pending.append((next_row, next_col))

            for current_row, current_col in component:
                output[current_row][current_col] = target
            for candidate_row in range(top, bottom + 1):
                for candidate_col in range(left, right + 1):
                    if ((candidate_row, candidate_col) not in component
                            and (candidate_row, candidate_col) not in outside):
                        output[candidate_row][candidate_col] = target

    return output
