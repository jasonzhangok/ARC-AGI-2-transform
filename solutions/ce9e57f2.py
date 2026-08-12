def transform(grid):
    output = [row[:] for row in grid]
    height = len(grid)
    width = len(grid[0])
    for col in range(width):
        segment_rows = [row for row in range(height) if grid[row][col] == 2]
        split = (len(segment_rows) + 1) // 2
        for row in segment_rows[split:]:
            output[row][col] = 8
    return output
