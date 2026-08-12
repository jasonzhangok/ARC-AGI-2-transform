def transform(grid):
    height = len(grid)
    width = len(grid[0])

    markers = []
    for top in range(height - 2):
        for left in range(width - 2):
            corners = [
                (top, left),
                (top, left + 2),
                (top + 2, left),
                (top + 2, left + 2),
            ]
            present = [cell for cell in corners if grid[cell[0]][cell[1]] == 4]
            if len(present) == 3:
                missing = next(cell for cell in corners if cell not in present)
                markers.append((top, left, missing))

    source = next(marker for marker in markers if grid[marker[2][0]][marker[2][1]] == 2)
    source_anchor = source[2]

    raw_template = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 2
    }

    # Keep the parts visible from the marked anchor along rows or columns.
    # The diagonally opposite extreme corner is retained as the far endpoint.
    template = set()
    for row in {row for row, _ in raw_template}:
        cells = [(row, col) for r, col in raw_template if r == row]
        template.add(min(cells, key=lambda cell: abs(cell[1] - source_anchor[1])))
    for col in {col for _, col in raw_template}:
        cells = [(row, col) for row, c in raw_template if c == col]
        template.add(min(cells, key=lambda cell: abs(cell[0] - source_anchor[0])))
    farthest = max(
        abs(row - source_anchor[0]) + abs(col - source_anchor[1])
        for row, col in raw_template
    )
    template.update(
        (row, col)
        for row, col in raw_template
        if abs(row - source_anchor[0]) + abs(col - source_anchor[1]) == farthest
    )

    def corner_sign(marker):
        top, left, (row, col) = marker
        return (-1 if row == top else 1, -1 if col == left else 1)

    source_row_sign, source_col_sign = corner_sign(source)
    relative = [
        (row - source_anchor[0], col - source_anchor[1])
        for row, col in template
    ]

    output = [
        [0 if value == 2 else value for value in row]
        for row in grid
    ]
    for marker in markers:
        target_anchor = marker[2]
        target_row_sign, target_col_sign = corner_sign(marker)
        for drow, dcol in relative:
            row = target_anchor[0] + drow * target_row_sign * source_row_sign
            col = target_anchor[1] + dcol * target_col_sign * source_col_sign
            if 0 <= row < height and 0 <= col < width:
                output[row][col] = 2

    return output
