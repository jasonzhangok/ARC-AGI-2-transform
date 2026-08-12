def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    rectangles = []

    for row in range(height):
        for column in range(width):
            if grid[row][column] != 3 or (row, column) in seen:
                continue
            stack = [(row, column)]
            seen.add((row, column))
            cells = []
            while stack:
                current_row, current_column = stack.pop()
                cells.append((current_row, current_column))
                for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = current_row + row_step
                    next_column = current_column + column_step
                    if (0 <= next_row < height and 0 <= next_column < width
                            and (next_row, next_column) not in seen
                            and grid[next_row][next_column] == 3):
                        seen.add((next_row, next_column))
                        stack.append((next_row, next_column))
            top = min(cell[0] for cell in cells)
            bottom = max(cell[0] for cell in cells)
            left = min(cell[1] for cell in cells)
            right = max(cell[1] for cell in cells)
            rectangles.append((top, left, bottom - top + 1, right - left + 1))

    output = [row[:] for row in grid]
    for top, left, rectangle_height, rectangle_width in rectangles:
        for direction in (-1, 1):
            step = 0
            while top + step * rectangle_height < height:
                copy_left = left + direction * step * rectangle_width
                if copy_left >= width or copy_left + rectangle_width <= 0:
                    break
                copy_top = top + step * rectangle_height
                copy_bottom = min(height, copy_top + rectangle_height)
                first_column = max(0, copy_left)
                last_column = min(width, copy_left + rectangle_width)
                for row in range(copy_top, copy_bottom):
                    for column in range(first_column, last_column):
                        output[row][column] = 3
                step += 1
    return output
