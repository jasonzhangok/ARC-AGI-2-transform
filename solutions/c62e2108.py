def transform(grid):
    height = len(grid)
    width = len(grid[0])
    color = next(
        value for row in grid for value in row if value not in (0, 1)
    )
    markers = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 1
    ]
    seen = set()
    sources = []

    for row in range(height):
        for col in range(width):
            if grid[row][col] != color or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            component = []
            while stack:
                cur_row, cur_col = stack.pop()
                component.append((cur_row, cur_col))
                for d_row, d_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row = cur_row + d_row
                    next_col = cur_col + d_col
                    if (0 <= next_row < height and 0 <= next_col < width
                            and (next_row, next_col) not in seen
                            and grid[next_row][next_col] == color):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))
            top = min(r for r, _ in component)
            left = min(c for _, c in component)
            pattern = {(r - top, c - left) for r, c in component}
            sources.append((top, left, pattern))

    output = [[0] * width for _ in range(height)]

    for top, left, pattern in sources:
        for pattern_row, pattern_col in pattern:
            row = top + pattern_row
            col = left + pattern_col
            if 0 <= row < height and 0 <= col < width:
                output[row][col] = color
        directions = []
        if any(top <= row < top + 4 and col < left for row, col in markers):
            directions.append((0, -4))
        if any(top <= row < top + 4 and col > left + 3 for row, col in markers):
            directions.append((0, 4))
        if any(left <= col < left + 4 and row < top for row, col in markers):
            directions.append((-4, 0))
        if any(left <= col < left + 4 and row > top + 3 for row, col in markers):
            directions.append((4, 0))

        for d_row, d_col in directions:
            next_top = top + d_row
            next_left = left + d_col
            while (next_top < height and next_left < width
                   and next_top + 3 >= 0 and next_left + 3 >= 0):
                for pattern_row, pattern_col in pattern:
                    row = next_top + pattern_row
                    col = next_left + pattern_col
                    if 0 <= row < height and 0 <= col < width:
                        output[row][col] = color
                next_top += d_row
                next_left += d_col
    return output
