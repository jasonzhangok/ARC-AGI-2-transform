def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    for top in range(height - 1):
        for bottom in range(top + 1, height):
            for left in range(width - 1):
                for right in range(left + 1, width):
                    if not all(
                        grid[row][column] != 0
                        for row in range(top, bottom + 1)
                        for column in range(left, right + 1)
                    ):
                        continue
                    if not any(grid[top][column] == 2 for column in range(left, right + 1)):
                        continue
                    if not any(grid[bottom][column] == 2 for column in range(left, right + 1)):
                        continue
                    if not any(grid[row][left] == 2 for row in range(top, bottom + 1)):
                        continue
                    if not any(grid[row][right] == 2 for row in range(top, bottom + 1)):
                        continue

                    for row in range(top, bottom + 1):
                        for column in range(left, right + 1):
                            if grid[row][column] != 2:
                                output[row][column] = 4

    return output
