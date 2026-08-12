def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    pivot = next(
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 5
    )
    segment = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 2
    ]

    for row, col in segment:
        output[row][col] = 3

    first_row, first_col = segment[0]
    d_row = (first_row > pivot[0]) - (first_row < pivot[0])
    d_col = (first_col > pivot[1]) - (first_col < pivot[1])
    rotated_row, rotated_col = d_col, -d_row
    for distance in range(1, len(segment) + 1):
        row = pivot[0] + distance * rotated_row
        col = pivot[1] + distance * rotated_col
        output[row][col] = 2
    return output
