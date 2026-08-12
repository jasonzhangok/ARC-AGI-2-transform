def transform(grid):
    compressed_rows = []
    for row in grid:
        if not compressed_rows or row != compressed_rows[-1]:
            compressed_rows.append(row[:])

    compressed_columns = []
    for col in range(len(compressed_rows[0])):
        column = [row[col] for row in compressed_rows]
        if not compressed_columns or column != compressed_columns[-1]:
            compressed_columns.append(column)

    return [
        [compressed_columns[col][row] for col in range(len(compressed_columns))]
        for row in range(len(compressed_rows))
    ]
