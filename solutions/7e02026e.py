def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    marked = set()

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            cross = {(row, col), (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)}
            if all(grid[cross_row][cross_col] == 0 for cross_row, cross_col in cross):
                marked |= cross

    for row, col in marked:
        output[row][col] = 3
    return output
