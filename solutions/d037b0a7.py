def transform(grid):
    output = [row[:] for row in grid]
    for c in range(len(grid[0])):
        current = 0
        for r in range(len(grid)):
            if grid[r][c] != 0:
                current = grid[r][c]
            elif current != 0:
                output[r][c] = current
    return output
