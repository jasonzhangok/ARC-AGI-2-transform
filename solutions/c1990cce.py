def transform(grid):
    width = len(grid[0])
    source_col = 0
    source_color = 0
    for col in range(width):
        if grid[0][col] != 0:
            source_col = col
            source_color = grid[0][col]

    result = [[0] * width for _ in range(width)]
    for row in range(width):
        for col in range(width):
            if col == source_col - row or col == source_col + row:
                result[row][col] = source_color
            elif abs(col - source_col) < row and (col - row - source_col) % 4 == 0:
                result[row][col] = 1
    output = result
    return output
