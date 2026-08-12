def transform(grid):
    output = [row[:] for row in grid]
    height = len(grid)
    width = len(grid[0]) if height else 0
    marks = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                marks.append((row, col))
    if not marks:
        return output
    top = min(row for row, col in marks)
    bottom = max(row for row, col in marks)
    left = min(col for row, col in marks)
    right = max(col for row, col in marks)
    box_height = bottom - top + 1
    box_width = right - left + 1
    horizontal_lines = []
    for row in range(top, bottom + 1):
        count = 0
        for col in range(left, right + 1):
            if grid[row][col] == 1:
                count += 1
        if count * 2 > box_width:
            horizontal_lines.append(row)
    vertical_lines = []
    for col in range(left, right + 1):
        count = 0
        for row in range(top, bottom + 1):
            if grid[row][col] == 1:
                count += 1
        if count * 2 > box_height:
            vertical_lines.append(col)
    for row in horizontal_lines:
        for col in range(left, right + 1):
            if output[row][col] == 0:
                output[row][col] = 2
    for col in vertical_lines:
        for row in range(top, bottom + 1):
            if output[row][col] == 0:
                output[row][col] = 2
    return output
