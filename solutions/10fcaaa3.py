def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [
        [grid[r % height][c % width] for c in range(2 * width)]
        for r in range(2 * height)
    ]
    colored = [
        (r, c)
        for r, row in enumerate(output)
        for c, value in enumerate(row)
        if value != 0
    ]
    for r, c in colored:
        for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            rr, cc = r + dr, c + dc
            if 0 <= rr < 2 * height and 0 <= cc < 2 * width and output[rr][cc] == 0:
                output[rr][cc] = 8
    return output
