def transform(grid):
    height, width = len(grid), len(grid[0])
    horizontal_lines = [
        row for row in range(height) if all(value == 8 for value in grid[row])
    ]
    vertical_lines = [
        col
        for col in range(width)
        if all(grid[row][col] == 8 for row in range(height))
    ]
    markers = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 2
    ]
    output = [row[:] for row in grid]
    crossings = []

    for row, col in markers:
        if horizontal_lines:
            above = [line for line in horizontal_lines if line < row]
            below = [line for line in horizontal_lines if line > row]
            endpoints = ([max(above)] if above else []) + ([min(below)] if below else [])
            for line in endpoints:
                for current_row in range(min(row, line), max(row, line) + 1):
                    output[current_row][col] = 2
                crossings.append((line, col))
        else:
            left = [line for line in vertical_lines if line < col]
            right = [line for line in vertical_lines if line > col]
            endpoints = ([max(left)] if left else []) + ([min(right)] if right else [])
            for line in endpoints:
                for current_col in range(min(col, line), max(col, line) + 1):
                    output[row][current_col] = 2
                crossings.append((row, line))

    for row, col in crossings:
        for current_row in range(row - 1, row + 2):
            for current_col in range(col - 1, col + 2):
                output[current_row][current_col] = 8
        output[row][col] = 2
    return output
