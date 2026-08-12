def transform(grid):
    height = len(grid)
    width = len(grid[0])
    centers = []
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if (
                grid[row][col] == 3
                and grid[row - 1][col] == 3
                and grid[row + 1][col] == 3
                and grid[row][col - 1] == 3
                and grid[row][col + 1] == 3
            ):
                centers.append((row, col))

    output = [row[:] for row in grid]
    for first_index in range(len(centers)):
        first_row, first_col = centers[first_index]
        for second_index in range(first_index + 1, len(centers)):
            second_row, second_col = centers[second_index]
            row_distance = second_row - first_row
            col_distance = second_col - first_col
            if abs(row_distance) != abs(col_distance):
                continue
            row_step = 1 if row_distance > 0 else -1
            col_step = 1 if col_distance > 0 else -1
            for step in range(1, abs(row_distance)):
                row = first_row + row_step * step
                col = first_col + col_step * step
                if output[row][col] == 0:
                    output[row][col] = 2
    return output
