def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    regions = []

    for row in range(height):
        for column in range(width):
            if grid[row][column] == 0 or (row, column) in seen:
                continue
            color = grid[row][column]
            cells = [(row, column)]
            seen.add((row, column))
            cursor = 0
            while cursor < len(cells):
                current_row, current_column = cells[cursor]
                cursor += 1
                for row_step, column_step in ((-1, -1), (-1, 0), (-1, 1),
                                               (0, -1), (0, 1),
                                               (1, -1), (1, 0), (1, 1)):
                    next_row = current_row + row_step
                    next_column = current_column + column_step
                    if (0 <= next_row < height and 0 <= next_column < width
                            and grid[next_row][next_column] == color
                            and (next_row, next_column) not in seen):
                        seen.add((next_row, next_column))
                        cells.append((next_row, next_column))

            points = sorted((cell_column, cell_row) for cell_row, cell_column in cells)
            lower = []
            for point in points:
                while len(lower) >= 2:
                    origin = lower[-2]
                    middle = lower[-1]
                    cross = ((middle[0] - origin[0]) * (point[1] - origin[1])
                             - (middle[1] - origin[1]) * (point[0] - origin[0]))
                    if cross > 0:
                        break
                    lower.pop()
                lower.append(point)
            upper = []
            for point in reversed(points):
                while len(upper) >= 2:
                    origin = upper[-2]
                    middle = upper[-1]
                    cross = ((middle[0] - origin[0]) * (point[1] - origin[1])
                             - (middle[1] - origin[1]) * (point[0] - origin[0]))
                    if cross > 0:
                        break
                    upper.pop()
                upper.append(point)
            hull = lower[:-1] + upper[:-1]
            regions.append((color, hull))

    output = [row[:] for row in grid]
    for row in range(height):
        for column in range(width):
            color = grid[row][column]
            if color == 0:
                continue
            for boundary_color, hull in regions:
                if boundary_color == color or len(hull) < 3:
                    continue
                nonnegative = True
                nonpositive = True
                for index in range(len(hull)):
                    start = hull[index]
                    end = hull[(index + 1) % len(hull)]
                    cross = ((end[0] - start[0]) * (row - start[1])
                             - (end[1] - start[1]) * (column - start[0]))
                    if cross < 0:
                        nonnegative = False
                    if cross > 0:
                        nonpositive = False
                if nonnegative or nonpositive:
                    output[row][column] = 0
                    break
    return output
