def transform(grid):
    width = len(grid[0])
    output = [row[:] for row in grid]
    target_parity = (width - 1) % 2
    for row in range(len(grid)):
        for col in range(width):
            if grid[row][col] == 5 and col % 2 == target_parity:
                output[row][col] = 3
    return output
