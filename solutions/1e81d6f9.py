def transform(grid):
    height, width = len(grid), len(grid[0])
    fives = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 5]
    top, bottom = min(r for r, _ in fives), max(r for r, _ in fives)
    left, right = min(c for _, c in fives), max(c for _, c in fives)
    reference_points = [
        (r, c)
        for r in range(top, bottom + 1)
        for c in range(left, right + 1)
        if grid[r][c] not in (0, 5)
    ]
    reference_color = grid[reference_points[0][0]][reference_points[0][1]]
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] == reference_color and (row, col) not in reference_points:
                output[row][col] = 0
    return output
