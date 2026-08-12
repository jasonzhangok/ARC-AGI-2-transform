def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    pairs = []

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 3:
                continue
            for d_row, d_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                next_row = row + d_row
                next_col = col + d_col
                if (0 <= next_row < height and 0 <= next_col < width
                        and grid[next_row][next_col] == 2):
                    pairs.append(((row, col), (next_row, next_col)))

    for three_cell, two_cell in pairs:
        output[three_cell[0]][three_cell[1]] = 8
        output[two_cell[0]][two_cell[1]] = 0
    return output
