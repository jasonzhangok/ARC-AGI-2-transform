def transform(grid):
    colors = {}
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != 0:
                colors[(r + c) % 3] = value
    output = [
        [colors[(r + c) % 3] for c in range(len(grid[0]))]
        for r in range(len(grid))
    ]
    return output
