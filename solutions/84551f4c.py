def transform(grid):
    height = len(grid)
    width = len(grid[0])
    bars = {}
    for col in range(width):
        bottom_color = grid[height - 1][col]
        if bottom_color == 0:
            continue
        top = height - 1
        while top > 0 and grid[top - 1][col] == bottom_color:
            top -= 1
        bar_height = height - top
        bars[col] = (bottom_color, bar_height, top)

    falling = set()
    pending = []
    for col in bars:
        if bars[col][0] == 1:
            pending.append(col)
    while pending:
        col = pending.pop()
        if col in falling:
            continue
        falling.add(col)
        next_col = col + bars[col][1]
        if next_col in bars and next_col not in falling:
            pending.append(next_col)

    output = [row[:] for row in grid]
    for col in falling:
        color, bar_height, top = bars[col]
        for row in range(top, height):
            output[row][col] = 0
    for col in falling:
        color, bar_height, top = bars[col]
        for target_col in range(col, min(width, col + bar_height)):
            output[height - 1][target_col] = color
    return output
