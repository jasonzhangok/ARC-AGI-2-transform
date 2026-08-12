def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    seen = set()

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 1 or (row, col) in seen:
                continue

            component = []
            queue = [(row, col)]
            seen.add((row, col))
            index = 0
            while index < len(queue):
                current_row, current_col = queue[index]
                index += 1
                component.append((current_row, current_col))
                for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = current_row + delta_row
                    next_col = current_col + delta_col
                    if (0 <= next_row < height and 0 <= next_col < width
                            and grid[next_row][next_col] == 1
                            and (next_row, next_col) not in seen):
                        seen.add((next_row, next_col))
                        queue.append((next_row, next_col))

            cells = set(component)
            min_row = min(point[0] for point in component)
            max_row = max(point[0] for point in component)
            min_col = min(point[1] for point in component)
            max_col = max(point[1] for point in component)
            box_top = max(0, min_row - 1)
            box_bottom = min(height - 1, max_row + 1)
            box_left = max(0, min_col - 1)
            box_right = min(width - 1, max_col + 1)

            exterior = set()
            flood = []
            for box_row in range(box_top, box_bottom + 1):
                for box_col in range(box_left, box_right + 1):
                    if ((box_row in (box_top, box_bottom)
                         or box_col in (box_left, box_right))
                            and (box_row, box_col) not in cells):
                        exterior.add((box_row, box_col))
                        flood.append((box_row, box_col))

            index = 0
            while index < len(flood):
                current_row, current_col = flood[index]
                index += 1
                for delta_row in (-1, 0, 1):
                    for delta_col in (-1, 0, 1):
                        next_row = current_row + delta_row
                        next_col = current_col + delta_col
                        if (box_top <= next_row <= box_bottom
                                and box_left <= next_col <= box_right
                                and (next_row, next_col) not in cells
                                and (next_row, next_col) not in exterior):
                            exterior.add((next_row, next_col))
                            flood.append((next_row, next_col))

            interior = set()
            for box_row in range(box_top, box_bottom + 1):
                for box_col in range(box_left, box_right + 1):
                    if ((box_row, box_col) not in cells
                            and (box_row, box_col) not in exterior):
                        interior.add((box_row, box_col))

            if not interior:
                continue

            for current_row, current_col in component:
                for delta_row in (-1, 0, 1):
                    for delta_col in (-1, 0, 1):
                        next_row = current_row + delta_row
                        next_col = current_col + delta_col
                        if (0 <= next_row < height and 0 <= next_col < width
                                and grid[next_row][next_col] == 0):
                            if (next_row, next_col) in interior:
                                output[next_row][next_col] = 3
                            elif (next_row, next_col) in exterior:
                                output[next_row][next_col] = 2

            if ((min_row, min_col) not in cells
                    and (min_row, min_col + 1) in cells
                    and (min_row + 1, min_col) in cells
                    and (min_row + 1, min_col + 1) in cells
                    and min_row > 0 and min_col > 0
                    and grid[min_row - 1][min_col - 1] == 0):
                output[min_row - 1][min_col - 1] = 2

    return output
