def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    seeds = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                seeds.append((row, col))

    for row, col in seeds:
        for neighbor_row in range(max(0, row - 1), min(height, row + 2)):
            for neighbor_col in range(max(0, col - 1), min(width, col + 2)):
                if output[neighbor_row][neighbor_col] == 0:
                    output[neighbor_row][neighbor_col] = 1
    return output
