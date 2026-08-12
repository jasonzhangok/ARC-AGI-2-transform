def transform(grid):
    height = len(grid)
    width = len(grid[0])
    marker = []
    shape = []
    for row in range(height):
        for column in range(width):
            if grid[row][column] == 6:
                marker.append((row, column))
            elif grid[row][column] == 4:
                shape.append((row, column))

    center_row = 0
    largest_row_count = -1
    for row in range(height):
        count = sum(grid[row][column] == 6 for column in range(width))
        if count > largest_row_count:
            largest_row_count = count
            center_row = row
    center_column = 0
    largest_column_count = -1
    for column in range(width):
        count = sum(grid[row][column] == 6 for row in range(height))
        if count > largest_column_count:
            largest_column_count = count
            center_column = column

    up = center_row - min(row for row, column in marker if column == center_column)
    down = max(row for row, column in marker if column == center_column) - center_row
    left = center_column - min(column for row, column in marker if row == center_row)
    right = max(column for row, column in marker if row == center_row) - center_column
    arms = [up, down, left, right]
    longest = arms.index(max(arms))

    top = min(row for row, column in shape)
    bottom = max(row for row, column in shape)
    left_edge = min(column for row, column in shape)
    right_edge = max(column for row, column in shape)
    output = [row[:] for row in grid]
    for row, column in marker:
        output[row][column] = 0
    for row, column in shape:
        if longest == 0:
            new_row = row
            new_column = 2 * left_edge - 1 - column
        elif longest == 1:
            new_row = row
            new_column = 2 * right_edge + 1 - column
        elif longest == 2:
            new_row = 2 * bottom + 1 - row
            new_column = column
        else:
            new_row = 2 * top - 1 - row
            new_column = column
        if 0 <= new_row < height and 0 <= new_column < width:
            output[new_row][new_column] = 4
    return output
