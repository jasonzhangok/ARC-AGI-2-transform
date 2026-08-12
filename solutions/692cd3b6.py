def transform(grid):
    height, width = len(grid), len(grid[0])
    markers = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 5
    ]
    mouths = []
    endpoints = []
    for row, col in markers:
        for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            mouth_row, mouth_col = row + delta_row, col + delta_col
            if (
                0 <= mouth_row < height
                and 0 <= mouth_col < width
                and grid[mouth_row][mouth_col] == 0
            ):
                mouths.append((mouth_row, mouth_col))
                endpoints.append((row + 2 * delta_row, col + 2 * delta_col))
                break

    start, end = endpoints
    row_step = 1 if start[0] < end[0] else -1 if start[0] > end[0] else 0
    col_step = 1 if start[1] < end[1] else -1 if start[1] > end[1] else 0
    rows = list(range(start[0], end[0] + row_step, row_step)) if row_step else [start[0]]
    cols = list(range(start[1], end[1] + col_step, col_step)) if col_step else [start[1]]

    from_start = set()
    for row in rows:
        for col in cols:
            if grid[row][col] != 0:
                continue
            if (
                (row, col) == start
                or (row_step and (row - row_step, col) in from_start)
                or (col_step and (row, col - col_step) in from_start)
            ):
                from_start.add((row, col))

    to_end = set()
    for row in reversed(rows):
        for col in reversed(cols):
            if grid[row][col] != 0:
                continue
            if (
                (row, col) == end
                or (row_step and (row + row_step, col) in to_end)
                or (col_step and (row, col + col_step) in to_end)
            ):
                to_end.add((row, col))

    output = [row[:] for row in grid]
    for row, col in from_start & to_end:
        output[row][col] = 4
    for row, col in mouths:
        output[row][col] = 4
    return output
