"""Solution for ARC task 6d0160f0."""


def _segments(length, separators):
    """Return the index ranges between separator lines."""
    segments = []
    start = 0
    for separator in separators:
        if start < separator:
            segments.append(range(start, separator))
        start = separator + 1
    if start < length:
        segments.append(range(start, length))
    return segments


def transform(grid):
    """Move the panel containing 4 to the panel named by 4's local position."""
    height = len(grid)
    width = len(grid[0])

    separator_rows = [
        row_index
        for row_index, row in enumerate(grid)
        if all(value == 5 for value in row)
    ]
    separator_columns = [
        column_index
        for column_index in range(width)
        if all(grid[row_index][column_index] == 5 for row_index in range(height))
    ]
    row_segments = _segments(height, separator_rows)
    column_segments = _segments(width, separator_columns)

    result = [
        [
            5
            if row_index in separator_rows or column_index in separator_columns
            else 0
            for column_index in range(width)
        ]
        for row_index in range(height)
    ]

    source = None
    destination = None
    for panel_rows in row_segments:
        for panel_columns in column_segments:
            for local_row, row_index in enumerate(panel_rows):
                for local_column, column_index in enumerate(panel_columns):
                    if grid[row_index][column_index] == 4:
                        source = [
                            [grid[r][c] for c in panel_columns]
                            for r in panel_rows
                        ]
                        destination = (local_row, local_column)

    if source is None:
        return [row[:] for row in grid]

    destination_rows = row_segments[destination[0]]
    destination_columns = column_segments[destination[1]]
    for local_row, row_index in enumerate(destination_rows):
        for local_column, column_index in enumerate(destination_columns):
            result[row_index][column_index] = source[local_row][local_column]

    return result
