def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    bars = []
    order = 0

    for row in range(height):
        for col in range(width):
            frame_color = grid[row][col]
            if frame_color in (0, 5) or (row, col) in seen:
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
                            and grid[next_row][next_col] == frame_color):
                        seen.add((next_row, next_col))
                        queue.append((next_row, next_col))

            top = min(point[0] for point in component)
            bottom = max(point[0] for point in component)
            left = min(point[1] for point in component)
            right = max(point[1] for point in component)
            marker_count = 0
            for inner_row in range(top + 1, bottom):
                for inner_col in range(left + 1, right):
                    if grid[inner_row][inner_col] == 5:
                        marker_count += 1
            bars.append((marker_count, order, frame_color))
            order += 1

    bars.sort()
    max_length = max(bar[0] for bar in bars)
    output = []
    for length, _, color in bars:
        output.append([color if col < length else 0
                       for col in range(max_length)])
    return output
