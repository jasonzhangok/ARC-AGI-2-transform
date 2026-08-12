def _spans(size, separators):
    result = []
    start = 0
    for separator in separators:
        result.append((start, separator))
        start = separator + 1
    result.append((start, size))
    return result


def transform(grid):
    height = len(grid)
    width = len(grid[0])
    separator_rows = [
        row for row in range(height)
        if all(value == 4 for value in grid[row])
    ]
    separator_cols = [
        col for col in range(width)
        if all(grid[row][col] == 4 for row in range(height))
    ]
    row_spans = _spans(height, separator_rows)
    col_spans = _spans(width, separator_cols)
    cell_height = min(bottom - top for top, bottom in row_spans)
    cell_width = min(right - left for left, right in col_spans)
    output = [row[:] for row in grid]

    for local_row in range(cell_height):
        for local_col in range(cell_width):
            values = [
                grid[top + local_row][left + local_col]
                for top, _ in row_spans
                for left, _ in col_spans
                if grid[top + local_row][left + local_col] not in (0, 4)
            ]
            if values:
                for top, _ in row_spans:
                    for left, _ in col_spans:
                        output[top + local_row][left + local_col] = values[0]
    return output
