def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    markers = [
        (row, col, grid[row][col])
        for row in range(0, height, 5)
        for col in range(0, width, 5)
        if grid[row][col] != 0
    ]
    ring = {
        (1, 2), (1, 3),
        (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 1), (3, 2), (3, 3), (3, 4),
        (4, 2), (4, 3),
    }
    for row, col, color in markers:
        output[row][col] = 0
        for dr, dc in ring:
            y, x = row + dr, col + dc
            if 0 <= y < height and 0 <= x < width:
                output[y][x] = color
    return output
