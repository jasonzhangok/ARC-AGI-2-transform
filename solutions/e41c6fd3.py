def transform(grid):
    height, width = len(grid), len(grid[0])
    reference_top = min(
        row
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 8
    )
    output = [[0] * width for _ in range(height)]

    colors = {value for row in grid for value in row if value != 0}
    for color in colors:
        cells = [
            (row, col)
            for row in range(height)
            for col in range(width)
            if grid[row][col] == color
        ]
        offset = reference_top - min(row for row, _ in cells)
        for row, col in cells:
            output[row + offset][col] = color
    return output
