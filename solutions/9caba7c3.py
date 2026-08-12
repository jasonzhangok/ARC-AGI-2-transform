def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    candidates = []

    for center_row in range(1, height - 1):
        for center_col in range(1, width - 1):
            values = []
            for row in range(center_row - 1, center_row + 2):
                for col in range(center_col - 1, center_col + 2):
                    values.append(grid[row][col])
            if grid[center_row][center_col] == 5 and 2 in values and all(value == 2 or value == 5 for value in values):
                candidates.append((-values.count(2), center_row, center_col))

    candidates.sort()
    occupied = set()
    for negative_count, center_row, center_col in candidates:
        window = {(row, col) for row in range(center_row - 1, center_row + 2) for col in range(center_col - 1, center_col + 2)}
        if window & occupied:
            continue
        occupied |= window
        for row, col in window:
            if row == center_row and col == center_col:
                output[row][col] = 4
            elif grid[row][col] == 5:
                output[row][col] = 7

    return output
