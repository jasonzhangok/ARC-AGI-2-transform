def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    seed_row, seed_col = next(
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 1
    )
    walls = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 2
    ]
    top = min(row for row, _ in walls)
    bottom = max(row for row, _ in walls)
    left = min(col for _, col in walls)
    right = max(col for _, col in walls)
    output[seed_row][seed_col] = 0

    if not left < seed_col < right:
        output[-1] = [1] * width
        return output

    region = set()
    stack = [(top, seed_col)]
    while stack:
        row, col = stack.pop()
        if ((row, col) in region
                or not (top <= row < bottom and left < col < right)
                or grid[row][col] == 2):
            continue
        region.add((row, col))
        stack.extend(((row - 1, col), (row + 1, col),
                      (row, col - 1), (row, col + 1)))

    leaks = any(
        grid[bottom][col] == 0
        for row, col in region
        if row == bottom - 1
    )
    if leaks:
        output[-1] = [1] * width
    else:
        for row, col in region:
            output[row][col] = 1
    return output
