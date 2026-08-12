def transform(grid):
    output = [row[:] for row in grid]
    template_columns = [col for col, value in enumerate(grid[0]) if value == 5]
    for row in range(1, len(grid)):
        if grid[row][-1] == 5:
            for col in template_columns:
                output[row][col] = 2
            output[row][-1] = 5
    return output
