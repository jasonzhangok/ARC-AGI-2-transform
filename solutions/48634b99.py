def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    source = None
    runs = []

    for col in range(width):
        row = 0
        while row < height:
            if grid[row][col] not in (8, 9):
                row += 1
                continue
            start = row
            values = []
            while row < height and grid[row][col] in (8, 9):
                values.append(grid[row][col])
                row += 1
            runs.append((start, row, col, values))
            if 9 in values:
                source = (start, row, col, values)

    start, end, col, values = source
    length = end - start
    top_half = values[0] == 9
    for row in range(start, end):
        output[row][col] = 8

    for run_start, run_end, run_col, run_values in runs:
        if run_end - run_start == length + 2 and all(value == 8 for value in run_values):
            half = (run_end - run_start) // 2
            if top_half:
                paint_start = run_start
                paint_end = run_start + half
            else:
                paint_start = run_end - half
                paint_end = run_end
            for row in range(paint_start, paint_end):
                output[row][run_col] = 9
            break

    return output
