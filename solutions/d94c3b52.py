def transform(grid):
    height = len(grid)
    width = len(grid[0])
    separator_rows = [
        row for row in range(height) if all(value == 0 for value in grid[row])
    ]
    separator_cols = [
        col for col in range(width)
        if all(grid[row][col] == 0 for row in range(height))
    ]
    row_spans = []
    start = 0
    for separator in separator_rows:
        if start < separator:
            row_spans.append((start, separator))
        start = separator + 1
    if start < height:
        row_spans.append((start, height))
    col_spans = []
    start = 0
    for separator in separator_cols:
        if start < separator:
            col_spans.append((start, separator))
        start = separator + 1
    if start < width:
        col_spans.append((start, width))

    exemplar = None
    for top, bottom in row_spans:
        for left, right in col_spans:
            if any(
                    grid[row][col] == 8
                    for row in range(top, bottom)
                    for col in range(left, right)):
                exemplar = tuple(
                    tuple(grid[row][col] != 0 for col in range(left, right))
                    for row in range(top, bottom)
                )

    endpoints = []
    for block_row, (top, bottom) in enumerate(row_spans):
        for block_col, (left, right) in enumerate(col_spans):
            mask = tuple(
                tuple(grid[row][col] != 0 for col in range(left, right))
                for row in range(top, bottom)
            )
            if mask == exemplar:
                endpoints.append((block_row, block_col))

    output = [row[:] for row in grid]

    recolor_requests = [(block_row, block_col, 8) for block_row, block_col in endpoints]
    for first in endpoints:
        for second in endpoints:
            if first[0] == second[0]:
                for block_col in range(
                        min(first[1], second[1]) + 1,
                        max(first[1], second[1])):
                    recolor_requests.append((first[0], block_col, 7))
            if first[1] == second[1]:
                for block_row in range(
                        min(first[0], second[0]) + 1,
                        max(first[0], second[0])):
                    recolor_requests.append((block_row, first[1], 7))
    for block_row, block_col, color in recolor_requests:
        recolor_top, recolor_bottom = row_spans[block_row]
        recolor_left, recolor_right = col_spans[block_col]
        for row in range(recolor_top, recolor_bottom):
            for col in range(recolor_left, recolor_right):
                if grid[row][col] != 0:
                    output[row][col] = color
    return output
