def transform(grid):
    output = [row[:] for row in grid]
    points = {
        value: (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value != 0
    }
    yellow_r, yellow_c = points[4]
    green_r, green_c = points[3]
    red_r, red_c = points[2]

    for c in range(min(yellow_c, green_c), max(yellow_c, green_c) + 1):
        if output[yellow_r][c] == 0:
            output[yellow_r][c] = 5
    for r in range(min(yellow_r, green_r), max(yellow_r, green_r) + 1):
        if output[r][green_c] == 0:
            output[r][green_c] = 5

    for r in range(min(yellow_r, red_r), max(yellow_r, red_r) + 1):
        if output[r][yellow_c] == 0:
            output[r][yellow_c] = 5
    for c in range(min(yellow_c, red_c), max(yellow_c, red_c) + 1):
        if output[red_r][c] == 0:
            output[red_r][c] = 5
    return output
