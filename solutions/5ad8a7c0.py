def transform(grid):
    output = [row[:] for row in grid]
    pairs = []
    minimum_span = None
    for row in range(len(grid)):
        columns = []
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                columns.append(col)
        if len(columns) == 2:
            span = columns[1] - columns[0]
            pairs.append((row, columns[0], columns[1], span))
            if minimum_span is None or span < minimum_span:
                minimum_span = span
    for row, left, right, span in pairs:
        if span == minimum_span:
            for col in range(left, right + 1):
                output[row][col] = 2
    return output
