def transform(grid):
    height = len(grid)
    width = len(grid[0])
    base_row = next(
        row for row in range(height)
        if all(value == 8 for value in grid[row])
    )
    seen = set()
    bars = []

    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            if color in (0, 8) or (row, col) in seen:
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
            bars.append((len(component), color))

    bars.sort()
    output = [[0] * width for _ in range(height)]
    output[base_row] = [8] * width
    first_row = base_row - len(bars)
    for offset, (length, color) in enumerate(bars):
        row = first_row + offset
        for col in range(width - length, width):
            output[row][col] = color
    return output
