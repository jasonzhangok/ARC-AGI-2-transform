def transform(grid):
    height = len(grid)
    width = len(grid[0])
    obstacle_row = 0
    for row in range(height):
        if 2 in grid[row]:
            obstacle_row = row
            break

    beam_columns = set()
    for row in range(obstacle_row):
        for col in range(width):
            if grid[row][col] == 8:
                beam_columns.add(col)

    output = [row[:] for row in grid]
    for col in beam_columns:
        for row in range(obstacle_row):
            output[row][col] = 8
        if grid[obstacle_row][col] != 2:
            for row in range(obstacle_row, height):
                if output[row][col] != 2:
                    output[row][col] = 8
            continue

        left = col
        right = col
        while left > 0 and grid[obstacle_row][left - 1] == 2:
            left -= 1
        while right + 1 < width and grid[obstacle_row][right + 1] == 2:
            right += 1
        left_target = left - 1
        right_target = right + 1
        if left_target < 0:
            target = right_target
        elif right_target >= width:
            target = left_target
        elif col - left_target < right_target - col:
            target = left_target
        else:
            target = right_target

        for other_col in range(min(col, target), max(col, target) + 1):
            output[obstacle_row - 1][other_col] = 8
        for row in range(obstacle_row, height):
            if output[row][target] != 2:
                output[row][target] = 8
    return output
