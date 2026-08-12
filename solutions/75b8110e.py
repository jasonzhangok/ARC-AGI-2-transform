def transform(grid):
    half_height = len(grid) // 2
    half_width = len(grid[0]) // 2
    priority = (5, 6, 9, 4)
    output = []
    for row in range(half_height):
        out_row = []
        for col in range(half_width):
            values = {
                grid[row][col],
                grid[row][col + half_width],
                grid[row + half_height][col],
                grid[row + half_height][col + half_width],
            }
            out_row.append(next((color for color in priority if color in values), 0))
        output.append(out_row)
    return output
