def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    colors = list(counts)
    target = set()
    target_rows = []
    target_columns = []
    for first_index in range(len(colors)):
        for second_index in range(first_index + 1, len(colors)):
            pair = {colors[first_index], colors[second_index]}
            rows = []
            for row in range(height):
                if any(grid[row][column] in pair for column in range(width)):
                    rows.append(row)
            columns = []
            for column in range(width):
                if any(grid[row][column] in pair for row in range(height)):
                    columns.append(column)
            if (len(rows) == len(columns)
                    and counts[colors[first_index]] + counts[colors[second_index]]
                    == len(rows) * len(columns)):
                target = pair
                target_rows = rows
                target_columns = columns

    output = []
    for row in target_rows:
        output.append([grid[row][column] for column in target_columns])
    return output
