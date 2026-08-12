def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    stamps = ((0, -1, 7), (0, 1, 6), (-1, 0, 2), (1, 0, 8))

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 1:
                continue
            for d_row, d_col, color in stamps:
                next_row = row + d_row
                next_col = col + d_col
                if 0 <= next_row < height and 0 <= next_col < width:
                    output[next_row][next_col] = color
    return output
