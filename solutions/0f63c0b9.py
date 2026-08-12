def transform(grid):
    height, width = len(grid), len(grid[0])
    seeds = sorted(
        (r, value)
        for r, row in enumerate(grid)
        for value in row
        if value != 0
    )
    output = [[0] * width for _ in range(height)]

    for r in range(height):
        seed_row, color = min(seeds, key=lambda seed: (abs(seed[0] - r), seed[0]))
        output[r][0] = color
        output[r][-1] = color

    for r, color in seeds:
        output[r] = [color] * width
    output[0] = [seeds[0][1]] * width
    output[-1] = [seeds[-1][1]] * width
    return output
