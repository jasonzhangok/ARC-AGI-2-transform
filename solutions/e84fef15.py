from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    separator_rows = {
        row for row in range(height) if all(value == 3 for value in grid[row])
    }
    separator_cols = {
        col
        for col in range(width)
        if all(grid[row][col] == 3 for row in range(height))
    }

    row_groups = []
    current = []
    for row in range(height):
        if row in separator_rows:
            if current:
                row_groups.append(current)
                current = []
        else:
            current.append(row)
    if current:
        row_groups.append(current)

    col_groups = []
    current = []
    for col in range(width):
        if col in separator_cols:
            if current:
                col_groups.append(current)
                current = []
        else:
            current.append(col)
    if current:
        col_groups.append(current)

    output = []
    for local_row in range(len(row_groups[0])):
        output_row = []
        for local_col in range(len(col_groups[0])):
            values = [
                grid[rows[local_row]][cols[local_col]]
                for rows in row_groups
                for cols in col_groups
            ]
            counts = Counter(values)
            output_row.append(values[0] if len(counts) == 1 else 1)
        output.append(output_row)
    return output
