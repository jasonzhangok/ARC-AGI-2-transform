def transform(grid):
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1

    background = max(counts, key=counts.get)
    foreground = background
    min_row = len(grid)
    max_row = -1
    min_col = len(grid[0])
    max_col = -1
    for row_index in range(len(grid)):
        for col_index in range(len(grid[0])):
            if grid[row_index][col_index] != background:
                foreground = grid[row_index][col_index]
                min_row = min(min_row, row_index)
                max_row = max(max_row, row_index)
                min_col = min(min_col, col_index)
                max_col = max(max_col, col_index)

    result = [[background for _ in range(16)] for _ in range(16)]
    side = 2 * max(max_row - min_row + 1, max_col - min_col + 1)
    at_top = min_row == 0
    at_left = min_col == 0

    for offset in range(side):
        row = offset if at_top else 15 - offset
        col = offset if at_left else 15 - offset
        result[0 if at_top else 15][col] = foreground
        result[row][0 if at_left else 15] = foreground
        diagonal_col = side - 1 - offset if at_left else 16 - side + offset
        result[row][diagonal_col] = foreground

    return result
