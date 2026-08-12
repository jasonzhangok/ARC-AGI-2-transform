def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [[0] * width for _ in range(height)]
    seen = set()

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 2 or (row, col) in seen:
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
                            and grid[next_row][next_col] == 2):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))

            top = min(r for r, _ in component)
            bottom = max(r for r, _ in component)
            left = min(c for _, c in component)
            right = max(c for _, c in component)
            if bottom - top >= 2 and right - left >= 2:
                for inner_row in range(top + 1, bottom):
                    for inner_col in range(left + 1, right):
                        output[inner_row][inner_col] = 3
    return output
