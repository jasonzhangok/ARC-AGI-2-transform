def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] != 4:
                continue
            if (start_row, start_col) in seen:
                continue
            component = []
            stack = [(start_row, start_col)]
            seen.add((start_row, start_col))
            while stack:
                row, col = stack.pop()
                component.append((row, col))
                for row_offset in (-1, 0, 1):
                    for col_offset in (-1, 0, 1):
                        next_row = row + row_offset
                        next_col = col + col_offset
                        if 0 <= next_row < height and 0 <= next_col < width:
                            if (next_row, next_col) not in seen:
                                if grid[next_row][next_col] == 4:
                                    seen.add((next_row, next_col))
                                    stack.append((next_row, next_col))
            top = min(row for row, col in component)
            bottom = max(row for row, col in component)
            left = min(col for row, col in component)
            right = max(col for row, col in component)
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    if output[row][col] == 0:
                        output[row][col] = 7
    return output
