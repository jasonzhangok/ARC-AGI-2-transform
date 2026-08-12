def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = set()
    for row in grid:
        for value in row:
            if value != 0 and value != 8:
                colors.add(value)

    separator_rows = []
    for row in range(height):
        if all(grid[row][column] != 8 for column in range(width)):
            separator_rows.append(row)
    separator_columns = []
    for column in range(width):
        if all(grid[row][column] != 8 for row in range(height)):
            separator_columns.append(column)

    output = [row[:] for row in grid]
    for color in colors:
        markers = []
        for row in range(height):
            for column in range(width):
                if grid[row][column] == color:
                    markers.append((row, column))

        minimum_row = min(row for row, column in markers)
        maximum_row = max(row for row, column in markers)
        minimum_column = min(column for row, column in markers)
        maximum_column = max(column for row, column in markers)
        top = max(row for row in separator_rows if row <= minimum_row)
        bottom = min(row for row in separator_rows if row >= maximum_row)
        left = max(column for column in separator_columns if column <= minimum_column)
        right = min(column for column in separator_columns if column >= maximum_column)

        for column in range(left, right + 1):
            if output[top][column] == 0:
                output[top][column] = color
            if output[bottom][column] == 0:
                output[bottom][column] = color
        for row in range(top, bottom + 1):
            if output[row][left] == 0:
                output[row][left] = color
            if output[row][right] == 0:
                output[row][right] = color

        for row in range(top + 1, bottom):
            for column in range(left + 1, right):
                if (grid[row][column] == 0
                        and grid[row - 1][column] == 8
                        and grid[row + 1][column] == 8
                        and grid[row][column - 1] == 8
                        and grid[row][column + 1] == 8):
                    output[row][column] = color
    return output
