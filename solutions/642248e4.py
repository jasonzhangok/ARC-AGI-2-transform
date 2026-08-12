def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    horizontal = (
        grid[0][0] != 0 and grid[-1][0] != 0 and
        all(value == grid[0][0] for value in grid[0]) and
        all(value == grid[-1][0] for value in grid[-1])
    )

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 1:
                continue
            if horizontal:
                if row < height - 1 - row:
                    output[row - 1][col] = grid[0][col]
                else:
                    output[row + 1][col] = grid[-1][col]
            else:
                if col < width - 1 - col:
                    output[row][col - 1] = grid[row][0]
                else:
                    output[row][col + 1] = grid[row][-1]
    return output
