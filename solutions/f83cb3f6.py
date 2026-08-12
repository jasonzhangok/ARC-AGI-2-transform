def transform(grid):
    height, width = len(grid), len(grid[0])
    horizontal_row = max(
        range(height), key=lambda row: sum(value == 8 for value in grid[row])
    )
    vertical_col = max(
        range(width), key=lambda col: sum(grid[row][col] == 8 for row in range(height))
    )
    horizontal = sum(value == 8 for value in grid[horizontal_row]) >= sum(
        grid[row][vertical_col] == 8 for row in range(height)
    )
    output = [[0] * width for _ in range(height)]

    if horizontal:
        for col, value in enumerate(grid[horizontal_row]):
            output[horizontal_row][col] = value
        for row in range(height):
            for col in range(width):
                color = grid[row][col]
                if color not in (0, 8) and grid[horizontal_row][col] == 8:
                    destination_row = horizontal_row - 1 if row < horizontal_row else horizontal_row + 1
                    output[destination_row][col] = color
    else:
        line_rows = [row for row in range(height) if grid[row][vertical_col] == 8]
        for row in line_rows:
            output[row][vertical_col] = 8
        for row in range(min(line_rows), max(line_rows) + 1):
            for col in range(width):
                color = grid[row][col]
                if color not in (0, 8):
                    destination_col = vertical_col - 1 if col < vertical_col else vertical_col + 1
                    output[row][destination_col] = color
    return output
