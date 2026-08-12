def transform(grid):
    height, width = len(grid), len(grid[0])
    distance = sum(value == 5 for row in grid for value in row)
    color = next(value for row in grid for value in row if value not in (0, 5))
    horizontal_row = next(
        row for row in range(height) if all(value == color for value in grid[row])
    )
    vertical_col = next(
        col
        for col in range(width)
        if all(grid[row][col] == color for row in range(height))
    )

    output = [[0] * width for _ in range(height)]
    for col in range(width):
        output[horizontal_row + distance][col] = color
    for row in range(height):
        output[row][vertical_col - distance] = color
    return output
