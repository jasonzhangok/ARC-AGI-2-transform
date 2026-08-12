def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    objects = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for next_row, next_col in ((current_row - 1, current_col), (current_row + 1, current_col), (current_row, current_col - 1), (current_row, current_col + 1)):
                    if 0 <= next_row < height and 0 <= next_col < width and grid[next_row][next_col] != 0 and (next_row, next_col) not in seen:
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))
            rows = [cell[0] for cell in cells]
            cols = [cell[1] for cell in cells]
            if len(cells) == 4 and max(rows) - min(rows) == 1 and max(cols) - min(cols) == 1:
                colors = set()
                for object_row, object_col in cells:
                    colors.add(grid[object_row][object_col])
                objects.append((max(rows), min(cols), max(cols), len(colors)))

    output = [row[:] for row in grid]
    for bottom, left, right, tail_height in objects:
        for row in range(bottom + 1, min(height, bottom + tail_height + 1)):
            for col in range(left, right + 1):
                if output[row][col] == 0:
                    output[row][col] = 3
    return output
