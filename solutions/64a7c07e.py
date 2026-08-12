def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [[0 for col in range(width)] for row in range(height)]
    seen = set()
    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == 0:
                continue
            if (start_row, start_col) in seen:
                continue
            component = []
            stack = [(start_row, start_col)]
            seen.add((start_row, start_col))
            while stack:
                row, col = stack.pop()
                component.append((row, col, grid[row][col]))
                for row_offset in (-1, 0, 1):
                    for col_offset in (-1, 0, 1):
                        next_row = row + row_offset
                        next_col = col + col_offset
                        if 0 <= next_row < height and 0 <= next_col < width:
                            if (next_row, next_col) not in seen:
                                if grid[next_row][next_col] != 0:
                                    seen.add((next_row, next_col))
                                    stack.append((next_row, next_col))
            left = min(col for row, col, color in component)
            right = max(col for row, col, color in component)
            object_width = right - left + 1
            for row, col, color in component:
                output[row][col + object_width] = color
    return output
