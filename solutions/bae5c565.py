def transform(grid):
    height = len(grid)
    width = len(grid[0])

    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)

    strip_row = 0
    strip_score = -1
    for row in range(height):
        score = sum(value != background for value in grid[row])
        if score > strip_score:
            strip_score = score
            strip_row = row

    axis = 0
    axis_score = -1
    for column in range(width):
        score = sum(
            row != strip_row and grid[row][column] == 8
            for row in range(height)
        )
        if score > axis_score:
            axis_score = score
            axis = column

    start = min(
        row
        for row in range(height)
        if row != strip_row and grid[row][axis] == 8
    )
    strip = grid[strip_row][:]
    output = [[background for _ in range(width)] for _ in range(height)]

    for row in range(start, height):
        radius = row - start
        left = max(0, axis - radius)
        right = min(width - 1, axis + radius)
        for column in range(left, right + 1):
            output[row][column] = strip[column]
        output[row][axis] = 8

    return output
