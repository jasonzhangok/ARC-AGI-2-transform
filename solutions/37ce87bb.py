def transform(grid):
    height, width = len(grid), len(grid[0])
    background = 7
    columns = []
    for col in range(width):
        pixels = [grid[row][col] for row in range(height) if grid[row][col] != background]
        if pixels:
            columns.append((col, pixels[0], len(pixels)))

    total = 0
    for _, color, line_height in columns:
        total += line_height if color == 8 else -line_height
    target_col = columns[-1][0] + 2
    output = [row[:] for row in grid]
    for row in range(height - total, height):
        output[row][target_col] = 5
    return output
