def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for color in row:
            if color != 0:
                counts[color] = counts.get(color, 0) + 1

    main_color = max(counts, key=counts.get)
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] == main_color:
                output[row][width - 1 - col] = main_color

    return output
