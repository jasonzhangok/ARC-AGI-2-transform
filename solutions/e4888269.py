def transform(grid):
    height, width = len(grid), len(grid[0])
    divider = next(
        col
        for col in range(width)
        if all(grid[row][col] == 2 for row in range(height))
    )
    output = [row[:] for row in grid]

    for legend_row in grid:
        source, target = legend_row[0], legend_row[1]
        if source == 0 or target == 0:
            continue
        for row in range(height):
            for col in range(divider + 1, width):
                if output[row][col] == source:
                    output[row][col] = target
    return output
