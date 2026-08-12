def transform(grid):
    height = len(grid)
    width = len(grid[0])
    nonzero = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0:
                nonzero.append((row, col))
    seed_row = min(row for row, col in nonzero)
    seed_col = min(col for row, col in nonzero)
    seed = [[grid[seed_row + row][seed_col + col] for col in range(2)]
            for row in range(2)]

    output = [[0 for col in range(width)] for row in range(height)]
    scale = 1
    while seed_col + 2 * (scale - 1) < width:
        block_top = seed_row - (scale - 1)
        block_left = seed_col + 2 * (scale - 1)
        for block_row in range(2):
            for block_col in range(2):
                top = block_top + block_row * scale
                left = block_left + block_col * scale
                for row in range(max(0, top), min(height, top + scale)):
                    for col in range(max(0, left), min(width, left + scale)):
                        output[row][col] = seed[block_row][block_col]
        scale *= 2
    return output
