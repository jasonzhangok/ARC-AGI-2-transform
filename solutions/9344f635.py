def transform(grid):
    height = len(grid)
    width = len(grid[0])
    color_counts = {}
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            color_counts[color] = color_counts.get(color, 0) + 1
    background = 0
    background_count = -1
    for color in color_counts:
        if color_counts[color] > background_count:
            background = color
            background_count = color_counts[color]

    seen = set()
    horizontal_lines = []
    vertical_lines = []
    for start_row in range(height):
        for start_col in range(width):
            color = grid[start_row][start_col]
            if color == background or (start_row, start_col) in seen:
                continue
            component = []
            stack = [(start_row, start_col)]
            seen.add((start_row, start_col))
            while stack:
                row, col = stack.pop()
                component.append((row, col))
                for next_row, next_col in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ):
                    if 0 <= next_row < height and 0 <= next_col < width:
                        if (next_row, next_col) not in seen:
                            if grid[next_row][next_col] == color:
                                seen.add((next_row, next_col))
                                stack.append((next_row, next_col))
            rows = set(row for row, col in component)
            cols = set(col for row, col in component)
            if len(rows) == 1:
                horizontal_lines.append((next(iter(rows)), color))
            elif len(cols) == 1:
                vertical_lines.append((next(iter(cols)), color))

    output = [row[:] for row in grid]
    for col, color in vertical_lines:
        for row in range(height):
            output[row][col] = color
    for row, color in horizontal_lines:
        for col in range(width):
            output[row][col] = color
    return output
