def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for col in range(width):
        markers = [(row, grid[row][col]) for row in range(height) if grid[row][col] != 0]
        if not markers or not any(color == 5 for _, color in markers):
            continue
        previous = -1
        for row, color in markers:
            for fill_row in range(previous + 1, row + 1):
                if output[fill_row][col] == 0:
                    output[fill_row][col] = color
            previous = row
    return output
