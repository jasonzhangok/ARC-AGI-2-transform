def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    seed_cells = []
    for row in range(height):
        for column in range(width):
            if grid[row][column] == 2:
                seed_cells.append((row, column))
    if not seed_cells:
        return output
    seed_row = max(cell[0] for cell in seed_cells)
    seed_columns = []
    for row, column in seed_cells:
        if row == seed_row:
            seed_columns.append(column)
    left = min(seed_columns)
    right = max(seed_columns)
    first_row = True

    for row in range(seed_row - 1, -1, -1):
        previous_right = right
        if first_row:
            right += 1
            first_row = False
        else:
            left += 1
            right += 1

        obstacle_columns = set()
        for column in range(width):
            if grid[row][column] == 1:
                obstacle_columns.add(column)
        overlap = []
        for column in obstacle_columns:
            if left <= column <= right:
                overlap.append(column)
        if overlap:
            block_right = max(overlap)
            while block_right + 1 in obstacle_columns:
                block_right += 1
            new_left = block_right + 1
            new_right = new_left + right - left
            for column in range(previous_right + 1, new_left + 1):
                if (0 <= column < width
                        and output[row + 1][column] == 0):
                    output[row + 1][column] = 2
            left = new_left
            right = new_right

        for column in range(left, right + 1):
            if 0 <= column < width and output[row][column] == 0:
                output[row][column] = 2
    return output
