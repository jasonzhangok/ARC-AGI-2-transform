def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    separator_rows = [r for r in range(height) if all(value == 5 for value in grid[r])]
    separator_columns = [
        c for c in range(width) if all(grid[r][c] == 5 for r in range(height))
    ]

    row_edges = [-1] + separator_rows + [height]
    column_edges = [-1] + separator_columns + [width]
    cells = []
    for ri in range(len(row_edges) - 1):
        top, bottom = row_edges[ri] + 1, row_edges[ri + 1]
        for ci in range(len(column_edges) - 1):
            left, right = column_edges[ci] + 1, column_edges[ci + 1]
            cells.append((top, bottom, left, right))

    key = next(
        cell
        for cell in cells
        if all(
            grid[r][c] != 8
            for r in range(cell[0], cell[1])
            for c in range(cell[2], cell[3])
        )
    )
    key_pattern = [
        grid[r][key[2] : key[3]]
        for r in range(key[0], key[1])
    ]

    for index, (top, bottom, left, right) in enumerate(cells):
        macro_row, macro_column = divmod(index, len(column_edges) - 1)
        fill = key_pattern[macro_row][macro_column]
        for r in range(top, bottom):
            for c in range(left, right):
                output[r][c] = fill
    return output
