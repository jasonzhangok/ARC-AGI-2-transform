def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    if all(color == 9 for color in grid[0]):
        row_step = -1
        col_step = 0
    elif all(color == 9 for color in grid[height - 1]):
        row_step = 1
        col_step = 0
    elif all(grid[row][0] == 9 for row in range(height)):
        row_step = 0
        col_step = -1
    else:
        row_step = 0
        col_step = 1

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 8:
                continue
            neighbors = []
            for neighbor_row, neighbor_col in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if 0 <= neighbor_row < height and 0 <= neighbor_col < width:
                    neighbors.append(grid[neighbor_row][neighbor_col])
            if 2 in neighbors:
                output[row][col] = 2
            else:
                target_row = row + row_step
                target_col = col + col_step
                if 0 <= target_row < height and 0 <= target_col < width and grid[target_row][target_col] == 7:
                    output[target_row][target_col] = 8

    return output
