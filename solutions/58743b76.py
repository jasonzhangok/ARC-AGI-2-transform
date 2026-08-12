def transform(grid):
    height = len(grid)
    width = len(grid[0])
    key_row = 0
    key_col = 0

    for candidate_row in (0, height - 2):
        for candidate_col in (0, width - 2):
            horizontal_bar = all(
                grid[row][col] == 8
                for row in range(candidate_row, candidate_row + 2)
                for col in range(width)
                if not candidate_col <= col < candidate_col + 2
            )
            vertical_bar = all(
                grid[row][col] == 8
                for row in range(height)
                if not candidate_row <= row < candidate_row + 2
                for col in range(candidate_col, candidate_col + 2)
            )
            colorful_key = all(
                grid[row][col] != 8
                for row in range(candidate_row, candidate_row + 2)
                for col in range(candidate_col, candidate_col + 2)
            )
            if horizontal_bar and vertical_bar and colorful_key:
                key_row = candidate_row
                key_col = candidate_col

    row_start = 2 if key_row == 0 else 0
    row_end = height if key_row == 0 else height - 2
    col_start = 2 if key_col == 0 else 0
    col_end = width if key_col == 0 else width - 2
    result = [row[:] for row in grid]

    for row in range(row_start, row_end):
        for col in range(col_start, col_end):
            if grid[row][col] != 0:
                quadrant_row = 0 if 2 * (row - row_start) < row_end - row_start else 1
                quadrant_col = 0 if 2 * (col - col_start) < col_end - col_start else 1
                result[row][col] = grid[key_row + quadrant_row][key_col + quadrant_col]

    output = result
    return output
