def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for color in row:
            if color != 7:
                counts[color] = counts.get(color, 0) + 1

    if not counts:
        size = max(16, height, width)
        return [[7 for col in range(size)] for row in range(size)]
    shape_height = min(counts.values())
    shape_width = max(counts.values())
    size = max(16, height, width, shape_height, shape_width)
    output = [[7 for col in range(size)] for row in range(size)]

    for distance in range(shape_height):
        row = size - 1 - distance
        for col in range(shape_width):
            output[row][col] = 2
        output[row][distance] = 4
        output[row][shape_width - 1 - distance] = 4
    return output
