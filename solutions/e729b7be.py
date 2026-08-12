def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)

    center_row = 0
    center_col = 0
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if grid[row][col] == 8:
                center_row = row
                center_col = col

    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(center_col):
            value = grid[row][col]
            if value == background or value == 8:
                continue
            new_row = 2 * center_row - row
            new_col = 2 * center_col - col
            if 0 <= new_row < height and 0 <= new_col < width:
                output[new_row][new_col] = value
    return output
