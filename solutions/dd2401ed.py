def transform(grid):
    height = len(grid)
    width = len(grid[0])
    divider = next(
        col
        for col in range(width)
        if all(grid[row][col] == 5 for row in range(height))
    )
    new_divider = 2 * divider + 1

    output = [row[:] for row in grid]
    for row in range(height):
        output[row][divider] = 0
        output[row][new_divider] = 5

    blue_count = sum(
        grid[row][col] == 1
        for row in range(height)
        for col in range(divider)
    )
    if blue_count % 2 == 1:
        for row in range(height):
            for col in range(divider + 1, new_divider):
                if output[row][col] == 2:
                    output[row][col] = 1

    return output
