def transform(grid):
    colors = sorted({value for row in grid for value in row if value != 0})
    layers = []
    for color in colors:
        cells = [
            (row, col)
            for row, line in enumerate(grid)
            for col, value in enumerate(line)
            if value == color
        ]
        height = max(row for row, _ in cells) - min(row for row, _ in cells) + 1
        width = max(col for _, col in cells) - min(col for _, col in cells) + 1
        layers.append((max(height, width), color, min(height, width)))
    layers.sort()

    inner_size = layers[0][2]
    size = inner_size + 2 * (len(layers) - 1)
    output = [[layers[-1][1]] * size for _ in range(size)]
    for layer, (_, color, _) in enumerate(reversed(layers)):
        for row in range(layer, size - layer):
            for col in range(layer, size - layer):
                if (layer == len(layers) - 1
                        or row in (layer, size - 1 - layer)
                        or col in (layer, size - 1 - layer)):
                    output[row][col] = color
    return output
