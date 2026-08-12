def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    centers = []

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if (grid[row - 1][col] == 3 and grid[row + 1][col] == 3 and
                    grid[row][col - 1] == 3 and grid[row][col + 1] == 3):
                centers.append((row, col, grid[row][col]))

    for row, col, color in centers:
        for direction in (-1, 1):
            current = col + 2 * direction
            while 0 <= current < width and grid[row][current] == 0:
                output[row][current] = color
                current += direction

    for row, col, color in centers:
        for direction in (-1, 1):
            current = row + 2 * direction
            while 0 <= current < height and grid[current][col] == 0:
                output[current][col] = color
                current += direction

    return output
