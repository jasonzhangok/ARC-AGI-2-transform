def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    additions = []

    for color, new_color in ((5, 4), (2, 3)):
        seen = set()
        for row in range(height):
            for col in range(width):
                if grid[row][col] != color or (row, col) in seen:
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
                                and (next_row, next_col) not in seen
                                and grid[next_row][next_col] == color):
                            seen.add((next_row, next_col))
                            queue.append((next_row, next_col))

                top = min(point[0] for point in component)
                bottom = max(point[0] for point in component)
                left = min(point[1] for point in component)
                right = max(point[1] for point in component)
                missing = None
                for corner_row in (top, bottom):
                    for corner_col in (left, right):
                        if (corner_row, corner_col) not in component:
                            missing = (corner_row, corner_col)

                delta_row = -1 if missing[0] == top else 1
                delta_col = -1 if missing[1] == left else 1
                if color == 2:
                    delta_row = -delta_row
                    delta_col = -delta_col
                for current_row, current_col in component:
                    additions.append((new_color,
                                      current_row + delta_row,
                                      current_col + delta_col))

    for new_color in (4, 3):
        for color, row, col in additions:
            if (color == new_color and 0 <= row < height and 0 <= col < width
                    and grid[row][col] == 7):
                output[row][col] = color

    return output
