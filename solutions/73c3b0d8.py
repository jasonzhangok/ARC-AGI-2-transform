def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    line_row = -1
    points = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 2:
                line_row = row
            elif grid[row][col] == 4:
                points.append((row, col))
                output[row][col] = 0

    for row, col in points:
        shifted_row = row + 1
        if shifted_row < height:
            output[shifted_row][col] = 4
        if row == line_row - 2:
            step = 1
            while shifted_row - step >= 0:
                branch_row = shifted_row - step
                left_col = col - step
                right_col = col + step
                if left_col >= 0:
                    output[branch_row][left_col] = 4
                if right_col < width:
                    output[branch_row][right_col] = 4
                step += 1
    return output
