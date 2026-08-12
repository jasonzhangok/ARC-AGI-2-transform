def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = set()
    for row in grid:
        for value in row:
            colors.add(value)

    separator = None
    best_score = -1
    for color in colors:
        fullest_row = 0
        for row in grid:
            amount = sum(value == color for value in row)
            if amount > fullest_row:
                fullest_row = amount
        fullest_column = 0
        for column in range(width):
            amount = sum(grid[row][column] == color for row in range(height))
            if amount > fullest_column:
                fullest_column = amount
        score = fullest_row / width + fullest_column / height
        if score > best_score:
            best_score = score
            separator = color

    divider_rows = []
    for row in range(height):
        if sum(grid[row][column] == separator for column in range(width)) >= width - 2:
            divider_rows.append(row)
    divider_columns = []
    for column in range(width):
        if sum(grid[row][column] == separator for row in range(height)) >= height - 2:
            divider_columns.append(column)

    output = [row[:] for row in grid]
    found = False
    for first_row_index in range(len(divider_rows)):
        for second_row_index in range(first_row_index + 1, len(divider_rows)):
            top = divider_rows[first_row_index]
            bottom = divider_rows[second_row_index]
            for first_column_index in range(len(divider_columns)):
                for second_column_index in range(first_column_index + 1,
                                                 len(divider_columns)):
                    left = divider_columns[first_column_index]
                    right = divider_columns[second_column_index]
                    if (grid[top][left] != separator
                            and grid[top][right] != separator
                            and grid[bottom][left] != separator
                            and grid[bottom][right] != separator):
                        output = [row[left:right + 1] for row in grid[top:bottom + 1]]
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if found:
            break
    return output
