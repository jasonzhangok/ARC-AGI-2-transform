def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    blocks = [
        ((0, 1), (0, 1)),
        ((0, 1), (width - 2, width - 1)),
        ((height - 2, height - 1), (0, 1)),
        ((height - 2, height - 1), (width - 2, width - 1)),
    ]
    counts = []
    for rows, cols in blocks:
        count = {}
        for row in rows:
            for col in cols:
                if grid[row][col] != 7:
                    count[grid[row][col]] = count.get(grid[row][col], 0) + 1
        counts.append(count)

    colors = set().union(*counts)
    target = {color: max(count.get(color, 0) for count in counts) for color in colors}
    for (rows, cols), count in zip(blocks, counts):
        missing = []
        for color, amount in target.items():
            missing.extend([color] * (amount - count.get(color, 0)))
        holes = [
            (row, col)
            for row in rows
            for col in cols
            if grid[row][col] == 7
        ]
        for (row, col), color in zip(holes, missing):
            output[row][col] = color

    return output
