def transform(grid):
    rows = []
    for row in grid:
        if not rows or row != rows[-1]:
            rows.append(row[:])

    columns = []
    for col in range(len(rows[0])):
        column = [row[col] for row in rows]
        if not columns or column != columns[-1]:
            columns.append(column)

    return [
        [columns[col][row] for col in range(len(columns))]
        for row in range(len(rows))
    ]
