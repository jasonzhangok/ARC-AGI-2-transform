def transform(grid):
    output = [row[:] for row in grid]
    markers = [
        (row, col)
        for row in range(len(grid))
        for col in range(len(grid[row]))
        if grid[row][col] == 3
    ]
    top = min(row for row, col in markers)
    bottom = max(row for row, col in markers)
    left = min(col for row, col in markers)
    right = max(col for row, col in markers)
    seed_row, seed_col = next(
        (row, col)
        for row, col in markers
        if top < row < bottom and left < col < right
    )

    for row in range(top + 1, bottom):
        for col in range(left + 1, right):
            if grid[row][col] == 0:
                distance = max(abs(row - seed_row), abs(col - seed_col))
                output[row][col] = 4 if distance % 2 else 2
    return output
