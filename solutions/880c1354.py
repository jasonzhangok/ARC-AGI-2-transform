def transform(grid):
    fixed_cells = [
        (row, col)
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] == 4
    ]
    center_row = sum(row for row, _ in fixed_cells) / len(fixed_cells)
    center_col = sum(col for _, col in fixed_cells) / len(fixed_cells)
    moving_colors = sorted({value for row in grid for value in row} - {4, 7})

    centers = {}
    for color in moving_colors:
        cells = [
            (row, col)
            for row in range(len(grid))
            for col in range(len(grid[0]))
            if grid[row][col] == color
        ]
        row = sum(r for r, _ in cells) / len(cells)
        col = sum(c for _, c in cells) / len(cells)
        centers[color] = (row - center_row, col - center_col)
    clockwise = []
    remaining = moving_colors[:]
    while remaining:
        best = 0
        for index in range(1, len(remaining)):
            ay, ax = centers[remaining[best]]
            by, bx = centers[remaining[index]]
            ah = 0 if ay < 0 or ay == 0 and ax >= 0 else 1
            bh = 0 if by < 0 or by == 0 and bx >= 0 else 1
            cross = ax * by - ay * bx
            if bh < ah or bh == ah and cross < 0:
                best = index
        clockwise.append(remaining.pop(best))
    replacement = {
        color: clockwise[(index - 1) % len(clockwise)]
        for index, color in enumerate(clockwise)
    }
    output = [[replacement.get(value, value) for value in row] for row in grid]
    return output
