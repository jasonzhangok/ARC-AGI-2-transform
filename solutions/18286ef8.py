def transform(grid):
    height, width = len(grid), len(grid[0])
    fives = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 5]
    top, bottom = min(r for r, _ in fives), max(r for r, _ in fives)
    left, right = min(c for _, c in fives), max(c for _, c in fives)
    center_row, center_col = (top + bottom) // 2, (left + right) // 2
    six_row, six_col = next(
        (r, c) for r in range(height) for c in range(width) if grid[r][c] == 6
    )
    dr = -1 if six_row < top else 1 if six_row > bottom else 0
    dc = -1 if six_col < left else 1 if six_col > right else 0
    output = [row[:] for row in grid]
    for row in range(top, bottom + 1):
        for col in range(left, right + 1):
            if output[row][col] == 9:
                output[row][col] = 5
    output[center_row + dr][center_col + dc] = 9
    output[six_row][six_col] = 9
    return output
