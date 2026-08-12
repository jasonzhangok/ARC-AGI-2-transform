def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    if all(grid[row][0] == 0 for row in range(height)):
        side = "left"
    elif all(grid[row][width - 1] == 0 for row in range(height)):
        side = "right"
    elif all(grid[0][col] == 0 for col in range(width)):
        side = "top"
    else:
        side = "bottom"

    ray_count = height if side == "left" or side == "right" else width
    ray_depth = width if side == "left" or side == "right" else height
    for position in range(ray_count):
        run = 0
        for distance in range(1, ray_depth):
            if side == "left":
                row, col = position, distance
            elif side == "right":
                row, col = position, width - 1 - distance
            elif side == "top":
                row, col = distance, position
            else:
                row, col = height - 1 - distance, position
            if grid[row][col] == 8:
                run += 1
            else:
                break

        if run == 1 and ray_depth > 2:
            if side == "left":
                row, col = position, 2
            elif side == "right":
                row, col = position, width - 3
            elif side == "top":
                row, col = 2, position
            else:
                row, col = height - 3, position
            output[row][col] = 8
        elif run > 1:
            for distance in range(1, run + 1):
                if side == "left":
                    row, col = position, distance
                    opposite_row, opposite_col = position, width - distance
                elif side == "right":
                    row, col = position, width - 1 - distance
                    opposite_row, opposite_col = position, distance - 1
                elif side == "top":
                    row, col = distance, position
                    opposite_row, opposite_col = height - distance, position
                else:
                    row, col = height - 1 - distance, position
                    opposite_row, opposite_col = distance - 1, position
                output[row][col] = 7
                output[opposite_row][opposite_col] = 0
    return output
